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
   - **title** — strip the index prefix and any `Café Athena -` or `Technique Folio -` prefix from the display name
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

Check the source file and `site/public/images/` to pre-populate known stages:

- **glossaryPull** — `true` if the source `.md` file contains a `## Glossary` section, otherwise `false`
- **keywordPull** — `true` if the source `.md` file contains both `## Keywords` and `## Category` sections, otherwise `false`
- **heroImage** — `true` if `site/public/images/{index}.webp` exists, otherwise `false`
- **heroImageOptimized** — same value as `heroImage` (images in `site/public/images/` are considered pre-optimized)
- **referenceImages** — `true` if any `site/public/images/{index}[a-z].webp` files exist, otherwise `false`
- **referenceImagesProcessed** — same value as `referenceImages`; `null` if no reference images
- All other stages (`formatAudit`, `deployed`) default to `false`

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
5. **Append to `The Manual/Cafe-Athena-The-Manual-Current-Version.md`** (the human-facing TOC):
   - Locate the `## CHAPTER {chapter}: ...` heading for this entry's chapter.
   - Find the last folio line in that chapter (lines beginning with `*` or `-` and a `XX-YY` index).
   - Insert a new line **immediately after** the last folio line, **matching that chapter's existing list style** (preserve `*` vs `-` and the `\-` vs `-` separator used in adjacent lines).
   - Format the entry as: `{bullet} {index} {prefix} {title}` — where `{prefix}` is `Technique Folio \-` for technique entries and `Café Athena \-` for recipes (or unescaped `-` if the chapter's existing entries use unescaped dashes).
   - Do not reformat or normalize other lines in the doc — append-only.
6. Confirm: *"`{index} — {title}` registered in recipes.json and appended to Current-Version doc."*
7. Output the next suggested actions:
   > **Next steps for `{index}`:**
   > - Run `/format-audit {index}` to validate structure
   > - Run `/keyword-pull {index}` if Keywords/Category sections are missing
   > - Run `/glossary-pull {index}` if glossaryPull is false
   > - Run `/recipe-hero-image {index}` when ready to create the hero image
