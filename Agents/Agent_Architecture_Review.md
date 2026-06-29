# Café Athena — Agent Architecture Review Brief

**Purpose of this document:** I'm asking you to evaluate my current agent architecture the way a senior agent architect at a company like Anthropic would — focused on separation of concerns, clear responsibility boundaries, documentation/context requirements, and reliable handoffs between agents. I have a specific reliability problem I need solved, but I also want a broader gut-check on whether the structure is sound as the project scales.

---

## 1. Project Overview

**Project:** Café Athena, the Manual (a cookbook/recipe manual + companion website)

**Working environment:**
- Primary repo work happens in VS Code using Claude CLI
- Chef agent work (recipe development) typically happens in Claude Desktop, so it's accessible on mobile
- GitHub Copilot Chat is used for select technical tasks handed off by the Technical Director agent
- Documentation is markdown-first across the project, except specific asset/website files
- Website is built in Astro

---

## 2. Repo Structure

```
/ (root)
├── README.md                  — master guide: what the project is, manual structure, website overview
├── CLAUDE.md                  — root-level Claude reference (not in .claude/)
├── .claude/
│   ├── agents/                 — agent definitions (CLI-usable)
│   ├── commands/                — 15 markdown command files (see §5)
│   ├── skills/                  — see §6
│   ├── settings.json            — smart link to global settings
│   └── settings.local.json      — local overrides
├── agents/
│   └── claude-desktop/          — Claude Desktop project instructions mirrored from .claude/agents
├── manual/
│   ├── [12 chapter folders]     — see §4
│   ├── glossary/
│   ├── recipes.json             — master recipe registry/log
│   ├── manual-status.md         — agent-facing status doc for the manual
│   ├── ideas.md                 — recipe idea intake
│   ├── content-plan.md          — minimum content targets per chapter
│   └── cafe-athena-manual-current-version.md  — live recipe/folio inventory, auto-updated on registration
├── brand/
│   ├── brand-guidelines.md
│   ├── brand-scope.md
│   └── brand-status.md          — agent-facing status doc for branding
├── marketing/
│   └── marketing-status.md      — agent-facing status doc for marketing
├── expo/                        — blog drafts/posts staging area (pre-publish)
├── site/                        — Astro website source
├── guidance/                    — Chef's templates, taxonomy, recipe format templates, technique-folio templates
├── docs/                        — technical reference: repo structure, stack overview, deploy commands, content pipeline, commands index
├── archive/                     — old/dev files, not tracked in GitHub
├── scripts/                     — automation scripts
└── project-status/              — root-level project status folder
```

**Project management:** A globally-installed project management skill provides slash commands. Various agents read the `*-status.md` files above as their "source of truth" check on invocation.

---

## 3. Agent Architecture

### 3.1 Three Primary Agents (each is also a Claude Desktop Project)

**Chef** (`agents/claude-desktop/` → "Project Instructions.md" is the root Claude Desktop project)
Three modes:
1. **Brainstorming/Ideation** — exploratory recipe/technique discussion
2. **Formalization** — takes a mode-1 recipe and writes it into the canonical Café Athena Manual recipe format, using template/example files from `guidance/`
3. **Advisor** — troubleshooting/revision on existing recipes ("this didn't work," "we need to fix this")

**Brand Manager**
Four modes:
1. Brand development
2. Marketing execution
3. Writing tasks (delegates to Café Athena Writing Director sub-agent)
4. Asset production (images, video, website creative)

**Technical Director**
Handles technical tasks; can hand off specific work to GitHub Copilot Chat.

All three Desktop Project instruction sets are built from / mirror the corresponding agent definitions in `.claude/agents/`.

### 3.2 Sub-Agents (live only in `.claude/agents/`, no Desktop Project equivalent)

- **Café Athena Writing Director** — callable by Brand Manager or root Chef agent
- **Markdown QA** — callable by Chef, root agent, or Technical Director; audits markdown formatting
- **Recipe Clarity Auditor** — ensures recipes are written in plain, clear language

