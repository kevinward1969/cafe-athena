#!/usr/bin/env python3
"""
Café Athena — Hero Image Rename Script (One-Time)

Renames existing hero images from freeform names to the
XX-YY.png convention based on their chapter and recipe index.

Run this ONCE before running prepare-content.sh

Usage: python3 scripts/rename-images.py
"""

import os
import sys

MANUAL_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'The Manual')

# Image → Index mapping (manually curated from audit)
IMAGE_MAP = {
    # Chapter 3 - Garde Manger
    'Chapter 3 - Garde Manger/Caprese Ravioli.png': '03-01',
    'Chapter 3 - Garde Manger/Modern Caprese.png': '03-03',
    'Chapter 3 - Garde Manger/Smoked Salmon & Compressed Cucumber on Potato Fondant.png': '03-04',
    'Chapter 3 - Garde Manger/Spicy Sesame & Yuzu Tuna Tartare.png': '03-05',
    # Chapter 5 - The Fishmonger
    'Chapter 5 - The Fishmonger/Pan-Seared Scallops with Pea Fluid Gel.png': '05-01',
    'Chapter 5 - The Fishmonger/Miso-Cured Black Cod (Saikyo Yaki).png': '05-02',
    # Chapter 6 - The Poulterer
    'Chapter 6 - The Poulterer/Itallian Wedding Soup - Polo Rustica.png': '06-01',
    'Chapter 6 - The Poulterer/Traditional Duck Confit.png': '06-03',
    'Chapter 6 - The Poulterer/Nashville Hot Chicken-The Weissman Method.png': '06-04',
    # Chapter 7 - The Butcher
    'Chapter 7 - The Butcher/Ribeye with Bone Marrow & Herb Baste.png': '07-01',
    'Chapter 7 - The Butcher/Braised _Boursin & Bacon_ Meatball Subs.png': '07-02',
    'Chapter 7 - The Butcher/KW Signature Smoked Pork Steaks.png': '07-03',
    'Chapter 7 - The Butcher/Beef Bourguignon - The Elevated Short Rib Braise.png': '07-04',
    'Chapter 7 - The Butcher/Oxtail Bourguignon.png': '07-05',
    'Chapter 7 - The Butcher/Steak au Poivre - Bistro Style.png': '07-06',
    'Chapter 7 - The Butcher/Skirt Steak Bordelaise.png': '07-07',
    'Chapter 7 - The Butcher/Braised Beef Stroganoff.png': '07-08',
    'Chapter 7 - The Butcher/MasterClass Beef Bourguignon.png': '07-09',
}

def main():
    print('🖼  Café Athena — Hero Image Rename')
    print('═' * 40)
    print()

    renamed = 0
    skipped = 0

    print(f'📋 Renaming {len(IMAGE_MAP)} images...')
    print()

    for old_rel_path, new_index in IMAGE_MAP.items():
        full_old = os.path.join(MANUAL_DIR, old_rel_path)
        directory = os.path.dirname(full_old)
        full_new = os.path.join(directory, f'{new_index}.png')

        if os.path.exists(full_old):
            os.rename(full_old, full_new)
            old_name = os.path.basename(old_rel_path)
            print(f'   ✅ {old_name} → {new_index}.png')
            renamed += 1
        else:
            print(f'   ⚠️  Not found: {old_rel_path}')
            skipped += 1

    print()
    print('═' * 40)
    print(f'✅ Rename complete!')
    print(f'   Renamed: {renamed}')
    print(f'   Skipped: {skipped}')
    print('═' * 40)
    print()
    print('You can now run: bash scripts/prepare-content.sh')


if __name__ == '__main__':
    main()
