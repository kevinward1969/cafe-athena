#!/usr/bin/env python3
"""
clarity_audit.py — Café Athena Clarity Audit Tool

Checks recipe folios for four instructional clarity issues:
  1. Forward references in ingredient sections          (code)
  2. Ambiguous cross-section parentheticals             (code)
  3. Ingredients referenced in Method but not listed    (code)
  4. Multi-action steps in Method                       (Ollama — needs semantic judgment)

Checks 1–3 are fully code-based: fast, deterministic, no false positives from LLM drift.
Check 4 uses a single focused Ollama call per recipe.

Usage:
    python3 scripts/clarity_audit.py                   # all un-audited recipes
    python3 scripts/clarity_audit.py --all             # all 176 recipes
    python3 scripts/clarity_audit.py --id 07-04        # single recipe
    python3 scripts/clarity_audit.py --chapter 7       # one chapter
    python3 scripts/clarity_audit.py --scan-only       # report only, no flag updates
    python3 scripts/clarity_audit.py --skip-llm        # skip Check 4 (no Ollama needed)
    python3 scripts/clarity_audit.py --status          # show clarityAudit coverage
    python3 scripts/clarity_audit.py --model qwen2.5:7b
"""

import argparse
import json
import re
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

DEFAULT_MODEL = "qwen2.5:7b"


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class ClarityIssue:
    check: int
    check_name: str
    line: str
    problem: str


@dataclass
class ClarityAudit:
    recipe_id: str
    title: str
    file_path: Path
    issues: list["ClarityIssue"] = field(default_factory=list)
    llm_skipped: bool = False
    ollama_failed: bool = False

    @property
    def is_clean(self):
        return not self.issues

    @property
    def fully_checked(self):
        return not self.llm_skipped and not self.ollama_failed


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def extract_section(text: str, heading: str) -> str:
    m = re.search(
        rf'^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)',
        text, re.MULTILINE | re.DOTALL,
    )
    return m.group(1).strip() if m else ""


def get_ingredient_lines(text: str) -> list[str]:
    """All bullet lines from the ## Ingredients section."""
    block = extract_section(text, "Ingredients")
    return [
        line.strip()
        for line in block.splitlines()
        if re.match(r'^\s*[*\-]\s+', line)
    ]


def ingredient_token_set(ingredient_lines: list[str]) -> set[str]:
    """
    Build a set of significant lowercase words from ingredient lines.
    Used for fuzzy membership checks — if ANY word from a Method bold item
    appears here, we consider it listed.
    """
    STOP = {
        'the', 'and', 'for', 'from', 'with', 'into', 'onto', 'over', 'under',
        'per', 'each', 'one', 'two', 'cup', 'tbsp', 'tsp', 'large', 'small',
        'medium', 'fine', 'fresh', 'dry', 'use', 'add', 'mix',
    }
    tokens: set[str] = set()
    for line in ingredient_lines:
        # Strip bullet + quantity prefix
        clean = re.sub(r'^\*\-?\s*', '', line)
        clean = re.sub(
            r'^[\d.,/ ]+\s*(?:g|kg|ml|l|oz|lb|tbsp|tsp|cups?|cloves?|sprigs?|'
            r'handfuls?|pinch|dash|x|pcs?|pieces?|sheets?|pkgs?|cans?|jars?|'
            r'heads?|bulbs?|stalks?|bunches?|slices?|strips?)\.?\s*',
            '', clean, flags=re.IGNORECASE,
        )
        # Remove parenthetical qualifiers
        clean = re.sub(r'\([^)]*\)', '', clean)
        # Collect words ≥ 3 chars
        for w in re.findall(r'\b[a-zA-Z]{3,}\b', clean.lower()):
            if w not in STOP:
                tokens.add(w)
    return tokens


# ---------------------------------------------------------------------------
# Check 1: Forward references in ingredient sections (code)
# ---------------------------------------------------------------------------

