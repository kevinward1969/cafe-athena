#!/bin/bash
# ============================================================
# Café Athena — Image Rename Script (One-Time)
#
# Renames existing hero images from freeform names to the
# XX-YY.png convention based on their chapter and recipe index.
#
# Run this ONCE before running prepare-content.sh
#
# Usage: bash scripts/rename-images.sh
# ============================================================

set -euo pipefail

MANUAL_DIR="../The Manual"
RENAMED=0
SKIPPED=0

echo "🖼  Café Athena — Hero Image Rename"
echo "════════════════════════════════════════"
echo ""

# Image → Index mapping (manually curated from audit)
declare -A IMAGE_MAP

# Chapter 3 - Garde Manger
IMAGE_MAP["Chapter 3 - Garde Manger/Caprese Ravioli.png"]="03-01"
IMAGE_MAP["Chapter 3 - Garde Manger/Modern Caprese.png"]="03-03"
IMAGE_MAP["Chapter 3 - Garde Manger/Smoked Salmon & Compressed Cucumber on Potato Fondant.png"]="03-04"
IMAGE_MAP["Chapter 3 - Garde Manger/Spicy Sesame & Yuzu Tuna Tartare.png"]="03-05"

# Chapter 5 - The Fishmonger
IMAGE_MAP["Chapter 5 - The Fishmonger/Pan-Seared Scallops with Pea Fluid Gel.png"]="05-01"
IMAGE_MAP["Chapter 5 - The Fishmonger/Miso-Cured Black Cod (Saikyo Yaki).png"]="05-02"

# Chapter 6 - The Poulterer
IMAGE_MAP["Chapter 6 - The Poulterer/Itallian Wedding Soup - Polo Rustica.png"]="06-01"
IMAGE_MAP["Chapter 6 - The Poulterer/Traditional Duck Confit.png"]="06-03"
IMAGE_MAP["Chapter 6 - The Poulterer/Nashville Hot Chicken-The Weissman Method.png"]="06-04"

# Chapter 7 - The Butcher
IMAGE_MAP["Chapter 7 - The Butcher/Ribeye with Bone Marrow & Herb Baste.png"]="07-01"
IMAGE_MAP["Chapter 7 - The Butcher/Braised _Boursin & Bacon_ Meatball Subs.png"]="07-02"
IMAGE_MAP["Chapter 7 - The Butcher/KW Signature Smoked Pork Steaks.png"]="07-03"
IMAGE_MAP["Chapter 7 - The Butcher/Beef Bourguignon - The Elevated Short Rib Braise.png"]="07-04"
IMAGE_MAP["Chapter 7 - The Butcher/Oxtail Bourguignon.png"]="07-05"
IMAGE_MAP["Chapter 7 - The Butcher/Steak au Poivre - Bistro Style.png"]="07-06"
IMAGE_MAP["Chapter 7 - The Butcher/Skirt Steak Bordelaise.png"]="07-07"
IMAGE_MAP["Chapter 7 - The Butcher/Braised Beef Stroganoff.png"]="07-08"
IMAGE_MAP["Chapter 7 - The Butcher/MasterClass Beef Bourguignon.png"]="07-09"

echo "📋 Renaming ${#IMAGE_MAP[@]} images..."
echo ""

for old_path in "${!IMAGE_MAP[@]}"; do
  new_index="${IMAGE_MAP[$old_path]}"
  full_old="$MANUAL_DIR/$old_path"
  dir=$(dirname "$full_old")
  full_new="$dir/${new_index}.png"

  if [ -f "$full_old" ]; then
    mv "$full_old" "$full_new"
    echo "   ✅ $(basename "$old_path") → ${new_index}.png"
    RENAMED=$((RENAMED + 1))
  else
    echo "   ⚠️  Not found: $old_path"
    SKIPPED=$((SKIPPED + 1))
  fi
done

echo ""
echo "════════════════════════════════════════"
echo "✅ Rename complete!"
echo "   Renamed: $RENAMED"
echo "   Skipped: $SKIPPED"
echo "════════════════════════════════════════"
echo ""
echo "You can now run: bash scripts/prepare-content.sh"
