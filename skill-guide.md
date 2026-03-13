# Cafe Athena - Antigravity Skill Guide

This guide outlines how to leverage the **Antigravity Awesome Skills** library (1,250+ tools) to enhance your work on the Café Athena cookbook. These skills are tailored to your role as a **Michelin-star Executive Chef** and are mapped to the project's operational modes.

## 🌌 Core Skills for the Michelin Chef

| Skill | Role in Cafe Athena | How to Invoke |
| :--- | :--- | :--- |
| **@brainstorming** | Used in **Mode 1 (The Lab)** for recipe ideation, flavor pairing, and avant-garde technique exploration. | `Use @brainstorming to develop a new dessert...` |
| **@doc-coauthoring** | Essential for creating new **Technique Folios** or detailed **Recipe Headnotes**. | `Use @doc-coauthoring to draft the headnote for...` |
| **@copy-editing** | Polishes the authoritative, professional Michelin tone. Ensures technically precise prose. | `Use @copy-editing to refine the wording of this method...` |
| **@lint-and-validate** | Automatically checks for formatting compliance with `Recipe-Format-Standard.md`. | `Use @lint-and-validate to audit this recipe's format.` |
| **@concise-planning** | Helps manage complex, multi-day culinary projects (e.g., long ferments or multi-component plating). | `Use @concise-planning to map out the 3-day prep for...` |
| **@kaizen** | Encourages continuous improvement of the cookbook's "Masterclass" content. | `Use @kaizen to identify areas for improvement in Chapter 2.` |

## 🛠️ Integration into Workflows

### Mode 1: The Lab (Recipe Development)
When exploring new concepts, invoke **`@brainstorming`**. It will lead you through a structured discovery process to define ingredients, methods, and sensory cues before you write the final manuscript.

### Mode 2: The Manual (Production Formatting)
Before finalising a recipe for the Manual, run **`@copy-editing`** to ensure the instructions are imperative and technically precise. Then use **`@lint-and-validate`** to ensure all fractions (Unicode), temperatures (dual format), and en-dashes are correct.

### Mode 3: The Masterclass (Technique Education)
When drafting new Folios, use **`@doc-coauthoring`**. It helps maintain the pedagogical layer, moving from simple science to complex application as required by the `Technique_Folio_Template_v1.md`.

### Glossary Management
Use **`@lint-and-validate`** during both `/audit-glossary` and `/glossary-pull` to ensure every term follows the strict `- Term: Definition` format and lacks messy bolding or broken lines.

## 🚀 Getting Started
Ensure you have the skills installed:
```bash
npx antigravity-awesome-skills --antigravity
```
Once installed, you can mention any skill name (e.g., `@brainstorming`) in your chat with the Antigravity assistant.
