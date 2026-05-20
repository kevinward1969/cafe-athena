---
description: Generates and appends ## Keywords and ## Category sections to a recipe file
---

# Keyword Pull Workflow

1. The user will provide a command like `/keyword-pull [file identifier]`, for example `/keyword-pull 10-23`.
2. Find the correct recipe document. Use the Glob tool with a pattern matching the file identifier (e.g., `The Manual/**/*[file identifier]*`).
3. Read the recipe document using the Read tool.
4. Check if `## Keywords` AND `## Category` sections already exist at the bottom of the file.
   - If BOTH sections exist: report "Keywords and Category already present — no changes made." and stop.
   - If either is missing: proceed to generate the missing section(s).
5. Read `Guidance/Recipe-Format-Standard.md` Sections 9 and 10 to confirm current format rules. Read `Guidance/Taxonomy.md` for all valid controlled vocabulary values.
6. Generate **Keywords** (8–15 comma-separated terms — full recipe folios typically land 10–15; foundation/technique folios 8–12; **collection folios** that bundle multiple distinct sub-recipes may extend to 8–20) covering:
   - Cooking techniques used
   - Primary ingredients
   - Cuisine origin
   - Equipment required
   - Flavor profile
   - Occasion or difficulty level
7. Assign **Category** using the controlled vocabulary from `Guidance/Taxonomy.md`:
   - `cuisine:` — ONE value from the allowed cuisine list
   - `style:` — ONE value from the allowed style list
   - `family:` — ONE value from the allowed family list for this chapter
   - `course:` — ONE value from the allowed course list (omit for technique folios)
   - `dietary:` — ONE or more comma-separated values (only if clearly applicable)
   - **Stop Point:** If any field is genuinely ambiguous, ask the user before assigning. Do not guess.
   - **Technique folios:** use `style: Technique Folio | family: [value]` only — no `cuisine:` or `course:`.
8. Format the new sections exactly as:

   ```
   ## Keywords
   term1, term2, term3, term4, term5, term6, term7, term8, term9, term10

   ## Category
   cuisine: French | style: Classical | family: Mother Sauce | course: Component
   ```

   (Include `| dietary: Vegetarian` only if applicable.)
9. Append the new sections to the end of the source recipe file, after the Glossary section, using the Edit tool.
10. Inform the user which sections were added and confirm the category assignment.
