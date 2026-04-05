#!/usr/bin/env python3
"""
audit.py — Café Athena Recipe Audit & Repair Tool

Scans recipe/folio files against the format standard, identifies issues,
generates fixes via Ollama where possible, and applies user-approved changes.

Usage:
    python3 scripts/audit.py                        # audit all recipes
    python3 scripts/audit.py --id 01-01             # audit one recipe
    python3 scripts/audit.py --chapter 3            # audit a chapter
    python3 scripts/audit.py --scan-only            # report issues, no fixes
    python3 scripts/audit.py --model gemma3:4b      # use different model
    python3 scripts/audit.py --status               # show audit status summary

Audit status values in recipes.json:
    pending       — never audited
    clean         — audited, no issues
    issues_found  — issues detected, fixes not yet approved
    approved      — fixes applied
"""

import argparse
import json
import re
import sys
import time
import urllib.request
import urllib.error
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

BASE = Path(__file__).parent.parent
RECIPES_JSON = BASE / "recipes.json"
MANUAL_DIR = BASE / "The Manual"
OLLAMA_URL = "http://localhost:11434/api/generate"
TODAY = date.today().isoformat()

# Standard section order per format standard
REQUIRED_SECTIONS = [
    "Headnote",
    "Mise en Place",
    "Ingredients",
    "Method",
    "Glossary",
    "Keywords",
    "Category",
]

# Sections that apply only to full recipes (not technique folios)
RECIPE_ONLY_SECTIONS = {"Ingredients"}

# Sections Claude can generate via Ollama
AUTO_FIXABLE = {"missing_glossary", "missing_keywords", "missing_category"}

CATEGORY_VALID_CUISINES = {
    "French", "Italian", "Japanese", "Korean", "Vietnamese",
    "Chinese", "American", "Mediterranean", "Asian-Fusion", "Global",
}
CATEGORY_VALID_STYLES = {
    "Classical", "Modern", "Rustic", "Competition", "Fine Dining",
    "Weeknight", "Pastry", "Technique Folio",
}

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class Issue:
    code: str           # e.g. "missing_glossary"
    description: str    # human-readable
    auto_fix: bool      # can Ollama generate a fix?
    fix_content: str = ""  # populated during fix generation


@dataclass
class RecipeAudit:
    recipe_id: str
    title: str
    recipe_type: str    # "recipe" or "technique"
    file_path: Path
    file_text: str
    issues: list[Issue] = field(default_factory=list)

    @property
    def has_issues(self):
        return bool(self.issues)

    @property
    def fixable_issues(self):
        return [i for i in self.issues if i.auto_fix]

    @property
    def manual_issues(self):
        return [i for i in self.issues if not i.auto_fix]


# ---------------------------------------------------------------------------
# Audit logic
# ---------------------------------------------------------------------------

def detect_old_format(text: str) -> bool:
    """True if the file uses pre-standard bold-header format (no ## headings)."""
    has_h2 = bool(re.search(r"^## ", text, re.MULTILINE))
    has_bold_section = bool(re.search(r"^\*\*[A-Z][^*]+\*\*", text, re.MULTILINE))
    return not has_h2 and has_bold_section


def find_sections(text: str) -> dict[str, int]:
    """Return {normalized_name: line_number} for all ## headings found."""
    sections = {}
    for m in re.finditer(r"^## (.+)$", text, re.MULTILINE):
        heading = m.group(1).strip()
        # Normalize variants
        normalized = heading
        if re.match(r"mise.?en.?place", heading, re.IGNORECASE):
            normalized = "Mise en Place"
        elif re.match(r"chef.?s.?notes?", heading, re.IGNORECASE):
            normalized = "Chef's Notes"
        sections[normalized] = m.start()
    return sections


