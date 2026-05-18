---
description: Runs a recipe or folio through the full publishing pipeline — audit, keyword/category pull, glossary pull, hero image check, build, and deploy. Driven entirely by recipes.json stage flags. Handles both new recipes (all stages false) and updates (resumes from first false stage). Single entry point after any Claude Desktop Mode 1/2/3 session.
---

# Pipeline Workflow

Invoked with: `/pipeline [id]`

Example: `/pipeline 12-23`

---

## Phase 0 — Registry Read

1. Read `recipes.json`. Search for an entry with `"id": "[id]"`.
2. **If no entry exists:** run `/register-recipe [id]` first to create it, then continue here.
3. Identify all stages currently set to `false`. These are the pending stages.
4. Determine pathway:
   - **New** — no `version` field present (recipe has never been modified by the pipeline)
   - **Update** — `version` field present (content was previously changed by a pipeline run)
5. Initialize a `needs_rebuild` flag to `false`. This flag is set to `true` only when the pipeline writes changes to a folio file or a glossary file. It is never set by a clean audit pass alone.

Print a one-line status before proceeding:
> `[id] — [title] | Pathway: [new/update] | Pending: [list of false stages]`

If all stages are already `true`, report that the recipe is fully complete and stop.

---

## Phase 1 — Format Audit → `formatAudit`

Skip if `formatAudit: true`.

1. Run: `python3 scripts/audit.py --id [id] --scan-only`
2. **If clean:** mark `formatAudit: true`. Do NOT set `needs_rebuild`. Continue.
3. **If issues found:** display each issue with its fix tag (`[auto-fix]`, `[regex-fix]`, or `[manual]`).
   - Auto-fixable issues: run `python3 scripts/audit.py --id [id]` (interactive mode), show proposed fixes, **prompt to approve** before applying.
   - Manual issues: list them and ask the user to resolve or explicitly flag as an exception. Do not advance past this phase until all issues are resolved or excepted.
4. If any fixes were written to the folio file: set `needs_rebuild = true`.
5. Mark `formatAudit: true`.

---

## Phase 2 — Keyword & Category Pull → `keywordPull`

Skip if `keywordPull: true`.

1. Read the folio file. Check for `## Keywords` and `## Category` sections.
2. **If both present:** mark `keywordPull: true`. Do not set `needs_rebuild`. Continue.
3. **If either missing:** generate via Ollama using `python3 scripts/audit.py --id [id]`, show the proposed content, **prompt to approve** before writing.
4. If content was written to the folio: set `needs_rebuild = true`. Mark `keywordPull: true`.

---

## Phase 3 — Glossary Pull → `glossaryPull`

Skip if `glossaryPull: true`.

1. Extract all bullet entries from the `## Glossary` section of the folio.
2. For each term, grep across all files in `The Manual/Glossary/` for an existing entry with the same name.
3. Present findings in two groups:
   - **New terms** — show proposed definition and target letter file
   - **Existing terms** — show current definition vs proposed; flag if the new version meaningfully adds to the existing one
4. Before writing, strip any recipe-specific context from definitions (e.g., "used here for...", "in this recipe..."). Definitions in the main glossary must be universal.
5. **Prompt to confirm** the full list before writing anything.
6. Write approved entries to the correct letter files in `The Manual/Glossary/`, inserting in alphabetical order within the file.
7. Set `needs_rebuild = true`. Mark `glossaryPull: true`.

---

## Phase 4 — Hero Image → `heroImage` + `heroImageOptimized`

Skip if `heroImage: true` AND `heroImageOptimized: true`.

1. Check for `site/public/images/[id].webp`:

   **File found:**
   Run a spec check using `sips`:
   ```bash
   sips -g pixelWidth -g pixelHeight -g fileSize "site/public/images/[id].webp"
   ```
   - Warn (non-blocking) if dimensions ≠ 1920×1080
   - Warn (non-blocking) if file size > 500 KB
   - Mark `heroImage: true` and `heroImageOptimized: true`. Continue.

   **File not found:**
   **STOP.** Output:
   > Hero image missing for `[id]`. Place `[id].webp` in `site/public/images/` then re-run `/pipeline [id]`. All completed stages are saved — the pipeline will resume from this point.

   Do not proceed to build or deploy.

---

## Phase 5 — Pre-Deploy Review

Run only if `needs_rebuild = true`.

1. Print a full summary of every change made during this pipeline run (folio edits, glossary additions/updates, registry flag changes).
2. Flag any items that warrant judgment before going live:
   - Keyword count outside 8–15 range (or 8–20 for collection folios)
   - Unresolved manual audit issues marked as exceptions
   - Glossary terms that updated an existing definition
3. **Prompt:** *"Deploy these changes to cookbook.kevinward.com? [y/n]"*
4. If `n`: stop. All registry flags are already written — re-running `/pipeline [id]` will skip completed stages and resume at this prompt.
5. If `y`: continue to Phase 6.

If `needs_rebuild = false`: skip entirely. Nothing changed, nothing to deploy.

---

## Phase 6 — Build & Deploy

Run only if `needs_rebuild = true` and user approved in Phase 5.

1. Run from the repo root:
   ```bash
   bash site/scripts/deploy.sh
   ```
   This runs `prepare-content.py` → `npm run build` (includes Pagefind) → rsync to FastComet.
2. Confirm rsync completed successfully (look for `✅ Deployed successfully!` in output).
3. Mark `deployed: true` in registry.

---

## Phase 7 — Registry & Tracking Finalization

1. Write all updated stage flags to `recipes.json`.
2. **Version bump** — only if `needs_rebuild = true` (content actually changed):
   - **No `version` field present:**
     - ID ends in `_2` or higher numeric suffix → add `version: "2.1"`
     - No suffix → add `version: "1.1"`
   - **`version` field present:** increment the minor version
     - `"1.1"` → `"1.2"`, `"1.9"` → `"1.10"`, `"2.1"` → `"2.2"`, etc.
   - Set `lastModified: [today's ISO date]`
3. Update `PROJECT_STATUS.md` Last Updated date.
4. Commit all changes in a single commit:
   ```
   chore([id]): pipeline — [comma-separated list of stages completed]
   ```
   Example: `chore(12-23): pipeline — formatAudit, glossaryPull, deploy`
5. Push to GitHub.

---

## Pipeline Rules

- **Registry drives everything.** Never run a stage that is already `true`. Never skip a stage that is `false`.
- **Never rebuild if nothing changed.** `needs_rebuild` must be `true` to trigger a build. A clean audit pass alone does not trigger a rebuild.
- **Never version-bump a no-content-change run.** Version increments only when folio or glossary files are written.
- **Always prompt before deploy.** Even if everything looks clean, require explicit approval before rsync.
- **Hero image absence is a hard stop.** Do not build or deploy without the image present.
- **Hero image spec warnings are non-blocking.** Warn on dimension or size issues, but continue.
- **Glossary definitions must be universal.** Strip recipe-specific language before writing to the main glossary.
- **One commit per pipeline run.** Bundle everything — folio changes, glossary changes, registry updates, PROJECT_STATUS — into a single commit.
