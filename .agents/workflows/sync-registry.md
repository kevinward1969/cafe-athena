---
description: Syncs recipes.json against the live Manual directory. Adds missing entries, updates stage flags that can be derived from the filesystem, and reports any discrepancies. Does not remove entries or reset completed stages.
---

# Sync Registry Workflow

Invoked with: `/sync-registry`

---

## Phase 1 — Scan The Manual

1. Use Glob to find all `*.md` files under `The Manual/Chapter*/`.
2. For each file, extract:
   - `index` — the XX-YY or XX-YYa prefix
   - `title` — display name (strip index prefix and `Café Athena - ` / `Technique Folio - ` prefixes)
   - `type` — `"technique"` if filename contains "Technique Folio", otherwise `"recipe"`
   - `chapter` and `chapterName` — from the parent folder name
3. Build a **live set** of all index values found in The Manual.

---

## Phase 2 — Read Current Registry

1. Read `recipes.json`.
2. Build a **registry set** of all `id` values currently in the `recipes` array.

---

## Phase 3 — Identify Gaps and Drift

Compare the two sets:

- **Missing entries** — in live set but not in registry set → will be added
- **Orphaned entries** — in registry but no matching file in The Manual → flag only, do not remove
- **Stage drift** — for existing entries, re-check filesystem-derivable stages and flag if they differ from the registry value:
  - `heroImage` — check for `{index}.webp` or `{index}.png` in chapter folder
  - `heroImageOptimized` — check for `{index}.webp`
  - `referenceImages` — check for `{index}[a-z].webp` or `{index}[a-z].png`
  - `referenceImagesProcessed` — check if any `{index}[a-z].png` still exist
  - `glossaryPull` — check for `## Glossary` section in source file

---

## Phase 4 — Report *(STOP POINT)*

Present a summary before making any changes:

```
SYNC REPORT
───────────────────────────────────────
Missing entries (will be added):    N
  - 10-24 — New Recipe Title
  - ...

Orphaned entries (no file found):   N
  - XX-YY — Title (flagged only, not removed)

Stage drift (filesystem vs registry): N
  - 04-11: heroImage registry=false → filesystem=true
  - ...

No changes:                         N entries already in sync
───────────────────────────────────────
```

Ask: *"Apply these changes? Orphaned entries will be flagged but not deleted."*

**WAIT** for confirmation.

---

## Phase 5 — Apply Changes

For each **missing entry**:
1. Detect initial stage state from filesystem (same logic as `/register-recipe` Phase 3).
2. Create entry with `"added": "{today's date}"`.
3. Append to `recipes` array.

For each **stage drift** item:
1. Update only the specific stage field(s) that differ.
2. Do not touch stages that were manually set (e.g., `formatAudit: true`).

For each **orphaned entry**:
1. Add `"orphaned": true` flag to the entry.
2. Do not delete — let the user decide.

Re-sort the `recipes` array by `id` ascending.

Write the updated `recipes.json`.

---

## Phase 6 — Confirm

Report:
```
✅ Registry synced.
   Added:         N new entries
   Updated:       N stage flags corrected
   Flagged:       N orphaned entries
   Total entries: N
```
