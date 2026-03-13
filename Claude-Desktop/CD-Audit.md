# CAFÉ ATHENA — CLAUDE DESKTOP AUDIT & IMPROVEMENT WORKPLAN

**Created:** 2026-03-12  
**Status:** Complete  
**Scope:** `Claude-Desktop/` folder + `PROJECT_INSTRUCTIONS.md`

---

## WORKPLAN

### Issue 1 — Mode Detection: Replace Keyword Triggers with Intent Classification
**File:** `PROJECT_INSTRUCTIONS.md` → MODE DETECTION & SELECTION section  
**Risk:** Medium-High  

Current keyword lists are fragile. Users rarely speak the exact trigger words. Replace with intent-based classification that asks for clarification when intent is unclear.

**Change:**
- Remove explicit keyword lists from mode definitions
- Add a CoT instruction: *Before responding, classify user intent as Mode 1, 2, or 3. If unclear, ask.*
- Add fallback question for ambiguous inputs: "To make sure I help correctly — are you (1) developing a recipe, (2) formatting for the cookbook, or (3) learning a technique?"

**Status:** [x] Complete — 2026-03-12

---

### Issue 2 — Mode 2 Index Scan: Add Verification Block to Output
**File:** `PROJECT_INSTRUCTIONS.md` → MODE 2 section  
**Risk:** Medium  

Silent index scan errors can produce wrong XX-YY numbers. Force Claude to show its work by appending a visible verification block to every Mode 2 output.

**Change:** Add to Mode 2 output protocol:
```
After generating the recipe, append:
---
INDEX VERIFICATION
Chapter scanned: [Chapter Name]
Last 3 entries found: [XX-01], [XX-02], [XX-03]
Assigned number: [XX-04]
---
User must confirm before adding to the Manual.
```

**Status:** [x] Complete — 2026-03-12

---

### Issue 3 — Documentation: Fix Line Count Discrepancy
**File:** `COPY_PASTE_TEMPLATE.md` → Step 2, line 29  
**Risk:** Low  

`COPY_PASTE_TEMPLATE.md` states PROJECT_INSTRUCTIONS.md is "~400 lines" — it is actually ~120 lines. This may cause users to think the paste is incomplete during setup.

**Change:** Update line 29 to accurately state the file length (~120 lines).

**Status:** [x] Complete — 2026-03-12

---

### Issue 4 — Multi-Intent Requests: Add Handling Rule
**File:** `PROJECT_INSTRUCTIONS.md` → MODE DETECTION & SELECTION section  
**Risk:** Low-Medium  

No handler exists for requests that span multiple modes (e.g., "Work on the sauce and then get it formatted"). Without a rule, Claude may skip directly to Mode 2.

**Change:** Add after AMBIGUOUS GREETING block:
```
MULTI-INTENT REQUESTS:
If user describes development AND formatting in one message:
→ Start in Mode 1
→ At completion, confirm: "Ready to move to Mode 2: The Manual?"
→ Never skip to Mode 2 without explicit user confirmation
```

**Status:** [ ] To Do

---

### Issue 5 — Context Window: Add Scaling Guidance for Large Manual Files
**File:** `SETUP_GUIDE.md` → MAINTENANCE section  
**Risk:** Medium (future)  

As the cookbook grows, the Manual file will eventually strain reliable context retrieval. No guidance currently exists for this scenario.

**Change:** Add to MAINTENANCE section:
```
SCALING NOTE:
If Mode 2 index scans begin returning incorrect numbers (without a CRITICAL ERROR), 
the Manual file may be too large for reliable retrieval. 
Split into per-chapter files once the cookbook exceeds ~200 entries.
```

**Status:** [ ] To Do

---

## GAP ISSUES

### Gap A — Version Tracking
**File:** `PROJECT_INSTRUCTIONS.md` (header) + `README.md`  

No way to identify which version of the system prompt is active. Add a version line to `PROJECT_INSTRUCTIONS.md` header and keep it in sync with `README.md`.

**Change:** Add `Version: 1.x` to `PROJECT_INSTRUCTIONS.md` header. Update when instructions change.

**Status:** [ ] To Do

---

### Gap B — Technique Folio Index Protocol (Mode 3 → Manual)
**File:** `PROJECT_INSTRUCTIONS.md` → MODE 3 section  

Recipes have a full Index Update Protocol (Mode 2) but Technique Folios entering the Manual have no equivalent. Folios need sequential numbers too.

**Change:** Add to Mode 3:
```
FOLIO INDEX PROTOCOL (when converting to Folio for Manual entry):
→ Scan Manual for target chapter
→ List last 3 entries (proof of scan)
→ Assign next sequential XX-YY number
→ Append INDEX DATA block (same format as Mode 2 recipes)
```

**Status:** [ ] To Do

---

