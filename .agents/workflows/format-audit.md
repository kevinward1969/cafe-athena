---
description: Audits recipes and technique folios for formatting and structural accuracy against templates.
---

# Format Audit Workflow

> **Note:** This slash command performs a deep AI-driven content review (sensory cues, Mise vs. Method violations, typographic checks). For bulk structural detection and automated glossary/keyword generation, use `scripts/audit.py` instead. The two tools are complementary — run `audit.py` first to close structural gaps, then `/format-audit` for content-level review.

1. The user will provide a command like `/format-audit [identifier]`. The identifier can be a specific file (e.g., `04-15`) or a broad scope like an entire chapter (e.g., `Chapter 4`).
2. Search the `The Manual/` directory using the Glob tool (with a wildcard pattern like `**/[identifier]*`) to locate all matching documents.
3. Determine if the target documents are Recipes or Technique Folios.
4. Read `Guidance/Recipe-Format-Standard.md` — it contains format rules for both Recipes and Technique Folios (see the "Technique Folio Format" section).
5. Loop through each discovered target document and Read its entirety.
6. Evaluate each document against the appropriate rules based on its type:

   **For Recipes**, check:
   - **Vertical Order:** Title Block → Headnote → Mise En Place → Ingredients → Method → Notes → Glossary → Keywords → Category
   - **Mise En Place vs. Method Violations:** No cooking steps (applying heat) in Mise. Relocate any found to Method.
   - **Typographical Checks:** Title Block format, proper fractions (⅔ not 2/3), dual temperatures (°F/°C), descriptive component headers, bolding.
   - **Content Completeness:** Sensory cues in Method steps, Yield/Timing data in Title Block.
   - **Keywords (non-blocking):** `## Keywords` exists with 8–15 lowercase comma-separated terms (full recipe folios typically land 10–15; foundation folios 8–12).
   - **Category (non-blocking):** `## Category` exists with valid `cuisine:` and `style:` fields.

   **For Technique Folios** (Chapters 1 & 2 are entirely folios; individual folios may appear in other chapters), check ONLY:
   - **Glossary:** `## Glossary` present and covers all technical terms used in the body.
   - **Keywords:** `## Keywords` present with 8–15 **lowercase** comma-separated terms (technique folios typically 8–12). Title Case keywords are a violation.
   - **Category:** `## Category` present and set to exactly `cuisine: Global | style: Technique Folio`.
   - **Temperatures:** Dual format `°F/°C` used throughout.
   - **No citation markers:** No `[source]`, `[1]`, or similar.
   - **Body headers:** Section headers use **bold inline text**, not H2 headings.
   - Do NOT flag missing Mise En Place, Ingredients, Yield/Timing, or Method phases — these do not apply to folios.
7. **AUTHORIZATION LAYER (CRITICAL):** Do NOT automatically apply the changes. Instead, stop and present an evaluation to the user.
   - For each analyzed document, provide a short, bulleted list of the suggested changes (keep each bullet point to 1-2 concise sentences).
   - Example: "Recipe 04-15: Move the step 'Sauté the baby spinach' from Mise En Place to Phase 1 of the Method."
   - Example: "Recipe 04-15: Update the temperature format to include both Fahrenheit and Celsius in step 2."
8. Prompt the user: "Do you accept these changes as is, would you like to recommend modifications, or do you need clarification?"
9. **WAIT** for the user's response. Do not proceed until the user authorizes the changes.
10. Once authorized (incorporating any specific modifications the user requested), apply the updates safely using the Edit tool (for targeted replacements) or the Write tool (for full file rewrites).
11. Present a final brief confirmation of what was successfully updated.
