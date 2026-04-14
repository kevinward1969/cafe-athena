#!/bin/bash
# ============================================================
# Café Athena — Content Preparation Script
#
# Copies markdown files from The Manual into Astro's content
# directory, auto-injects YAML frontmatter, and copies hero
# images using the XX-YY.png naming convention.
#
# Usage: bash scripts/prepare-content.sh
# ============================================================

set -euo pipefail

MANUAL_DIR="../The Manual"
CONTENT_DIR="src/content/recipes"
GLOSSARY_DIR="../The Manual/Glossary"
GLOSSARY_DEST="src/content/glossary.md"
IMAGES_DIR="public/images"

# Chapter name mapping
declare -A CHAPTER_NAMES
CHAPTER_NAMES[1]="The Lab"
CHAPTER_NAMES[2]="The Foundation"
CHAPTER_NAMES[3]="Garde Manger"
CHAPTER_NAMES[4]="The Mill"
CHAPTER_NAMES[5]="The Fishmonger"
CHAPTER_NAMES[6]="The Poulterer"
CHAPTER_NAMES[7]="The Butcher"
CHAPTER_NAMES[8]="The Field"
CHAPTER_NAMES[9]="The Pâtissier"
CHAPTER_NAMES[10]="Stocks & Mother Sauces"
CHAPTER_NAMES[11]="Spice Blends & Oils"

echo "🧹 Cleaning previous content..."
rm -rf "$CONTENT_DIR"
rm -rf "$IMAGES_DIR"
mkdir -p "$CONTENT_DIR"
mkdir -p "$IMAGES_DIR"

echo "📖 Assembling glossary from split files..."
if [ -d "$GLOSSARY_DIR" ]; then
  {
    printf '# Cafe Athena - Glossary\n\nAlphabetized glossary terms extracted from chapter and recipe glossaries.\n'
    for letter_file in "$GLOSSARY_DIR"/Café\ Athena\ \ -\ Glossary\ *.md; do
      [ -f "$letter_file" ] || continue
      printf '\n'
      awk '/^## /{found=1} found{print}' "$letter_file"
    done
  } > "$GLOSSARY_DEST"
  echo "   ✅ Glossary assembled"
else
  echo "   ⚠️  Glossary directory not found at: $GLOSSARY_DIR"
fi

echo "📋 Processing chapters..."

RECIPE_COUNT=0
IMAGE_COUNT=0

for chapter_dir in "$MANUAL_DIR"/Chapter*/; do
  [ -d "$chapter_dir" ] || continue

  # Extract chapter number from dirname (e.g., "Chapter 3 - Garde Manger" → 3)
  dir_name=$(basename "$chapter_dir")
  chapter_num=$(echo "$dir_name" | grep -oE '[0-9]+' | head -1)
  # Remove leading zero
  chapter_num=$((10#$chapter_num))
  chapter_name="${CHAPTER_NAMES[$chapter_num]:-Unknown}"

  echo ""
  echo "📂 Chapter $chapter_num: $chapter_name"

  for md_file in "$chapter_dir"*.md; do
    [ -f "$md_file" ] || continue

    filename=$(basename "$md_file")

    # Extract the index from the filename.
    # Handles: "03-01 Café Athena - ...", "[03-13] Café Athena - ...", "07-10.2 Café Athena - ..."
    index=$(echo "$filename" | grep -oE '^[\[]*[0-9]{2}-[0-9]{2}(\.[0-9]+)?[a-z]*[\]]*' | tr -d '[]')

    if [ -z "$index" ]; then
      echo "   ⚠️  Skipping (no index): $filename"
      continue
    fi

    # Extract title from filename
    # Remove index prefix, "Café Athena - " prefix, and .md extension
    title=$(echo "$filename" | sed -E 's/^[\[]*[0-9]{2}-[0-9]{2}(\.[0-9]+)?[a-z]*[\]]* //' | sed 's/\.md$//')
    # Remove "Café Athena - " or "Technique Folio - " prefix for display
    display_title=$(echo "$title" | sed -E 's/^(Café Athena - |Technique Folio - )//')

    # Determine type
    if echo "$title" | grep -qi "Technique Folio"; then
      content_type="technique"
    else
      content_type="recipe"
    fi

    # Check for hero image — prefer .webp, fall back to .png
    hero_image=""
    if [ -f "$chapter_dir${index}.webp" ]; then
      hero_image="${index}.webp"
      cp "$chapter_dir${index}.webp" "$IMAGES_DIR/${index}.webp"
      IMAGE_COUNT=$((IMAGE_COUNT + 1))
    elif [ -f "$chapter_dir${index}.png" ]; then
      hero_image="${index}.png"
      cp "$chapter_dir${index}.png" "$IMAGES_DIR/${index}.png"
      IMAGE_COUNT=$((IMAGE_COUNT + 1))
    fi

    # Slugify the index for the filename
    slug="${index}"

    # Read original content (skip any existing frontmatter)
    original_content=$(cat "$md_file")

    # Check if content already has frontmatter
    if echo "$original_content" | head -1 | grep -q '^---$'; then
      # Skip files that already have frontmatter
      body=$(echo "$original_content" | sed -n '/^---$/,/^---$/!p' | tail -n +1)
    else
      body="$original_content"
    fi

    # Escape quotes in title for YAML
    yaml_title=$(echo "$display_title" | sed "s/\"/'/g")

    # Write processed file with frontmatter
    cat > "$CONTENT_DIR/${slug}.md" << FRONTMATTER
---
title: "${yaml_title}"
index: "${index}"
chapter: ${chapter_num}
chapterName: "${chapter_name}"
type: "${content_type}"
heroImage: "${hero_image}"
---

${body}
FRONTMATTER

    RECIPE_COUNT=$((RECIPE_COUNT + 1))
    icon="📄"
    [ -n "$hero_image" ] && icon="🖼 "
    echo "   ${icon} ${index} — ${display_title}"

  done

  # Also copy any remaining images not yet matched (reference images, technique diagrams, etc.)
  for img_file in "$chapter_dir"*.png "$chapter_dir"*.webp; do
    [ -f "$img_file" ] || continue
    img_name=$(basename "$img_file")
    # Skip hero images already copied above (XX-YY or XX-YY.N — no letter suffix)
    if echo "$img_name" | grep -qE '^[0-9]{2}-[0-9]{2}(\.[0-9]+)?\.(png|webp)$'; then
      continue
    fi
    cp "$img_file" "$IMAGES_DIR/$img_name"
    echo "   🎨 Copied image: $img_name"
  done
done

echo ""
echo "════════════════════════════════════════"
echo "✅ Content preparation complete!"
echo "   📄 Recipes/Folios: $RECIPE_COUNT"
echo "   🖼  Hero Images:    $IMAGE_COUNT"
echo "════════════════════════════════════════"