# Prep-instruction words that are NEVER forward references,
# even when they appear in parentheticals.
PREP_WORDS = {
    'minced', 'chopped', 'diced', 'sliced', 'julienned', 'cleaned', 'trimmed',
    'peeled', 'grated', 'shredded', 'torn', 'halved', 'quartered', 'scored',
    'pounded', 'butterflied', 'deboned', 'deveined', 'boneless', 'skinless',
    'softened', 'melted', 'tempered', 'toasted', 'roasted', 'smoked', 'dried',
    'ground', 'crushed', 'pressed', 'strained', 'rendered', 'reduced',
    'room', 'temperature', 'refrigerated', 'frozen', 'thawed', 'chilled',
    'optional', 'approximately', 'about', 'roughly', 'packed', 'heaped',
    'lightly', 'finely', 'coarsely', 'roughly', 'thinly', 'thickly',
    'sifted', 'zested', 'juiced', 'squeezed', 'rinsed', 'drained', 'patted',
    'separated', 'crumbled', 'flaked', 'shaved',
}

# Parenthetical patterns that indicate a named component or section reference —
# i.e., something the reader hasn't encountered yet.
FORWARD_REF_PATTERNS = [
    # (reserved from X) — only a violation when X is a named component, not a prep word
    (r'\(reserved from (\w+)\)', 'ingredient reserved from a component not yet introduced'),
    # (save X for Y) / (set aside for Y) in ingredient context
    (r'\(save [^)]+for (\w+)\)', '"save for" references a section not yet encountered'),
    # (from the X section) or (from the X)
    (r'\(from the (\w[\w ]*?)\)', '"from the …" references a section not yet encountered'),
    # explicit cross-recipe reference in ingredient list
    (r'\(see \d{2}-\d{2}\)', 'cross-recipe reference in ingredient list without inline description'),
    # (from X) where X is a named component word (garnish, sauce, stock, etc.)
    (r'\(from (garnish|sauce|stock|broth|base|brine|cure|marinade|rub|dressing|emulsion|gel|foam|crisp|crumble)\)',
     '"from …" references a component not yet introduced in the ingredients'),
]


def check_forward_references(text: str) -> list[ClarityIssue]:
    """Check 1: ingredient lines with parentheticals that point to things not yet introduced."""
    issues = []
    for line in get_ingredient_lines(text):
        for pattern, explanation in FORWARD_REF_PATTERNS:
            m = re.search(pattern, line, re.IGNORECASE)
            if not m:
                continue
            # If the pattern captured a word, verify it's not a prep instruction
            if m.lastindex and m.group(1).lower() in PREP_WORDS:
                continue
            issues.append(ClarityIssue(
                check=1,
                check_name="Forward Reference in Ingredient Section",
                line=line[:120],
                problem=explanation,
            ))
            break  # one issue per line
    return issues


# ---------------------------------------------------------------------------
# Check 2: Ambiguous cross-section parentheticals (code)
# ---------------------------------------------------------------------------

AMBIGUOUS_PATTERNS = [
    (r'\(from above\)',                  '"from above" — vague, source not specified'),
    (r'\(see above\)',                   '"see above" — vague, source not specified'),
    (r'\(see below\)',                   '"see below" — forward reference before it is introduced'),
    (r'\(from below\)',                  '"from below" — forward reference before it is introduced'),
    (r'\(to follow\)',                   '"to follow" — forward reference before it is introduced'),
    (r'\(as prepared\)',                 '"as prepared" — does not say where or when'),
    (r'\(as made\)',                     '"as made" — does not say where or when'),
    (r'\bprepared below\b',              '"prepared below" — used before the preparation appears'),
    (r'\(reserved\)(?!\s*from|\s*for)',  '"(reserved)" without specifying reserved from what'),
]


