---
description: Full onboarding workflow for a newly added recipe — runs format audit, keyword pull, glossary pull, then offers to deploy and commit.
---

# New Recipe Workflow

Invoked with: `/new-recipe [file identifier]`, e.g. `/new-recipe 04-18`

This workflow runs all four onboarding steps in sequence. It has two mandatory stop points that require user authorization before proceeding.

---

## Phase 1 — Locate the Recipe

1. Search the `The Manual/` directory using the Glob tool with a wildcard pattern matching the identifier (e.g., `The Manual/**/*04-18*`).
2. Confirm the file path and display the recipe title to the user before proceeding.
3. Read the full recipe file using the Read tool.
4. Read `recipes.json` and check whether an entry with `"id": "{identifier}"` already exists.
   - If missing: invoke the `/register-recipe {identifier}` workflow inline (see `.agents/workflows/register-recipe.md`) before proceeding to Phase 2. This ensures registry state can be updated as each phase completes.
   - If present: continue.

---

## Phase 2 — Format Audit

1. Read `Guidance/Recipe-Format-Standard.md` for the current format rules.
2. Evaluate the recipe against the standard. Check for:
   - **Section Order:** Title Block → Headnote → Mise en Place → Ingredients → Method → Notes → Glossary → Keywords → Category (strict vertical succession).
   - **Mise en Place Violations:** Any cooking steps (applying heat) inside Mise en Place must move to the Method.
   - **Typography:** Correct fractions, dual temperatures (°F/°C), bolded component headers, proper title block formatting.
   - **Content Completeness:** Missing sensory cues in Method, missing Yield/Timing data.
   - **Keywords:** Flag if `## Keywords` is absent or has fewer than 10 terms (non-blocking).
   - **Category:** Flag if `## Category` is absent or uses non-standard values (non-blocking).

3. **STOP POINT 1 — Format Audit Authorization:**
   Present a bulleted list of all suggested format changes to the user. Keep each bullet to 1–2 sentences.
   Ask: *"Do you accept these changes, would you like to modify any of them, or do you need clarification?"*
   **WAIT** for the user's response. Do not proceed until authorized.

4. Apply authorized format changes to the recipe file.
5. Update `recipes.json`: set `formatAudit: true` on this entry.

---

## Phase 3 — Keyword Pull

1. Re-read the (now updated) recipe file.
2. Check if `## Keywords` AND `## Category` sections already exist.
   - If BOTH exist: set `recipes.json` `keywordPull: true` and skip to Phase 4.
   - If either is missing: generate them.
3. Read `Guidance/Recipe-Format-Standard.md` Sections 8 and 9 for the controlled vocabulary.
4. Generate **Keywords** (8–15 comma-separated terms — full recipe folios typically 10–15; foundation/technique folios 8–12) covering: cooking techniques, primary ingredients, cuisine origin, equipment, flavor profile, occasion/difficulty.
5. Assign **Category** using controlled vocabulary:
    - `cuisine:` — ONE value from the allowed cuisine list
    - `style:` — ONE value from the allowed style list
    - `dietary:` — ONE value only if clearly applicable
    - **Stop Point:** If cuisine or style is genuinely ambiguous, ask the user before assigning. Do not guess.
6. Append the new sections to the end of the recipe file after the Glossary, formatted exactly as:

    ```
    ## Keywords
    term1, term2, term3, ...

    ## Category
    cuisine: French | style: Classical
    ```

7. Update `recipes.json`: set `keywordPull: true` on this entry.

---

## Phase 4 — Glossary Pull

1. Read the recipe's `## Glossary` section and extract all terms.
2. Identify the first letter of each new term and read the corresponding split glossary file from `The Manual/Glossary/Café Athena  - Glossary [LETTER].md` (e.g., `Café Athena  - Glossary A.md` for terms starting with A).
3. For each extracted term, check for duplicates (exact term name match = skip).
4. Format new terms as `- Term: Definition` (no bold asterisks).
5. Insert new terms under the correct alphabetical `## [Letter]` heading in alphabetical order within that section.
6. Apply updates to the corresponding split glossary file(s).
7. Report which terms were added and which were skipped as duplicates.
8. Update `recipes.json`: set `glossaryPull: true` on this entry.

---

## Phase 5 — Deploy & Commit

1. **STOP POINT 2 — Deploy Authorization:**
    Present a summary of all changes made across Phases 2–4.
    Ask: *"Ready to deploy to cookbook.kevinward.com and commit to GitHub?"*
    **WAIT** for the user's response.

2. If authorized:
    - Run `bash site/scripts/deploy.sh` to build and deploy the Astro site.
    - After successful deploy, update `recipes.json`: set `deployed: true` on this entry.
    - Stage modified files **by name** (do NOT use `git add -A`) and commit with a message in the format:
      `feat: onboard recipe [id] — [Recipe Title]`
    - Push to `origin/main`.
    - Confirm success and report the commit hash.
