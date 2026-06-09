---
description: Audits the main glossary for formatting, alphabetical ordering, and duplicates
---

# Audit Glossary Workflow

1. The user will provide a command like `Audit Glossary` or `/audit-glossary`.
2. Read the split glossary files from `The Manual/Glossary/` — one file per letter (`Café Athena  - Glossary A.md` through `Café Athena  - Glossary Z.md`). Read each letter file relevant to the audit scope, or all of them for a full audit.
3. Analyze the glossary for the following issues:
   - **Formatting**: Each term should follow the strict format `- Term: Definition`. Check for missing leading hyphens, missing colons, messy bolding, or broken lines (lines cut off mid-sentence).
   - **Alphabetical Order**: The letter sections (`## A`, `## B`, etc.) must be in A-Z order. The terms _within_ each letter section must be strictly alphabetical.
   - **Duplicates**: Ensure no term is listed more than once across the entire document. If duplicates exist, compare their definitions—keep the most descriptive one or merge them gracefully.
   - **Structure**: Ensure the file begins with the main `# Cafe Athena - Glossary` header and description, followed by the `## Letter` headers. Look out for any misplaced content or formatting glitches.
4. Prepare a consolidated corrected version of the glossary text.
5. Use the Edit tool (targeted replacement per section) or the Write tool (full rewrite) to replace the flawed sections with the clean, perfectly alphabetized, and deduplicated version.
6. Present a clear summary to the user detailing precisely what was fixed (e.g., "Removed duplicate 'Beurre Noisette', fixed alphabetical order in section H, repaired broken formatting on 'Laceration'").