def check_ambiguous_parentheticals(text: str) -> list[ClarityIssue]:
    """Check 2: ingredient lines with vague cross-section parentheticals."""
    issues = []
    for line in get_ingredient_lines(text):
        for pattern, explanation in AMBIGUOUS_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                issues.append(ClarityIssue(
                    check=2,
                    check_name="Ambiguous Cross-Section Parenthetical",
                    line=line[:120],
                    problem=explanation,
                ))
                break
    return issues


# ---------------------------------------------------------------------------
# Check 3: Ingredients referenced in Method but not listed (code)
# ---------------------------------------------------------------------------

# Bold items in Method that start with these prefixes are NOT ingredient references.
NON_INGREDIENT_STARTS = re.compile(
    r'^(phase \d+[:\s]|visual cue[:\s]|sensory cue[:\s]|why[:\s]|note[:\s]|'
    r'tip[:\s]|warning[:\s]|technique[:\s]|storage[:\s]|make-ahead[:\s]|'
    r'the base|the sauce|the protein|the crunch|the garnish|the brine|'
    r'the cure|the rub|the stock|the broth|the gel|the foam|the crisp)',
    re.IGNORECASE,
)

# Single action verbs — bold text that is just a verb is not an ingredient.
ACTION_VERBS = {
    'add', 'season', 'heat', 'cook', 'cooking', 'stir', 'fold', 'whisk', 'sear',
    'roast', 'reduce', 'reduction', 'strain', 'blend', 'chill', 'rest', 'serve',
    'plate', 'finish', 'transfer', 'deglaze', 'baste', 'brine', 'cure', 'smoke',
    'grill', 'fry', 'boil', 'simmer', 'sauté', 'saute', 'poach', 'steam',
    'blanch', 'render', 'caramelize', 'toast', 'press', 'coat', 'dredge', 'dust',
    'combine', 'mix', 'toss', 'taste', 'adjust', 'remove', 'reserve', 'cut',
    'slice', 'dice', 'chop', 'mince', 'grate', 'zest', 'peel', 'drain', 'pat',
    'pound', 'score', 'truss', 'tie', 'temper', 'mount', 'emulsify', 'pass',
    'allow', 'let', 'continue', 'repeat', 'check', 'ensure', 'bring', 'return',
    'place', 'pour', 'pull', 'push', 'flip', 'turn', 'cover', 'uncover', 'wrap',
    'unwrap', 'discard', 'keep', 'hold', 'set', 'start', 'stop', 'begin',
    'create', 'build', 'make', 'prepare', 'assemble', 'arrange', 'layer',
    'spread', 'drizzle', 'dot', 'scatter', 'garnish', 'swipe', 'quenelle',
    # Additional action/technique verbs
    'bake', 'laminate', 'touch', 'wait', 'inject', 'infuse', 'hydrate', 'knead',
    'shape', 'form', 'roll', 'fold', 'crimp', 'seal', 'brush', 'glaze', 'shock',
    'broil', 'wipe', 'minced', 'cubed', 'julienned', 'diced', 'sliced', 'chopped',
    'dusting', 'seasoning', 'coating', 'resting', 'chilling', 'finishing',
}

# Equipment words — bold items that are primarily equipment are not ingredients
EQUIPMENT_WORDS = {
    'bowl', 'pan', 'pot', 'skillet', 'saucepan', 'plate', 'spoon', 'blender',
    'processor', 'knife', 'board', 'rack', 'tray', 'sheet', 'mold', 'ring',
    'bag', 'sieve', 'strainer', 'spatula', 'whisk', 'towel', 'cloth', 'wrap',
    'liner', 'parchment', 'silpat', 'thermometer', 'scale', 'timer', 'ladle',
}

