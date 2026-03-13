# Café Athena

**AI-powered recipe development, manuscript production, and culinary technique education system.**

An integrated platform for professional chefs and food scientists to develop recipes systematically, produce manuscript-ready documentation, and create formal technique education materials.

---

## 🎯 Overview

Café Athena is a structured methodology + AI implementation for:

- **The Lab** (Mode 1): Iterative recipe development with technical feedback
- **The Manual** (Mode 2): Manuscript-ready recipe formatting with automatic indexing
- **The MasterClass** (Mode 3): Deep-dive culinary technique education and folio creation

All content follows rigorous standards for food science, formatting precision, and pedagogical clarity.

---

## 📁 Repository Structure

```
cafe-athena/
├── .gitignore                          # Standard GitHub ignores
├── README.md                           # This file
├── GITHUB_SETUP.md                     # Initial setup instructions
│
├── Claude-Desktop/                     # Claude Project configuration
│   ├── PROJECT_INSTRUCTIONS.md         # Core system instructions
│   ├── SETUP_GUIDE.md                 # Claude Desktop setup guide
│   ├── COPY_PASTE_TEMPLATE.md         # Quick-reference for fields
│   ├── MODE_CHECKLISTS.md             # Pre-conversation checklists
│   ├── README.md                       # Folder overview
│   └── SYSTEM_OVERVIEW.md             # Decision trees & reference
│
├── Guidance/                           # Documentation standards (GitHub-synced)
│   ├── CAFÉ ATHENA - GEM INSTRUCTIONS.md
│   ├── Cafe-Athena-Workflow-Guide.md
│   ├── Recipe-Format-Standard.md       # ⭐ Master document
│   ├── Recipe-Example.md
│   ├── Technique-Folio-Example.md
│   ├── Technique_Folio_Template_v1.md
│   └── archived/
│
└── The Manual/                         # Cookbook manuscript (local only)
    ├── Cafe-Athena-The-Manual-Current-Version.md
    └── Chapter */
```

---

## 🚀 Quick Start

### For Claude Desktop Setup

See [Claude-Desktop/README.md](Claude-Desktop/README.md) for step-by-step instructions.

**TL;DR:**

1. Create Claude project: "Café Athena - Recipe Development & Documentation"
2. Paste `Claude-Desktop/PROJECT_INSTRUCTIONS.md` into project Instructions
3. In Files section → Connect GitHub repo → Select this repository
4. Claude automatically accesses Guidance/ files from GitHub

### For Local Development

See [GITHUB_SETUP.md](GITHUB_SETUP.md) for Git initialization and push instructions.

---

## 📖 Key Documents

### Claude-Desktop/ (Project Setup)

| File                      | Purpose                                         |
| ------------------------- | ----------------------------------------------- |
| `PROJECT_INSTRUCTIONS.md` | Core instructions (paste into Claude project)   |
| `SETUP_GUIDE.md`          | Full Claude Desktop setup with field references |
| `COPY_PASTE_TEMPLATE.md`  | Quick copy/paste values for project fields      |
| `MODE_CHECKLISTS.md`      | Pre-conversation checklists for each mode       |
| `SYSTEM_OVERVIEW.md`      | Decision trees, workflows, reference phrases    |
| `README.md`               | Folder overview and file relationships          |

### Guidance/ (Reference Standards)

All files in this folder are **synced from GitHub** in Claude Desktop. They serve as the system assets:

| File                             | Purpose                                            |
| -------------------------------- | -------------------------------------------------- |
| `Recipe-Format-Standard.md`      | **MASTER** formatting rules for all recipe outputs |
| `Recipe-Example.md`              | Sample recipe showing proper formatting            |
| `Technique-Folio-Example.md`     | Sample technique folio                             |
| `Technique_Folio_Template_v1.md` | Structural template for technique folios           |
| `Cafe-Athena-Workflow-Guide.md`  | Workflow methodology (Lab → Manual → Publish)      |

### The Manual/ (Local Cookbook)

| File                                        | Purpose                              |
| ------------------------------------------- | ------------------------------------ |
| `Cafe-Athena-The-Manual-Current-Version.md` | Master index of all cookbook content |
| `Chapter 1 - The Lab/`                      | Technique folios                     |
| `Chapter 2 - The Foundation/`               | Foundational techniques & recipes    |
| ...                                         | Additional chapters                  |

