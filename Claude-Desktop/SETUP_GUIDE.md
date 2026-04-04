# CAFÉ ATHENA - CLAUDE DESKTOP PROJECT SETUP GUIDE

## Overview

This folder contains the lean, optimized setup for running the Café Athena AI Agent in Claude Desktop. The project uses:

- **PROJECT_INSTRUCTIONS.md** as the Claude Project's "Instructions" field
- **GitHub Connection** (via Project "Files" tab) for universal read-access and portability
- **Filesystem Access** (via MCP/Antigravity) for local write-access and indexing

---

## SETUP STEPS

### 1. Create Claude Desktop Project

Go to [Claude Desktop](https://claude.ai/projects) and create a new project with:

**Project Name:**

```
Café Athena - Recipe Development & Documentation
```

**Project Description:**

```
AI Chef for iterative recipe development, manuscript-ready formatting, and culinary technique education. Three modes: The Lab (development), The Manual (publication), The MasterClass (education).
```

### 2. Copy PROJECT_INSTRUCTIONS.md Content

1. Open `PROJECT_INSTRUCTIONS.md` (in this folder)
2. Copy the entire content
3. In Claude Desktop project settings, paste under **Instructions**

### 3. File Access & Portability

There are two primary ways to give the AI access to your repo. **Option A is recommended for mobile/web use.**

#### **Option A: GitHub Connector (Best for Portability)**

*Recommended if you want to use the agent via Claude.ai (Web) or Mobile.*

1. In your Claude Project, go to the **Files** tab.
2. Click **Connect to GitHub**.
3. Select your `cafe-athena` repository.
4. The AI can now **read** all files in `Guidance/`, `The Manual/`, and `PROJECT_STATUS.md` from any device.

#### **Option B: Filesystem MCP (Best for Local Execution)**

*Required if you want the AI to **write** recipes directly to your local folders and update indexes.*

1. Ensure **Claude Desktop** is configured with a Filesystem MCP server pointing to `/Users/kevinward/Projects/Cafe Athena`.
2. The AI can now **read and write** directly across the entire repo.

| Key Reference Paths | Purpose |
|------|---------|
| `Guidance/Recipe-Format-Standard.md` | Master formatting rules |
| `Guidance/Cafe-Athena-Workflow-Guide.md` | Strategic transitions |
| `The Manual/Chapter X/` | **CRITICAL:** Live indexing |
| `PROJECT_STATUS.md` | **SESSION BRIDGE:** Handoff context |

*Note: Avoid "attaching" static files manually in the Claude Project UI; they will not stay in sync with your GitHub pushes.*

---

## ANTIGRAVITY SKILLS SETUP

To use the advanced agentic skills referenced in the documentation:

1. **Install Skills Library:**
   Run this command in your terminal (installs to `~/.agent/skills/`):

   ```bash
   npx antigravity-awesome-skills --antigravity
   ```

2. **Verify Installation:**

   ```bash
   test -d ~/.agent/skills && echo "Skills installed successfully"
   ```

3. **Usage:**
   Reference skills in chat using the `@` prefix (e.g., `Use @brainstorming to...`).

---

## FILE REFERENCE GUIDE

### System Assets (Live Reading)

**Recipe-Format-Standard.md**

- Master formatting rules for all recipe outputs
- Required sections: Title Block, Headnote, Mise en Place, Ingredients, Method, Chef's Notes, Glossary
- Temperature/measurement standards (dual format, proper Unicode)
- Zero-citation protocol (no [source] or [1], [2], etc.)

**Cafe-Athena-Workflow-Guide.md**

- Workflow A: New Recipe Cycle (Lab → Manual → Publish)
- Workflow B: Learning/Folio Cycle (MasterClass content)
- Workflow C: System Integrity & Archiving

**Recipe-Example.md**

- "Spicy Brown Butter & Lemon Cheesecake Cookies"
- Reference for proper structure, tone, and formatting

**Technique-Folio-Example.md**

- "Salinity & Equilibrium"
- Reference for educational folio depth and structure

**Technique_Folio_Template_v1.md**

- Structural template for all technique folios
- Sections: Concept Definition, The Science, Technique/Practical Application, Reference Values, Safety & Constraints, Applications & Links, Sources

**The Manual/** ⭐ CRITICAL

- The AI scans the live chapter directories (e.g., `The Manual/Chapter 4/`) to assign correct XX-YY numbers.
- Never assign a number based on the `Current Version` document; it is for structural reference only.
- Agent must prove it read the live filesystem by listing the last 3 files in the target directory.

---

## KEY FUNCTIONAL DIFFERENCES FROM GEM INSTRUCTIONS

This condensed version maintains all functionality by:

✓ **Removing redundancy**: Combined mode-specific stop points into universal guidance  
✓ **Prioritizing decision logic**: When to ask vs. execute (at end)  
✓ **Filesystem precision**: Replaces static "attached" reference files with dynamic path-based reading
✓ **Keeping hard stops**: All critical safety/indexing stops preserved  
✓ **Simplifying language**: Same technical rigor, fewer words  

---

## TROUBLESHOOTING PROJECT ISSUES

**If Claude doesn't follow format standard:**
→ Confirm it has access to the `Guidance/` directory and can read the standard file

**If chapter indexing fails:**
→ Ensure the AI can see the live subdirectories in `The Manual/` and is scanning the files directly

**If mode detection fails:**
→ Check that PROJECT_INSTRUCTIONS.md keywords match user input exactly

**If citations appear in output:**
→ Remind Claude of "Zero-Citation Protocol" section in instructions

---

## MAINTENANCE

- **Update PROJECT_INSTRUCTIONS.md** if you change mode keywords or core constraints
- **Test with sample request** in each mode before production use

### SCALING NOTE

If Mode 2 index scans begin returning incorrect numbers (without a CRITICAL ERROR), the Manual file may be too large for reliable retrieval. Split into per-chapter files once the cookbook exceeds ~200 entries.
