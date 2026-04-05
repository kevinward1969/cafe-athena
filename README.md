# Café Athena

**A culinary manuscript system — AI-powered recipe development, technique education, and a published digital cookbook.**

Café Athena is a structured three-mode methodology for professional recipe development, backed by a published Astro website. The Manual is the source-of-truth manuscript; the site is the digital face of it.

---

## Overview

The system operates in three modes:

- **The Lab** (Mode 1): Iterative recipe development with technical AI feedback
- **The Manual** (Mode 2): Manuscript-ready formatting with automatic indexing
- **The MasterClass** (Mode 3): Deep-dive technique education and folio creation

All content follows rigorous standards for food science, formatting precision, and pedagogical clarity.

---

## 📁 Repository Structure

```
cafe-athena/
├── README.md
├── PROJECT_STATUS.md               # Active development tracker
│
├── The Manual/                     # Cookbook manuscript (local only)
│   ├── Cafe-Athena-The-Manual-Current-Version.md
│   ├── Café Athena - Glossary.md
│   ├── Chapter 1 - The Lab/
│   ├── Chapter 2 - The Foundation/
│   ├── Chapter 3 - Garde Manger/
│   ├── Chapter 4 - The Mill/
│   ├── Chapter 5 - The Fishmonger/
│   ├── Chapter 6 - The Poulterer/
│   ├── Chapter 7 - The Butcher/
│   ├── Chapter 8 - The Field/
│   ├── Chapter 9 - The Pâtissier/
│   ├── Chapter 10 - Stocks & Mother Sauces/
│   └── Chapter 11 - Spice Blends & Oils/
│
├── site/                           # Astro website (public cookbook)
│   ├── src/
│   │   ├── content/recipes/        # Compiled recipe content (123 entries)
│   │   ├── layouts/                # BaseLayout, RecipeLayout, SectionLayout
│   │   ├── pages/                  # index, academy, brigade, glossary, larder, search
│   │   ├── plugins/                # remark-ref-images.mjs
│   │   └── styles/                 # global.css (Tailwind + custom)
│   ├── public/images/              # Hero and reference images
│   ├── scripts/                    # prepare-content.py (content pipeline)
│   └── astro.config.mjs
│
├── Guidance/                       # Standards and workflow definitions
│   ├── Recipe-Format-Standard.md   # ⭐ Master formatting document
│   ├── Recipe-Example.md
│   ├── Technique-Folio-Example.md
│   ├── Technique_Folio_Template_v1.md
│   ├── Cafe-Athena-Workflow-Guide.md
│   ├── CAFÉ ATHENA - GEM INSTRUCTIONS.md       # Gemini Gem 1 (culinary AI)
│   ├── CAFÉ ATHENA - HERO IMAGE GEM INSTRUCTIONS.md  # Gemini Gem 2 (image AI)
│   └── archived/
│
├── .claude/                        # Claude Code (Antigravity) configuration
│   ├── agents/
│   │   └── Cafe Athena Chef.agent.md  # Sub-agent definition
│   └── settings.local.json
│
├── .agents/                        # Claude Code slash-command workflow files
│   └── workflows/
│       ├── new-recipe.md
│       ├── format-audit.md
│       ├── glossary-pull.md
│       ├── keyword-pull.md
│       ├── audit-glossary.md
│       ├── recipe-hero-image.md
│       └── session-handoff.md
│
├── scripts/                        # Local Python utility scripts (Ollama-powered)
│   ├── audit.py                    # ⭐ Recipe audit & repair tool
│   ├── add-glossary-sections.py    # (superseded by audit.py)
│   └── extract-keywords.py         # (superseded by audit.py)
│
└── Claude-Desktop/                 # Legacy Claude Desktop configuration
```

---

## 🌐 The Website

The Astro site is the published face of the cookbook.

**Stack:** Astro 6, Tailwind CSS 4, GSAP, Pagefind (full-text search)

| Route | Purpose |
| --- | --- |
| `/` | Homepage |
| `/larder` | Recipes browsed by chapter |
| `/academy` | Technique folios by chapter |
| `/glossary` | Full culinary glossary |
| `/search` | Full-text search (Pagefind) |
| `/brigade` | About |

### Content Pipeline

Manual → Site is a one-command transform:

```bash
cd site
python scripts/prepare-content.py   # converts The Manual → src/content/recipes/
npm run build                        # builds + indexes for Pagefind
```

`prepare-content.py` reads Markdown files from `The Manual/`, transforms them into Astro-compatible frontmatter, and writes compiled files to `site/src/content/recipes/`.

### Images

There are two image types: **hero images** (one per recipe, shown at the top of the recipe page) and **reference images** (inline figures within the recipe body).

**Naming convention:**

| Type | Filename pattern | Example |
| --- | --- | --- |
| Hero image | `{index}.webp` | `04-16.webp` |
| Reference image | `{index}{letter}.webp` | `04-16a.webp`, `04-16b.webp` |

