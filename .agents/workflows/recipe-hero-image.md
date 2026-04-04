---
description: Two-mode workflow for hero images — Create mode builds a Gemini prompt from recipe frontmatter; Optimize mode converts PNGs to WebP and reports size savings. Both modes operate on the chapter source folders, not site/public/images.
---

# Recipe Hero Image Workflow

Invoked with:

- `/recipe-hero-image [index]` — Create mode, e.g. `/recipe-hero-image 04-17`
- `/recipe-hero-image optimize [index|chapter-N|all]` — Optimize mode, e.g. `/recipe-hero-image optimize 04-17` or `/recipe-hero-image optimize 04-17a` or `/recipe-hero-image optimize chapter-4` or `/recipe-hero-image optimize all`
- `/recipe-hero-image insert [index] "[position hint]" "[caption]"` — Insert mode, e.g. `/recipe-hero-image insert 04-11 "after the gnocchi shapes list" "Gnocchi shape guide"`

---

## Phase 0 — Mode Detection

1. If the first argument is `optimize`, branch to **Optimize Mode** below.
2. If the first argument is `insert`, branch to **Insert Mode** below.
3. Otherwise, treat the argument as a recipe index and continue with **Create Mode**.

---

## CREATE MODE

### Phase 1 — Locate Recipe & Identify Chapter Folder

1. Read the built recipe file at `site/src/content/recipes/{index}.md` to get frontmatter: `title`, `chapterName`, `chapter`, `cuisine`, `style`, `keywords`, `heroImage`.
2. Identify the source chapter folder:
   - Search `The Manual/` for the folder matching `Chapter {chapter} -` (e.g., `The Manual/Chapter 4 - The Mill/`).
3. Check for an existing hero image:
   - Look for `{index}.png` OR `{index}.webp` in the chapter folder.
   - If found, warn the user: *"A hero image already exists for {index} (`{filename}`). Continuing will create a replacement prompt — the existing file will not be deleted until you save a new one over it."*
4. Read the source recipe folio from the chapter folder (filename matches `{index}*`).
5. Extract the **headnote** — the first descriptive paragraph after the main `#` heading — for visual and sensory cues.

---

### Phase 2 — Build Gemini Prompt *(STOP POINT 1)*

Construct a detailed prompt using:

- **Dish name** (`title`)
- **Headnote** — texture, color, components, garnish cues
- **Cuisine** and **style** for cultural/plating context
- **3–5 primary visual keywords** from `keywords` (pick the most visually concrete: ingredients, plating techniques, colors — avoid abstract terms like "classical")
- **Fixed photography direction** appended to every prompt:
  > Professional food photography, ¾ overhead angle, soft natural side lighting, shallow depth of field, neutral linen or dark slate surface, 16:9 cinematic crop, high resolution.

Present the full prompt to the user formatted as a blockquote. Ask:

> *"Does this prompt capture the dish well, or would you like to adjust it before taking it to Gemini?"*

**WAIT** for the user's response. Apply any adjustments before proceeding.

---

### Phase 3 — Image Handoff

Present the following instructions to the user:

1. Open Gemini (Nano Banana)
2. Paste the prompt and generate the image
3. Save the output file as **`{index}.png`** into the chapter folder:
   `The Manual/Chapter {chapter} - {chapterName}/`
4. Reply here once the file is saved

**WAIT** for the user to confirm the file is saved.

---

### Phase 4 — Confirm & Suggest Next Step

1. Verify the file now exists at the expected path.
2. Report success: *"`{index}.png` found in the chapter folder. It will appear on the site after the next deploy."*
3. Suggest optimization: *"Run `/recipe-hero-image optimize {index}` to convert it to WebP and reduce file size before deploying."*

---

---

## INSERT MODE

### Phase 1 — Locate Folio and Determine Next Letter

1. Identify the source chapter folder from the index (e.g., `04-11` → `The Manual/Chapter 4 - The Mill/`).
2. Read the source `.md` file (filename matches `{index}*`).
3. Scan the file for existing `[ref:{index}*]` shortcodes to determine which letters are already used.
4. The next available letter is the one immediately after the highest used (e.g., if `04-11a` and `04-11b` exist, next is `04-11c`). If none exist, start with `a`.

