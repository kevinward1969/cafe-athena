---
description: Registers a single new Expo post in Expo/expo.json after the source file is written to Expo/Posts/. Creates the entry with all stages defaulted to false.
---

# Register Expo Workflow

Invoked with: `/register-expo [slug]`

The slug is the filename without the `.md` extension.

Example: `/register-expo baguette-walkthrough`

---

## Phase 1 — Locate the Source File

1. Check that `Expo/Posts/[slug].md` exists.
2. If not found, **STOP** and report:
   > "No file found at `Expo/Posts/[slug].md`. Confirm the post has been written to Expo/Posts/ before registering."
3. Read the file and extract from its frontmatter:
   - **title** — the `title:` field value
   - **date** — the `date:` field value (ISO format, e.g. `2026-06-16`)

---

## Phase 2 — Check for Existing Entry

1. Read `Expo/expo.json`.
2. Search the `posts` array for an entry with `"id": "[slug]"`.
3. If found, **STOP** and report:
   > "`[slug]` is already registered in Expo/expo.json (title: `[existing title]`). Use `/sync-expo-registry` if the entry needs updating."

---

## Phase 3 — Detect Initial Stage State

Check the filesystem to pre-populate known stages:

- **written** — `true` if `Expo/Posts/[slug].md` exists (it does, or we'd have stopped in Phase 1)
- **heroImage** — `true` if `site/public/images/[heroImage value from frontmatter]` exists, otherwise `false`. If the `heroImage` frontmatter field is absent or empty, set `false`.
- **deployed** — `false`

---

## Phase 4 — Write Entry *(STOP POINT)*

Present the entry that will be written:

```
New registry entry for [slug]:
  title:     [title]
  date:      [date]
  stages:    written=true, heroImage=[heroImage], deployed=false
```

Ask: *"Register this entry?"*

**WAIT** for confirmation before writing.

---

## Phase 5 — Insert and Confirm

1. Read `Expo/expo.json`.
2. Build the new entry:
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
3. Append the new entry to the `posts` array.
4. Re-sort the array by `date` ascending (then by `id` ascending for same-date entries).
5. Write the updated file using the Write tool.
6. Update the `**Last Updated:**` date in `Expo/EXPO_TODO.md` to today's date.
7. Confirm:
   > "`[slug]` — `[title]` registered in Expo/expo.json."
8. Output next suggested actions:
   > **Next steps for `[slug]`:**
   > - Run `python3 site/scripts/prepare-expo.py` to rebuild expo content
   > - Run `cd site && npm run build` to verify the post renders correctly
   > - Place optimized hero image at `site/public/images/[heroImage]` when ready, then set `heroImage: true` in expo.json