**Canonical location:** `site/public/images/` is the source of truth for all processed images. Chapter folders in `The Manual/` are working directories — images are deleted from them once processed and deployed.

#### Hero Image Workflow

Use `/recipe-hero-image` (three modes):

| Mode | Command | What it does |
| --- | --- | --- |
| Create | `/recipe-hero-image 04-17` | Reads recipe frontmatter + headnote, builds a Gemini prompt, hands off to you to generate and save the PNG |
| Insert | `/recipe-hero-image insert 04-11 "after the shapes list" "Caption"` | Inserts a `[ref:]` shortcode at the right position in the source folio and assigns the next available letter |
| Optimize | `/recipe-hero-image optimize 04-17` | Converts PNG → WebP (quality 85, max 1920×1080), deletes the original PNG, deploys, then deletes the WebP from the chapter folder |

You can also optimize a full chapter or everything at once:

```
/recipe-hero-image optimize chapter-4
/recipe-hero-image optimize all
```

**Bypass path:** If you have already optimized the image and placed the WebP directly into `site/public/images/`, tell Claude Code — it will skip optimization, update `recipes.json`, deploy, and commit without touching the chapter folder.

#### Reference Image Shortcode

Place this shortcode as a standalone paragraph (blank line above, blank line below) anywhere in the recipe body:

```
[ref:04-16a | The laminated pasta dough at final thickness]
```

The custom remark plugin (`remark-ref-images.mjs`) transforms it into a captioned `<figure>` pulling from `public/images/04-16a.webp`. Letters are assigned sequentially — if `04-16a` and `04-16b` already exist, the next is `04-16c`. Use `/recipe-hero-image insert` to handle this automatically.

---

## 🎓 The Three Modes

### Mode 1: The Lab — Recipe Development

- **Goal:** Develop and iterate on a recipe
- **Input:** Concept + rough ingredients
- **Output:** Tested recipe (not yet formatted)
- **Process:** Iterative refinement (1–10 passes)
- **Exit:** User says "Finalize" or "Ready for Manual"

**Starter:**

```
"Let's work on a risotto. I want to focus on starch leaching
and how it creates that creamy texture without cream. Starting
ingredients: Carnaroli rice, homemade stock, white wine,
butter, Parmigiano."
```

### Mode 2: The Manual — Production Formatting

- **Goal:** Convert a tested recipe to manuscript-ready format
- **Input:** Finalized recipe from Mode 1
- **Output:** Formatted recipe + INDEX DATA block
- **Process:** Single-pass formatting + auto-indexing
- **Requirement:** Chapter must be identified; Manual scanned for next sequence number

**Starter:**

```
"Format this for publication. Chapter: Chapter 4 - The Mill.
Here's the finalized version: [recipe text]"
```

### Mode 3: The MasterClass — Technique Education

- **Goal:** Educate on a culinary technique
- **Input:** Technique topic + specific questions
- **Output:** Tutorial → (on request) Technique Folio
- **Template:** `Technique_Folio_Template_v1.md`

**Starter:**

```
"Teach me about the Maillard reaction — not just browning,
the actual chemistry and how temperature affects it."
```

---

## 🔧 Local Python Tools

