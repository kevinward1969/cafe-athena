#!/usr/bin/env python3
"""
add-glossary-sections.py

Uses a local Ollama model to generate ## Glossary sections for Café Athena
recipe/technique folios that don't have one yet.

Usage:
    python3 scripts/add-glossary-sections.py [--model MODEL] [--dry-run] [--id ID]

Options:
    --model MODEL    Ollama model name (default: llama3.2:latest)
    --dry-run        Print proposed glossary sections without writing files
    --id ID          Process a single recipe by ID (e.g. 01-01), else all pending
    --limit N        Process at most N recipes (useful for testing)
"""

import argparse
import json
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

BASE = Path(__file__).parent.parent
RECIPES_JSON = BASE / "recipes.json"
MANUAL_DIR = BASE / "The Manual"
OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """\
You are a culinary reference editor for a professional cookbook called Café Athena.
Your job is to extract culinary terminology from a recipe or technique folio and write
precise, accurate glossary definitions.

Rules:
- Extract 3 to 8 terms that a serious home cook or culinary student would benefit from knowing.
- Only include terms that are genuinely culinary, scientific, or technique-specific.
- Skip common everyday words (e.g. "salt", "water", "pan", "stir").
- Definitions must be accurate, concise (1–2 sentences), and written in cookbook voice.
- Format EXACTLY as:
  * **Term:** Definition here.
- Return ONLY the bulleted list. No preamble, no explanation, no extra text.
"""

PROMPT_TEMPLATE = """\
Recipe/folio content:

{content}

---

Extract culinary glossary terms from the content above. Return only the bulleted list.
"""

# ---------------------------------------------------------------------------
# Ollama helpers
# ---------------------------------------------------------------------------

def call_ollama(model: str, content: str, timeout: int = 120) -> str:
    """Send content to Ollama and return the model's text response."""
    prompt = PROMPT_TEMPLATE.format(content=content[:6000])  # cap to avoid context overflow
    payload = json.dumps({
        "model": model,
        "prompt": prompt,
        "system": SYSTEM_PROMPT,
        "stream": False,
        "options": {"temperature": 0.2, "num_predict": 512},
    }).encode("utf-8")

    req = urllib.request.Request(
        OLLAMA_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result.get("response", "").strip()
    except urllib.error.URLError as e:
        print(f"  ERROR: Cannot reach Ollama — {e}", file=sys.stderr)
        return ""


def parse_terms(raw: str) -> list[tuple[str, str]]:
    """Parse '* **Term:** Definition' lines into (term, definition) pairs."""
    terms = []
    for line in raw.splitlines():
        line = line.strip()
        m = re.match(r"^\*\s+\*\*([^*:]+)\*\*:\s+(.+)$", line)
        if m:
            terms.append((m.group(1).strip(), m.group(2).strip()))
    return terms


def format_glossary_section(terms: list[tuple[str, str]]) -> str:
    lines = ["## Glossary", ""]
    for term, defn in terms:
        lines.append(f"* **{term}:** {defn}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# File helpers
# ---------------------------------------------------------------------------

def find_recipe_file(recipe_id: str) -> Path | None:
    matches = list(MANUAL_DIR.rglob(f"{recipe_id}*.md"))
    # Exclude the main glossary file
    matches = [m for m in matches if "Glossary" not in m.name]
    return matches[0] if matches else None


def has_glossary_section(text: str) -> bool:
    return bool(re.search(r"^##\s+Glossary", text, re.MULTILINE))


def insert_glossary(text: str, glossary_block: str) -> str:
    """Insert glossary before ## Keywords, ## Category, or at end of file."""
    for marker in (r"^## Keywords", r"^## Category"):
        m = re.search(marker, text, re.MULTILINE)
        if m:
            return text[: m.start()] + glossary_block + "\n\n" + text[m.start() :]
    return text.rstrip() + "\n\n" + glossary_block + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Generate glossary sections via Ollama")
    parser.add_argument("--model", default="llama3.2:latest", help="Ollama model name")
    parser.add_argument("--dry-run", action="store_true", help="Print only, don't write")
    parser.add_argument("--id", help="Process a single recipe ID")
    parser.add_argument("--limit", type=int, default=0, help="Max recipes to process")
    args = parser.parse_args()

    # Load registry
    with open(RECIPES_JSON) as f:
        data = json.load(f)

    if args.id:
        pending_ids = [args.id]
    else:
        pending_ids = [
            r["id"] for r in data["recipes"] if not r["stages"].get("glossaryPull")
        ]

    print(f"Model: {args.model}")
    print(f"Pending recipes: {len(pending_ids)}")
    if args.dry_run:
        print("DRY RUN — no files will be written\n")

    if args.limit:
        pending_ids = pending_ids[: args.limit]
        print(f"(Limited to {args.limit})\n")

    skipped_no_file = []
    skipped_already_has = []
    skipped_no_terms = []
    processed = []
    errors = []

    for i, rid in enumerate(pending_ids, 1):
        print(f"[{i}/{len(pending_ids)}] {rid} ", end="", flush=True)

        fpath = find_recipe_file(rid)
        if not fpath:
            print("— file not found, skipping")
            skipped_no_file.append(rid)
            continue

        text = fpath.read_text(encoding="utf-8")

        if has_glossary_section(text):
            print("— already has ## Glossary, skipping")
            skipped_already_has.append(rid)
            # Mark complete in registry even though we're skipping
            if not args.dry_run:
                for r in data["recipes"]:
                    if r["id"] == rid:
                        r["stages"]["glossaryPull"] = True
            continue

        t0 = time.time()
        raw = call_ollama(args.model, text)
        elapsed = time.time() - t0

        if not raw:
            print(f"— Ollama returned nothing ({elapsed:.1f}s), skipping")
            errors.append(rid)
            continue

        terms = parse_terms(raw)
        if not terms:
            print(f"— no parseable terms returned ({elapsed:.1f}s), skipping")
            print(f"  Raw output: {raw[:200]}")
            skipped_no_terms.append(rid)
            continue

        print(f"— {len(terms)} terms ({elapsed:.1f}s)")

        glossary_block = format_glossary_section(terms)

        if args.dry_run:
            print(f"\n--- {fpath.name} ---")
            print(glossary_block)
            print()
        else:
            updated = insert_glossary(text, glossary_block)
            fpath.write_text(updated, encoding="utf-8")

            # Mark complete in registry
            for r in data["recipes"]:
                if r["id"] == rid:
                    r["stages"]["glossaryPull"] = True

        processed.append(rid)

    # Save registry
    if not args.dry_run and processed:
        with open(RECIPES_JSON, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    # Summary
    print("\n" + "=" * 50)
    print(f"Processed:          {len(processed)}")
    print(f"Already had glossary: {len(skipped_already_has)}")
    print(f"No parseable terms: {len(skipped_no_terms)}")
    print(f"File not found:     {len(skipped_no_file)}")
    print(f"Ollama errors:      {len(errors)}")

    if skipped_no_terms:
        print(f"\nNo terms parsed (manual review needed): {skipped_no_terms}")
    if errors:
        print(f"Errors: {errors}")


if __name__ == "__main__":
    main()
