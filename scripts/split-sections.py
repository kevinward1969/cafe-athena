#!/usr/bin/env python3
"""
split-sections.py — Split "Chef's Notes / Variations" into two correct sections.

Reads each recipe with the combined heading, sends numbered item labels to Ollama
for classification per v3.2 rules, shows the proposed split, and applies changes.

Usage:
    python3 scripts/split-sections.py              # all flagged recipes
    python3 scripts/split-sections.py --id 03-02   # one recipe
    python3 scripts/split-sections.py --dry-run    # show proposals, write nothing

At each recipe, press:
    y  — apply this split
    n  — skip
    q  — quit
"""

import argparse
import json
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path

BASE = Path(__file__).parent.parent
MANUAL_DIR = BASE / "The Manual"
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:7b"

COMBINED_HEADING = "## Chef's Notes / Variations"

CLASSIFY_PROMPT = """\
You are a culinary editor. Each numbered item below came from a cookbook section \
called "Chef's Notes / Variations". Classify each item number into VARIATIONS or CHEF'S NOTES.

VARIATIONS — use ONLY for items that rebuild the recipe into something fundamentally different:
- A full vegan, gluten-free, or dairy-free rebuild requiring changes to MULTIPLE ingredients AND techniques
- Swapping the primary protein/main ingredient so the dish becomes a different dish entirely
- A named technique alternate that produces a materially different texture or structure

CHEF'S NOTES — use for everything else:
- Any single-ingredient swap, even if called a "variant" → CHEF'S NOTES
- Freezing, make-ahead, or storage instructions → CHEF'S NOTES
- Scaling, serving size, or timing notes → CHEF'S NOTES
- Technique explanations or science notes → CHEF'S NOTES
- Heat/spice adjustments → CHEF'S NOTES
- "If you don't have X, use Y" → CHEF'S NOTES

KEY RULES:
- If only ONE ingredient changes → always CHEF'S NOTES, even if labeled "Variant" or "Substitution"
- Items titled "Substitution", "Alternative", "Substitute", or "Variant" that replace one ingredient with another → always CHEF'S NOTES
- Storage or make-ahead → always CHEF'S NOTES
- When in doubt → CHEF'S NOTES

EXAMPLES:
- "Cheese Substitution: If Boursin is unavailable, use cream cheese..." → CHEF'S NOTES (single ingredient swap)
- "Bacon Variant: Pancetta can substitute for bacon..." → CHEF'S NOTES (single ingredient swap)
- "Vegan Version: Replace butter with coconut oil, eggs with flax eggs, and cream with oat milk..." → VARIATIONS (multiple changes, different dietary profile)
- "Sous Vide Variation: Seal chicken in vacuum bags and cook at 63°C for 2 hours instead of roasting..." → VARIATIONS (technique produces materially different result)

Return ONLY a raw JSON object with two arrays of integers (item numbers). No markdown. No explanation.
Example: {{"variations": [2, 5], "chefs_notes": [1, 3, 4]}}

NUMBERED ITEMS TO CLASSIFY:
{numbered_list}
"""


def find_flagged_files():
    """Return all recipe files containing the combined heading."""
    flagged = []
    for path in sorted(MANUAL_DIR.rglob("*.md")):
        if path.name.startswith("Cafe-Athena"):
            continue
        text = path.read_text(encoding="utf-8")
        if COMBINED_HEADING in text:
            flagged.append(path)
    return flagged


def extract_section(text):
    """
    Return (prefix, content, suffix) where:
      prefix  = everything up to and including the combined heading line
      content = the body of the section (between heading and next ##)
      suffix  = everything from the next ## onward
    """
    pattern = re.compile(
        r"(.*?## Chef's Notes / Variations\n)(.*?)(^## .*)",
        re.DOTALL | re.MULTILINE,
    )
    m = pattern.search(text)
    if not m:
        return None, None, None
    return m.group(1), m.group(2), m.group(3)


