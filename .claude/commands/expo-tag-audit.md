---
description: Scans all Expo/Posts/*.md files and reports tag usage — full tag list with counts, single-use candidates, and near-duplicate candidates. Read-only, no writes.
---

# Expo Tag Audit Workflow

1. Use the Glob tool to find all `Expo/Posts/*.md` files (excluding `.gitkeep`).
2. Read each file and extract the `tags[]` array from its frontmatter.
3. Build a frequency map: for each tag, count how many posts use it.
4. Identify near-duplicate candidates:
   - Tags that differ only by pluralization (e.g. `ortolan` vs. `ortolans`)
   - Tags that differ only by a separator style (e.g. `mise-en-place` vs. `mise en place`)
   - Tags that are substrings of another tag (e.g. `confit` and `duck-confit`)
   Use case-insensitive comparison. Flag pairs — do not auto-resolve them.
5. Output a structured report with these sections:

   ```
   ## Expo Tag Audit

   ### All Tags (alphabetical)
   beurre-blanc (2 posts)
   confit (3 posts)
   ...

   ### Single-Use Tags (review candidates)
   placeholder (1 post — placeholder-post)
   ...

   ### Near-Duplicate Candidates
   ortolan / ortolans — check: consolidate to singular?
   ...

   ### Summary
   Total unique tags: N
   Total posts scanned: N
   Single-use tags: N
   Near-duplicate pairs: N
   ```

6. Do not write any files. This command is read-only — it produces a report in the conversation only.
7. If no posts exist yet (only `.gitkeep`), report "No posts found — Expo/Posts/ contains no Markdown files."