### 3.3 Skills (`.claude/skills/`)
Astro, Audit Agent Instructions, Avoid AI Writing, Café Athena Site Dev, Fixing Metadata, NotebookLM Folio Explainer, Project Health, SEO, AEO Schema Generator, SEO Images.

---

## 4. The Manual — Content Structure

Three parts:

| Part | Name | Chapters | Focus |
|---|---|---|---|
| I | The Academy | 1–2 | Technique & theory |
| II | The Brigade | 3–9 | Core recipes |
| III | The Larder | 10–12 | Building blocks |

**Chapters:**
1. The Lab
2. The Foundation
3. Garde Manger
4. The Mill
5. The Fishmonger
6. The Poulterer
7. The Butcher
8. The Field
9. The Pâtissière
10. Stocks, Sauces, and Condiments
11. Spice Blends, Oils, and Pastes
12. Fonds

Plus a standalone Glossary.

**The Expo** is *not* part of the manual — it's the blog section, staged in `/expo` pre-publish, and lives on the website once published.

---

## 5. Workflow: Recipe Lifecycle

1. **Mode 1 (Chef):** Brainstorm a recipe idea.
2. **Mode 2 (Chef):** Formalize it using manual templates → written into the correct `manual/[chapter]/` folder.
3. **Registration (root/CLI agent):** Kevin provides chapter-recipe number (e.g., `01-01`). This triggers:
   - Markdown QA audit (format compliance)
   - Recipe Clarity Auditor pass (plain-language check)
   - Entry added to `manual/recipes.json`
   - Can be used to "reserve" a recipe number before the recipe itself is written
4. **Pipeline command (CLI):** Runs glossary pool, keyword pool, and the other registry/audit commands, then publishes to the Astro site (`/site`) and deploys.

### Commands (`.claude/commands/`, 15 total, all `.md`)
audit-glossary, clarity-audit, expo-keyword-pool, expo-tag-audit, format-audit, glossary-pool, keyword-pool, new-recipe, pipeline, recipe-update, register-expo, register-recipe, session-handoff, sync-expo-registry, sync-registry

---

## 6. The Problem

**Symptom:** The Brand Manager agent is inconsistent about reading its own source-of-truth documents (e.g., `marketing/marketing-status.md`).

- When used for **general brand conversation**, it performs well.
- When used for **specific execution tasks** — e.g., "let's build a marketing plan" — it *sometimes* reads `marketing-status.md` first, and sometimes doesn't, leading to plans built without current context.
- This isn't a one-off — it's a recurring pattern severe enough that Kevin has taken to ending sessions and starting fresh ones with more explicit instructions, which helps somewhat but doesn't fully resolve it.
- Suspicion: the Brand Manager may be **overloaded** — one agent juggling four distinct modes (brand development, marketing execution, writing-task delegation, asset production) may be diluting its consistency on mode-specific context-loading behavior.

---

## 7. What I'm Asking You To Do

Acting as a senior agent architect, please:

1. **Diagnose** why a single agent with multiple modes might inconsistently load mode-specific context documents, even when explicitly instructed.
2. **Evaluate** whether Marketing Execution (and possibly other modes) should be split out of the Brand Manager into their own dedicated agent(s) — with the same Desktop Project / `.claude/agents` mirroring pattern used elsewhere in this project.
3. If a split is recommended, specify:
   - What the new agent's instructions/context-loading rules should look like (e.g., a hard requirement to read `marketing-status.md` before any execution task)
   - How it should hand off to/from the Brand Manager and other agents (Chef, Technical Director, Writing Director sub-agent)
   - What guardrails or structural patterns (similar to how Markdown QA / Recipe Clarity Auditor are scoped) would keep it from drifting the same way
4. **Flag** any other structural risks you notice in the broader architecture described above (e.g., agents with too many modes, missing source-of-truth enforcement, unclear sub-agent invocation rules) — even ones I haven't explicitly asked about.
5. Recommend concrete next steps I can execute directly in this VS Code / Claude CLI environment.

I'd rather get a thorough, best-practices-grounded recommendation than a quick patch — this project will keep growing and I want the agent structure to scale with it.