These scripts run locally and use [Ollama](https://ollama.com) for AI generation — no API tokens consumed.

### Prerequisites

```bash
# Install Ollama (macOS)
brew install ollama
ollama serve         # starts the local server at localhost:11434

# Pull the models used by audit.py
ollama pull llama3.2   # default — fast, 2 GB
ollama pull gemma3:4b  # higher quality output, 3.3 GB
```

### audit.py — Recipe Audit & Repair

The primary local tool. Scans every recipe file against the format standard, identifies structural issues, generates fixes via Ollama for auto-fixable problems, and applies changes only after user approval. Results are written back to `recipes.json` under an `audit` block.

```bash
# Audit all recipes (scan only — no changes)
python3 scripts/audit.py --scan-only

# Show current audit status summary
python3 scripts/audit.py --status

# Audit a single recipe (with fix generation + approval)
python3 scripts/audit.py --id 04-15

# Audit an entire chapter
python3 scripts/audit.py --chapter 3

# Audit only recipes not yet audited
python3 scripts/audit.py --pending-only

# Use a different model (gemma3:4b produces richer definitions)
python3 scripts/audit.py --model gemma3:4b

# Apply all generated fixes without interactive prompts (use when running via Claude Code)
python3 scripts/audit.py --auto-approve
```

**What it detects:**

| Issue | Auto-fix via Ollama? |
| --- | --- |
| Missing `## Headnote` | No — manual rewrite needed |
| Missing `## Mise en Place` | No — manual rewrite needed |
| Missing `## Ingredients` | No — manual rewrite needed |
| Missing `## Method` | No — manual rewrite needed |
| Missing `## Glossary` | **Yes** — generates 3–8 culinary definitions |
| Missing `## Keywords` | **Yes** — generates 10–15 comma-separated terms |
| Missing `## Category` | **Yes** — assigns from controlled vocabulary |
| Malformed `## Category` | **Yes** — rewrites to correct format |
| Sections out of order | No — flagged for manual correction |
| Pre-standard bold-header format | No — flagged for full reformat in Claude Desktop |

**Approval flow:** For each recipe with auto-fixable issues, `audit.py` calls Ollama, displays the proposed content, and asks `[y/n/edit]` before writing anything. Approved fixes are applied to the source file in `The Manual/` and the `audit` field in `recipes.json` is updated.

**recipes.json `audit` block:**

```json
"audit": {
  "lastRun": "2026-04-05",
  "status": "clean | issues_found | approved",
  "issues": ["missing_glossary", "missing_keywords"]
}
```

### Relationship to `/format-audit`

The `/format-audit` slash command (Claude Code) and `audit.py` are **complementary, not competing**:

| Tool | Scope | Depth | Use when |
| --- | --- | --- | --- |
| `audit.py` | Structural section detection | Fast, pattern-based | Bulk scanning and glossary/keyword generation |
| `/format-audit` | Deep content review | AI-driven, nuanced | Checking sensory cues, Mise vs. Method violations, typographic correctness |

Run `audit.py` first to fix structural gaps, then `/format-audit` for deep content review.

---

## ⚡ Claude Code Workflows

Slash commands for common tasks — type directly in the Antigravity chat (Claude Code):

| Command | Example | Description |
| --- | --- | --- |
| `/new-recipe` | `/new-recipe` | Scaffold a new recipe through Mode 1 |
| `/format-audit` | `/format-audit 04-15` or `/format-audit Chapter 4` | Audit a recipe against format standards with authorization layer |
| `/glossary-pull` | `/glossary-pull 04-15` | Extract and merge glossary terms from a recipe |
| `/audit-glossary` | `/audit-glossary` | Fix alphabetization + duplicates in the main glossary |
| `/keyword-pull` | `/keyword-pull 04-15` | Extract keywords for site metadata |
| `/recipe-hero-image` | `/recipe-hero-image 04-15` | Generate a hero image brief for a recipe |
| `/session-handoff` | `/session-handoff` | Update PROJECT_STATUS.md and commit all session changes |

Workflow definitions live in `.agents/workflows/`.

---

## 📋 Format Standards

Every recipe must include, in strict order:

1. Title Block (3 separate lines)
2. Headnote (2–5 sentences + Teaching Idea)
3. Mise en Place (action checklist — no cooking steps)
4. Ingredients (grouped by component)
5. Method (phased instructions with sensory cues)
6. Chef's Notes / Variations
7. Glossary (technical terms defined)

See `Guidance/Recipe-Format-Standard.md` for the full specification.

**Zero-Citation Protocol:** No `[source]`, `[1]`, `[cite]`, or bracketed references. All references are integrated into text or the glossary. Content is manuscript-ready.

---

## 🗂️ Indexing System

Every recipe and folio has a unique index in `XX-YY` format:

- `XX` = Chapter number (zero-padded)
- `YY` = Sequential entry number within the chapter

Example: `04-11` = Chapter 4, entry 11.

The hero image filename matches the folio index: `04-11.webp`.

Reference images extend this with a letter suffix: `04-11a`, `04-11b`.

Claude scans the live Manual directory before assigning any new number to prevent conflicts.

---

## 🛡️ Critical Constraints

- **Food Safety:** Claude stops on HACCP violations or unsafe temperatures
- **Format Validation:** Claude enforces `Recipe-Format-Standard.md`
- **Index Integrity:** Claude scans the live Manual before assigning any number
- **Stop Points:** Critical decisions require user confirmation before proceeding

---

## 🛠️ Local Development

### Astro Site

```bash
cd site
npm install
npm run dev        # dev server at localhost:4321
npm run build      # production build + Pagefind index
npm run preview    # preview production build
```

### Content Pipeline

Run after adding or editing any files in `The Manual/`:

```bash
cd site
python scripts/prepare-content.py
```

---

## 📄 Key Documents

| File | Purpose |
| --- | --- |
| `Guidance/Recipe-Format-Standard.md` | Master formatting rules |
| `Guidance/Cafe-Athena-Workflow-Guide.md` | Full workflow methodology |
| `Guidance/Technique_Folio_Template_v1.md` | Template for technique folios |
| `The Manual/Cafe-Athena-The-Manual-Current-Version.md` | Master index of all content |
| `The Manual/Café Athena - Glossary.md` | Consolidated culinary glossary |
| `PROJECT_STATUS.md` | Active work, pending items, strategic context |
| `MULTI_AGENT_ARCHITECTURE.md` | Full multi-agent system map, evaluation, and improvement roadmap |

---

**Version:** 2.0  
**Status:** Active — 123 entries across 11 chapters  
**Last Updated:** April 2026
