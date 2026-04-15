# CAFÉ ATHENA - SYSTEM OVERVIEW & DECISION TREE

Quick reference for understanding the three modes and when to use them.

---

## THE THREE MODES AT A GLANCE

```
┌─────────────────────────────────────────────────────────────────┐
│                    CAFÉ ATHENA AI AGENT                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                ┌─────────────┼─────────────┐
                ▼             ▼             ▼
         ┌──────────┐  ┌──────────┐  ┌─────────────┐
         │ MODE 1   │  │ MODE 2   │  │  MODE 3     │
         │ THE LAB  │  │THE MANUAL│  │MASTERCLASS  │
         └──────────┘  └──────────┘  └─────────────┘
              │             │              │
         [Develop]      [Format]      [Educate]
```

---

## MODE SELECTION DECISION TREE

```
START → What do you want to do?

├─ "Work on / develop / iterate / refine a recipe"
│  └─→ MODE 1: THE LAB
│       Role: Iterate on technique, flavor, variables
│       Input: Concept + rough ingredients
│       Output: Tested recipe (not yet formatted)
│       Duration: 1-10 iterative passes
│       Exit: Say "Finalize" or "Ready for Manual"
│
├─ "Generate / format / finalize for publication"
│  └─→ MODE 2: THE MANUAL
│       Role: Convert to manuscript-ready format
│       Input: Tested recipe from Mode 1
│       Workflow: Scan Manual index → assign XX-YY → format
│       Output: Formatted recipe + INDEX DATA
│       Duration: Single pass (once)
│       Requirement: Must have Category + Chapter confirmed
│
└─ "Teach me / explain / technique folio"
   └─→ MODE 3: THE MASTERCLASS
        Role: Deep-dive technical education
        Input: Technique/topic to learn
        Output: Tutorial → (on request) Technique Folio
        Duration: 1-3 passes
        Exit: Convert to Folio format when ready
```

---

## WORKFLOW MAP

```
WORKFLOW A: New Recipe Development
═══════════════════════════════════

[Manual Work]          [Claude Work]          [Manual Work]
─────────────          ─────────────          ─────────────
   │                       │
   ├─ Concept          ┌────┴────┐           ┌─ Taste/
   ├─ Rough recipe     │ MODE 1  │           │   refine
   │                   │ The Lab │           │
   ├─ Initial test  ←──┤ [ITERATE]─────→  ┌──┴─ Adjust
   │                   │ [1-10 passes]    │  │
   └─ Finalize        └─────┬──────┘       │  │
      (say "ready")         │      ┌───────┘  │
                            │      │          │
                        [MODE 2]   │ [Test]   │
                        The Manual ├──────────┘
                        [SINGLE]   │
                        [Format]   ├─→ Write to
                                   │   The Manual/
                                   └─→ Run pipeline
                                       → Site live
```

---

## WORKFLOW B: Technique Education

```
[Manual Work]         [Claude Work]           [Manual Work]
─────────────         ─────────────           ─────────────
   │
   ├─ Topic request
   │                  ┌──────────────┐
   ├─ Questions    →  │   MODE 3     │       ┌─ Archive
   │                  │ MasterClass  │       │  in Manual
   └─ Ready?          │   [TUTORIAL] │ ─────→├─ Chapter?
                      └──────┬───────┘       │  Entry #?
                             │ (Request)     │
                             │ conversion    │
                             ▼               │
                      ┌──────────────┐      │
                      │  [FOLIO]     │      │
                      │  [FORMAT]    │──────┘
                      └──────────────┘
```

---

## STOP POINT TRIGGER MAP

Claude will STOP and wait for your confirmation when:

```
┌────────────────────────────────────────────────────────┐
│ UNIVERSAL STOP CONDITIONS (All Modes)                  │
├────────────────────────────────────────────────────────┤
│ ❌ Food Safety      → Unsafe temp, HACCP violation    │
│ ❌ Format Conflict  → Contradicts Recipe-Standard.md  │
│ ❌ Missing Info     → Critical data incomplete        │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│ MODE-SPECIFIC STOPS                                    │
├────────────────────────────────────────────────────────┤
│ MODE 1 STOPS:                                          │
│ • Before Mode 1→2 transition (needs "finalize")      │
│                                                        │
│ MODE 2 STOPS:                                          │
│ • Chapter unclear                                      │
│ • Chapter prefix mismatch (XX-YY doesn't fit chapter) │
│ • Cannot read Manual index file                        │
│ • Missing: yield, cooking method, ingredient list    │
│                                                        │
│ MODE 3 STOPS:                                          │
│ • Before tutorial→folio conversion (needs approval)   │
│ • Diagrams required but only text available           │
└────────────────────────────────────────────────────────┘
```

**Claude's STOP Response:**

```
"I need clarification on [specific element] before proceeding."
OR
"This contradicts standard culinary practice. Confirm?"
OR
"Missing [X]. Please provide before continuing."
OR
"CRITICAL ERROR: Index Scan Failed. Provide last 3 entries manually."
```