def check_category_format(text: str) -> bool:
    """True if ## Category section has valid cuisine: X | style: Y format."""
    m = re.search(r"^## Category\s*\n(.+)$", text, re.MULTILINE)
    if not m:
        return False
    line = m.group(1).strip()
    cuisine_m = re.search(r"cuisine:\s*(\w[\w\- ]+)", line)
    style_m = re.search(r"style:\s*([\w\- ]+)", line)
    if not cuisine_m or not style_m:
        return False
    cuisine = cuisine_m.group(1).strip()
    style = style_m.group(1).strip()
    return cuisine in CATEGORY_VALID_CUISINES and style in CATEGORY_VALID_STYLES


def audit_file(recipe_id: str, title: str, recipe_type: str, fpath: Path) -> RecipeAudit:
    text = fpath.read_text(encoding="utf-8")
    audit = RecipeAudit(recipe_id, title, recipe_type, fpath, text)

    # Old format check — flag and stop (can't meaningfully audit structure)
    if detect_old_format(text):
        audit.issues.append(Issue(
            code="old_format",
            description="Pre-standard format (bold headers, no ## sections). Needs full reformat.",
            auto_fix=False,
        ))
        return audit

    sections = find_sections(text)

    # Check required sections
    for section in REQUIRED_SECTIONS:
        if section in RECIPE_ONLY_SECTIONS and recipe_type != "recipe":
            continue
        if section not in sections:
            code = f"missing_{section.lower().replace(' ', '_')}"
            can_fix = code in AUTO_FIXABLE
            audit.issues.append(Issue(
                code=code,
                description=f"Missing section: ## {section}",
                auto_fix=can_fix,
            ))

    # Check section order (only for sections that exist)
    present = [s for s in REQUIRED_SECTIONS if s in sections]
    positions = [sections[s] for s in present]
    if positions != sorted(positions):
        audit.issues.append(Issue(
            code="section_order",
            description=f"Sections out of order. Found: {present}",
            auto_fix=False,
        ))

    # Check Category format if section exists
    if "Category" in sections and not check_category_format(text):
        audit.issues.append(Issue(
            code="bad_category_format",
            description="## Category exists but format is invalid (expected: cuisine: X | style: Y)",
            auto_fix=True,
        ))

    return audit


# ---------------------------------------------------------------------------
# Ollama helpers
# ---------------------------------------------------------------------------

GLOSSARY_SYSTEM = """\
You are a culinary reference editor for a professional cookbook called Café Athena.
Extract culinary terminology from the recipe/folio content and write precise glossary definitions.

Rules:
- Extract 3–8 terms that are genuinely culinary, scientific, or technique-specific.
- Skip common everyday words (salt, water, pan, stir, add, etc.).
- Definitions must be accurate, concise (1–2 sentences), in cookbook voice.
- Format EXACTLY as one term per line:
  * **Term:** Definition here.
- Return ONLY the bulleted list. No preamble, no explanation.
"""

KEYWORDS_SYSTEM = """\
You are a culinary SEO editor for a professional cookbook called Café Athena.
Generate a Keywords line for the given recipe/folio.

Rules:
- 10–15 comma-separated terms on a single line.
- Cover: cooking technique, primary ingredients, cuisine origin, equipment, flavor profile.
- Use lowercase except for proper nouns.
- Return ONLY the comma-separated line. No heading, no explanation.
"""

CATEGORY_SYSTEM = """\
You are a culinary metadata editor for a professional cookbook called Café Athena.
Assign a Category line using ONLY the controlled vocabulary below.

cuisine: French · Italian · Japanese · Korean · Vietnamese · Chinese · American · Mediterranean · Asian-Fusion · Global
style: Classical · Modern · Rustic · Competition · Fine Dining · Weeknight · Pastry · Technique Folio
dietary (optional): Vegetarian · Pescatarian

Format EXACTLY as:
cuisine: X | style: Y

Or with dietary:
cuisine: X | style: Y | dietary: Z

Return ONLY that single line. No explanation.
"""


