# Café Athena — Claude Code Instructions

## Working Style

- Default to action. Explain only when the task is complex or you need clarification.
- Use the minimum tokens necessary to complete the task.

---

## Status Query Protocol

When the user asks for a status update, what's next, where we are, what's pending, or anything semantically equivalent, read these four sources **before answering** — never respond from memory alone:

1. `PROJECT_STATUS.md` — active work, bugs, pending items
2. `IDEAS.md` — future/deferred backlog
3. `recipes.json` — live per-recipe state (run `python3 scripts/audit.py --status` for the rollup)
4. `CLAUDE.md` — this file, for architectural context

Produce a rollup in this order: **active work first, then open issues, then backlog highlights.** Do not dump the full `IDEAS.md` — surface only what's relevant to the current session's direction.

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

You enter through technique, cook through the brigade, build from the larder, and culminate in service. Part IV is not yet started — see `IDEAS.md`.

---

## How the AI Surfaces Are Divided

| Surface | Responsibilities |
|---------|-----------------|
| **Claude Desktop** | Recipe development (Mode 1), formatting (Mode 2), technique education (Mode 3) — all culinary creative work |
| **Claude Code** (you) | Format audits, glossary operations, web/site development, QA, deploys, image optimization |
| **Gemini Gem 1** | Alternative surface for recipe development; generates hero image briefs |
| **Gemini Gem 2** | Hero image and web image generation only |

---

## Key Files

| File | Role |
|------|------|
| `PROJECT_STATUS.md` | Session state — active recipes, strategic context, pending tasks. Check this at the start of each session. **Does not duplicate registry state** — hero image + format audit status live in `recipes.json`. |
| `recipes.json` | Pipeline registry — single source of truth for per-recipe state. Each entry has `stages` (formatAudit, glossaryPull, heroImage, heroImageOptimized, deployed, etc.) and an `audit` block (`lastRun`, `status`, `issues[]`). Updated via `/register-recipe`, `/sync-registry`, and `scripts/audit.py`. Run `python3 scripts/audit.py --status` for a rollup. |
| `IDEAS.md` | Future recipe, folio, technique, and editorial ideas — low-priority backlog. Not active work; drop new ideas here. |
| `Guidance/Recipe-Format-Standard.md` | Single source of truth for all recipe formatting rules |
| `AGENT_CHANGELOG.md` | Version history for all four agent surfaces |
| `MULTI_AGENT_ARCHITECTURE.md` | Full architecture reference and improvement roadmap |
| `.claude/agents/Cafe Athena Chef.agent.md` | **Canonical master** for the culinary agent system prompt |
| `.agents/workflows/` | Slash-command workflow definitions |
| `scripts/audit.py` | Local Ollama-powered audit & repair tool — scans all recipes for structural issues, generates glossary/keyword fixes, applies with user approval |
| `The Manual/Glossary/` | Split culinary glossary — one file per letter (`Café Athena  - Glossary [LETTER].md`, A–Z + 0-9) |
| `The Manual/` | Full cookbook manuscript (source files) |
| `site/src/content/recipes/` | Built recipe files consumed by the Astro site |

---

## ⚠️ Version Bump Rule

**Whenever any agent file is modified, you must:**

1. Bump the version number in the file header (e.g. `Version: 1.1` → `Version: 1.2`)
2. Add an entry to `AGENT_CHANGELOG.md` describing what changed and why
3. Follow the propagation rule below for any changes that affect secondary surfaces

This applies to: `.claude/agents/Cafe Athena Chef.agent.md`, `Claude-Desktop/PROJECT_INSTRUCTIONS.md`, `Guidance/CAFÉ ATHENA - GEM INSTRUCTIONS.md`, `Guidance/CAFÉ ATHENA - HERO IMAGE GEM INSTRUCTIONS.md`, and any `.agents/workflows/*.md` file.

---

## ⚠️ Agent Propagation Rule

**When any of the following files are modified, stop and remind the user to manually update the corresponding external surfaces before committing.**

| File Changed | Manual Update Required |
|-------------|----------------------|
| `.claude/agents/Cafe Athena Chef.agent.md` | Copy changes to `Guidance/CAFÉ ATHENA - GEM INSTRUCTIONS.md` (Gemini Gem 1) and `Claude-Desktop/PROJECT_INSTRUCTIONS.md` (Claude Desktop) |
| `Guidance/Recipe-Format-Standard.md` | Re-attach the updated file in Claude Desktop (it is a file attachment, not pasted text); verify Gemini Gem 1 instructions still reference it correctly |
| `.agents/workflows/*.md` | No external update needed — workflows run in Claude Code only |
| `Guidance/CAFÉ ATHENA - HERO IMAGE GEM INSTRUCTIONS.md` | Paste updated content into the Gemini Gem 2 configuration |
| `Claude-Desktop/PROJECT_INSTRUCTIONS.md` | Paste updated content into the Claude Desktop project instructions |

