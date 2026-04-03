#!/usr/bin/env python3
"""
Café Athena — Keyword & Category Backfill Script

Reads all recipe markdown files from The Manual, generates keywords and
category tags using the local Ollama API (gemma3:4b), and appends
## Keywords and ## Category sections to each source file.

Idempotent: skips files that already have BOTH sections.

Usage:
    python3 scripts/extract-keywords.py
    python3 scripts/extract-keywords.py --dry-run     # preview only, no writes
    python3 scripts/extract-keywords.py --model llama3.2:latest

Requirements:
    pip install requests
    Ollama running locally: http://localhost:11434
"""

import argparse
import glob
import json
import os
import re
import sys
import time

import requests

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
MANUAL_DIR = os.path.join(PROJECT_DIR, 'The Manual')

OLLAMA_URL = 'http://localhost:11434/api/generate'
DEFAULT_MODEL = 'gemma3:4b'

CUISINE_VALUES = [
    'French', 'Italian', 'Japanese', 'Korean', 'Vietnamese',
    'Chinese', 'American', 'Mediterranean', 'Asian-Fusion', 'Global',
]
STYLE_VALUES = [
    'Classical', 'Modern', 'Rustic', 'Competition',
    'Fine Dining', 'Weeknight', 'Pastry', 'Technique Folio',
]
DIETARY_VALUES = ['Vegetarian', 'Pescatarian']

SYSTEM_PROMPT = """You are a culinary metadata specialist. Given a recipe or technique folio, you output structured metadata in exactly the format requested. You are precise and concise."""

KEYWORD_PROMPT_TEMPLATE = """Analyze this recipe and generate exactly 10-15 comma-separated keywords covering:
- Cooking techniques used (e.g., braising, emulsification, confit)
- Primary ingredients (e.g., duck, miso, puff pastry)
- Cuisine origin (e.g., French, Korean, Italian)
- Equipment required (e.g., pressure cooker, stand mixer)
- Flavor profile (e.g., umami, smoky, fermented, bright)
- Occasion or difficulty (e.g., competition, weeknight, pastry)

Also assign ONE cuisine category and ONE style category from the lists below.

CUISINE OPTIONS: {cuisine_options}
STYLE OPTIONS: {style_options}
DIETARY OPTIONS (only include if clearly applicable): {dietary_options}

RECIPE TITLE: {title}

RECIPE CONTENT (excerpt):
{content}

Respond in this EXACT format with no extra text:
KEYWORDS: term1, term2, term3, term4, term5, term6, term7, term8, term9, term10
CUISINE: [one value from cuisine list]
STYLE: [one value from style list]
DIETARY: [one value from dietary list, or NONE]"""


def has_sections(content):
    """Check if file already has both ## Keywords and ## Category sections."""
    has_keywords = bool(re.search(r'^## Keywords', content, re.MULTILINE))
    has_category = bool(re.search(r'^## Category', content, re.MULTILINE))
    return has_keywords, has_category


def extract_title(filename):
    """Extract display title from filename."""
    title = re.sub(r'^\[?\d{2}-\d{2}[a-z]*\]?\s+', '', filename)
    title = title.replace('.md', '')
    title = re.sub(r'^(Café Athena\s*[-–—]\s*|Technique Folio\s*[-–—]\s*)', '', title)
    return title.strip()


def truncate_content(content, max_chars=2000):
    """Truncate content to keep prompt size manageable."""
    if len(content) <= max_chars:
        return content
    return content[:max_chars] + '\n[... content truncated for brevity ...]'


def call_ollama(prompt, model, timeout=60):
    """Call the Ollama API and return the response text."""
    payload = {
        'model': model,
        'prompt': prompt,
        'system': SYSTEM_PROMPT,
        'stream': False,
        'options': {
            'temperature': 0.2,
            'top_p': 0.9,
        },
    }
    response = requests.post(OLLAMA_URL, json=payload, timeout=timeout)
    response.raise_for_status()
    return response.json().get('response', '').strip()


def parse_ollama_response(response_text):
    """Parse the structured response from Ollama."""
    keywords = []
    cuisine = ''
    style = ''
    dietary = ''

    for line in response_text.splitlines():
        line = line.strip()
        if line.startswith('KEYWORDS:'):
            raw = line[len('KEYWORDS:'):].strip()
            keywords = [k.strip() for k in raw.split(',') if k.strip()]
        elif line.startswith('CUISINE:'):
            val = line[len('CUISINE:'):].strip().strip('[]')
            if val in CUISINE_VALUES:
                cuisine = val
        elif line.startswith('STYLE:'):
            val = line[len('STYLE:'):].strip().strip('[]')
            if val in STYLE_VALUES:
                style = val
        elif line.startswith('DIETARY:'):
            val = line[len('DIETARY:'):].strip().strip('[]')
            if val in DIETARY_VALUES:
                dietary = val

    return keywords, cuisine, style, dietary


def build_sections(keywords, cuisine, style, dietary):
    """Build the ## Keywords and ## Category markdown sections."""
    keyword_line = ', '.join(keywords)
    sections = f'\n## Keywords\n{keyword_line}\n\n## Category\ncuisine: {cuisine} | style: {style}'
    if dietary:
        sections += f' | dietary: {dietary}'
    sections += '\n'
    return sections