def call_ollama(model: str, system: str, content: str, timeout: int = 120) -> str:
    payload = json.dumps({
        "model": model,
        "system": system,
        "prompt": content[:5000],
        "stream": False,
        "options": {"temperature": 0.2, "num_predict": 512},
    }).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_URL, data=payload,
        headers={"Content-Type": "application/json"}, method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8")).get("response", "").strip()
    except urllib.error.URLError as e:
        print(f"\n  [Ollama error: {e}]", file=sys.stderr)
        return ""


def generate_fix(issue: Issue, audit: RecipeAudit, model: str) -> str:
    text = audit.file_text

    if issue.code == "missing_glossary":
        raw = call_ollama(model, GLOSSARY_SYSTEM, text)
        if not raw:
            return ""
        # Validate at least one parseable term
        # Handles both **Term:** (colon inside bold) and **Term**: (colon outside)
        if re.search(r"^\*\s+\*\*[^*]+\*\*:?", raw, re.MULTILINE):
            return "## Glossary\n\n" + raw
        return ""

    elif issue.code == "missing_keywords":
        raw = call_ollama(model, KEYWORDS_SYSTEM, text)
        raw = raw.strip().strip("`").strip()
        if raw and "," in raw:
            return "## Keywords\n\n" + raw
        return ""

    elif issue.code in {"missing_category", "bad_category_format"}:
        raw = call_ollama(model, CATEGORY_SYSTEM, text)
        raw = raw.strip()
        if re.match(r"cuisine:\s*\w", raw):
            return "## Category\n\n" + raw
        return ""

    return ""


# ---------------------------------------------------------------------------
# Apply fixes to file text
# ---------------------------------------------------------------------------

def insert_before(text: str, new_block: str, markers: list[str]) -> str:
    """Insert new_block before the first marker found, or append at end."""
    for marker in markers:
        m = re.search(rf"^## {re.escape(marker)}", text, re.MULTILINE)
        if m:
            return text[: m.start()] + new_block + "\n\n" + text[m.start():]
    return text.rstrip() + "\n\n" + new_block + "\n"


def replace_section(text: str, heading: str, new_block: str) -> str:
    """Replace an existing ## Section block with new_block."""
    pattern = rf"(^## {re.escape(heading)}\s*\n)(.*?)(?=^## |\Z)"
    replacement = new_block + "\n\n"
    result = re.sub(pattern, replacement, text, flags=re.MULTILINE | re.DOTALL)
    return result if result != text else text


def apply_fix(issue: Issue, text: str) -> str:
    if issue.code == "missing_glossary":
        return insert_before(text, issue.fix_content, ["Keywords", "Category"])
    elif issue.code == "missing_keywords":
        return insert_before(text, issue.fix_content, ["Category"])
    elif issue.code == "missing_category":
        return text.rstrip() + "\n\n" + issue.fix_content + "\n"
    elif issue.code == "bad_category_format":
        return replace_section(text, "Category", issue.fix_content)
    return text


# ---------------------------------------------------------------------------
# recipes.json helpers
# ---------------------------------------------------------------------------

def load_registry() -> dict:
    with open(RECIPES_JSON) as f:
        return json.load(f)


