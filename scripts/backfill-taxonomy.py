#!/usr/bin/env python3
"""
backfill-taxonomy.py — Phase 2 of the Site IA & Taxonomy Upgrade

Appends `family:` and `course:` fields to the ## Category line of every folio
in The Manual/ that doesn't already have them, using the vocabulary defined in
Guidance/Taxonomy.md and PROJECT_BRIEF_SITE_IA.md.

Usage:
    python3 scripts/backfill-taxonomy.py            # dry-run: show what would change
    python3 scripts/backfill-taxonomy.py --apply    # write changes to files
    python3 scripts/backfill-taxonomy.py --chapter 10   # target one chapter
    python3 scripts/backfill-taxonomy.py --id 10-01     # target one folio
"""

import argparse
import re
import sys
from pathlib import Path

BASE = Path(__file__).parent.parent
MANUAL_DIR = BASE / "The Manual"

# ---------------------------------------------------------------------------
# Taxonomy — family assignments per folio ID
# Source: Guidance/Taxonomy.md + PROJECT_BRIEF_SITE_IA.md
# ---------------------------------------------------------------------------

FAMILY_MAP: dict[str, str] = {
    # Chapter 1 — The Lab
    "01-01": "Heat & Thermodynamics",
    "01-02": "Salinity & Seasoning",
    "01-03": "Starch & Dough Science",
    "01-04": "Emulsification & Bonding",
    "01-05": "Emulsification & Bonding",
    "01-06": "Emulsification & Bonding",
    "01-07": "Hydrocolloids & Gels",
    "01-08": "Starch & Dough Science",
    "01-09": "Starch & Dough Science",
    "01-10": "Starch & Dough Science",
    "01-11": "Preservation & Transformation",
    "01-12": "Hydrocolloids & Gels",
    "01-13": "Heat & Thermodynamics",
    "01-14": "Hydrocolloids & Gels",       # Collagen Hydrolysis & Extraction
    "01-15": "Fermentation",
    "01-16": "Fermentation",
    "01-17": "Fermentation",
    "01-18": "Fermentation",
    "01-19": "Fermentation",
    "01-20": "Preservation & Transformation",
    "01-21": "Fermentation",
    "01-22": "Preservation & Transformation",
    "01-23": "Preservation & Transformation",
    # Chapter 2 — The Foundation
    "02-01": "Kitchen Management",
    "02-02": "Kitchen Management",
    "02-03": "Kitchen Management",
    "02-04": "Skills",
    "02-05": "Kitchen Management",
    "02-06": "Kitchen Management",
    "02-07": "Kitchen Management",
    # Chapter 3 — Garde Manger
    "03-01": "Amuse-Bouche",
    "03-02": "Canapé",
    "03-03": "Cold Plate",
    "03-04": "Cold Plate",
    "03-05": "Tartare & Raw",
    "03-06": "Preserved & Pickled",
    "03-07": "Mousse & Pâté",
    "03-08": "Mousse & Pâté",
    "03-09": "Salad",
    "03-10": "Mousse & Pâté",
    "03-11": "Cold Plate",
    "03-12": "Mousse & Pâté",
    "03-13": "Mousse & Pâté",
    "03-14": "Canapé",
    # Chapter 4 — The Mill
    "04-01": "Bread",
    "04-02": "Rice",
    "04-03": "Rice",
    "04-04": "Pasta",
    "04-05": "Bread",
    "04-06": "Polenta",
    "04-07": "Gnocchi",
    "04-08": "Pasta",
    "04-09": "Polenta",
    "04-10": "Pasta",
    "04-11": "Bread",
    "04-12": "Grain & Legume",
    "04-13": "Pasta",
    "04-14": "Bread",
    # Chapter 5 — The Fishmonger
    "05-01": "Mollusc",
    "05-02": "Finfish",
    "05-03": "Finfish",
    "05-04": "Finfish",
    # Chapter 6 — The Poulterer
    "06-01": "Chicken",
    "06-02": "Chicken",
    "06-03": "Duck",
    "06-04": "Chicken",
    "06-05": "Chicken",
    "06-06": "Chicken",
    # Chapter 7 — The Butcher
    "07-01": "Beef",
    "07-02": "Ground & Formed",
    "07-03": "Pork",
    "07-04": "Beef",
    "07-05": "Beef",
    "07-06": "Beef",
    "07-07": "Beef",
    "07-08": "Beef",
    "07-09": "Beef",
    "07-10": "Beef",
    "07-10_2": "Beef",
    "07-11": "Beef",
    "07-12": "Pork",
    "07-13": "Beef",
    # Chapter 8 — The Field
    "08-01": "Mushroom",
    "08-02": "Roasted & Grilled",
    "08-03": "Mash & Purée",
    "08-04": "Salad & Dressed",
    "08-05": "Salad & Dressed",
    "08-06": "Tuber",
    "08-07": "Roasted & Grilled",
    "08-08": "Stuffed",
    "08-09": "Steamed & Braised",
    "08-10": "Tuber",
    # Chapter 9 — The Pâtissier
    "09-01": "Brownie & Bar",
    "09-02": "Cookie",
    "09-03": "Cookie",
    "09-04": "Small Cake & Pastry",
    "09-05": "Posset & Panna Cotta",
    "09-06": "Brownie & Bar",
    # Chapter 10 — Stocks & Mother Sauces
    "10-01": "Stock",
    "10-02": "Cold Blended Sauce",
    "10-03": "Mother Sauce",
    "10-04": "Derivative Sauce",
    "10-05": "Derivative Sauce",
    "10-06": "Derivative Sauce",
    "10-07": "Compound Butter",
    "10-08": "Mother Sauce",
    "10-09": "Emulsion",
    "10-10": "Derivative Sauce",
    "10-11": "Derivative Sauce",
    "10-12": "Cream Sauce",
    "10-13": "Ragù & Meat Sauce",
    "10-14": "Cold Blended Sauce",
    "10-15": "Mother Sauce",
    "10-16": "Mother Sauce",
    "10-17": "Stock",
    "10-18": "Mother Sauce",
    "10-19": "Derivative Sauce",
    "10-20": "Cold Blended Sauce",
    "10-21": "Cream Sauce",
    "10-22": "Compound Butter",
    "10-23": "Dipping Sauce",
    "10-24": "Dipping Sauce",
    "10-25": "Emulsion",
    # Chapter 11 — Spice Blends & Oils
    "11-01": "Herb Oil",
    "11-02": "Specialty Salt",
    "11-03": "Specialty Salt",
    "11-04": "Specialty Salt",
    "11-05": "Wet Paste",
    "11-06": "Dry Spice Blend",
    # Chapter 12 — Les Fonds
    "12-01": "Platform & Vessel",
    "12-02": "Pastry Dough",
    "12-03": "Pastry Dough",
    "12-04": "Pastry Dough",
    "12-05": "Pastry Dough",
    "12-06": "Pastry Dough",
    "12-07": "Pasta Dough",
    "12-08": "Pasta Dough",
    "12-09": "Pasta Dough",
    "12-10": "Pasta Dough",
    "12-11": "Cream & Filling",
    "12-12": "Cream & Filling",
    "12-13": "Cream & Filling",
    "12-14": "Cream & Filling",
    "12-15": "Platform & Vessel",
    "12-16": "Platform & Vessel",
    "12-17": "Garnish & Component",
    "12-18": "Batter & Coating",
    "12-19": "Batter & Coating",
    "12-20": "Garnish & Component",
    "12-21": "Batter & Coating",
    "12-22": "Garnish & Component",
    "12-23": "Caramel & Sugar",
}


