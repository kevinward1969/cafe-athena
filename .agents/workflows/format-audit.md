---
description: Audits recipes and technique folios for formatting and structural accuracy against templates.
---

# Format Audit Workflow

1. The user will provide a command like `/format-audit [identifier]`. The identifier can be a specific file (e.g., `04-15`) or a broad scope like an entire chapter (e.g., `Chapter 4`).
2. Search the `/Users/kevinward/Projects/Cafe Athena/The Manual/` directory using the `find_by_name` tool (with a wildcard pattern matching the identifier) to locate all matching documents.
3. Determine if the target documents are Recipes or Technique Folios.
4. Read the corresponding reference templates from the `/Users/kevinward/Projects/Cafe Athena/Guidance/` directory using the `view_file` tool:
   - For Recipes: `Recipe-Format-Standard.md`
   - For Technique Folios: `Technique_Folio_Template_v1.md`
5. Loop through each discovered target document and `view_file` to read its entirety.
6. Evaluate the document deeply against the template rules. Look specifically for:
   - **Vertical Order Validation:** Verify Title Block, Headnote, Mise En Place, Ingredients, Method, Notes, Glossary, Keywords, Category are all in the correct strict vertical succession.
   - **Mise En Place vs. Method Violation Checks:** Ensure that NO cooking steps (applying heat) live within the Mise En Place section. Any "cooking" steps found in Mise En Place must be relocated to the Method section.
   - **Typographical Checks:** Check for correct formatting in the Title Block, fractions, dual temperatures (e.g., Fahrenheit/Celsius), descriptive component headers, and proper bolding.
   - **Content Completeness:** Check for missing sensory cues in the Method section or missing Yield/Timing data.
   - **Keywords Check (non-blocking):** Check if `## Keywords` section exists and contains 10–15 comma-separated terms. If missing or fewer than 10 terms, flag as a formatting gap. Do not block audit on this — report only.
   - **Category Check (non-blocking):** Check if `## Category` section exists and uses valid controlled vocabulary values (`cuisine:` and `style:` fields from Recipe-Format-Standard.md Section 9). If missing or values are non-standard, flag as a formatting gap. Report only — do not halt.
7. **AUTHORIZATION LAYER (CRITICAL):** Do NOT automatically apply the changes. Instead, stop and present an evaluation to the user.
   - For each analyzed document, provide a short, bulleted list of the suggested changes (keep each bullet point to 1-2 concise sentences).
   - Example: "Recipe 04-15: Move the step 'Sauté the baby spinach' from Mise En Place to Phase 1 of the Method."
   - Example: "Recipe 04-15: Update the temperature format to include both Fahrenheit and Celsius in step 2."
8. Prompt the user: "Do you accept these changes as is, would you like to recommend modifications, or do you need clarification?"
9. **WAIT** for the user's response. Do not proceed until the user authorizes the changes.
10. Once authorized (incorporating any specific modifications the user requested), apply the updates safely using `replace_file_content` or `write_to_file`.
11. Present a final brief confirmation of what was successfully updated.
