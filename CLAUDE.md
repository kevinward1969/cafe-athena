# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Working Style

- Default to action. Explain only when the task is complex or you need clarification.
- Use the minimum tokens necessary to complete the task.

---

## Commands

All `npm` commands run from `site/` — there is no root-level `package.json`.

```bash
# Site development
cd site && npm run dev           # local dev server (Astro, hot reload)
cd site && npm run build         # production build + Pagefind search index
cd site && npm run preview       # preview the production build locally

# Content pipeline (run from repo root)
python3 site/scripts/prepare-content.py   # Manual → site/src/content/recipes/ (no build)
bash site/scripts/deploy.sh               # full pipeline: prep + build + rsync to FastComet
```

`npm run build` runs `astro build` followed by `npx pagefind` — both must succeed for site search to work. Do not run `astro build` directly when building for deployment.

---

## Status Query Protocol

When the user asks for a status update, what's next, where we are, what's pending, or anything semantically equivalent, read these four sources **before answering** — never respond from memory alone:

1. `PROJECT_STATUS.md` — active work, bugs, pending items
2. `The Manual/IDEAS.md` — future/deferred backlog
3. `The Manual/recipes.json` — live per-recipe state (run `python3 scripts/audit.py --status` for the rollup)
4. `CLAUDE.md` — this file, for architectural context

Produce a rollup in this order: **active work first, then open issues, then backlog highlights.** Do not dump the full `The Manual/IDEAS.md` — surface only what's relevant to the current session's direction.

---

## What This Project Is

A culinary cookbook project with a published Astro site at `cookbook.kevinward.com`. The cookbook manuscript lives in `The Manual/`. The site is in `site/`. Recipes and technique folios are written in Markdown and processed through a build pipeline before deployment.

### Manuscript Architecture — Four-Part Arc

| Part | Chapters | Theme |
| :--- | :--- | :--- |
| **Part I: The Academy** | Ch. 1–2 (The Lab, The Foundation) | Technique |
| **Part II: The Brigade** | Ch. 3–9 (Garde Manger → The Pâtissier) | Cooking through the stations |
| **Part III: The Larder** | Ch. 10–12 (Stocks & Sauces, Spice Blends, Les Fonds) | Building blocks |
| **Part IV: The Expo** | Ch. 13–15 (Planning, Plating, Service) | Capstone — how it reaches the guest |

You enter through technique, cook through the brigade, build from the larder, and culminate in service. Part IV is not yet started — see `The Manual/IDEAS.md`.

---

## How the AI Surfaces Are Divided

| Surface | Responsibilities |
|---------|-----------------|
| **Claude Desktop** | Recipe development (Mode 1), formatting (Mode 2), technique education (Mode 3) — all culinary creative work |
| **Claude Code** (you) | Format audits, glossary operations, web/site development, QA, deploys, image optimization |
| **Gemini Gem 1** | Fallback surface for recipe development (maintained, not primary) |
| **Gemini Gem 2** | Hero image and web image generation only |

---

## Key Files

| File | Role |
|------|------|
| `PROJECT_STATUS.md` | Session state — active recipes, strategic context, pending tasks. Check this at the start of each session. **Does not duplicate registry state** — hero image + format audit status live in `The Manual/recipes.json`. |
| `The Manual/CONTENT_PLAN.md` | Chapter-by-chapter content gap analysis — minimum recipe counts, category coverage gaps, RecipeIdeas assignments, and development sequence. Reference when planning new recipe development. |
| `The Manual/recipes.json` | Pipeline registry — single source of truth for per-recipe state. Each entry has `stages` (formatAudit, glossaryPull, heroImage, heroImageOptimized, deployed, etc.) and an `audit` block (`lastRun`, `status`, `issues[]`). Updated via `/register-recipe`, `/sync-registry`, and `scripts/audit.py`. Run `python3 scripts/audit.py --status` for a rollup. |
| `The Manual/IDEAS.md` | Future recipe, folio, technique, and editorial ideas — low-priority backlog. Not active work; drop new ideas here. |
| `Guidance/Recipe-Format-Standard.md` | Single source of truth for all recipe formatting rules |
| `Guidance/Taxonomy.md` | Canonical controlled vocabulary — all valid `cuisine:`, `style:`, `family:`, `course:`, and `dietary:` values. Referenced by agents, pipelines, and `audit.py`. Add new terms here first. |
| `Agents/AGENT_CHANGELOG.md` | Version history for all agent surfaces |
| `Agents/MULTI_AGENT_ARCHITECTURE.md` | Full architecture reference and improvement roadmap |
| `.claude/agents/Cafe Athena Chef.agent.md` | **Canonical master** for the culinary agent system prompt |
| `.claude/commands/` | Slash-command workflow definitions |
| `scripts/audit.py` | Local Ollama-powered audit & repair tool — scans all recipes for structural issues, generates glossary/keyword fixes, applies with user approval |
| `The Manual/Cafe-Athena-The-Manual-Current-Version.md` | **Master manuscript index** — the human-facing table of contents for every folio in the book. Must be updated every time a new recipe or technique folio is added. Updated by `/register-recipe` (automatic) or manually when bypassing that workflow. |
| `The Manual/Glossary/` | Split culinary glossary — one file per letter (`Café Athena  - Glossary [LETTER].md`, A–Z + 0-9) |
| `The Manual/` | Full cookbook manuscript (source files) |
| `site/src/content/recipes/` | Built recipe files consumed by the Astro site |