### Gap C — Persona Consistency Across Modes
**File:** `PROJECT_INSTRUCTIONS.md` → ROLE & PERSONA section  

The Chef persona is defined once at the top but not reinforced per-mode. Long iterative sessions (especially Mode 1 with 10 passes) can cause persona drift.

**Change:** Add one-line persona reminder to each mode block:
```
[Tone: professional, authoritative, technically precise — Michelin-star Chef perspective]
```

**Status:** [ ] To Do

---

### Gap D — Mode-Appropriate Reasoning Depth
**File:** `PROJECT_INSTRUCTIONS.md`  

No guidance on varying reasoning style by mode. Each mode has a distinct purpose that benefits from a different cognitive approach:
- Mode 1: Creative, generative, exploratory
- Mode 2: Precise, deterministic, rule-following
- Mode 3: Explanatory, layered, pedagogical

**Change:** Add one-line tone/reasoning directive to each mode block:
```
Mode 1: Exploratory — prioritize creativity and variation
Mode 2: Precise — follow format standard exactly, no improvisation
Mode 3: Pedagogical — layer concepts from simple to complex
```

**Status:** [ ] To Do

---

## COMPLETION CHECKLIST

- [x] Issue 1 — Mode detection rewrite ✓
- [x] Issue 2 — Mode 2 verification block ✓
- [x] Issue 3 — Fix line count in COPY_PASTE_TEMPLATE.md ✓
- [x] Issue 4 — Multi-intent request handler ✓ *(done in Issue 1)*
- [x] Issue 5 — Context scaling guidance in SETUP_GUIDE.md ✓
- [x] Gap A — Version tracking ✓
- [x] Gap B — Folio index protocol ✓
- [x] Gap C — Persona consistency ✓
- [x] Gap D — Reasoning depth per mode ✓

---

## OBSERVATIONS (New Issues Found During Editing)

### Obs-1 — `[action]` vs `[summarize intent]` in Mode Responses
**Found during:** Issue 1 rewrite  
**File:** `PROJECT_INSTRUCTIONS.md` → Mode confirmations  
The original `[action]` placeholder could lead Claude to parrot back the user's literal phrase rather than restating the understood intent. The rewrite updated this to `[summarize intent]` — this is a minor clarification but worth confirming is the right behavior.

### Obs-2 — Workflow Guide Not Referenced in Modes
**Found during:** Issue 1 rewrite  
**File:** `PROJECT_INSTRUCTIONS.md` → SYSTEM ASSETS list (line 3 of asset list)  
`Cafe-Athena-Workflow-Guide.md` is listed as asset #3 in SYSTEM ASSETS with no indication of *which mode* should consult it. Mode 1 references the Format Standard and Recipe Example; Mode 2 references the Manual; Mode 3 references the Folio files — but the Workflow Guide floats without an explicit mode anchor. It likely belongs in Mode 1 or as a global reference. Worth deciding.

### Obs-3 — ANTIGRAVITY section is inside the system prompt paste
**Found during:** Issue 1 review  
**File:** `PROJECT_INSTRUCTIONS.md` → lines 110–119 (ANTIGRAVITY CA PROJECT WORKFLOWS section)  
This section contains `/format-audit`, `/glossary-pull`, and `/audit-glossary` slash commands — which are Antigravity-specific and explicitly noted as "executed exclusively via the Antigravity assistant UI." Including this block in the Claude Desktop paste is harmless but adds noise to a Claude Desktop context where those commands don't apply. Consider whether to strip it from the clipboard version or keep as-is.

### Obs-4 — Duplicate Index Failure Message
**Found during:** Issue 2 edit  
**File:** `PROJECT_INSTRUCTIONS.md` → CRITICAL STOP POINTS section  
The CRITICAL STOP POINTS section already contained: `Cannot read Index: output "CRITICAL ERROR: Index Scan Failed."` The new Mode 2 OUTPUT PROTOCOL step 5 now contains the same error message. Both are retained (one is a global stop rule, the other is mode-specific), which is fine — but the wording should be kept identical in both places. Currently they match exactly. Flag if either is edited later.

### Obs-5 — STEP 4 Test Prompt Uses Old Expected Response
**Found during:** Issue 3 edit  
**File:** `COPY_PASTE_TEMPLATE.md` → STEP 4: Test the Setup (lines 73–78)  
The "Expected Response" example shows: `"I understand you want to develop a recipe. Let's proceed in Mode 1: The Lab."` This now reads correctly against the new system prompt (which uses `[summarize intent]`), but the setup test prompt `"Let's work on a new pasta recipe."` no longer matches any keyword from the old system. Under the new intent-based classification this will still trigger Mode 1 correctly — but the *expected response text* in the example should also be updated to match the new confirmation format more faithfully (e.g., show `"I understand you want to develop a new pasta recipe."`). Low priority but worth tidying.
