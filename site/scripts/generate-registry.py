#!/usr/bin/env python3
"""
Café Athena — Recipe Registry Generator

Scans The Manual/ and produces recipes.json in the project root.
Run this once to bootstrap the registry. After that, use /register-recipe
and /sync-registry workflows to keep it current.

Usage: python3 site/scripts/generate-registry.py
"""

import os
import re
import json
from pathlib import Path
from datetime import date

# ── Configuration ──────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
MANUAL_DIR = PROJECT_ROOT / "The Manual"
REGISTRY_FILE = PROJECT_ROOT / "recipes.json"

CHAPTER_NAMES = {
    1:  "The Lab",
    2:  "The Foundation",
    3:  "Garde Manger",
    4:  "The Mill",
    5:  "The Fishmonger",
    6:  "The Poulterer",
    7:  "The Butcher",
    8:  "The Field",
    9:  "The Pâtissier",
    10: "Stocks & Mother Sauces",
    11: "Spice Blends & Oils",
}

# Regex: matches XX-YY, XX-YY.N, or XX-YYa at the start of a filename
INDEX_RE = re.compile(r'^(\d{2}-\d{2}(?:\.\d+)?[a-z]?)')

# ── Helpers ────────────────────────────────────────────────────────────────────

def extract_index(filename: str) -> str | None:
    """Extract XX-YY or XX-YYa index from a filename."""
    filename = filename.lstrip('[').replace(']', '')
    m = INDEX_RE.match(filename)
    return m.group(1) if m else None

def extract_title(filename: str) -> str:
    """Extract display title from a filename."""
    name = Path(filename).stem
    name = re.sub(r'^\[?\d{2}-\d{2}(?:\.\d+)?[a-z]?\]?\s*', '', name)
    name = re.sub(r'^(Café Athena\s*[-–]\s*|Technique Folio\s*[-–]\s*)', '', name)
    return name.strip()

def detect_type(filename: str) -> str:
    return "technique" if "Technique Folio" in filename else "recipe"

def has_glossary(filepath: Path) -> bool:
    try:
        content = filepath.read_text(encoding='utf-8')
        return bool(re.search(r'^## Glossary', content, re.MULTILINE))
    except Exception:
        return False

def find_hero_image(chapter_dir: Path, index: str) -> tuple[bool, bool, bool]:
    """
    Returns (has_hero, is_optimized, is_png_only).
    Prefers .webp over .png — consistent with prepare-content.sh logic.
    """
    webp = chapter_dir / f"{index}.webp"
    png = chapter_dir / f"{index}.png"
    if webp.exists():
        return True, True, False
    if png.exists():
        return True, False, True
    return False, False, False

def find_reference_images(chapter_dir: Path, index: str) -> tuple[bool, bool | None]:
    """
    Returns (has_refs, refs_processed).
    refs_processed is None if no refs, True if all webp, False if any png remain.
    """
    # Reference images follow XX-YYa, XX-YYb, etc. pattern
    base = re.sub(r'[a-z]$', '', index)  # strip letter suffix if index itself has one
    webps = list(chapter_dir.glob(f"{base}[a-z].webp"))
    pngs = list(chapter_dir.glob(f"{base}[a-z].png"))

    # Exclude the hero image itself (XX-YY.webp / XX-YY.png without letter)
    webps = [f for f in webps if re.search(r'[a-z]\.webp$', f.name)]
    pngs = [f for f in pngs if re.search(r'[a-z]\.png$', f.name)]

    total = len(webps) + len(pngs)
    if total == 0:
        return False, None
    processed = len(pngs) == 0
    return True, processed

# ── Main ───────────────────────────────────────────────────────────────────────

def build_entry(chapter_num: int, md_file: Path, chapter_dir: Path) -> dict | None:
    index = extract_index(md_file.name)
    if not index:
        return None

    title = extract_title(md_file.name)
    entry_type = detect_type(md_file.name)
    chapter_name = CHAPTER_NAMES.get(chapter_num, "Unknown")

    glossary_done = has_glossary(md_file)
    has_hero, hero_optimized, hero_is_png = find_hero_image(chapter_dir, index)
    has_refs, refs_processed = find_reference_images(chapter_dir, index)

    return {
        "id": index,
        "title": title,
        "chapter": chapter_num,
        "chapterName": chapter_name,
        "type": entry_type,
        "added": str(date.today()),
        "stages": {
            "formatAudit": False,
            "keywordPull": False,
            "glossaryPull": glossary_done,
            "heroImage": has_hero,
            "heroImageOptimized": hero_optimized,
            "referenceImages": has_refs,
            "referenceImagesProcessed": refs_processed,
            "deployed": False,
        }
    }


def generate():
    entries = []

    for chapter_dir in sorted(MANUAL_DIR.glob("Chapter*/")):
        m = re.search(r'Chapter\s+(\d+)', chapter_dir.name)
        if not m:
            continue
        chapter_num = int(m.group(1))

        for md_file in sorted(chapter_dir.glob("*.md")):
            entry = build_entry(chapter_num, md_file, chapter_dir)
            if entry:
                entries.append(entry)

    # Sort by id for consistent ordering
    entries.sort(key=lambda e: e["id"])

    registry = {
        "_meta": {
            "description": "Café Athena recipe pipeline registry. Tracks stage completion for every recipe and technique folio.",
            "generatedOn": str(date.today()),
            "stages": {
                "formatAudit": "Format audit run via /format-audit",
                "keywordPull": "Keywords + Category sections added via /keyword-pull",
                "glossaryPull": "Glossary terms extracted via /glossary-pull",
                "heroImage": "Hero image exists in chapter folder (PNG or WebP)",
                "heroImageOptimized": "Hero image converted to WebP via /recipe-hero-image optimize",
                "referenceImages": "Inline reference images exist (XX-YYa convention)",
                "referenceImagesProcessed": "Reference images converted to WebP (null = n/a)",
                "deployed": "Included in last site deploy"
            }
        },
        "recipes": entries
    }

    REGISTRY_FILE.write_text(
        json.dumps(registry, ensure_ascii=False, indent=2),
        encoding='utf-8'
    )

    total = len(entries)
    done_counts = {
        stage: sum(1 for e in entries if e["stages"].get(stage) is True)
        for stage in ["formatAudit", "keywordPull", "glossaryPull", "heroImage",
                      "heroImageOptimized", "referenceImages", "deployed"]
    }

    print(f"✅ Registry generated: {REGISTRY_FILE}")
    print(f"   Total entries: {total}")
    print()
    print("   Stage completion:")
    for stage, count in done_counts.items():
        pct = round(count / total * 100)
        print(f"   {stage:28s} {count:3d}/{total} ({pct}%)")


if __name__ == "__main__":
    generate()