---

## ⚠️ Version Bump Rule

**Whenever any agent file is modified, you must:**

1. Bump the version number in the file header (e.g. `Version: 1.1` → `Version: 1.2`)
2. Add an entry to `Agents/AGENT_CHANGELOG.md` describing what changed and why
3. Follow the propagation rule below for any changes that affect secondary surfaces

This applies to: `.claude/agents/Cafe Athena Chef.agent.md`, `Agents/Claude-Desktop/PROJECT_INSTRUCTIONS.md`, `Agents/Gemini-Gems/CAFÉ ATHENA - VISUAL DIRECTOR GEM INSTRUCTIONS.md`, and any `.claude/commands/*.md` file.

---

## ⚠️ Agent Propagation Rule

**When the canonical master is modified, apply changes to secondary surfaces as follows. File edits are done directly — only UI pastes require manual action by Kevin.**

| File Changed | Action Required |
|-------------|----------------------|
| `.claude/agents/Cafe Athena Chef.agent.md` | **Edit directly:** port changes to `Agents/Claude-Desktop/PROJECT_INSTRUCTIONS.md`. **Remind Kevin:** paste updated `PROJECT_INSTRUCTIONS.md` content into Claude Desktop project settings, and port relevant changes to `Agents/Gemini-Gems/CAFÉ ATHENA - GEM INSTRUCTIONS.md` then paste into Gemini Gem 1 config. |
| `Guidance/Recipe-Format-Standard.md` | No action needed — Claude Desktop reads this file live from the filesystem via MCP |
| `.claude/commands/*.md` | No action needed — workflows run in Claude Code only |
| `Agents/Gemini-Gems/CAFÉ ATHENA - VISUAL DIRECTOR GEM INSTRUCTIONS.md` | **Remind Kevin:** paste updated content into the Gemini Gem 2 configuration |
| `Agents/Claude-Desktop/PROJECT_INSTRUCTIONS.md` | **Remind Kevin:** paste updated content into the Claude Desktop project settings |

After propagating changes, bump the version number in the modified file and add an entry to `Agents/AGENT_CHANGELOG.md`.

---

## ⚠️ New Recipe Mandatory Updates

Every time a new recipe or technique folio is added, **all four of these must be updated before committing**:

1. **The folio file** — `The Manual/Chapter N - Name/XX-YY Café Athena - [Recipe Title].md`
2. **`The Manual/recipes.json`** — register the entry with correct stage flags
3. **`The Manual/Cafe-Athena-The-Manual-Current-Version.md`** — append the entry under the correct chapter heading
4. **`PROJECT_STATUS.md`** — update the Last Updated date

`/register-recipe` handles items 2 and 3 automatically. Items 1 and 4 are always manual.

---

## Slash Commands

Run these in Claude Code. Full definitions in `.claude/commands/`.

| Command | Purpose |
|---------|---------|
| `/format-audit [id\|Chapter N]` | Audit recipe(s) against format standard |
| `/glossary-pull [id]` | Merge recipe glossary terms into main glossary |
| `/keyword-pull [id]` | Add missing Keywords + Category sections |
| `/audit-glossary` | Fix alphabetization + duplicates in main glossary |
| `/new-recipe` | Scaffold a new recipe through the full pipeline |
| `/register-recipe [id]` | Register a new entry in `The Manual/recipes.json` **and** update the Current Version index after Claude Desktop Mode 2 |
| `/sync-registry` | Sync `The Manual/recipes.json` against live Manual directory — adds missing entries, corrects filesystem-derivable stages |
| `/session-handoff` | Update PROJECT_STATUS.md, commit, push, output summary |

---

## Local Python Scripts (Ollama)

