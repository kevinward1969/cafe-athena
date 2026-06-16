---
description: Syncs Expo/expo.json against the live Expo/Posts/ directory. Adds missing entries, updates filesystem-derivable stage flags, and reports discrepancies. Does not remove entries or reset completed stages.
---

# Sync Expo Registry Workflow

Invoked with: `/sync-expo-registry`

---

## Phase 1 — Scan Expo/Posts/

1. Use Glob to find all `*.md` files under `Expo/Posts/` (recursive, `**/*.md`).
2. For each file, extract:
   - `id` — the filename without the `.md` extension (this is the slug and URL segment)
   - `title` — the `title:` field from frontmatter; `null` if absent
   - `date` — the `date:` field from frontmatter; `null` if absent
   - `heroImage` — the `heroImage:` field from frontmatter; `null` if absent
3. Build a **live set** of all `id` values found in `Expo/Posts/`.

---

## Phase 2 — Read Current Registry

1. Read `Expo/expo.json`.
2. Build a **registry set** of all `id` values in the `posts` array.

---

## Phase 3 — Identify Gaps and Drift

Compare the sets:

- **Missing entries** — in live set but not in registry → will be added
- **Orphaned entries** — in registry but no matching file in `Expo/Posts/` → flag only, do not remove
- **Stage drift** — for existing entries, re-check filesystem-derivable stages and flag if they differ:
  - `heroImage` — check if `site/public/images/[heroImage frontmatter value]` exists. If the frontmatter `heroImage` field is absent, skip this check.
  - `written` — always `true` if the file exists (it does, or it's an orphan)
  - `deployed` — cannot be derived from filesystem; leave existing value unchanged

---

## Phase 4 — Report *(STOP POINT)*

Present a summary before making any changes:

```
EXPO SYNC REPORT
───────────────────────────────────────
Missing entries (will be added):    N
  - baguette-walkthrough — Baguette Walkthrough (2026-07-01)
  - ...

Orphaned entries (no file found):   N
  - old-post — Old Post Title (flagged only, not removed)

Stage drift (filesystem vs registry): N
  - placeholder-post: heroImage registry=false → filesystem=true

No changes:                         N entries already in sync
───────────────────────────────────────
```

Ask: *"Apply these changes? Orphaned entries will be flagged but not deleted."*

**WAIT** for confirmation.

---

## Phase 5 — Apply Changes

For each **missing entry**:
1. Read the source file frontmatter to extract `title`, `date`, and `heroImage`.
2. Detect initial stage state from filesystem (same logic as `/register-expo` Phase 3).
3. Create the entry:
   ```json
   {
     "id": "[slug]",
     "title": "[title]",
     "date": "[date]",
     "stages": {
       "written": true,
       "heroImage": [true|false],
       "deployed": false
     }
   }
   ```
4. Append to `posts` array.

For each **stage drift** item:
1. Update only the specific stage field(s) that differ.
2. Do not touch stages that were manually set or cannot be derived from the filesystem.

For each **orphaned entry**:
1. Add `"orphaned": true` flag to the entry.
2. Do not delete — let the user decide.

Re-sort the `posts` array by `date` ascending (then `id` ascending for same-date entries).

Write the updated `Expo/expo.json`.

---

## Phase 6 — Confirm

Report:
```
✅ Expo registry synced.
   Added:         N new entries
   Updated:       N stage flags corrected
   Flagged:       N orphaned entries
   Total entries: N
```