def get_course(folio_id: str) -> str | None:
    """
    Return the course value for a folio.

    Rules (from PROJECT_BRIEF_SITE_IA.md):
      Ch. 1–2  — omit (technique; concept doesn't map cleanly)
      Ch. 3–8  — Dinner (restaurant service context; largest reasonable default)
      Ch. 9    — Dessert
      Ch. 10–12 — Component
    """
    chapter = int(folio_id.split("-")[0])
    if chapter in (1, 2):
        return None
    if chapter == 9:
        return "Dessert"
    if chapter >= 10:
        return "Component"
    return "Dinner"


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def parse_category_line(line: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for part in line.split("|"):
        part = part.strip()
        if ":" in part:
            key, _, val = part.partition(":")
            fields[key.strip()] = val.strip()
    return fields


def format_category_line(fields: dict[str, str]) -> str:
    """Reassemble fields in canonical order."""
    order = ["cuisine", "style", "family", "course", "dietary"]
    parts = [f"{k}: {fields[k]}" for k in order if k in fields and fields[k]]
    return " | ".join(parts)


def extract_folio_id(filename: str) -> str | None:
    m = re.match(r"^(\d{2}-\d+(?:_\d+)?)", filename)
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# Core processing
# ---------------------------------------------------------------------------

def process_folio(path: Path, folio_id: str, apply: bool) -> str | None:
    """
    Inspect one folio and optionally update its ## Category line.
    Returns a description of the change, or None if no change needed.
    """
    text = path.read_text(encoding="utf-8")

    cat_match = re.search(r"(^## Category\s*\n)([ \t]*(.+))", text, re.MULTILINE)
    if not cat_match:
        return f"  [SKIP] no ## Category section found"

    cat_line = cat_match.group(3).strip()
    fields = parse_category_line(cat_line)

    family = FAMILY_MAP.get(folio_id)
    course = get_course(folio_id)

    already_has_family = "family" in fields
    already_has_course = "course" in fields

    if already_has_family and already_has_course:
        return None  # nothing to do

    if family:
        fields["family"] = family
    elif not already_has_family:
        return f"  [WARN] {folio_id} not in FAMILY_MAP — skipping family"

    if course and not already_has_course:
        fields["course"] = course

    new_cat_line = format_category_line(fields)

    if new_cat_line == cat_line:
        return None

    change_desc = f"  {folio_id}  →  {new_cat_line}"

    if apply:
        old_block = cat_match.group(2)
        indent = cat_match.group(2)[: len(cat_match.group(2)) - len(cat_match.group(2).lstrip())]
        new_block = indent + new_cat_line
        new_text = text[: cat_match.start(2)] + new_block + text[cat_match.end(2):]
        path.write_text(new_text, encoding="utf-8")

    return change_desc


def find_all_folios(chapter_filter: int | None = None) -> list[tuple[Path, str]]:
    """Return (path, folio_id) pairs sorted by ID."""
    results = []
    for path in MANUAL_DIR.rglob("*.md"):
        fid = extract_folio_id(path.name)
        if fid is None:
            continue
        if chapter_filter is not None:
            ch = int(fid.split("-")[0])
            if ch != chapter_filter:
                continue
        results.append((path, fid))
    results.sort(key=lambda x: x[1])
    return results


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Backfill family: and course: into folio ## Category sections")
    parser.add_argument("--apply", action="store_true", help="Write changes (default: dry-run)")
    parser.add_argument("--chapter", type=int, help="Process only this chapter number")
    parser.add_argument("--id", help="Process only this folio ID")
    args = parser.parse_args()

    folios = find_all_folios(chapter_filter=args.chapter)
    if args.id:
        folios = [(p, fid) for p, fid in folios if fid == args.id]

    if not folios:
        print("No folios matched.")
        sys.exit(0)

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"backfill-taxonomy.py — {mode} — {len(folios)} folios\n")

    changed = 0
    skipped = 0
    warned = 0

    for path, fid in folios:
        result = process_folio(path, fid, apply=args.apply)
        if result is None:
            skipped += 1
        elif "[SKIP]" in result or "[WARN]" in result:
            print(result)
            warned += 1
        else:
            print(result)
            changed += 1

    action = "Updated" if args.apply else "Would update"
    print(f"\n{action} {changed} folios.  Skipped (already set): {skipped}.  Warnings: {warned}.")
    if not args.apply and changed:
        print("Re-run with --apply to write changes.")


if __name__ == "__main__":
    main()