# Words too generic to be useful for ingredient matching — also includes
# in-recipe prepared components that are built from listed ingredients.
MATCH_STOPWORDS = {
    'the', 'and', 'for', 'from', 'with', 'into', 'onto', 'over', 'under',
    'per', 'each', 'one', 'two', 'hot', 'cold', 'warm', 'cool', 'room',
    'large', 'small', 'medium', 'whole', 'half', 'fresh', 'dry', 'raw',
    'cooked', 'fried', 'baked', 'grilled', 'liquid', 'solid',
    # Prepared-component nouns — always built from listed ingredients in-recipe
    'emulsion', 'mixture', 'brine', 'marinade', 'cure', 'rub', 'base',
    'sauce', 'broth', 'stock', 'fond', 'gel', 'foam', 'crisp', 'crumble',
    'aromatic', 'aromatics', 'reduction', 'infusion', 'vinaigrette',
    # Equipment/appliance mode settings (Instant Pot, stand mixer, etc.)
    'pressure', 'release', 'natural', 'high', 'low', 'full',
    # Texture and visual descriptor labels (not ingredient names)
    'peak', 'peaks', 'stiff', 'color', 'colour', 'setting', 'possible',
    # Culinary technique labels used as step markers
    'liaison', 'matrix', 'die', 'lowest', 'highest',
    # Spatial/directional instruction terms
    'side', 'sides', 'short', 'long', 'end', 'grain', 'against', 'time',
    # Coating/technique qualifier words
    'coarse', 'fine', 'light', 'aggressively', 'wet', 'binder', 'batches',
}


def check_unlisted_method_ingredients(text: str) -> list[ClarityIssue]:
    """Check 3: bold items in Method that have no corresponding ingredient."""
    ingredient_lines = get_ingredient_lines(text)
    if not ingredient_lines:
        return []  # No ingredients section — skip (technique folio or collection)

    tokens = ingredient_token_set(ingredient_lines)
    method_text = extract_section(text, "Method")
    if not method_text:
        return []

    issues = []
    seen: set[str] = set()  # deduplicate same bold text appearing multiple times

    for m in re.finditer(r'\*\*([^*\n]{2,60})\*\*', method_text):
        item = m.group(1).strip()
        item_key = item.lower()

        if item_key in seen:
            continue
        seen.add(item_key)

        # Skip non-ingredient starts (labels, cues, section names)
        if NON_INGREDIENT_STARTS.match(item):
            continue

        # Skip phase headers and statement-style sentences
        if re.match(r'^Phase \d+', item) or item.endswith('.'):
            continue

        # Skip labels (anything ending with a colon)
        if item.rstrip().endswith(':'):
            continue

        # Skip time expressions: "2 minutes", "45–60 seconds", "at least 2 hours", etc.
        if re.search(r'\b\d+', item) or re.match(r'^(at least|about|approximately|up to)\b', item, re.IGNORECASE):
            continue

        # Skip section headers containing em-dash or en-dash (e.g. "Option A — By Hand", "Sauté – More")
        if '—' in item or '–' in item or ' - ' in item:
            continue

        # Skip appliance mode labels containing slash (e.g. "Meat/Stew")
        if '/' in item:
            continue

        # Skip negative instruction phrases (e.g. "Do not touch them")
        if re.match(r"^do not\b|^don't\b|^never\b", item, re.IGNORECASE):
            continue

        # Skip Option-style method subheadings (e.g. "Option A", "Option B")
        if re.match(r'^option [a-z]\b', item, re.IGNORECASE):
            continue

        # Build word set for remaining checks
        item_words_set = {w.lower() for w in re.findall(r'\b[a-zA-Z]{3,}\b', item)}

        # Skip if any word is an action verb or equipment (catches "carryover cooking", etc.)
        if item_words_set & (ACTION_VERBS | EQUIPMENT_WORDS):
            continue

        # Collect significant words from this bold item
        item_words = [
            w.lower() for w in re.findall(r'\b[a-zA-Z]{3,}\b', item)
            if w.lower() not in MATCH_STOPWORDS
        ]
        if not item_words:
            continue

        # If ANY significant word appears in ingredient tokens → listed, skip
        if any(w in tokens for w in item_words):
            continue

        # Nothing matched — this ingredient is not listed
        issues.append(ClarityIssue(
            check=3,
            check_name="Ingredient Referenced in Method but Not Listed",
            line=f"**{item}**",
            problem="Bold item in Method has no corresponding entry in the Ingredients block.",
        ))

    return issues