def check_ollama_available(model):
    """Check that Ollama is running and the model is available."""
    try:
        resp = requests.get('http://localhost:11434/api/tags', timeout=5)
        resp.raise_for_status()
        models = [m['name'] for m in resp.json().get('models', [])]
        if model not in models:
            print(f'  ⚠️  Model "{model}" not found in Ollama.')
            print(f'     Available: {", ".join(models)}')
            print(f'     Run: ollama pull {model}')
            return False
        return True
    except requests.exceptions.ConnectionError:
        print('  ✗ Cannot connect to Ollama at http://localhost:11434')
        print('    Make sure Ollama is running: ollama serve')
        return False


def process_file(md_file, model, dry_run):
    """Process a single recipe file. Returns status string."""
    filename = os.path.basename(md_file)
    title = extract_title(filename)

    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    has_kw, has_cat = has_sections(content)

    if has_kw and has_cat:
        return 'skipped'

    # Build prompt
    content_excerpt = truncate_content(content)
    prompt = KEYWORD_PROMPT_TEMPLATE.format(
        cuisine_options=', '.join(CUISINE_VALUES),
        style_options=', '.join(STYLE_VALUES),
        dietary_options=', '.join(DIETARY_VALUES),
        title=title,
        content=content_excerpt,
    )

    response_text = call_ollama(prompt, model)
    keywords, cuisine, style, dietary = parse_ollama_response(response_text)

    # Validate we got usable results
    if not keywords or not cuisine or not style:
        print(f'     ⚠️  Incomplete response for {filename}:')
        print(f'        keywords={keywords}, cuisine={cuisine!r}, style={style!r}')
        return 'failed'

    new_sections = build_sections(keywords, cuisine, style, dietary)

    if dry_run:
        print(f'     [DRY RUN] Would append:{new_sections}')
        return 'dry_run'

    # Strip any partial existing sections before appending
    clean_content = content
    if has_kw:
        clean_content = re.sub(r'\n## Keywords\n.*', '', clean_content, flags=re.DOTALL)
    if has_cat:
        clean_content = re.sub(r'\n## Category\n.*', '', clean_content, flags=re.DOTALL)

    clean_content = clean_content.rstrip('\n')
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(clean_content + new_sections)

    return 'processed'


def main():
    parser = argparse.ArgumentParser(description='Backfill keywords and categories for all recipes.')
    parser.add_argument('--dry-run', action='store_true', help='Preview output without writing files')
    parser.add_argument('--model', default=DEFAULT_MODEL, help=f'Ollama model to use (default: {DEFAULT_MODEL})')
    parser.add_argument('--chapter', type=str, help='Only process a specific chapter number (e.g., "7")')
    parser.add_argument('--files', type=str, nargs='+', help='Only process specific file identifiers (e.g., 03-10 07-06)')
    args = parser.parse_args()

    print('════════════════════════════════════════')
    print(' Café Athena — Keyword Backfill')
    print('════════════════════════════════════════')
    print(f'  Model:   {args.model}')
    print(f'  Dry run: {args.dry_run}')
    print()

    if not check_ollama_available(args.model):
        sys.exit(1)

    # Find all recipe files
    if args.files:
        # Target specific file identifiers — .md only
        md_files = []
        for fid in args.files:
            matches = glob.glob(os.path.join(MANUAL_DIR, 'Chapter *', f'{fid}*.md'))
            if matches:
                md_files.extend(matches)
            else:
                print(f'  ⚠️  No file found for identifier: {fid}')
        md_files = sorted(md_files)
    else:
        # Chapter directories are named "Chapter N - Name" so we need wildcard suffix
        if args.chapter:
            chapter_pattern = f'Chapter {args.chapter} *' if args.chapter.isdigit() else args.chapter + '*'
        else:
            chapter_pattern = 'Chapter *'
        md_files = sorted(glob.glob(os.path.join(MANUAL_DIR, chapter_pattern, '*.md')))

    if not md_files:
        print('  No markdown files found matching criteria.')
        sys.exit(1)

    print(f'  Found {len(md_files)} files to check.\n')

    counts = {'processed': 0, 'skipped': 0, 'failed': 0, 'dry_run': 0}

    for md_file in md_files:
        filename = os.path.basename(md_file)
        title = extract_title(filename)

        # Check prefix pattern — skip files without XX-YY index
        if not re.match(r'^\[?\d{2}-\d{2}', filename):
            continue

        print(f'  📄 {filename[:50]}')

        # Skip Google Drive placeholder stubs
        with open(md_file, 'r', encoding='utf-8') as _f:
            _preview = _f.read(500)
        if 'docs.google.com' in _preview and 'download it manually' in _preview:
            print('     ⏭  Placeholder file (Google Drive stub) — skipping')
            counts['skipped'] += 1
            continue

        try:
            status = process_file(md_file, args.model, args.dry_run)
            counts[status] = counts.get(status, 0) + 1

            if status == 'skipped':
                print('     ✓ Already has keywords + category — skipped')
            elif status in ('processed', 'dry_run'):
                print('     ✅ Done')
            elif status == 'failed':
                print('     ✗ Failed — check output above')

        except requests.exceptions.Timeout:
            print('     ✗ Ollama timeout — model may be overloaded, skipping')
            counts['failed'] += 1
        except Exception as e:
            print(f'     ✗ Error: {e}')
            counts['failed'] += 1

        # Small pause to avoid hammering the local model
        time.sleep(0.5)

    print()
    print('════════════════════════════════════════')
    print('  Summary')
    print(f'  ✅ Processed: {counts["processed"]}')
    print(f'  ⏭  Skipped:   {counts["skipped"]}')
    print(f'  ✗  Failed:    {counts["failed"]}')
    if args.dry_run:
        print(f'  👁  Dry run:  {counts["dry_run"]}')
    print('════════════════════════════════════════')


if __name__ == '__main__':
    main()