**Note:** The Manual is kept locally and optionally in a private branch. It's not in the main GitHub repo as it contains unpublished content.

---

## 🔄 GitHub Integration (Claude Desktop)

Claude Desktop has a built-in GitHub feature that automatically syncs files.

**Setup:**

1. Create this repository on GitHub
2. In Claude project → Files section → Connect GitHub
3. Select `cafe-athena` repository
4. Claude automatically accesses all files in Guidance/ (latest version always used)

**Benefits:**

- Single source of truth in GitHub
- Claude always uses current versions
- No manual file management
- Perfect for collaborative development
- Version control built-in

---

## 🎓 The Three Modes Explained

### Mode 1: The Lab – Recipe Development

- **Goal:** Develop and iterate on a recipe
- **Input:** Concept + rough ingredients
- **Output:** Tested recipe (not formatted)
- **Process:** Iterative refinement (1–10 passes)
- **Exit:** User says "Finalize" or "Ready for Manual"

### Mode 2: The Manual – Production Formatting

- **Goal:** Convert tested recipe to manuscript-ready format
- **Input:** Finalized recipe from Mode 1
- **Output:** Formatted recipe + INDEX DATA
- **Process:** Single-pass formatting + auto-indexing
- **Requirement:** Chapter must be identified; Manual scanned for next sequence number
- **File Used:** `Cafe-Athena-The-Manual-Current-Version.md` (from Claude project)

### Mode 3: The MasterClass – Technique Education

- **Goal:** Educate on culinary techniques
- **Input:** Technique/topic + specific questions
- **Output:** Tutorial → (on request) Technique Folio
- **Process:** Educational narrative, then formal structure
- **Template Used:** `Technique_Folio_Template_v1.md`

---

## 📋 Standards & Best Practices

### Recipe Format (Mode 2)

Every recipe must include (in strict order):

1. Title Block (3 separate lines)
2. Headnote (2–5 sentences + Teaching Idea)
3. Mise en Place (action checklist, no cooking steps)
4. Ingredients (grouped by component)
5. Method (phased instructions with sensory cues)
6. Chef's Notes / Variations
7. Glossary (technical terms defined)

See `Recipe-Format-Standard.md` for full details.

### Indexing (Mode 2)

- Format: `XX-YY` where XX = Chapter number, YY = Sequential entry
- Example: `09-03` = Chapter 9, Entry 3
- Claude scans the Manual to determine next number
- Prevents conflicts and maintains organization

### Zero-Citation Protocol

- No `[source]`, `[1]`, `[2]`, `[cite]`, or bracketed references
- Recipes are manuscript-ready for publication
- All references integrated into text or glossary

---

## 🛡️ Critical Constraints

✓ **Food Safety:** Claude stops on HACCP violations or unsafe temperatures  
✓ **Format Validation:** Claude enforces Recipe-Format-Standard.md  
✓ **Index Integrity:** Claude scans Manual before assigning numbers  
✓ **Stop Points:** Critical decisions require user confirmation

See `Claude-Desktop/PROJECT_INSTRUCTIONS.md` for complete stop point protocol.

---

## 🔗 Workflow Overview

```
New Recipe Idea
    ↓
Mode 1: The Lab (iterate)
    ↓ (user says "finalize")
Mode 2: The Manual (format + index)
    ↓
Transfer to Manual Manuscript
    ↓
Archive in GitHub + Local Storage

---

Technique Topic
    ↓
Mode 3: The MasterClass (educate)
    ↓ (user requests conversion)
Technique Folio (formatted)
    ↓
Transfer to Manual as Chapter entry
```

---

## 💬 Usage Example

### Mode 1 Conversation Starter

```
"Let's work on a risotto recipe. I want to focus on
the starch leaching technique and how it creates that
creamy texture without cream. Starting ingredients:
Carnaroli rice, homemade stock, white wine, butter, Parmigiano."
```

### Mode 2 Conversation Starter

```
"Format this recipe for publication. Chapter:
Chapter 4 - The Mill. Here's the finalized version: [recipe text]"
```

### Mode 3 Conversation Starter

