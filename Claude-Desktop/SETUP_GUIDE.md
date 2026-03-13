# CAFÉ ATHENA - CLAUDE DESKTOP PROJECT SETUP GUIDE

## Overview

This folder contains the lean, optimized setup for running the Café Athena AI Agent in Claude Desktop. The project uses:
- **PROJECT_INSTRUCTIONS.md** as the Claude Project's "Instructions" field
- **Attached files** (listed below) as reference documents

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

### 3. Attach Reference Files

In Claude Desktop, use the **Attach Files** feature to add (in order):

| File | Purpose |
|------|---------|
| [Recipe-Format-Standard.md](../Guidance/Recipe-Format-Standard.md) | Master formatting rules for all recipe outputs |
| [Cafe-Athena-Workflow-Guide.md](../Guidance/Cafe-Athena-Workflow-Guide.md) | Strategic workflow (Lab → Manual → Publish) |
| [Recipe-Example.md](../Guidance/Recipe-Example.md) | Sample recipe following the standard |
| [Technique-Folio-Example.md](../Guidance/Technique-Folio-Example.md) | Sample technique folio |
| [Technique_Folio_Template_v1.md](../Guidance/Technique_Folio_Template_v1.md) | Technique folio structure template |
| [Cafe-Athena-The-Manual-Current-Version.md](../The%20Manual/Cafe-Athena-The-Manual-Current-Version.md) | **CRITICAL:** Master index of all cookbook content |
| [skill-guide.md](../skill-guide.md) | Reference for Antigravity Awesome Skills |

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

### System Assets (Attached)

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

**Cafe-Athena-The-Manual-Current-Version.md** ⭐ CRITICAL
- Single source of truth for cookbook structure
- Used for INDEX UPDATE PROTOCOL in Mode 2
- Agent must scan this file to assign correct XX-YY numbers to new recipes/folios
- Format: `Chapter N - [Chapter Name]` followed by indexed entries

---

## KEY FUNCTIONAL DIFFERENCES FROM GEM INSTRUCTIONS

This condensed version maintains all functionality by:

✓ **Removing redundancy**: Combined mode-specific stop points into universal guidance  
✓ **Prioritizing decision logic**: When to ask vs. execute (at end)  
✓ **File-based detail**: Complex protocols moved to attached documents  
✓ **Keeping hard stops**: All critical safety/indexing stops preserved  
✓ **Simplifying language**: Same technical rigor, fewer words  

---

## TROUBLESHOOTING PROJECT ISSUES

**If Claude doesn't follow format standard:**
→ Ensure Recipe-Format-Standard.md is attached and Claude references it explicitly

**If chapter indexing fails:**
→ Ensure Cafe-Athena-The-Manual-Current-Version.md is attached and Claude scans it for last 3 entries

**If mode detection fails:**
→ Check that PROJECT_INSTRUCTIONS.md keywords match user input exactly

**If citations appear in output:**
→ Remind Claude of "Zero-Citation Protocol" section in instructions

---

## MAINTENANCE

- **Update PROJECT_INSTRUCTIONS.md** if you change mode keywords or core constraints
- **Replace attached files** if Guidance/ versions are updated (excepting Template)
- **Refresh Manual file** if you add new recipes to maintain accurate indexing
- **Test with sample request** in each mode before production use

### SCALING NOTE
If Mode 2 index scans begin returning incorrect numbers (without a CRITICAL ERROR), the Manual file may be too large for reliable retrieval. Split into per-chapter files once the cookbook exceeds ~200 entries.