---

### Phase 2 — Find Insertion Point *(STOP POINT)*

1. Parse the position hint to identify the target section (e.g., `"after the gnocchi shapes list"` → look for the relevant heading or last list item in that section).
2. Show the user the exact line where the shortcode will be inserted and the shortcode that will be written:

   > *"I'll insert `[ref:04-11c | Caption]` after the line: `* **Pici di Patate:** …`"*

**WAIT** for the user to confirm.

---

### Phase 3 — Insert Shortcode

1. Insert the shortcode as a standalone paragraph (blank line above, blank line below):

   ```
   [ref:{index}{letter} | {caption}]
   ```

2. Confirm insertion: *"`[ref:04-11c | Caption]` inserted. Rename your source image to `04-11c.png` and run `/recipe-hero-image optimize 04-11c` before deploying."*

---

## OPTIMIZE MODE

### Phase 1 — Identify Targets

Determine which chapter-folder PNG/WebP files to process:

- **`optimize {index}`** — single file: find `{index}.png` in the chapter folder for that recipe
- **`optimize {index}{letter}`** — single reference image: find `{index}{letter}.png` (e.g., `04-11a.png`) in the chapter folder
- **`optimize chapter-N`** — all `*.png` files in `The Manual/Chapter N - */`
- **`optimize all`** — all `*.png` files across all chapter folders in `The Manual/`

For each target file, report:

- Full path
- Current file size (MB)
- Current dimensions (w × h px)

---

### Phase 2 — Optimization Plan *(STOP POINT 2)*

Present a summary table of files to process:

| Index | File | Size | Dimensions |
|-------|------|------|------------|
| 04-17 | Chapter 4 - The Mill/04-17.png | 6.2 MB | 3200 × 1746 |

Settings that will be applied:

- Output format: WebP, quality 85
- Max dimensions: 1920 × 1080 (downscale only, aspect ratio preserved)
- Original PNG deleted after successful conversion

Ask: *"Ready to optimize these [N] image(s)? This will permanently replace the PNGs with WebP files."*

**WAIT** for the user's response.

---

### Phase 3 — Run Optimization

Write a temporary Python script to `/tmp/optimize_hero.py` and execute it:

```python
#!/usr/bin/env python3
from PIL import Image
from pathlib import Path
import sys

def optimize(png_path: Path):
    webp_path = png_path.with_suffix('.webp')
    with Image.open(png_path) as img:
        if img.mode not in ('RGB', 'RGBA'):
            img = img.convert('RGB')
        elif img.mode == 'RGBA':
            bg = Image.new('RGB', img.size, (255, 255, 255))
            bg.paste(img, mask=img.split()[3])
            img = bg
        img.thumbnail((1920, 1080), Image.Resampling.LANCZOS)
        img.save(webp_path, 'WEBP', quality=85, method=6)
    original_size = png_path.stat().st_size
    new_size = webp_path.stat().st_size
    png_path.unlink()
    return original_size, new_size

paths = [Path(p) for p in sys.argv[1:]]
total_before = total_after = 0
for p in paths:
    before, after = optimize(p)
    total_before += before
    total_after += after
    saved_pct = (1 - after / before) * 100
    print(f"{p.name}: {before/1024/1024:.1f} MB → {after/1024/1024:.1f} MB ({saved_pct:.0f}% saved)")

total_saved_pct = (1 - total_after / total_before) * 100 if total_before > 0 else 0
print(f"\nTotal: {total_before/1024/1024:.1f} MB → {total_after/1024/1024:.1f} MB ({total_saved_pct:.0f}% saved)")
```

Run it passing all target PNG paths as arguments.

---

### Phase 4 — Report

Display the optimization results table and total savings reported by the script.

Note to user: *"WebP files are now in the chapter folders. The deploy script will pick them up automatically on the next run of `bash scripts/deploy.sh`."*

---

## Notes

- **`site/public/images/` is never touched directly.** It is fully managed by `prepare-content.py` which runs as Step 1 of `deploy.sh`.
- `prepare-content.py` supports both `.png` and `.webp` hero images — it checks for `.webp` first, then falls back to `.png`.
- The built recipe files in `site/src/content/recipes/` are auto-generated. Never edit them manually.
