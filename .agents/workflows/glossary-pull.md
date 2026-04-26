---
description: Pulls glossary terms from a given recipe document and adds them to the main glossary
---

# Glossary Pull Workflow

1. The user will provide a command like `/glossary-pull [file identifier]`, for example `/glossary-pull 04-15`.
2. Find the correct recipe document. Use the Glob tool in the project directory with a pattern matching the file identifier (e.g., `The Manual/**/*[file identifier]*`).
3. Use Read to read the recipe document and extract the terms listed under the `## Glossary` heading at the bottom of the file. Note how each term is formatted in the source — older folios may use `* **Term:** Definition`; current standard is `- Term: Definition`.
4. Identify the first letter of each new term and read the corresponding split glossary file from `The Manual/Glossary/Café Athena  - Glossary [LETTER].md` (e.g., `Café Athena  - Glossary A.md` for terms starting with A).
5. For each extracted term, check if it already exists in the main glossary.
   - A term is a duplicate if the exact term name already appears in the glossary.
   - If it's a duplicate, skip it.
6. For the new terms, format them strictly as `- Term: Definition` (without the bolding asterisks `**`, matching the existing glossary style).
7. Insert the new terms under the correct alphabetical headings (e.g., `## A`, `## B`) in the main glossary. Ensure that they are placed in alphabetical order within that letter section. If a letter section doesn't exist, create it.
8. Use the Edit tool (targeted replacement per section) or the Write tool (full file rewrite) to apply the updates to the main glossary file.
9. Inform the user which terms were successfully added and which were ignored as duplicates.