def parse_items(content):
    """
    Split section content into individual items.

    Items start at a bold header line (**Title** or * **Title**) or a top-level
    bullet (*). Everything until the next item boundary (or end of content) belongs
    to the same item. Trailing horizontal rules (---) and blank lines are stripped.
    Items that are only a horizontal rule or whitespace are dropped.
    """
    # Remove trailing horizontal rules and whitespace
    content = re.sub(r'\n*^---\s*$', '', content, flags=re.MULTILINE).strip()
    if not content:
        return []

    # Split on lines that start a new item:
    # - lines starting with ** (bold header)
    # - lines starting with * ** (bullet bold header)
    # - lines starting with * [A-Z] or * The/On/For (top-level prose bullets)
    item_start = re.compile(
        r'^(?:\*\s*)?\*\*|^\*\s+(?=[A-Z])',
        re.MULTILINE,
    )

    boundaries = [m.start() for m in item_start.finditer(content)]

    if not boundaries:
        # No bold headers found — treat each non-empty paragraph as an item
        items = [b.strip() for b in re.split(r'\n{2,}', content)]
        return [i for i in items if i and not re.match(r'^-{3,}$', i)]

    items = []
    for idx, start in enumerate(boundaries):
        end = boundaries[idx + 1] if idx + 1 < len(boundaries) else len(content)
        block = content[start:end].strip()
        if block and not re.match(r'^-{3,}$', block):
            items.append(block)

    return items


def item_label(item):
    """Return a short one-line label for display and Ollama input."""
    first = item.splitlines()[0]
    # Strip leading bullet markers
    first = re.sub(r"^\*+\s*", "", first)
    # Strip bold markers for readability
    first = re.sub(r"\*\*", "", first)
    return first[:100]


DEFINITE_NOTES_PATTERNS = re.compile(
    r'\b(substitut\w*|alternative\w*|swap\w*|make.ahead|make ahead|storage|freez\w*|scaling|'
    r'serving size|can replace|can be replaced|instead of|if you don.t have|if unavailable)',
    re.IGNORECASE,
)


def pre_classify(items):
    """
    Programmatically assign Chef's Notes to items that are unambiguously minor.
    Returns (certain_notes_indices, remaining_indices).
    certain_notes_indices will skip Ollama; remaining go to the model.
    """
    certain = []
    remaining = []
    for i, item in enumerate(items):
        if DEFINITE_NOTES_PATTERNS.search(item):
            certain.append(i)
        else:
            remaining.append(i)
    return certain, remaining