def save_registry(data: dict):
    with open(RECIPES_JSON, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_registry_entry(data: dict, recipe_id: str) -> dict | None:
    for r in data["recipes"]:
        if r["id"] == recipe_id:
            return r
    return None


def update_audit_status(entry: dict, audit: RecipeAudit, status: str):
    if "audit" not in entry:
        entry["audit"] = {}
    entry["audit"]["lastRun"] = TODAY
    entry["audit"]["status"] = status
    entry["audit"]["issues"] = [i.code for i in audit.issues]


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

BOLD = "\033[1m"
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
DIM = "\033[2m"
RESET = "\033[0m"

def print_header(text: str):
    print(f"\n{BOLD}{CYAN}{'─' * 60}{RESET}")
    print(f"{BOLD}{CYAN}{text}{RESET}")
    print(f"{BOLD}{CYAN}{'─' * 60}{RESET}")

def print_issue(issue: Issue):
    tag = f"{GREEN}[auto-fix]{RESET}" if issue.auto_fix else f"{YELLOW}[manual]{RESET}"
    print(f"  {tag} {issue.description}")

def prompt_yn(question: str, default: str = "y") -> bool:
    hint = "[Y/n]" if default == "y" else "[y/N]"
    while True:
        ans = input(f"  {question} {hint} ").strip().lower() or default
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False

def prompt_choice(question: str, options: list[str]) -> str:
    opts = "/".join(options)
    while True:
        ans = input(f"  {question} [{opts}] ").strip().lower()
        if ans in [o.lower() for o in options]:
            return ans


# ---------------------------------------------------------------------------
# Main audit loop
# ---------------------------------------------------------------------------

def run_audit(
    target_ids: list[str],
    data: dict,
    model: str,
    scan_only: bool,
    auto_approve: bool = False,
):
    id_to_entry = {r["id"]: r for r in data["recipes"]}

    all_files = list(MANUAL_DIR.rglob("*.md"))
    id_to_file: dict[str, Path] = {}
    for f in all_files:
        m = re.match(r"^(\d{2}-\d{2}(?:\.\d+)?)", f.name)
        if m:
            id_to_file[m.group(1)] = f

    total = len(target_ids)
    clean_count = 0
    issues_count = 0
    not_found = []
    registry_dirty = False

    for idx, rid in enumerate(target_ids, 1):
        entry = id_to_entry.get(rid)
        if not entry:
            not_found.append(rid)
            continue

        fpath = id_to_file.get(rid)
        if not fpath:
            not_found.append(rid)
            continue

        title = entry.get("title", "Unknown")
        recipe_type = entry.get("type", "recipe")

        # --- Audit ---
        audit = audit_file(rid, title, recipe_type, fpath)

        if not audit.has_issues:
            clean_count += 1
            update_audit_status(entry, audit, "clean")
            registry_dirty = True
            print(f"[{idx}/{total}] {GREEN}✓{RESET} {rid} — {title}")
            continue

        issues_count += 1
        print_header(f"[{idx}/{total}] {rid} — {title}")
        for issue in audit.issues:
            print_issue(issue)

        update_audit_status(entry, audit, "issues_found")
        registry_dirty = True

        if scan_only:
            continue

        # --- Generate fixes for auto-fixable issues ---
        fixable = audit.fixable_issues
        if not fixable:
            print(f"\n  {YELLOW}No auto-fixable issues. Manual review required.{RESET}")
            continue

        print(f"\n  Generating fixes via Ollama ({model})...")
        generated = []
        for issue in fixable:
            t0 = time.time()
            print(f"    {DIM}→ {issue.code}...{RESET}", end="", flush=True)
            content = generate_fix(issue, audit, model)
            elapsed = time.time() - t0
            if content:
                issue.fix_content = content
                generated.append(issue)
                print(f" {GREEN}done{RESET} ({elapsed:.1f}s)")
            else:
                print(f" {RED}failed{RESET} ({elapsed:.1f}s)")

        if not generated:
            print(f"  {RED}All fix generations failed. Skipping.{RESET}")
            continue

        # --- Show proposed fixes and get approval ---
        print()
        for issue in generated:
            print(f"\n  {BOLD}Proposed fix for [{issue.code}]:{RESET}")
            # Show a preview (first 20 lines)
            preview_lines = issue.fix_content.splitlines()[:20]
            for line in preview_lines:
                print(f"    {DIM}{line}{RESET}")
            if len(issue.fix_content.splitlines()) > 20:
                print(f"    {DIM}... ({len(issue.fix_content.splitlines())} lines total){RESET}")

        print()
        if auto_approve:
            action = "y"
            print(f"  {DIM}(--auto-approve) applying {len(generated)} fix(es)...{RESET}")
        else:
            action = prompt_choice(
                f"Apply {len(generated)} fix(es) to {fpath.name}?",
                ["y", "n", "edit"],
            )

        if action == "n":
            print(f"  {YELLOW}Skipped.{RESET}")
            continue

        if action == "edit":
            print(f"  {YELLOW}Open {fpath} in your editor, then re-run audit.{RESET}")
            continue

        # Apply
        updated_text = audit.file_text
        for issue in generated:
            updated_text = apply_fix(issue, updated_text)

        fpath.write_text(updated_text, encoding="utf-8")
        update_audit_status(entry, audit, "approved")
        registry_dirty = True

        # Mark individual stages complete
        for issue in generated:
            if issue.code == "missing_glossary":
                entry["stages"]["glossaryPull"] = True
            elif issue.code in {"missing_keywords", "missing_category", "bad_category_format"}:
                entry["stages"]["keywordPull"] = True

        print(f"  {GREEN}✓ Applied {len(generated)} fix(es).{RESET}")

    # Save registry
    if registry_dirty:
        # Ensure _meta documents the audit field
        if "audit" not in data["_meta"]["stages"]:
            data["_meta"]["stages"]["audit"] = "Format audit results tracked per recipe"
        save_registry(data)

    # Summary
    print_header("Audit Summary")
    print(f"  Total scanned:   {total}")
    print(f"  {GREEN}Clean:           {clean_count}{RESET}")
    print(f"  {YELLOW}Issues found:    {issues_count}{RESET}")
    if not_found:
        print(f"  {RED}Not found:       {len(not_found)} — {not_found}{RESET}")


def show_status(data: dict):
    """Print a summary of audit status across all recipes."""
    counts = {"pending": [], "clean": [], "issues_found": [], "approved": []}
    for r in data["recipes"]:
        status = r.get("audit", {}).get("status", "pending")
        counts.setdefault(status, []).append(r["id"])

    print_header("Audit Status")
    for status, ids in counts.items():
        color = {
            "pending": DIM, "clean": GREEN, "issues_found": YELLOW, "approved": CYAN,
        }.get(status, RESET)
        print(f"  {color}{status:<16}{RESET} {len(ids):>4}  {DIM}{', '.join(ids[:8])}{'...' if len(ids) > 8 else ''}{RESET}")

    # Show issue frequency
    issue_freq: dict[str, int] = {}
    for r in data["recipes"]:
        for issue in r.get("audit", {}).get("issues", []):
            issue_freq[issue] = issue_freq.get(issue, 0) + 1
    if issue_freq:
        print(f"\n  {BOLD}Issue frequency:{RESET}")
        for code, count in sorted(issue_freq.items(), key=lambda x: -x[1]):
            print(f"    {YELLOW}{code:<30}{RESET} {count}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Café Athena audit & repair tool")
    parser.add_argument("--id", help="Audit a single recipe by ID")
    parser.add_argument("--chapter", type=int, help="Audit all recipes in a chapter")
    parser.add_argument("--scan-only", action="store_true", help="Detect issues only, no fixes")
    parser.add_argument("--model", default="llama3.2:latest", help="Ollama model")
    parser.add_argument("--status", action="store_true", help="Show audit status summary")
    parser.add_argument("--pending-only", action="store_true", help="Only audit never-audited recipes")
    parser.add_argument("--auto-approve", action="store_true", help="Apply all generated fixes without prompting")
    args = parser.parse_args()

    data = load_registry()

    if args.status:
        show_status(data)
        return

    # Build target list
    all_recipes = data["recipes"]

    if args.id:
        target_ids = [args.id]
    elif args.chapter:
        target_ids = [r["id"] for r in all_recipes if r["chapter"] == args.chapter]
    elif args.pending_only:
        target_ids = [r["id"] for r in all_recipes if r.get("audit", {}).get("status", "pending") == "pending"]
    else:
        target_ids = [r["id"] for r in all_recipes]

    if not target_ids:
        print("No recipes matched the filter.")
        return

    print(f"{BOLD}Café Athena — Recipe Audit{RESET}")
    print(f"Model: {args.model} | Recipes: {len(target_ids)} | Scan only: {args.scan_only}")

    run_audit(target_ids, data, args.model, args.scan_only, args.auto_approve)


if __name__ == "__main__":
    main()
