#!/usr/bin/env python3
"""
Validate YAML frontmatter in all built recipe files and all Manual source files.

Checks:
  - Built files (site/src/content/recipes/): valid YAML frontmatter
  - Source files (The Manual/): keywords/category sections contain no --- separators
    or unescaped characters that would break the pipeline

Usage:
  python3 scripts/validate-recipe-yaml.py
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
BUILT_DIR = REPO_ROOT / "site" / "src" / "content" / "recipes"
MANUAL_DIR = REPO_ROOT / "The Manual"

errors = []
warnings = []


def check_built_files():
    for path in sorted(BUILT_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            errors.append(f"{path.name}: no frontmatter opening ---")
            continue

        parts = text.split("---", 2)
        if len(parts) < 3:
            errors.append(f"{path.name}: frontmatter not closed")
            continue

        frontmatter = parts[1]

        try:
            import yaml
            yaml.safe_load(frontmatter)
        except Exception as e:
            errors.append(f"{path.name}: YAML parse error — {e}")
            continue

        # Check keywords field specifically for embedded --- or newlines
        kw_match = re.search(r'^keywords:\s*(.+)$', frontmatter, re.MULTILINE)
        if kw_match:
            kw_val = kw_match.group(1)
            if "---" in kw_val:
                errors.append(f"{path.name}: keywords field contains ---")
            if "\n" in kw_val and not kw_val.strip().startswith("["):
                warnings.append(f"{path.name}: keywords field spans multiple lines")


def check_source_files():
    for path in sorted(MANUAL_DIR.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(REPO_ROOT)

        kw_match = re.search(r'^## Keywords\n(.*?)(?=\n## |\Z)', text, re.MULTILINE | re.DOTALL)
        if not kw_match:
            continue

        raw_kw = kw_match.group(1)

        if "---" in raw_kw:
            warnings.append(
                f"{rel}: Keywords section contains --- separator "
                f"(pipeline will stop at it — verify keywords are complete)"
            )

        # Check for unmatched quotes in keyword values
        for kw in raw_kw.split(","):
            kw = kw.strip()
            if '"' in kw or "'" in kw:
                warnings.append(f"{rel}: keyword contains quote character: {kw!r}")


def main():
    try:
        import yaml
    except ImportError:
        print("pyyaml not installed — run: pip3 install pyyaml")
        sys.exit(1)

    print("Checking built files...")
    check_built_files()

    print("Checking source files...")
    check_source_files()

    if errors:
        print(f"\n❌ {len(errors)} ERROR(S):")
        for e in errors:
            print(f"   {e}")

    if warnings:
        print(f"\n⚠️  {len(warnings)} WARNING(S):")
        for w in warnings:
            print(f"   {w}")

    if not errors and not warnings:
        print(f"\n✅ All recipe files clean.")
    elif not errors:
        print(f"\n✅ No errors. Review warnings above.")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
