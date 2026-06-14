---
name: notebooklm-folio-explainer
description: >
  Generates ready-to-paste prompts for all four NotebookLM Studio outputs
  (Video Overview, Infographic, Slide Deck, and Briefing Doc) from any
  Café Athena Technique Folio. Use this skill whenever the user mentions
  NotebookLM, a folio number (e.g. "01-02"), "video explainer", "infographic
  prompt", "slide deck prompt", or asks to prepare a Technique Folio for any
  NotebookLM Studio tool. Technique Folios only — does not apply to recipe files.
---

# NotebookLM Folio Explainer

Generates four sets of copy-paste-ready prompts — one per NotebookLM Studio
tool — calibrated to the content of a specific Technique Folio and the
Café Athena brand voice.

---

## Step 1 — Locate the Folio

**If the user provides a folio number** (e.g. "01-02"):
- Resolve the path: `/Users/kevinward/Projects/Cafe Athena/The Manual/Chapter {N} - {Name}/`
- Use Bash (`ls` on the chapter directory) to find the exact filename. The filename must contain "Technique Folio" — if no matching file exists, or the resolved file is a recipe file (not a Technique Folio), stop and tell the user: "I couldn't find a Technique Folio for that number. Confirm the folio ID or upload the file."
- Use the Read tool to load the file once located.

**If the user uploads a file** *(Claude.ai web interface only — not available in Claude Code)*:
- Read it from `/mnt/user-data/uploads/`.

**If neither is available:**
- Ask: "Which folio? Give me the number (e.g. 01-02) or upload the file."

---

## Step 2 — Analyze the Folio

Before generating any prompts, extract these four things from the folio content:

1. **The core reframe** — the single sentence that flips the reader's assumption (e.g. "Salt is not a seasoning — it's a water management tool."). If the folio is operational or procedural (no scientific reframe), use its central organizing principle or primary teaching goal as the hook instead.
2. **The mechanisms** — the 2–4 named scientific or technique concepts the folio teaches
3. **The practical payoff** — the hands-on exercise, timing rule, or decision the reader walks away with
4. **Visual texture** — any physical details in the folio that would render well as images (textures, comparisons, before/after states)

Do not show this analysis to the user — use it internally to write the prompts.

---

## Step 2.5 — Confirm Folio Loaded

Output this single line to the user before generating the four blocks:

> **Loaded:** [exact filename] — [folio title]

---

## Step 3 — Generate All Four Prompt Sets

Output all four in sequence, clearly labeled. Each block should be ready to paste with no editing required.

---

### 1. VIDEO OVERVIEW

**Settings to tell the user:**
- Style: Custom (selected)

**Paste into "Describe a custom visual style":**
> Warm editorial kitchen aesthetic — rich earth tones, olive, amber, cream, dark wood. Close-up textures relevant to the folio subject. Natural light, unhurried pacing. Feels like a craftsman's notebook, not a cooking show.

**Paste into "What should the AI hosts focus on?":**
> [Core reframe as the hook]. Walk through [mechanisms] in sequence — explain what is physically happening, not just what to do. Cover [the practical payoff]. Keep tone curious and precise. No "amazing" or "game-changer" language.

---

### 2. INFOGRAPHIC

**Settings to tell the user:**
- Orientation: Landscape
- Visual Style: Editorial
- Level of Detail: Detailed

**Before writing the paste block**, count the mechanisms from Step 2 and resolve the layout:
- 1 mechanism → full-width single panel
- 2 mechanisms → two-column split
- 3 mechanisms → three-column
- 4 mechanisms → four-panel grid

Also determine: does the folio contain timing data or a direct before/after comparison? If yes, include a timing strip or comparison table in the copy below.

**Paste into "Describe the infographic you want to create":**
> Warm earth tones — olive, amber, cream, dark steel. [Resolved layout — e.g. "Three-column layout, one column per mechanism"]. Each section shows what is happening inside the food, not just a label. [If applicable: include a timing strip / comparison table.] End with [the practical payoff as a visual takeaway].

---

### 3. SLIDE DECK

**Settings to tell the user:**
- Format: Detailed Deck
- Length: Default

**Paste into "Describe the slide deck you want to create":**
> Warm editorial tone — olive, amber, cream. Open with the reframe: [core reframe]. One slide per mechanism with plain-language explanation of what is physically happening. Follow with [timing/decision rule if present]. Close with [practical exercise or takeaway]. No filler slides.

---

### 4. BRIEFING DOC

*(No customization UI — NotebookLM generates this automatically. Provide context for the user.)*

> The Briefing Doc will summarize the folio as written. No prompt needed — just generate. For best results, the folio's core explanation and practical application sections should be fully developed.

---

## Brand Voice Rules (apply to all outputs)

- Never use: "game-changer," "amazing," "revolutionary," "deep dive," "unpack"
- Tone: direct, craft-driven, technically precise, warm but not chatty
- Audience assumption: competent home cook who wants to understand the *why*
- The folio IS the source of truth — do not invent mechanisms or steps not present in the file

---

## Chapter Directory Map

| Chapter | Path fragment |
|---------|--------------|
| 1 | `Chapter 1 - The Lab` |
| 2 | `Chapter 2 - The Foundation` |
| 3 | `Chapter 3 - Garde Manger` |
| 4 | `Chapter 4 - The Mill` |
| 5 | `Chapter 5 - The Fishmonger` |
| 6 | `Chapter 6 - The Poulterer` |
| 7 | `Chapter 7 - The Butcher` |
| 8 | `Chapter 8 - The Field` |
| 9 | `Chapter 9 - The Pâtissier` |
| 10 | `Chapter 10 - Stocks, Sauces & Condiments` |
| 11 | `Chapter 11 - Spice Blends, Oils & Pastes` |
| 12 | `Chapter 12 - Les Fonds` |
