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
    python3 scripts/audit.py --model gemma3:4b      # generation model (glossary, keywords, category)
    python3 scripts/audit.py --detect-model qwen2.5:7b  # detection model (mise violation)
    python3 scripts/audit.py --deep                 # enable LLM-based Mise/Method violation check
    python3 scripts/audit.py --status               # show audit status summary
    python3 scripts/audit.py --sync-metadata        # backfill cuisine/style/family/course/keywords/dietary from folios

Audit status values in recipes.json:
    pending       — never audited
    clean         — audited, no issues
    issues_found  — issues detected, fixes not yet approved
    approved      — fixes applied

Checks performed:
    Structural (always):  missing sections, section order (incl. optional Variations/Chef's Notes),
                          old combined Variations & Chef's Notes heading, category format
    Regex (always):       dual temperatures, keywords count, bold phase headers
    LLM detection (--deep): mise en place heat-step violations via qwen2.5:7b
    LLM generation:       glossary, keywords, category content via llama3.2
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
RECIPES_JSON = BASE / "The Manual" / "recipes.json"
MANUAL_DIR = BASE / "The Manual"
OLLAMA_URL = "http://localhost:11434/api/generate"
TODAY = date.today().isoformat()

# Model defaults
DEFAULT_GEN_MODEL = "llama3.2:latest"    # generation: glossary, keywords, category
DEFAULT_DETECT_MODEL = "qwen2.5:7b"      # detection: mise violation analysis

# Keywords count bounds per format standard
KEYWORDS_MIN = 8
KEYWORDS_MAX = 15
KEYWORDS_MAX_COLLECTION = 20  # collection folios bundle multiple sub-recipes

# Required sections — used for "missing section" checks
# (recipe-only sections are skipped for technique folios)
REQUIRED_SECTIONS = [
    "Headnote",
    "Ingredients",
    "Mise en Place",
    "Method",
    "Glossary",
    "Keywords",
    "Category",
]

# Full section order per format standard v3.2, including optional sections.
# Used for order checking — any present section must follow this sequence.
FULL_SECTION_ORDER = [
    "Headnote",
    "Ingredients",
    "Mise en Place",
    "Method",
    "Variations",
    "Chef's Notes",
    "Glossary",
    "Keywords",
    "Category",
]

# Sections that apply only to full recipes (not technique folios)
RECIPE_ONLY_SECTIONS = {"Headnote", "Mise en Place", "Ingredients", "Method"}

# Sections Claude can generate via Ollama
AUTO_FIXABLE = {"missing_glossary", "missing_keywords", "missing_category"}

# Issues fixed by local regex (no Ollama needed)
REGEX_FIXABLE = {"phase_header_format"}

CATEGORY_VALID_CUISINES = {
    "French", "Italian", "Japanese", "Korean", "Vietnamese",
    "Chinese", "Greek", "Spanish", "Indian", "Middle Eastern",
    "Mexican", "Latin American", "Thai", "American",
    "Mediterranean", "Asian-Fusion", "Global",
    # Middle Eastern sub-cuisines
    "Turkish", "Lebanese", "Persian", "Moroccan", "North African",
    # American sub-cuisines
    "Southern", "Cajun",
}
CATEGORY_VALID_STYLES = {
    "Classical", "Modern", "Rustic", "Competition", "Fine Dining",
    "Brunch", "Weeknight", "Pastry", "Modernist", "Technique Folio",
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


def check_category_format(text: str, recipe_type: str = "recipe") -> bool:
    """Validate ## Category section.

    Recipe folios require `cuisine: X | style: Y` with both values in the valid set.
    Technique folios carry no cuisine (techniques are universal) and validate
    against `style: Technique Folio` alone.
    """
    m = re.search(r"^## Category\s*\n(.+)$", text, re.MULTILINE)
    if not m:
        return False
    line = m.group(1).strip()
    style_m = re.search(r"style:\s*([\w\- ]+)", line)
    if not style_m:
        return False
    style = style_m.group(1).strip()
    if style not in CATEGORY_VALID_STYLES:
        return False
    if recipe_type == "technique":
        return style == "Technique Folio"
    cuisine_m = re.search(r"cuisine:\s*(\w[\w\- ]+)", line)
    if not cuisine_m:
        return False
    cuisine = cuisine_m.group(1).strip()
    return cuisine in CATEGORY_VALID_CUISINES


def check_dual_temperatures(text: str) -> list[str]:
    """Return Method section lines containing a lone °F or °C without its paired unit.

    Scoped to ## Method only — avoids false positives in headnotes, chef's notes,
    and educational/science prose in technique folios.
    """
    m = re.search(r'^## Method\s*\n(.*?)(?=^## |\Z)', text, re.MULTILINE | re.DOTALL)
    if not m:
        return []  # No Method section — structural checks cover that separately
    issues = []
    for line in m.group(1).splitlines():
        has_f = bool(re.search(r'\d+°F', line))
        has_c = bool(re.search(r'\d+°C', line))
        if has_f and not has_c:
            issues.append(line.strip()[:80])
        elif has_c and not has_f:
            issues.append(line.strip()[:80])
    return issues


def check_keywords_count(text: str) -> int | None:
    """Return the number of comma-separated keywords, or None if section is absent."""
    m = re.search(r'^## Keywords\s*\n+(.+)$', text, re.MULTILINE)
    if not m:
        return None
    terms = [t.strip() for t in m.group(1).split(',') if t.strip()]
    return len(terms)


def check_keywords_casing(text: str) -> bool:
    """True if any keyword in ## Keywords starts with an uppercase letter (Title Case violation).

    Folios require all-lowercase keywords per the format standard.
    Proper nouns are an exception but are rare enough to flag for manual review.
    """
    m = re.search(r'^## Keywords\s*\n+(.+)$', text, re.MULTILINE)
    if not m:
        return False
    terms = [t.strip() for t in m.group(1).split(',') if t.strip()]
    return any(t and t[0].isupper() for t in terms)


def check_bold_phase_headers(text: str) -> list[str]:
    """Return lines in Method containing 'Phase N:' that don't use **Phase N: Title.** format."""
    m = re.search(r'^## Method\s*\n(.*?)(?=^## |\Z)', text, re.MULTILINE | re.DOTALL)
    if not m:
        return []
    violations = []
    for line in m.group(1).splitlines():
        if re.search(r'Phase \d+:', line):
            # Valid format: line (trimmed) starts with **Phase N:
            if not re.match(r'^\*\*Phase \d+:', line.strip()):
                violations.append(line.strip()[:80])
    return violations


MISE_DETECT_SYSTEM = """\
You are auditing the "Mise en Place" section of a recipe.

Your ONLY job: identify bullet points that apply direct heat.
Direct heat means: sautéing, boiling, frying, roasting, toasting, blanching, \
rendering, searing, reducing, sweating, caramelizing, or any cooking action.

Pure prep is fine and should NOT be flagged: chopping, measuring, portioning, \
mincing, slicing, draining, patting dry, separating, peeling, zesting, \
placing items near the stove, or having something ready.

If you find a heat-applying bullet, respond with exactly:
VIOLATION: [quote the bullet text verbatim, max 120 chars]

If no heat-applying steps are present, respond with exactly:
PASS
"""


def extract_mise_section(text: str) -> str:
    """Return only the Mise en Place section text, or empty string."""
    m = re.search(
        r'^## Mise en Place.*?\n(.*?)(?=^## |\Z)',
        text, re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    return m.group(1).strip() if m else ""


def detect_mise_violation(text: str, detect_model: str) -> str:
    """Ask the detect model to find heat steps in Mise en Place.
    Returns the violation description string, or empty string if none."""
    mise = extract_mise_section(text)
    if not mise:
        return ""
    raw = call_ollama(detect_model, MISE_DETECT_SYSTEM, mise, timeout=60)
    if raw.startswith("VIOLATION:"):
        return raw[len("VIOLATION:"):].strip()
    return ""


def audit_file(recipe_id: str, title: str, recipe_type: str, fpath: Path,
               deep: bool = False, detect_model: str = DEFAULT_DETECT_MODEL,
               format_exception: str = "") -> RecipeAudit:
    text = fpath.read_text(encoding="utf-8")
    audit = RecipeAudit(recipe_id, title, recipe_type, fpath, text)

    is_collection = format_exception == "collection-folio"

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
        # Collection folios embed sub-recipe sections inline; skip structural checks
        if section in RECIPE_ONLY_SECTIONS and is_collection:
            continue
        if section not in sections:
            code = f"missing_{section.lower().replace(' ', '_')}"
            can_fix = code in AUTO_FIXABLE
            audit.issues.append(Issue(
                code=code,
                description=f"Missing section: ## {section}",
                auto_fix=can_fix,
            ))

    # Detect any combined Variations/Chef's Notes heading (pre-v3.2 template)
    # Catch all combined heading variants: ## heading and **bold** inline heading
    combined_heading = re.search(
        r"^(?:## |\*\*)(?:Variations\s*[&/]\s*Chef.?s.?Notes?|Chef.?s.?Notes?\s*[&/]\s*Variations)(?:\*\*)?",
        text, re.MULTILINE | re.IGNORECASE,
    )
    if combined_heading:
        label = re.sub(r"^[#* ]+|[* ]+$", "", combined_heading.group(0)).strip()
        audit.issues.append(Issue(
            code="old_combined_variations",
            description=f'"{label}" should be split into ## Variations and ## Chef\'s Notes (v3.2)',
            auto_fix=True,
        ))

    # Check section order against the full known sequence (required + optional)
    present = [s for s in FULL_SECTION_ORDER if s in sections]
    positions = [sections[s] for s in present]
    if positions != sorted(positions):
        audit.issues.append(Issue(
            code="section_order",
            description=f"Sections out of order. Found: {present}",
            auto_fix=False,
        ))

    # Check Category format if section exists
    if "Category" in sections and not check_category_format(text, recipe_type):
        expected = (
            "style: Technique Folio" if recipe_type == "technique"
            else "cuisine: X | style: Y"
        )
        audit.issues.append(Issue(
            code="bad_category_format",
            description=f"## Category exists but format is invalid (expected: {expected})",
            auto_fix=True,
        ))

    # Dual temperature format check
    temp_issues = check_dual_temperatures(text)
    if temp_issues:
        audit.issues.append(Issue(
            code="dual_temperature",
            description=(
                f"Temperature(s) missing F/C pair on {len(temp_issues)} line(s): "
                f"{temp_issues[0][:60]}{'...' if len(temp_issues) > 1 else ''}"
            ),
            auto_fix=False,
        ))

    # Keywords count check (only if section is present)
    if "Keywords" in sections:
        kw_count = check_keywords_count(text)
        kw_max = KEYWORDS_MAX_COLLECTION if is_collection else KEYWORDS_MAX
        if kw_count is not None and not (KEYWORDS_MIN <= kw_count <= kw_max):
            audit.issues.append(Issue(
                code="keywords_count",
                description=f"Keywords has {kw_count} terms (expected {KEYWORDS_MIN}–{kw_max})",
                auto_fix=False,
            ))

    # Folio-specific: keyword casing (must be lowercase)
    if recipe_type == "technique" and "Keywords" in sections:
        if check_keywords_casing(text):
            audit.issues.append(Issue(
                code="keywords_title_case",
                description="Keywords contain Title Case — folio keywords must be all lowercase",
                auto_fix=False,
            ))

    # Bold phase header check
    unbolded = check_bold_phase_headers(text)
    if unbolded:
        audit.issues.append(Issue(
            code="phase_header_format",
            description=f"### phase header(s) in Method (will convert to **bold**): {len(unbolded)} found",
            auto_fix=True,
        ))

    # LLM-based Mise/Method violation check (only with --deep)
    if deep and "Mise en Place" in sections:
        violation = detect_mise_violation(text, detect_model)
        if violation:
            audit.issues.append(Issue(
                code="mise_method_violation",
                description=f"Heat step in Mise en Place: {violation}",
                auto_fix=False,
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

CATEGORY_SYSTEM_TECHNIQUE = """\
You are a culinary metadata editor for a professional cookbook called Café Athena.
This is a TECHNIQUE FOLIO, not a recipe. Technique folios have no cuisine.

Format EXACTLY as:
style: Technique Folio

Return ONLY that single line. No explanation.
"""

SPLIT_VARIATIONS_SYSTEM = """\
Classify each recipe bullet as V (Variation) or N (Chef's Note).

V = a dedicated alternate preparation: different ingredient, dietary swap, technique
change, or named variant that produces a distinct result. Bold header typically
contains "Variant", "Version", "Alternative", "Without", or names a specific variant.

N = everything else: technique tips, science, storage, warnings, substitution side-notes,
ingredient explanations, flavor observations.

Output ONE label per line in the same order as the input bullets. Nothing else.

Example input:
1. **Storage:** Keep refrigerated for 2 weeks.
2. **Yogurt Variant:** Substitute buttermilk with yogurt for a sharper result.
3. **Sweet Crème:** For dessert use, stir in powdered sugar after cooling.

Example output:
N
V
V
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


def fix_phase_headers(text: str) -> str:
    """Convert ### Phase N: Title → **Phase N: Title.** within the Method section."""
    method_m = re.search(
        r'^(## Method\s*\n)(.*?)(?=^## |\Z)', text, re.MULTILINE | re.DOTALL
    )
    if not method_m:
        return text

    def replace_header(m):
        title = m.group(1).strip()
        if not title.endswith('.'):
            title += '.'
        return f'**{title}**'

    fixed_body = re.sub(
        r'^### (Phase \d+:.+?)$', replace_header,
        method_m.group(2), flags=re.MULTILINE,
    )
    return text[:method_m.start(2)] + fixed_body + text[method_m.end(2):]


def generate_fix(issue: Issue, audit: RecipeAudit, model: str) -> str:
    text = audit.file_text

    if issue.code == "phase_header_format":
        # Pure regex fix — no Ollama needed. Return a preview of affected lines.
        violations = check_bold_phase_headers(text)
        preview = "\n".join(f"  {v[:70]} → **{v.lstrip('#').strip()}.**" for v in violations[:8])
        return preview or "No violations found."

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
        if audit.recipe_type == "technique":
            raw = call_ollama(model, CATEGORY_SYSTEM_TECHNIQUE, text)
            raw = raw.strip()
            if re.match(r"style:\s*Technique Folio", raw):
                return "## Category\n\n" + raw
            return "## Category\n\nstyle: Technique Folio"
        raw = call_ollama(model, CATEGORY_SYSTEM, text)
        raw = raw.strip()
        if re.match(r"cuisine:\s*\w", raw):
            return "## Category\n\n" + raw
        return ""

    elif issue.code == "old_combined_variations":
        # Match both ## heading and **bold** inline heading formats
        m = re.search(
            r'^(?:## |\*\*)(?:Variations\s*[&/]\s*Chef.?s.?Notes?|Chef.?s.?Notes?\s*[&/]\s*Variations)(?:\*\*)?\s*\n(.*?)(?=^## |\Z)',
            text, re.MULTILINE | re.DOTALL | re.IGNORECASE,
        )
        if not m:
            return ""
        section_body = re.sub(r'^---+\s*$', '', m.group(1), flags=re.MULTILINE).strip()
        # Split into paragraphs — handles both "- bullet" and "**Header:** paragraph" formats
        paragraphs = [p.strip() for p in re.split(r'\n\s*\n', section_body) if p.strip()]
        items = [p for p in paragraphs if re.match(r'^[-*\*]\s', p) or re.match(r'^\*\*\w', p)]
        if not items:
            return ""
        _VARIATION_KW = {
            "variant", "version", "alternative", "without", "option",
            "adaptation", "swap", "substitution",
        }
        def _is_variation(item: str) -> bool:
            first = item.splitlines()[0]
            hdr = re.search(r'\*\*([^*]+)\*\*', first)
            return bool(hdr and any(kw in hdr.group(1).lower() for kw in _VARIATION_KW))
        variations = [b for b in items if _is_variation(b)]
        notes = [b for b in items if not _is_variation(b)]
        parts = []
        if variations:
            parts.append("## Variations\n\n" + "\n\n".join(variations))
        if notes:
            parts.append("## Chef's Notes\n\n" + "\n\n".join(notes))
        return "\n\n".join(parts) if parts else ""

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
    if issue.code == "phase_header_format":
        return fix_phase_headers(text)
    if issue.code == "missing_glossary":
        return insert_before(text, issue.fix_content, ["Keywords", "Category"])
    elif issue.code == "missing_keywords":
        return insert_before(text, issue.fix_content, ["Category"])
    elif issue.code == "missing_category":
        return text.rstrip() + "\n\n" + issue.fix_content + "\n"
    elif issue.code == "bad_category_format":
        return replace_section(text, "Category", issue.fix_content)
    elif issue.code == "old_combined_variations":
        pattern = (
            r'^(?:## |\*\*)(?:Variations\s*[&/]\s*Chef.?s.?Notes?|Chef.?s.?Notes?\s*[&/]\s*Variations)(?:\*\*)?'
            r'\s*\n.*?(?=^## |\Z)'
        )
        replacement = issue.fix_content + "\n\n"
        result = re.sub(pattern, replacement, text, flags=re.MULTILINE | re.DOTALL | re.IGNORECASE)
        return result if result != text else text
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
    if issue.code in REGEX_FIXABLE:
        tag = f"{GREEN}[regex-fix]{RESET}"
    elif issue.auto_fix:
        tag = f"{GREEN}[auto-fix]{RESET}"
    else:
        tag = f"{YELLOW}[manual]{RESET}"
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
    deep: bool = False,
    detect_model: str = DEFAULT_DETECT_MODEL,
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
        format_exception = entry.get("formatException", "")

        # --- Audit ---
        audit = audit_file(rid, title, recipe_type, fpath, deep=deep, detect_model=detect_model,
                           format_exception=format_exception)

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
# Metadata sync (--sync-metadata)
# ---------------------------------------------------------------------------

def parse_category_line(line: str) -> dict:
    """Parse 'cuisine: X | style: Y | family: Z | ...' into a dict."""
    result = {}
    for part in line.split("|"):
        part = part.strip()
        if ":" in part:
            key, _, val = part.partition(":")
            result[key.strip()] = val.strip()
    return result


def parse_keywords_section(text: str) -> list[str]:
    """Extract the ## Keywords section and return a list of terms."""
    m = re.search(r"^## Keywords\s*\n(.*?)(?=^##|\Z)", text, re.MULTILINE | re.DOTALL)
    if not m:
        return []
    block = m.group(1).strip()
    # Handle comma-separated inline list or newline-separated list items
    terms = []
    for raw in re.split(r"[,\n]", block):
        term = raw.strip().lstrip("-* ").strip()
        if term:
            terms.append(term)
    return terms


def find_folio_path(recipe_id: str) -> Path | None:
    """Locate the source .md file for a recipe ID in The Manual/."""
    for path in MANUAL_DIR.rglob(f"{recipe_id} *.md"):
        return path
    for path in MANUAL_DIR.rglob(f"{recipe_id}_*.md"):
        return path
    return None


def sync_metadata(data: dict, dry_run: bool = False) -> int:
    """
    Read each folio's ## Category and ## Keywords sections and populate
    the corresponding recipes.json entry with cuisine, style, family,
    course, dietary, and keywords fields.

    Returns the number of entries updated.
    """
    print_header("Metadata Sync — reading folios into recipes.json")
    updated = 0
    missing_files = []

    for entry in data["recipes"]:
        rid = entry["id"]
        fpath = find_folio_path(rid)
        if fpath is None:
            missing_files.append(rid)
            continue

        text = fpath.read_text(encoding="utf-8")

        # Parse ## Category
        cat_m = re.search(r"^## Category\s*\n\s*(.+)", text, re.MULTILINE)
        cat_fields: dict = {}
        if cat_m:
            cat_fields = parse_category_line(cat_m.group(1))

        keywords = parse_keywords_section(text)

        # Build the update dict (only non-empty values)
        updates: dict = {}
        for field in ("cuisine", "style", "family", "course"):
            val = cat_fields.get(field)
            if val:
                updates[field] = val
        updates["dietary"] = cat_fields.get("dietary") or None
        if keywords:
            updates["keywords"] = keywords

        # Detect changes
        changed_keys = []
        for k, v in updates.items():
            if entry.get(k) != v:
                changed_keys.append(k)

        if not changed_keys:
            continue

        summary = ", ".join(f"{k}={repr(updates[k])}" for k in changed_keys)
        print(f"  {DIM}{rid}{RESET}  {summary}")

        if not dry_run:
            entry.update(updates)
        updated += 1

    if missing_files:
        print(f"\n  {YELLOW}No source file found for:{RESET} {', '.join(missing_files)}")

    action = "Would update" if dry_run else "Updated"
    print(f"\n  {GREEN}{action} {updated} entries.{RESET}")

    if not dry_run and updated:
        save_registry(data)
        print(f"  {GREEN}recipes.json saved.{RESET}")

    return updated


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Café Athena audit & repair tool")
    parser.add_argument("--id", help="Audit a single recipe by ID")
    parser.add_argument("--chapter", type=int, help="Audit all recipes in a chapter")
    parser.add_argument("--scan-only", action="store_true", help="Detect issues only, no fixes")
    parser.add_argument("--model", default=DEFAULT_GEN_MODEL, help="Generation model (glossary, keywords, category)")
    parser.add_argument("--detect-model", default=DEFAULT_DETECT_MODEL, help="Detection model (mise violation)")
    parser.add_argument("--deep", action="store_true", help="Enable LLM-based Mise/Method violation check")
    parser.add_argument("--status", action="store_true", help="Show audit status summary")
    parser.add_argument("--pending-only", action="store_true", help="Only audit never-audited recipes")
    parser.add_argument("--auto-approve", action="store_true", help="Apply all generated fixes without prompting")
    parser.add_argument("--sync-metadata", action="store_true", help="Backfill cuisine/style/family/course/keywords/dietary from folio files into recipes.json")
    parser.add_argument("--dry-run", action="store_true", help="With --sync-metadata: show what would change without writing")
    args = parser.parse_args()

    data = load_registry()

    if args.status:
        show_status(data)
        return

    if args.sync_metadata:
        sync_metadata(data, dry_run=args.dry_run)
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
    print(f"Gen model: {args.model} | Detect model: {args.detect_model} | Deep: {args.deep} | Recipes: {len(target_ids)}")

    run_audit(
        target_ids, data, args.model, args.scan_only, args.auto_approve,
        deep=args.deep, detect_model=args.detect_model,
    )


if __name__ == "__main__":
    main()