---

## FILE ATTACHMENT HIERARCHY

When Claude processes your request, it references files in this order:

```
1. PROJECT_INSTRUCTIONS.md
   └─→ Core Role, Mode Detection, Stop Points

2. Recipe-Format-Standard.md
   └─→ Required sections, formatting rules, standards

3. [Mode-Specific Files]
   ├─→ Mode 1: Recipe-Example.md
   ├─→ Mode 2: Cafe-Athena-The-Manual-Current-Version.md (CRITICAL)
   └─→ Mode 3: Technique-Folio-Template_v1.md + Example.md

4. Context Files
   ├─→ Cafe-Athena-Workflow-Guide.md (workflow context)
   └─→ Any previous conversation history
```

---

## QUICK REFERENCE: What To Say

### Starting a Mode

**MODE 1:**

```
"Let's work on [dish name]. Here's my concept: [idea]. 
Starting ingredients: [list]. I want to focus on [technique]."
```

**MODE 2:**

```
"Format this recipe for publication. Target chapter: [Chapter Name]. 
Here's the finalized version: [paste recipe]."
```

**MODE 3:**

```
"Teach me about [technique]. I want to understand [specific aspect]."
```

### Switching Modes

```
"Switch to Mode [1/2/3]: The [Lab/Manual/MasterClass]"
```

### Triggering Completion

**Mode 1 → Mode 2:**

```
"Finalize this recipe"
OR
"Ready for Manual"
```

**Mode 3 → Folio:**

```
"Ready to convert this to a Technique Folio?"
OR
"Format this as a Folio"
```

### Override (use rarely)

```
"Proceed anyway"  ← Only after Claude stops
```

---

## CRITICAL FILE: THE MANUAL

**Cafe-Athena-The-Manual-Current-Version.md is essential because:**

✓ Single source of truth for cookbook structure  
✓ Determines Chapter boundaries  
✓ Assigns next sequential XX-YY numbers  
✓ Validates new recipe placement  
✓ Prevents duplicate entries  
✓ **MUST be readable** (if not → CRITICAL ERROR)  

**Format Example:**

```
# Chapter 9 - The Pâtissier

## 09-01 Royal Icing (The Base)
## 09-02 Sugar Paste (The Medium)
## 09-03 Spicy Brown Butter & Lemon Cheesecake Cookies
```

Claude scans this to find the last entry and assign 09-04 to the next recipe.

---

## ZERO-CITATION RULE

🚫 **FORBIDDEN** in all output:

- `[source]`
- `[1]`, `[2]`, `[3]`
- `[cite]`
- `[web:1]`
- Any bracketed reference notation

✅ **WHY**: Recipes are manuscript-ready for cookbook publication. Citations break the clean copy requirement.

---

## CHEAT SHEET: Mode Characteristics

| Feature | MODE 1 | MODE 2 | MODE 3 |
|---------|--------|--------|--------|
| **Duration** | 1–10 iterations | 1 pass | 1–3 iterations |
| **Input Type** | Concept + notes | Tested recipe | Question + research |
| **Output Type** | Tested version | Formatted manuscript | Tutorial or Folio |
| **Format Standard** | Loose | Strict (Standard.md) | Template-based |
| **Requires Manual scan** | No | YES ⭐ | No |
| **Exit Condition** | "Finalize" | Single output | "Convert to Folio" |
| **Publishing Ready** | No | YES | (After Folio) YES |

---

## CLAUDE CODE SLASH COMMANDS

Run in the Claude Code CLI (Antigravity). Full definitions in `.agents/workflows/`.

| Command | Example | Purpose |
|---------|---------|---------|
| `/new-recipe` | `/new-recipe` | Scaffold a new recipe through Mode 1 |
| `/format-audit` | `/format-audit 04-15` | Audit recipe against format standard |
| `/glossary-pull` | `/glossary-pull 04-15` | Merge recipe glossary terms into main glossary |
| `/keyword-pull` | `/keyword-pull 04-15` | Add missing Keywords + Category sections |
| `/audit-glossary` | `/audit-glossary` | Fix alphabetization + duplicates in main glossary |
| `/recipe-hero-image` | `/recipe-hero-image 07-13` | Build Gemini image prompt (Create mode) |
| `/recipe-hero-image optimize` | `/recipe-hero-image optimize all` | Convert PNG → WebP, delete originals |
| `/recipe-hero-image insert` | `/recipe-hero-image insert 12-08 "after shapes list" "Caption"` | Insert `[ref:]` shortcode at position |
| `/session-handoff` | `/session-handoff` | Update PROJECT_STATUS.md, commit, push, output handoff summary |

---

## RED FLAGS (Stop Immediately)

🛑 **Claude should refuse or stop before:**

- Temperature/timing would result in food poisoning
- Chapter assignment doesn't exist in Manual
- Cannot read Manual file (index unreadable)
- Ingredient list, yield, or method missing (Modes 1→2 transition)
- Instruction contradicts established standard