def call_ollama(items):
    """
    Send numbered item labels to Ollama.
    Returns dict {"variations": [int,...], "chefs_notes": [int,...]} or None.
    """
    numbered = "\n".join(f"{i+1}. {item_label(item)}" for i, item in enumerate(items))
    prompt = CLASSIFY_PROMPT.format(numbered_list=numbered)

    payload = json.dumps({
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.0},
    }).encode("utf-8")

    req = urllib.request.Request(
        OLLAMA_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            raw = data.get("response", "").strip()
            raw = re.sub(r"^```(?:json)?\n?", "", raw)
            raw = re.sub(r"\n?```$", "", raw)
            m = re.search(r'\{[^{}]*\}', raw)
            if not m:
                print(f"  [error] No JSON object in Ollama response")
                print(f"  [debug] {raw[:200]}")
                return None
            return json.loads(m.group(0))
    except (urllib.error.URLError, urllib.error.HTTPError) as e:
        print(f"  [error] Ollama request failed: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"  [error] JSON parse failed: {e}")
        return None


def build_replacement(items, var_indices, note_indices):
    """Build replacement section text from original item texts and classified indices."""
    variations = [items[i] for i in var_indices if i < len(items)]
    notes = [items[i] for i in note_indices if i < len(items)]

    parts = []
    if variations:
        parts.append("## Variations\n\n" + "\n\n".join(variations) + "\n")
    if notes:
        parts.append("## Chef's Notes\n\n" + "\n\n".join(notes) + "\n")

    return ("\n".join(parts) + "\n") if parts else ""


def process_file(path, dry_run=False):
    """Classify and optionally apply the split for one file. Returns True if applied."""
    text = path.read_text(encoding="utf-8")
    prefix, content, suffix = extract_section(text)

    if content is None:
        print(f"  [skip] Could not parse section in {path.name}")
        return False

    items = parse_items(content)

    if not items:
        # Empty combined section — just rename the heading
        new_text = prefix.replace(COMBINED_HEADING, "## Chef's Notes") + content + suffix
        return _show_and_apply(path, text, new_text, dry_run, [], [], empty=True)

    certain_note_idx, remaining_idx = pre_classify(items)

    var_idx = []
    note_idx = list(certain_note_idx)

    if remaining_idx:
        remaining_items = [items[i] for i in remaining_idx]
        print(f"  Pre-classified {len(certain_note_idx)} as Chef's Notes; "
              f"sending {len(remaining_items)} to Ollama ({MODEL})…")
        result = call_ollama(remaining_items)
        if result is None:
            print("  [skip] Classification failed.")
            return False

        # Model returns 1-based indices into remaining_items; map back to original
        for raw_i in result.get("variations", []):
            if isinstance(raw_i, int) and 1 <= raw_i <= len(remaining_items):
                var_idx.append(remaining_idx[raw_i - 1])
        for raw_i in result.get("chefs_notes", []):
            if isinstance(raw_i, int) and 1 <= raw_i <= len(remaining_items):
                note_idx.append(remaining_idx[raw_i - 1])

        # Unclassified by model → Chef's Notes
        classified = set(var_idx) | set(note_idx)
        for i in remaining_idx:
            if i not in classified:
                note_idx.append(i)
    else:
        print(f"  All {len(items)} item(s) pre-classified as Chef's Notes (no Ollama call needed).")

    replacement = build_replacement(items, var_idx, note_idx)
    heading_line = "## Chef's Notes / Variations\n"
    new_text = prefix[: prefix.rfind(heading_line)] + replacement + suffix

    variations = [items[i] for i in var_idx if i < len(items)]
    notes = [items[i] for i in note_idx if i < len(items)]
    return _show_and_apply(path, text, new_text, dry_run, variations, notes)


def _show_and_apply(path, original, new_text, dry_run, variations, notes, empty=False):
    """Print the proposed split and prompt for confirmation."""
    print()
    if empty:
        print("  [empty section — renaming to ## Chef's Notes]")
    else:
        if variations:
            print("  ── VARIATIONS ──────────────────────────────")
            for v in variations:
                print(f"    • {item_label(v)}")
        else:
            print("  ── VARIATIONS — (none)")
        print()
        if notes:
            print("  ── CHEF'S NOTES ────────────────────────────")
            for n in notes:
                print(f"    • {item_label(n)}")
        else:
            print("  ── CHEF'S NOTES — (none)")
    print()

    if dry_run:
        print("  [dry-run] No changes written.")
        return False

    while True:
        choice = input("  Apply? [y/n/q]: ").strip().lower()
        if choice == "y":
            path.write_text(new_text, encoding="utf-8")
            print("  ✓ Written.")
            return True
        elif choice == "n":
            print("  Skipped.")
            return False
        elif choice == "q":
            print("Quitting.")
            sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description="Split Chef's Notes / Variations sections")
    parser.add_argument("--id", help="Process a single recipe by ID (e.g. 03-02)")
    parser.add_argument("--dry-run", action="store_true", help="Show proposals without writing")
    args = parser.parse_args()

    if args.id:
        matches = list(MANUAL_DIR.rglob(f"{args.id}*.md"))
        if not matches:
            print(f"No file found for ID {args.id}")
            sys.exit(1)
        flagged = [matches[0]]
    else:
        flagged = find_flagged_files()

    if not flagged:
        print("No files with combined heading found.")
        sys.exit(0)

    print(f"Found {len(flagged)} file(s) to process.\n")
    applied = 0

    for i, path in enumerate(flagged, 1):
        print(f"[{i}/{len(flagged)}] {path.name}")
        if process_file(path, dry_run=args.dry_run):
            applied += 1

    print(f"\nDone. {applied} file(s) updated.")


if __name__ == "__main__":
    main()