These scripts run against a local [Ollama](https://ollama.com) server (`localhost:11434`) — no API tokens used.

**Installed models:** `llama3.2:latest` (generation, 2 GB), `qwen2.5:7b` (detection, 4.7 GB), `gemma3:4b` (3.3 GB)

| Script | Purpose | Use when |
|--------|---------|----------|
| `scripts/audit.py` | Bulk audit + Ollama-powered repair | Run first to detect structural issues and generate glossary/keyword content |
| `scripts/extract-keywords.py` | Keywords/Category backfill | Superseded by `audit.py` — use `audit.py --scan-only` + approve instead |
| `scripts/add-glossary-sections.py` | Glossary section generation | Superseded by `audit.py` |

**Common commands:**

```bash
python3 scripts/audit.py --scan-only              # scan all, no changes
python3 scripts/audit.py --status                 # show audit status summary
python3 scripts/audit.py --chapter 3              # audit + fix Chapter 3
python3 scripts/audit.py --deep                   # add LLM-based Mise/Method violation check (qwen2.5:7b)
python3 scripts/audit.py --model llama3.2:latest  # generation model (glossary, keywords, category)
python3 scripts/audit.py --detect-model qwen2.5:7b  # detection model (mise violation)
```

See `README.md` for full documentation and the Ollama approval workflow.

---

## Site & Build Notes

- Recipe source files: `The Manual/Chapter N - Name/XX-YY Café Athena - [Recipe Title].md`
- Built recipe files: `site/src/content/recipes/XX-YY.md`
- Hero images: `site/public/images/XX-YY.webp` — canonical location, pre-processed externally before placement
- Build pipeline: `site/scripts/prepare-content.py` processes Manual → site content. Safe to run during deploy — preserves already-optimized WebP images in `site/public/images/` matching `\d{2}-\d{2}[a-z]?\.webp` (fixed 2026-04-05, commit c84bc51).

### Content Pipeline Transform

`prepare-content.py` is the bridge between `The Manual/` and the Astro site. Understanding what it does is critical when editing either side:

1. **Strips the leading H1** — every folio file starts with `# Café Athena - Title` or `# **Technique Folio - Title**`. The script removes this line because `RecipeLayout.astro` renders the title from frontmatter; leaving it in the body causes a double title.
2. **Extracts `## Keywords` and `## Category` from the body** — these sections exist in the folio source but do not appear on the page. The script pulls them out and maps them into YAML frontmatter fields (`keywords[]`, `cuisine`, `style`, `family`, `course`, `dietary`), then strips the sections from the rendered body.
3. **Injects frontmatter** — every built file gets: `title`, `index`, `chapter`, `chapterName`, `type` (`recipe` or `technique`), `heroImage`, `referenceImages[]`, `keywords[]`, `cuisine`, `style`, `family`, `course`, `dietary`. The schema is defined in `site/src/content.config.ts`.
4. **Copies images** — hero images (`XX-YY.webp/.png`) and reference images (`XX-YYa.webp`, etc.) are copied from chapter folders to `site/public/images/`. Already-optimized WebP files already present in `site/public/images/` are preserved (not overwritten).

The Astro content collection at `site/src/content/recipes/` is **ephemeral** — it is fully regenerated each time `prepare-content.py` runs. Never hand-edit those files; edit the source in `The Manual/` instead, then re-run the pipeline.

### Site Page Routing

All recipe pages are served by a single dynamic route: `site/src/pages/[...slug].astro`. Each recipe's URL is its index (`/12-23`, `/01-01`, etc.).

The three section landing pages are static Astro files that act as chapter-group entry points:

| Page | URL | Covers |
|------|-----|--------|
| `academy.astro` | `/academy` | Ch. 1–2 (technique folios) |
| `brigade.astro` | `/brigade` | Ch. 3–9 (station recipes) |
| `larder.astro` | `/larder` | Ch. 10–12 (building blocks) |

A custom remark plugin (`site/src/plugins/remark-ref-images.mjs`) handles reference image embedding in recipe body content.

### Deploy Workflow

The live site is hosted on FastComet. **Pushing to GitHub alone does NOT deploy the site** — only the rsync in `deploy.sh` updates the live site. Never report the site as deployed until rsync completes successfully.

1. Place optimized WebP files in `site/public/images/`
2. Update `The Manual/recipes.json` (heroImage, heroImageOptimized, deployed flags)
3. Commit and push to GitHub
4. Run `bash site/scripts/deploy.sh` from the repo root — handles content prep, build, and rsync

If images go missing after a deploy, check git history — they were likely committed and can be restored with `git checkout HEAD -- site/public/images/XX-YY.webp`.

### ⚠️ heroImage Frontmatter Format (CRITICAL)

The `heroImage` field in `site/src/content/recipes/XX-YY.md` must be the **filename only** — e.g. `"07-10.webp"`. **Never** use a path like `"/images/07-10.webp"`.

The template (`[...slug].astro:30`) automatically prepends `/images/` when rendering. Using a full path results in a broken double-path like `/images//images/07-10.webp`.

When manually adding heroImage frontmatter (not via prepare-content.py), always use: `heroImage: "XX-YY.webp"`

### Image Placement

All hero and reference images live in `site/public/images/` — this is the only location. Images are processed externally (Photoshop: remove Gemini watermark, export WebP at 80% quality, 1920×1080) before being placed here. The pipeline validates presence and spec at deploy time via `sips`. Never place images in `The Manual/` chapter folders.

### Hero Image Prompt Format

When generating a prompt for Gemini Gem 2, always use this structured brief — not a prose paragraph:

```
Recipe: [dish name]
Chapter: [chapter name]
Description: [headnote — key visual elements, texture, color, sauce, garnish]
Cuisine: [cuisine type]
Key elements: [3–5 primary visual ingredients or techniques]
```

The Gem's aesthetic rules (`Agents/Gemini-Gems/CAFÉ ATHENA - VISUAL DIRECTOR GEM INSTRUCTIONS.md`) handle all style direction automatically — do not repeat surface, lighting, or composition instructions in the brief.

---

## Image Lifecycle & Cleanup Policy

Images in `The Manual/` are working files. Once processed and confirmed in `site/public/images/`, they should be deleted from The Manual folder.

**Delete from `The Manual/` when:**

- Hero image: `The Manual/recipes.json` shows `heroImageOptimized: true`
- Reference image: `The Manual/recipes.json` shows `referenceImagesProcessed: true`

This applies equally to hero images (`XX-YY.webp`) and reference images (`XX-YYa.webp`, etc.).

**Canonical location for all processed images:** `site/public/images/`

The `.png` originals in The Manual may be kept until optimized, then deleted once `heroImageOptimized: true`. Reference the `The Manual/recipes.json` registry as the source of truth for what has been processed.

---

## Git Workflow

- **Commit directly to main.** No feature branches, no PRs. All changes — format audits, content updates, site changes — go directly to main with a single commit and push.
- **Always one commit.** Bundle everything in the working tree into a single commit. Never split, never propose options, never ask. Exception: if the user says "commit only X," stage exactly those files.

---

## Operational Heuristics

Session-relevant learnings that shape how work should be done in this project.

- **Filesystem Authority**: Always scan live directories for folio numbers — never infer from stale docs.
- **Scaling Nuance**: Ingredients scale linearly; reduction times do NOT (surface area constraints).
- **Formula Trust**: Use established adaptive hydration rates for pasta.
- **Tool Awareness**: Antigravity is used for local project orchestration. If unsure of its capabilities, ask.
- **Frico Method (2026-04-21)**: Baked frico is structurally superior to stovetop-pan frico — even browning, longer plastic-shaping window (~30–45 sec on counter vs. 5–10 sec off the pan), hands-free batching. Silpat beats parchment for structural/molded fricos (clean release protects lace; mat retains counter heat long enough to shape). Parchment only wins on pure flat tiles where bottom crispness matters more than shape-hold.
- **Built recipe files**: `site/src/content/recipes/` is ephemeral — fully regenerated by `prepare-content.py`. If those files show as bulk-modified in git, it means the script ran and overwrote them — that is a regression, not an improvement. Investigate the diff before staging; discard if lines are only being removed.

---

## Project Skills — Auto-Trigger Rules

Five skills are installed in `.claude/skills/`. Invoke them automatically when their trigger conditions are met — do not wait to be asked.

| Skill | Invoke when… |
|-------|-------------|
| `astro` | Working on any file in `site/` — `.astro` pages, `content.config.ts`, `prepare-content.py`, build errors, content collection schema changes, or routing questions |
| `avoid-ai-writing` | Reviewing or editing any prose in `The Manual/` — headnotes, technique descriptions, glossary entries, or any free-text web copy — before it is committed |
| `seo-aeo-schema-generator` | Adding a new recipe to the site, or when asked about schema, structured data, JSON-LD, or rich results |
| `fixing-metadata` | Editing `[...slug].astro`, layout files, `<head>` content, OG tags, or any site-wide metadata |
| `seo-images` | Processing or placing hero images, running the deploy pipeline, or auditing `site/public/images/` for missing/oversized files |