# ---------------------------------------------------------------------------
# Check 4: Multi-action steps (Ollama)
# ---------------------------------------------------------------------------

MULTIACTION_SYSTEM = """\
You are checking Method steps in a recipe for multi-action violations.

A violation is a single step that forces the cook to perform two DISTINCT physical actions \
simultaneously or in direct sequence, using these specific connectors:
  • "while [gerund], [imperative]"  — e.g. "While the brine cools, process the vegetables."
  • "[action], then [distinct action]" — e.g. "Sear the beef, then deglaze with wine."

NOT a violation:
  • One action followed by a result cue: "Sear until deeply browned."
  • Sequential steps on the same ingredient: "Stir until smooth, about 2 minutes."
  • Setup phrases: "Working quickly, add the butter."
  • Two sentences that are part of one continuous motion.
  • A timing condition before a single action: "While still hot, transfer to a blender." — the "while still hot" is a temperature cue, not a second action.
  • Descriptive elaboration of a single motion: "Whisk vigorously, reaching the bottom of the bowl."
  • Classic emulsification technique: "While whisking constantly, drizzle in the oil." — this is ONE unified motion.
  • A single-word wait step: "Wait 15–30 seconds." — one action.
  • Urgency notes: "Working quickly while the rice is still hot" — not a second action.

Be very conservative. Only flag steps where a cook literally cannot complete both actions at once as a single unified motion.

Output format:
VIOLATION_4: [quote the exact connector phrase or step, max 80 chars]
...one line per violation.

If no violations: output exactly PASS_4
Output NOTHING else.
"""


def check_multi_action_steps(text: str, model: str) -> tuple[list[ClarityIssue], bool]:
    """Check 4: Ollama-based detection of multi-action Method steps."""
    method_text = extract_section(text, "Method")
    if not method_text:
        return [], False

    raw = call_ollama(model, MULTIACTION_SYSTEM, method_text[:4000])
    if not raw:
        return [], True  # Ollama failed

    if raw.strip() == "PASS_4":
        return [], False

    issues = []
    for line in raw.splitlines():
        line = line.strip().lstrip("*- ")
        if line.startswith("VIOLATION_4:"):
            quoted = line[len("VIOLATION_4:"):].strip().strip("*_`\"'")
            # Guard: skip if LLM echoed the PASS token
            if quoted and not re.match(r'^PASS', quoted, re.IGNORECASE):
                issues.append(ClarityIssue(
                    check=4,
                    check_name="Multi-Action Step",
                    line=quoted[:120],
                    problem="Step chains two distinct physical actions — consider splitting into two steps.",
                ))

    return issues, False


# ---------------------------------------------------------------------------
# Ollama helpers
# ---------------------------------------------------------------------------

def call_ollama(model: str, system: str, content: str, timeout: int = 120) -> str:
    payload = json.dumps({
        "model": model,
        "system": system,
        "prompt": content,
        "stream": False,
        "options": {"temperature": 0.1, "num_predict": 400},
    }).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_URL, data=payload,
        headers={"Content-Type": "application/json"}, method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8")).get("response", "").strip()
    except urllib.error.URLError:
        return ""


def check_ollama_available(model: str) -> bool:
    try:
        payload = json.dumps({
            "model": model, "prompt": "ping", "stream": False,
            "options": {"num_predict": 1},
        }).encode("utf-8")
        req = urllib.request.Request(
            OLLAMA_URL, data=payload,
            headers={"Content-Type": "application/json"}, method="POST",
        )
        with urllib.request.urlopen(req, timeout=10):
            return True
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Main audit function
# ---------------------------------------------------------------------------

