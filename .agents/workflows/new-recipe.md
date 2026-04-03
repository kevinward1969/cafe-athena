---
description: Full onboarding workflow for a newly added recipe — runs format audit, keyword pull, glossary pull, then offers to deploy and commit.
---

# New Recipe Workflow

Invoked with: `/new-recipe [file identifier]`, e.g. `/new-recipe 04-18`

This workflow runs all four onboarding steps in sequence. It has two mandatory stop points that require user authorization before proceeding.

---

## Phase 1 — Locate the Recipe

1. Search the `/Users/kevinward/Projects/Cafe Athena/The Manual/` directory for a file matching the identifier (e.g., `*04-18*`).
2. Confirm the file path and display the recipe title to the user before proceeding.
3. Read the full recipe file.

---

## Phase 2 — Format Audit

4. Read `Guidance/Recipe-Format-Standard.md` for the current format rules.
5. Evaluate the recipe against the standard. Check for:
   - **Section Order:** Title Block → Headnote → Mise en Place → Ingredients → Method → Notes → Glossary → Keywords → Category (strict vertical succession).
   - **Mise en Place Violations:** Any cooking steps (applying heat) inside Mise en Place must move to the Method.
   - **Typography:** Correct fractions, dual temperatures (°F/°C), bolded component headers, proper title block formatting.
   - **Content Completeness:** Missing sensory cues in Method, missing Yield/Timing data.
   - **Keywords:** Flag if `## Keywords` is absent or has fewer than 10 terms (non-blocking).
   - **Category:** Flag if `## Category` is absent or uses non-standard values (non-blocking).

6. **STOP POINT 1 — Format Audit Authorization:**
   Present a bulleted list of all suggested format changes to the user. Keep each bullet to 1–2 sentences.
   Ask: *"Do you accept these changes, would you like to modify any of them, or do you need clarification?"*
   **WAIT** for the user's response. Do not proceed until authorized.

7. Apply authorized format changes to the recipe file.

---

## Phase 3 — Keyword Pull

8. Re-read the (now updated) recipe file.
9. Check if `## Keywords` AND `## Category` sections already exist.
   - If BOTH exist: skip to Phase 4.
   - If either is missing: generate them.
10. Read `Guidance/Recipe-Format-Standard.md` Sections 8 and 9 for the controlled vocabulary.
11. Generate **Keywords** (10–15 comma-separated terms) covering: cooking techniques, primary ingredients, cuisine origin, equipment, flavor profile, occasion/difficulty.
12. Assign **Category** using controlled vocabulary:
    - `cuisine:` — ONE value from the allowed cuisine list
    - `style:` — ONE value from the allowed style list
    - `dietary:` — ONE value only if clearly applicable
    - **Stop Point:** If cuisine or style is genuinely ambiguous, ask the user before assigning. Do not guess.
13. Append the new sections to the end of the recipe file after the Glossary, formatted exactly as:
    ```
    ## Keywords
    term1, term2, term3, ...

    ## Category
    cuisine: French | style: Classical
    ```

---

## Phase 4 — Glossary Pull

14. Read the recipe's `### Glossary` section and extract all terms.
15. Read the main glossary at `/Users/kevinward/Projects/Cafe Athena/The Manual/Café Athena  - Glossary.md`.
16. For each extracted term, check for duplicates (exact term name match = skip).
17. Format new terms as `- Term: Definition` (no bold asterisks).
18. Insert new terms under the correct alphabetical `## [Letter]` heading in alphabetical order within that section.
19. Apply updates to the main glossary file.
20. Report which terms were added and which were skipped as duplicates.

---

## Phase 5 — Deploy & Commit

21. **STOP POINT 2 — Deploy Authorization:**
    Present a summary of all changes made across Phases 2–4.
    Ask: *"Ready to deploy to cookbook.kevinward.com and commit to GitHub?"*
    **WAIT** for the user's response.

22. If authorized:
    - Run `site/scripts/deploy.sh` to build and deploy the Astro site.
    - Stage all modified files and commit with a message in the format:
      `feat: onboard recipe [id] — [Recipe Title]`
    - Push to `origin/main`.
    - Confirm success and report the commit hash.