```
"Teach me about the Maillard reaction. I understand
it's browning, but I want to know the actual chemistry
and how temperature affects it."
```

---

## 🛠️ Development Workflow

### Local Work

1. Clone this repository
2. Work on Claude-Desktop/ or Guidance/ files locally
3. Commit and push to GitHub
4. Claude Desktop automatically syncs Guidance/ files

### Publishing New Content

1. Develop in Mode 1 (local)
2. Format in Mode 2 (Claude Desktop synced)
3. Add to Manual (local)
4. Push Manual changes to private branch or local archive

### Branching Strategy

- **main** (or master): Public Guidance/ + Claude-Desktop/ setup files
- **private/manual** (optional): Unpublished cookbook content
- **develop**: Work-in-progress updates

---

## 📝 File Maintenance

| File                                        | When to Update                  | Who   |
| ------------------------------------------- | ------------------------------- | ----- |
| `Recipe-Format-Standard.md`                 | Never (unless standard changes) | Admin |
| `Cafe-Athena-Workflow-Guide.md`             | Never (unless workflow changes) | Admin |
| Templates & Examples                        | Yearly or when standards change | Admin |
| `PROJECT_INSTRUCTIONS.md`                   | If modes or core rules change   | Admin |
| `Cafe-Athena-The-Manual-Current-Version.md` | Every new recipe/folio added    | Chef  |

---

## 🚨 Troubleshooting

**Claude doesn't follow format:**
→ Verify `Recipe-Format-Standard.md` is attached in Claude project

**Mode assignment fails:**
→ Check that `PROJECT_INSTRUCTIONS.md` keywords match user input

**Indexing errors in Mode 2:**
→ Ensure `Cafe-Athena-The-Manual-Current-Version.md` is up-to-date and accessible

**GitHub sync not working:**
→ Verify Claude project GitHub integration is connected to this repo

See `Claude-Desktop/SETUP_GUIDE.md` for more troubleshooting.

---

## 📚 Documentation

- **For Claude Setup:** See `Claude-Desktop/README.md`
- **For GitHub Setup:** See `GITHUB_SETUP.md` (this repo)
- **For Workflows:** See `Guidance/Cafe-Athena-Workflow-Guide.md`
- **For Format Standards:** See `Guidance/Recipe-Format-Standard.md`
- **For User Checklists:** See `Claude-Desktop/MODE_CHECKLISTS.md`

---

## ⚡ Antigravity CA Project Workflows

These slash commands are exclusive custom workflows built specifically for the Antigravity CA Project to automate formatting and auditing tasks.

To use them, type the slash command directly into the Antigravity chat:

| Command           | Usage                                                 | Description                                                                                                                                                                                                                                                                   |
| ----------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/audit-glossary` | `/audit-glossary`                                     | Audits the main glossary file for exact formatting (`- Term: Definition`), A-Z alphabetization, and removes duplicate entries.                                                                                                                                                |
| `/glossary-pull`  | `/glossary-pull 04-15`                                | Extracts terms from a specific recipe's glossary block and merges them alphabetically into the main project glossary (preventing duplicates).                                                                                                                                 |
| `/format-audit`   | `/format-audit 04-15` or<br>`/format-audit Chapter 4` | Deeply analyzes recipes or folios against master templates. Checks structural order, formatting, and ensures no cooking steps exist in _Mise En Place_. **Includes an authorization layer** where the AI presents suggested changes for your approval before modifying files. |

---

## 🧑‍🍳 Who This Is For

- **Professional Chefs:** Develop recipes systematically with AI feedback
- **Food Scientists:** Document techniques with rigorous methodology
- **Culinary Educators:** Create formal, structured educational content
- **Cookbook Authors:** Produce manuscript-ready recipes with automatic indexing
- **Food Writers:** Maintain consistent formatting across publications

---

## 📄 License & Use

This system is designed for professional culinary documentation. Adapt as needed for your use case.

---

## 🔗 Links

- **Claude Desktop:** https://claude.ai/projects
- **GitHub Integration:** See project Files section
- **Local Setup:** See `GITHUB_SETUP.md` for Git commands

---

**Version:** 1.1 (March 2026)  
**Status:** Ready for Claude Desktop deployment  
**Last Updated:** March 13, 2026
