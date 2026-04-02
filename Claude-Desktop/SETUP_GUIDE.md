# CAFÉ ATHENA - CLAUDE DESKTOP PROJECT SETUP GUIDE

## Overview

This folder contains the lean, optimized setup for running the Café Athena AI Agent in Claude Desktop. The project uses:
- **PROJECT_INSTRUCTIONS.md** as the Claude Project's "Instructions" field
- **Filesystem Access** via MCP/Antigravity for reference documents

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

### 3. Filesystem Access (Recommended)

To ensure the AI always uses the most current reference materials, it is recommended to use **Filesystem MCP** (in Claude Desktop) or **Antigravity**. The instructions are configured to read these paths directly:

| Path | Purpose |
|------|---------|
| `Guidance/Recipe-Format-Standard.md` | Master formatting rules for all recipe outputs |
| `Guidance/Cafe-Athena-Workflow-Guide.md` | Strategic workflow (Lab → Manual → Publish) |
| `Guidance/Recipe-Example.md` | Sample recipe following the standard |
| `Guidance/Technique-Folio-Example.md` | Sample technique folio |
| `Guidance/Technique_Folio_Template_v1.md` | Technique folio structure template |
| `The Manual/` | **CRITICAL:** Chapter directories for live indexing |
| `The Manual/Cafe-Athena-The-Manual-Current-Version.md` | Structural reference only |

*Note: If you do not have filesystem access, you must manually attach these files in the Claude Project UI, but be aware they will not automatically stay in sync with your local edits.*

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