After propagating changes, bump the version number in the modified file and add an entry to `AGENT_CHANGELOG.md`.

---

## Slash Commands

Run these in Claude Code. Full definitions in `.agents/workflows/`.

| Command | Purpose |
|---------|---------|
| `/format-audit [id\|Chapter N]` | Audit recipe(s) against format standard |
| `/glossary-pull [id]` | Merge recipe glossary terms into main glossary |
| `/keyword-pull [id]` | Add missing Keywords + Category sections |
| `/audit-glossary` | Fix alphabetization + duplicates in main glossary |
| `/recipe-hero-image [id]` | Build Gemini image prompt for a recipe |
| `/recipe-hero-image optimize [id\|chapter-N\|all]` | Convert PNG hero images to WebP |
| `/recipe-hero-image insert [id] "[position]" "[caption]"` | Insert image shortcode into a folio |
| `/new-recipe` | Scaffold a new recipe through the full pipeline |
| `/register-recipe [id]` | Register a new entry in `recipes.json` after Claude Desktop Mode 2 |
| `/sync-registry` | Sync `recipes.json` against live Manual directory — adds missing entries, corrects filesystem-derivable stages |
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

- Recipe source files: `The Manual/Chapter N - Name/XX-YY.md`
- Built recipe files: `site/src/content/recipes/XX-YY.md`
- Hero images (source): `The Manual/Chapter N - Name/XX-YY.png` (or `.webp`)
- Hero images (site): `site/public/images/XX-YY.webp`
- Build pipeline: `site/scripts/prepare-content.py` processes Manual → site content. Safe to run during deploy — preserves already-optimized WebP images in `site/public/images/` matching `\d{2}-\d{2}[a-z]?\.webp` (fixed 2026-04-05, commit c84bc51).

### Deploy Workflow

The live site is hosted on FastComet. **Pushing to GitHub alone does NOT deploy the site** — only the rsync in `deploy.sh` updates the live site. Never report the site as deployed until rsync completes successfully.

1. Place optimized WebP files in `site/public/images/`
2. Update `recipes.json` (heroImage, heroImageOptimized, deployed flags)
3. Commit and push to GitHub
4. Run `bash site/scripts/deploy.sh` from the repo root — handles content prep, build, and rsync

If images go missing after a deploy, check git history — they were likely committed and can be restored with `git checkout HEAD -- site/public/images/XX-YY.webp`.

### ⚠️ heroImage Frontmatter Format (CRITICAL)

The `heroImage` field in `site/src/content/recipes/XX-YY.md` must be the **filename only** — e.g. `"07-10.webp"`. **Never** use a path like `"/images/07-10.webp"`.

The template (`[...slug].astro:30`) automatically prepends `/images/` when rendering. Using a full path results in a broken double-path like `/images//images/07-10.webp`.

When manually adding heroImage frontmatter (not via prepare-content.py), always use: `heroImage: "XX-YY.webp"`

### Two Image Workflows

1. **Via The Manual:** Place `.png` in `The Manual/Chapter N/` → `prepare-content.py` copies it to `site/public/images/` and sets the frontmatter automatically.
2. **Direct placement:** Place optimized `.webp` directly in `site/public/images/` → manually set `heroImage: "XX-YY.webp"` in `site/src/content/recipes/XX-YY.md` (filename only, no path prefix).

---

## Image Lifecycle & Cleanup Policy

Images in `The Manual/` are working files. Once processed and confirmed in `site/public/images/`, they should be deleted from The Manual folder.

**Delete from `The Manual/` when:**

- Hero image: `recipes.json` shows `heroImageOptimized: true`
- Reference image: `recipes.json` shows `referenceImagesProcessed: true`

This applies equally to hero images (`XX-YY.webp`) and reference images (`XX-YYa.webp`, etc.).

**Canonical location for all processed images:** `site/public/images/`

The `.png` originals in The Manual may be kept until optimized, then deleted once `heroImageOptimized: true`. Reference the `recipes.json` registry as the source of truth for what has been processed.

---

## Operational Heuristics

Session-relevant learnings that shape how work should be done in this project.

- **Filesystem Authority**: Always scan live directories for folio numbers — never infer from stale docs.
- **Scaling Nuance**: Ingredients scale linearly; reduction times do NOT (surface area constraints).
- **Formula Trust**: Use established adaptive hydration rates for pasta.
- **Tool Awareness**: Antigravity is used for local project orchestration. If unsure of its capabilities, ask.
- **Frico Method (2026-04-21)**: Baked frico is structurally superior to stovetop-pan frico — even browning, longer plastic-shaping window (~30–45 sec on counter vs. 5–10 sec off the pan), hands-free batching. Silpat beats parchment for structural/molded fricos (clean release protects lace; mat retains counter heat long enough to shape). Parchment only wins on pure flat tiles where bottom crispness matters more than shape-hold.
