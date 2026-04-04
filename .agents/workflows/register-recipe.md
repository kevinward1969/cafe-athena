---
description: Registers a single new recipe or technique folio in recipes.json after Claude Desktop Mode 2 completes. Creates the entry with all pipeline stages defaulted to false.
---

# Register Recipe Workflow

Invoked with: `/register-recipe [index]`

Example: `/register-recipe 10-24`

---

## Phase 1 — Locate the Source File

1. Search `The Manual/` for a file whose name starts with `{index}` (e.g., `The Manual/Chapter 10 - Stocks & Mother Sauces/10-24 Café Athena - *.md`).
2. If no file is found, **STOP** and report:
   > "No file found for `{index}` in The Manual. Confirm the recipe has been written to the manuscript before registering."
3. Extract from the filename:
   - **title** — strip the index prefix and any `Café Athena - ` or `Technique Folio - ` prefix from the display name
   - **type** — `"technique"` if the filename contains "Technique Folio", otherwise `"recipe"`
   - **chapter** — the numeric chapter from the folder name (e.g., `Chapter 10 - ...` → `10`)
   - **chapterName** — the chapter name after the number (e.g., `Stocks & Mother Sauces`)

---

## Phase 2 — Check for Existing Entry

1. Read `recipes.json`.
2. Search the `recipes` array for an entry with `"id": "{index}"`.
3. If found, **STOP** and report:
   > "`{index}` is already registered in recipes.json (title: `{existing title}`). Use `/sync-registry` if the entry needs updating."

---

## Phase 3 — Detect Initial Stage State

Check the source file and chapter folder to pre-populate known stages:

- **glossaryPull** — `true` if the source `.md` file contains a `## Glossary` section, otherwise `false`
- **heroImage** — `true` if `{index}.webp` or `{index}.png` exists in the chapter folder
- **heroImageOptimized** — `true` if `{index}.webp` exists, `false` if only `.png` exists, `false` if no image
- **referenceImages** — `true` if any `{index}[a-z].webp` or `{index}[a-z].png` files exist in the chapter folder
- **referenceImagesProcessed** — `true` if reference images exist and all are `.webp`; `false` if any `.png` remain; `null` if no reference images
- All other stages (`formatAudit`, `keywordPull`, `deployed`) default to `false`

---

## Phase 4 — Write Entry *(STOP POINT)*

Present the entry that will be written:

```
New registry entry for {index}:
  title:    {title}
  chapter:  {chapter} — {chapterName}
  type:     {type}
  stages:   glossaryPull={glossaryPull}, heroImage={heroImage}, heroImageOptimized={heroImageOptimized}
            referenceImages={referenceImages}, referenceImagesProcessed={referenceImagesProcessed}
            formatAudit=false, keywordPull=false, deployed=false
```

Ask: *"Register this entry?"*

**WAIT** for confirmation before writing.

---

## Phase 5 — Insert and Confirm

1. Read `recipes.json`.
2. Append the new entry to the `recipes` array.
3. Re-sort the array by `id` ascending to maintain order.
4. Write the updated file using the Write tool.
5. Confirm: *"`{index} — {title}` registered in recipes.json."*
6. Output the next suggested actions:
   > **Next steps for `{index}`:**
   > - Run `/format-audit {index}` to validate structure
   > - Run `/keyword-pull {index}` if Keywords/Category sections are missing
   > - Run `/glossary-pull {index}` if glossaryPull is false
   > - Run `/recipe-hero-image {index}` when ready to create the hero image