def audit_clarity(
    recipe_id: str,
    title: str,
    fpath: Path,
    skip_llm: bool,
    model: str,
) -> ClarityAudit:
    text = fpath.read_text(encoding="utf-8")
    result = ClarityAudit(recipe_id=recipe_id, title=title, file_path=fpath)

    # Checks 1–3: code-based, always run
    result.issues.extend(check_forward_references(text))
    result.issues.extend(check_ambiguous_parentheticals(text))
    result.issues.extend(check_unlisted_method_ingredients(text))

    # Check 4: Ollama
    if skip_llm:
        result.llm_skipped = True
    else:
        llm_issues, failed = check_multi_action_steps(text, model)
        if failed:
            result.ollama_failed = True
        else:
            result.issues.extend(llm_issues)

    result.issues.sort(key=lambda i: i.check)
    return result


# ---------------------------------------------------------------------------
# recipes.json helpers
# ---------------------------------------------------------------------------

def load_registry() -> dict:
    with open(RECIPES_JSON) as f:
        return json.load(f)


def save_registry(data: dict):
    with open(RECIPES_JSON, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def get_entry(data: dict, recipe_id: str) -> dict | None:
    for r in data["recipes"]:
        if r["id"] == recipe_id:
            return r
    return None


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

BOLD   = "\033[1m"
RED    = "\033[91m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
CYAN   = "\033[96m"
DIM    = "\033[2m"
RESET  = "\033[0m"

CHECK_LABELS = {
    1: "Check 1: Forward Reference",
    2: "Check 2: Ambiguous Parenthetical",
    3: "Check 3: Unlisted Method Ingredient",
    4: "Check 4: Multi-Action Step",
}


def print_header(text: str):
    print(f"\n{BOLD}{CYAN}{'─' * 60}{RESET}")
    print(f"{BOLD}{CYAN}{text}{RESET}")
    print(f"{BOLD}{CYAN}{'─' * 60}{RESET}")


def show_status(data: dict):
    recipes = data["recipes"]
    true_count  = sum(1 for r in recipes if r.get("stages", {}).get("clarityAudit"))
    false_count = len(recipes) - true_count
    print_header("clarityAudit Coverage")
    print(f"  {GREEN}Audited (True):{RESET}   {true_count:>4}")
    print(f"  {YELLOW}Pending (False):{RESET}  {false_count:>4}")
    print(f"  {DIM}Total:{RESET}            {len(recipes):>4}")


# ---------------------------------------------------------------------------
# Main run loop
# ---------------------------------------------------------------------------

def run(
    target_ids: list[str],
    data: dict,
    model: str,
    scan_only: bool,
    skip_llm: bool,
):
    id_to_entry = {r["id"]: r for r in data["recipes"]}

    id_to_file: dict[str, Path] = {}
    for f in MANUAL_DIR.rglob("*.md"):
        m = re.match(r"^(\d{2}-\d{2}(?:\.\d+)?)", f.name)
        if m:
            id_to_file[m.group(1)] = f

    total = len(target_ids)
    clean_count = 0
    issues_count = 0
    ollama_fail_count = 0
    not_found: list[str] = []
    registry_dirty = False

    if not skip_llm:
        print(f"{DIM}Checking Ollama ({model})...{RESET}", end="", flush=True)
        if check_ollama_available(model):
            print(f" {GREEN}ready{RESET}")
        else:
            print(f" {RED}unavailable — running checks 1–3 only (skip Check 4){RESET}")
            skip_llm = True

    mode_parts = ["checks 1–3 (code)"]
    if not skip_llm:
        mode_parts.append(f"check 4 (Ollama/{model})")
    print(f"\n{BOLD}Café Athena — Clarity Audit{RESET}")
    print(f"Checks: {', '.join(mode_parts)} | Recipes: {total} | scan-only: {scan_only}\n")

    issues_by_recipe: list[tuple[str, str, list[ClarityIssue]]] = []

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
        print(f"[{idx:>3}/{total}] {DIM}{rid}{RESET} {title[:50]:<50}", end="", flush=True)
        t0 = time.time()

        result = audit_clarity(rid, title, fpath, skip_llm=skip_llm, model=model)
        elapsed = time.time() - t0

        if result.ollama_failed:
            ollama_fail_count += 1
            print(f"  {RED}[ollama error]{RESET} ({elapsed:.1f}s)")
            continue

        if result.is_clean:
            clean_count += 1
            print(f"  {GREEN}✓{RESET} ({elapsed:.1f}s)")
            if not scan_only:
                entry["stages"]["clarityAudit"] = True
                registry_dirty = True
        else:
            issues_count += 1
            llm_note = f" {DIM}[no check 4]{RESET}" if result.llm_skipped else ""
            print(f"  {YELLOW}⚠ {len(result.issues)} issue(s){RESET}{llm_note} ({elapsed:.1f}s)")
            issues_by_recipe.append((rid, title, result.issues))

    if registry_dirty:
        save_registry(data)

    if issues_by_recipe:
        print_header(f"Issues Found — {len(issues_by_recipe)} recipe(s)")
        for rid, title, issues in issues_by_recipe:
            print(f"\n  {BOLD}{rid} — {title}{RESET}")
            for issue in issues:
                label = CHECK_LABELS.get(issue.check, f"Check {issue.check}")
                print(f"    {YELLOW}[{label}]{RESET}")
                print(f"      Line:    {DIM}{issue.line}{RESET}")
                print(f"      Problem: {issue.problem}")

    print_header("Clarity Audit Summary")
    print(f"  Total scanned:     {total}")
    print(f"  {GREEN}Clean (marked ✓):{RESET}  {clean_count}")
    print(f"  {YELLOW}Issues found:{RESET}      {issues_count}")
    if ollama_fail_count:
        print(f"  {RED}Ollama failures:{RESET}   {ollama_fail_count}")
    if not_found:
        print(f"  {RED}Not found:{RESET}         {len(not_found)} — {not_found}")
    if scan_only:
        print(f"\n  {DIM}--scan-only: no recipes.json changes written{RESET}")
    elif clean_count:
        print(f"\n  {GREEN}clarityAudit: True set for {clean_count} recipe(s){RESET}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Café Athena clarity audit tool")
    parser.add_argument("--id",        help="Audit a single recipe by ID")
    parser.add_argument("--chapter",   type=int, help="Audit all recipes in a chapter")
    parser.add_argument("--all",       action="store_true", help="Audit all 176 recipes")
    parser.add_argument("--scan-only", action="store_true", help="Report only — do not update recipes.json")
    parser.add_argument("--skip-llm",  action="store_true", help="Skip Check 4 (no Ollama needed)")
    parser.add_argument("--model",     default=DEFAULT_MODEL, help=f"Ollama model for Check 4 (default: {DEFAULT_MODEL})")
    parser.add_argument("--status",    action="store_true", help="Show clarityAudit coverage and exit")
    args = parser.parse_args()

    data = load_registry()

    if args.status:
        show_status(data)
        return

    all_recipes = data["recipes"]

    if args.id:
        target_ids = [args.id]
    elif args.chapter:
        target_ids = [r["id"] for r in all_recipes if r.get("chapter") == args.chapter]
    elif args.all:
        target_ids = [r["id"] for r in all_recipes]
    else:
        target_ids = [
            r["id"] for r in all_recipes
            if not r.get("stages", {}).get("clarityAudit")
        ]

    if not target_ids:
        print(f"{GREEN}All recipes already have clarityAudit: True.{RESET}")
        return

    run(target_ids, data, model=args.model, scan_only=args.scan_only, skip_llm=args.skip_llm)


if __name__ == "__main__":
    main()
