#!/usr/bin/env python3
"""
Café Athena — Content Preparation Script

Copies markdown files from The Manual into Astro's content
directory, auto-injects YAML frontmatter, and copies hero
images using the XX-YY.png naming convention.

Usage: python3 scripts/prepare-content.py
"""

import os
import re
import shutil
import glob as globmod

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.dirname(SCRIPT_DIR)
MANUAL_DIR = os.path.join(SITE_DIR, '..', 'The Manual')
CONTENT_DIR = os.path.join(SITE_DIR, 'src', 'content', 'recipes')
GLOSSARY_SRC = os.path.join(MANUAL_DIR, 'Café Athena  - Glossary.md')
GLOSSARY_DEST = os.path.join(SITE_DIR, 'src', 'content', 'glossary.md')
IMAGES_DIR = os.path.join(SITE_DIR, 'public', 'images')

CHAPTER_NAMES = {
    1: 'The Lab',
    2: 'The Foundation',
    3: 'Garde Manger',
    4: 'The Mill',
    5: 'The Fishmonger',
    6: 'The Poulterer',
    7: 'The Butcher',
    8: 'The Field',
    9: 'The Pâtissier',
    10: 'Stocks & Mother Sauces',
    11: 'Spice Blends & Oils',
}


def clean_dirs():
    """Remove and recreate output directories."""
    for d in [CONTENT_DIR, IMAGES_DIR]:
        if os.path.exists(d):
            shutil.rmtree(d)
        os.makedirs(d, exist_ok=True)


def copy_glossary():
    """Copy the glossary file."""
    os.makedirs(os.path.dirname(GLOSSARY_DEST), exist_ok=True)
    if os.path.exists(GLOSSARY_SRC):
        shutil.copy2(GLOSSARY_SRC, GLOSSARY_DEST)
        print('   ✅ Glossary copied')
    else:
        print(f'   ⚠️  Glossary not found at: {GLOSSARY_SRC}')


def extract_index(filename):
    """Extract the XX-YY index from a filename."""
    # Handles: "03-01 Café Athena - ..." and "[03-13] Café Athena - ..."
    match = re.match(r'^\[?(\d{2}-\d{2}[a-z]*)\]?\s', filename)
    if match:
        return match.group(1)
    return None


def extract_title(filename, index):
    """Extract display title from the filename."""
    # Remove index prefix and .md extension
    title = re.sub(r'^\[?\d{2}-\d{2}[a-z]*\]?\s+', '', filename)
    title = title.replace('.md', '')
    # Remove "Café Athena - " or "Technique Folio - " prefix
    title = re.sub(r'^(Café Athena\s*[-–—]\s*|Technique Folio\s*[-–—]\s*)', '', title)
    return title.strip()


def determine_type(filename):
    """Determine if this is a recipe or technique folio."""
    if 'Technique Folio' in filename or 'Technique_Folio' in filename:
        return 'technique'
    return 'recipe'


def process_chapter(chapter_dir):
    """Process all markdown files in a chapter directory."""
    dir_name = os.path.basename(chapter_dir)

    # Extract chapter number
    num_match = re.search(r'(\d+)', dir_name)
    if not num_match:
        return 0, 0
    chapter_num = int(num_match.group(1))
    chapter_name = CHAPTER_NAMES.get(chapter_num, 'Unknown')

    print(f'\n📂 Chapter {chapter_num}: {chapter_name}')

    recipe_count = 0
    image_count = 0

    md_files = sorted(globmod.glob(os.path.join(chapter_dir, '*.md')))

    for md_file in md_files:
        filename = os.path.basename(md_file)
        index = extract_index(filename)

        if not index:
            print(f'   ⚠️  Skipping (no index): {filename}')
            continue

        display_title = extract_title(filename, index)
        content_type = determine_type(filename)

        # Check for hero image
        hero_image = ''
        hero_path = os.path.join(chapter_dir, f'{index}.png')
        if os.path.exists(hero_path):
            hero_image = f'{index}.png'
            shutil.copy2(hero_path, os.path.join(IMAGES_DIR, f'{index}.png'))
            image_count += 1

        # Read original content
        with open(md_file, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # Strip existing frontmatter if present
        body = original_content
        if body.startswith('---'):
            parts = body.split('---', 2)
            if len(parts) >= 3:
                body = parts[2].lstrip('\n')

        # Escape quotes for YAML
        yaml_title = display_title.replace('"', "'")

        # Build frontmatter
        frontmatter = f"""---
title: "{yaml_title}"
index: "{index}"
chapter: {chapter_num}
chapterName: "{chapter_name}"
type: "{content_type}"
heroImage: "{hero_image}"
---

"""
        # Write processed file
        output_path = os.path.join(CONTENT_DIR, f'{index}.md')
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter + body)

        recipe_count += 1
        icon = '🖼 ' if hero_image else '📄'
        print(f'   {icon} {index} — {display_title}')

    # Copy technique diagram images (non XX-YY.png named)
    png_files = globmod.glob(os.path.join(chapter_dir, '*.png'))
    for img_file in png_files:
        img_name = os.path.basename(img_file)
        if re.match(r'^\d{2}-\d{2}[a-z]*\.png$', img_name):
            continue  # Already handled
        dest = os.path.join(IMAGES_DIR, img_name)
        if not os.path.exists(dest):
            shutil.copy2(img_file, dest)
            print(f'   🎨 Copied diagram: {img_name}')

    return recipe_count, image_count


def main():
    print('🧹 Cleaning previous content...')
    clean_dirs()

    print('📖 Copying glossary...')
    copy_glossary()

    print('📋 Processing chapters...')

    total_recipes = 0
    total_images = 0

    # Find all chapter directories
    chapter_dirs = sorted(globmod.glob(os.path.join(MANUAL_DIR, 'Chapter *')))

    for chapter_dir in chapter_dirs:
        if not os.path.isdir(chapter_dir):
            continue
        r, i = process_chapter(chapter_dir)
        total_recipes += r
        total_images += i

    print()
    print('═' * 40)
    print('✅ Content preparation complete!')
    print(f'   📄 Recipes/Folios: {total_recipes}')
    print(f'   🖼  Hero Images:    {total_images}')
    print('═' * 40)


if __name__ == '__main__':
    main()
