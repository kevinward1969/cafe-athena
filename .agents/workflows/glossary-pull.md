---
description: Pulls glossary terms from a given recipe document and adds them to the main glossary
---

# Glossary Pull Workflow

1. The user will provide a command like `/glossary-pull [file identifier]`, for example `/glossary-pull 04-15`.
2. Find the correct recipe document to read from. Use the `find_by_name` tool in the project directory (`/Users/kevinward/Projects/Cafe Athena/`) with a pattern matching the file identifier (e.g., `*[file identifier]*`).
3. Use `view_file` to read the recipe document and extract the terms listed under the `### **Glossary**` heading at the bottom of the file. Note how each term is formatted (usually `* **Term:** Definition`).
4. Read the main glossary file located at `/Users/kevinward/Projects/Cafe Athena/The Manual/Café Athena  - Glossary.md`.
5. For each extracted term, check if it already exists in the main glossary.
   - A term is a duplicate if the exact term name already appears in the glossary.
   - If it's a duplicate, skip it.
6. For the new terms, format them strictly as `- Term: Definition` (without the bolding asterisks `**`, matching the existing glossary style).
7. Insert the new terms under the correct alphabetical headings (e.g., `## A`, `## B`) in the main glossary. Ensure that they are placed in alphabetical order within that letter section. If a letter section doesn't exist, create it.
8. Use the `replace_file_content` or `multi_replace_file_content` tool to apply the updates to the main glossary file.
9. Inform the user which terms were successfully added and which were ignored as duplicates.
