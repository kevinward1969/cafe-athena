#!/usr/bin/env python3
"""
Café Athena — Expo Content Preparation Script

Copies markdown files from Expo/Posts/ into Astro's expo content
directory, strips the leading H1 (if any), passes through existing
frontmatter, and copies hero images to site/public/images/.

Already-optimized WebP files in site/public/images/ are never
overwritten — same guard as prepare-content.py.

Usage: python3 site/scripts/prepare-expo.py
"""

import os
import re
import shutil
import glob as globmod

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.dirname(SCRIPT_DIR)
REPO_DIR = os.path.dirname(SITE_DIR)
EXPO_POSTS_DIR = os.path.join(REPO_DIR, 'Expo', 'Posts')
CONTENT_DIR = os.path.join(SITE_DIR, 'src', 'content', 'expo')
IMAGES_DIR = os.path.join(SITE_DIR, 'public', 'images')


def clean_expo_content():
    """Remove and recreate the expo content output directory."""
    if os.path.exists(CONTENT_DIR):
        shutil.rmtree(CONTENT_DIR)
    os.makedirs(CONTENT_DIR, exist_ok=True)


def copy_image_if_needed(src_path, image_name):
    """Copy image to site/public/images/, skipping already-optimized WebP files."""
    os.makedirs(IMAGES_DIR, exist_ok=True)
    dest_path = os.path.join(IMAGES_DIR, image_name)
    if image_name.lower().endswith('.webp') and os.path.exists(dest_path):
        return 'exists'
    shutil.copy2(src_path, dest_path)
    return 'copied'


def process_post(md_file):
    """Process a single Expo post source file and write to CONTENT_DIR."""
    filename = os.path.basename(md_file)
    slug = os.path.splitext(filename)[0]

    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Separate frontmatter from body
    frontmatter_raw = ''
    body = content
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter_raw = parts[1]
            body = parts[2].lstrip('\n')

    if not frontmatter_raw:
        print(f'   ⚠️  No frontmatter found in {filename} — writing as-is')

    # Strip leading H1 (same guard as prepare-content.py)
    body = re.sub(r'^# [^\n]*\n+', '', body)

    # Extract heroImage value from frontmatter
    hero_image = ''
    if frontmatter_raw:
        hero_match = re.search(r'^heroImage:\s*["\']?([^"\'>\n]+?)["\']?\s*$',
                               frontmatter_raw, re.MULTILINE)
        if hero_match:
            hero_image = hero_match.group(1).strip()

    # Copy hero image from Expo/Posts/ if present there
    image_status = ''
    if hero_image:
        src_img = os.path.join(os.path.dirname(md_file), hero_image)
        if os.path.exists(src_img):
            image_status = copy_image_if_needed(src_img, hero_image)
        elif os.path.exists(os.path.join(IMAGES_DIR, hero_image)):
            image_status = 'exists'

    # Write processed file: frontmatter unchanged, body with H1 stripped
    if frontmatter_raw:
        output = f'---{frontmatter_raw}---\n\n{body.strip()}\n'
    else:
        output = body.strip() + '\n'

    output_path = os.path.join(CONTENT_DIR, f'{slug}.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)

    has_image = image_status in ('copied', 'exists')
    icon = '🖼 ' if has_image else '📄'
    return slug, icon


def main():
    if not os.path.isdir(EXPO_POSTS_DIR):
        print(f'⚠️  Expo/Posts/ not found at {EXPO_POSTS_DIR} — nothing to process.')
        return

    print('🧹 Cleaning expo content...')
    clean_expo_content()

    print('📋 Processing Expo posts...')

    md_files = sorted(globmod.glob(
        os.path.join(EXPO_POSTS_DIR, '**', '*.md'), recursive=True
    ))

    count = 0
    for md_file in md_files:
        slug, icon = process_post(md_file)
        print(f'   {icon} {slug}')
        count += 1

    if count == 0:
        print('   (no posts found — Expo/Posts/ is empty)')

    print()
    print('═' * 40)
    print('✅ Expo content preparation complete!')
    print(f'   📄 Posts: {count}')
    print('═' * 40)


if __name__ == '__main__':
    main()
