# CAFÉ ATHENA - CLAUDE DESKTOP PROJECT

This folder contains everything you need to run the Café Athena AI Agent in Claude Desktop, optimized for:
- **Recipe development** (Mode 1: The Lab)
- **Manuscript production** (Mode 2: The Manual)
- **Technique education** (Mode 3: The MasterClass)

---

## 📁 WHAT'S IN THIS FOLDER

| File | Purpose |
|------|---------|
| **PROJECT_INSTRUCTIONS.md** | Core instructions for Claude (paste into Project instructions field) |
| **SETUP_GUIDE.md** | Step-by-step setup for Claude Desktop |
| **MODE_CHECKLISTS.md** | Pre-conversation checklists for each mode (user guide) |
| **skill-guide.md** | Reference for using Antigravity Awesome Skills |
| **README.md** | This file |

---

## 🚀 QUICK START

### 1. Create Claude Desktop Project
Go to [claude.ai/projects](https://claude.ai/projects) → New Project → Name it:
```
Café Athena - Recipe Development & Documentation
```

### 2. Copy Instructions
- Open `PROJECT_INSTRUCTIONS.md` (in this folder)
- Copy all content
- Paste into Claude project **Instructions** field

### 3. Filesystem Access (Recommended)
Ensure Claude Desktop has filesystem access (via MCP or Antigravity). The instructions now point directly to project paths for the latest versions of:
1. `Guidance/Recipe-Format-Standard.md`
2. `Guidance/Cafe-Athena-Workflow-Guide.md`
3. `Guidance/Recipe-Example.md`
4. `Guidance/Technique-Folio-Example.md`
5. `Guidance/Technique_Folio_Template_v1.md`
6. `The Manual/` (for Chapter directories and `Cafe-Athena-The-Manual-Current-Version.md`)

*Note: Avoid "attaching" these files in the Claude Project UI as they may become stale. The AI will read the live filesystem.*

### 4. Test
Start a conversation with:
```
"Let's work on a new pasta recipe."
```
Claude should detect Mode 1: The Lab and confirm.

---

## 📖 HOW TO USE

### **Before Each Conversation**
- Review `MODE_CHECKLISTS.md` for the mode you want
- Make sure you have the information Claude needs
- Reduces stop points and speeds up work

### **During Conversation**
- Claude will auto-detect your mode (Lab, Manual, or MasterClass)
- Follow its guidance on stop points
- Provide sensory cues and explanations when asked

### **Mode Switching**
Say: `"Switch to Mode 2: The Manual"` anytime

---

## 🔑 KEY DIFFERENCES FROM ORIGINAL GEM INSTRUCTIONS

The condensed PROJECT_INSTRUCTIONS.md maintains **all functionality** but:

✅ **Removed 235 lines → ~400 lines** (condensed for readability)
✅ **Eliminated redundancy** (combined overlapping protocols)
✅ **Moved detail to files** (examples, templates, workflows are attached)
✅ **Kept all hard stops** (food safety, indexing, format validation)
✅ **Same technical rigor** (no capability lost)

---

## 🛑 CRITICAL FEATURES PRESERVED

### Stop Point Protocol
Claude will STOP and ask before:
- Finalizing a recipe (Mode 1→2 transition)
- Food safety violations
- Missing critical information
- Chapter indexing errors
- Index file cannot be read

### Index Update Protocol
In Mode 2, Claude MUST:
1. Scan Manual file for target chapter
2. List last 3 entries (proof of scan)
3. Assign next sequential XX-YY number
4. Fail if index cannot be read ("CRITICAL ERROR")

### Zero-Citation Protocol
No `[source]`, `[1]`, `[cite]`, or bracketed references—manuscript-ready output only.

### Format Standard
All recipes follow strict order:
1. Title Block
2. Headnote
3. Mise en Place
4. Ingredients
5. Method
6. Chef's Notes
7. Glossary

---

## ❓ FAQ

**Q: Why is the Manual file critical?**  
A: It's the index for all cookbook content. Claude scans it to assign correct recipe numbers (e.g., 09-06).

**Q: What if Claude forgets to scan the Manual?**  
A: The Stop Point Protocol requires Claude to output "CRITICAL ERROR: Index Scan Failed" if it can't read the file. You'll know immediately.

**Q: Can I skip the checklists?**  
A: You can, but they reduce stop points. More information upfront = faster results.

**Q: What if the reference files change?**  
A: No action needed. Because the instructions use direct filesystem paths, the AI always reads the most current version from your repository.

**Q: How do I know which mode to use?**  
A: See MODE_CHECKLISTS.md or just tell Claude what you want:
- "Develop a recipe" → Mode 1
- "Format for publication" → Mode 2
- "Teach me about technique" → Mode 3

---

## 🔗 FILE RELATIONSHIPS

```
Claude Desktop Project
├── PROJECT_INSTRUCTIONS.md (Core directives)
└── Filesystem Paths (Live Reading):
    ├── Guidance/Recipe-Format-Standard.md
    ├── Guidance/Recipe-Example.md
    ├── Guidance/Technique-Folio-Example.md
    ├── Guidance/Technique_Folio_Template_v1.md
    ├── Guidance/Cafe-Athena-Workflow-Guide.md
    └── The Manual/ (Chapters & Index)
```

---

## 📋 MAINTENANCE CHECKLIST

- [ ] PROJECT_INSTRUCTIONS.md copied into Claude project
- [ ] All 6 files attached to Claude project
- [ ] Manual file is current version
- [ ] Tested all 3 modes
- [ ] Reviewed MODE_CHECKLISTS.md before first use
- [ ] Confirmed stop points work (e.g., missing chapter info)

---

## 📞 SUPPORT

If Claude:
- **Ignores format standard** → Confirm the AI has access to `Guidance/Recipe-Format-Standard.md` via its filesystem tool
- **Can't index recipes** → Ensure the AI can see the `The Manual/` directory and its chapter folders
- **Generates citations** → Remind of Zero-Citation Protocol
- **Misses stop points** → Paste relevant section from PROJECT_INSTRUCTIONS.md into chat

---

**Version**: 1.0 (Feb 2026)  
**Status**: Ready for v1 Claude Desktop deployment  
**Tested Modes**: All three (Lab, Manual, MasterClass)
