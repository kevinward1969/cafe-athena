# Café Athena — Claude Code Instructions

## What This Project Is

A culinary cookbook project with a published Astro site at `cookbook.kevinward.com`. The cookbook manuscript lives in `The Manual/`. The site is in `site/`. Recipes and technique folios are written in Markdown and processed through a build pipeline before deployment.

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
| `PROJECT_STATUS.md` | Session state — active recipes, pending tasks. Check this at the start of each session. |
| `recipes.json` | Pipeline registry — tracks stage completion per recipe. Each entry has `stages` (formatAudit, glossaryPull, heroImage, etc.) and an `audit` block (`lastRun`, `status`, `issues[]`). Updated via `/register-recipe`, `/sync-registry`, and `scripts/audit.py`. |
| `Guidance/Recipe-Format-Standard.md` | Single source of truth for all recipe formatting rules |
| `AGENT_CHANGELOG.md` | Version history for all four agent surfaces |
| `MULTI_AGENT_ARCHITECTURE.md` | Full architecture reference and improvement roadmap |
| `.claude/agents/Cafe Athena Chef.agent.md` | **Canonical master** for the culinary agent system prompt |
| `.agents/workflows/` | Slash-command workflow definitions |
| `scripts/audit.py` | Local Ollama-powered audit & repair tool — scans all recipes for structural issues, generates glossary/keyword fixes, applies with user approval |
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
- Build pipeline: `site/scripts/prepare-content.py` processes Manual → site content
- Deploy: `site/scripts/deploy.sh` (from project root) — but **do not run prepare-content.py** during deploy if images have been placed directly in `site/public/images/`, as it can wipe them.

### ⚠️ heroImage Frontmatter Format (CRITICAL)

The `heroImage` field in `site/src/content/recipes/XX-YY.md` must be the **filename only** — e.g. `"07-10.webp"`. **Never** use a path like `"/images/07-10.webp"`.

The template (`[...slug].astro:30`) automatically prepends `/images/` when rendering. Using a full path results in a broken double-path like `/images//images/07-10.webp`.

When manually adding heroImage frontmatter (not via prepare-content.py), always use: `heroImage: "XX-YY.webp"`

### Two Image Workflows

1. **Via The Manual:** Place `.png` in `The Manual/Chapter N/` → `prepare-content.py` copies it to `site/public/images/` and sets the frontmatter automatically.
2. **Direct placement:** Place optimized `.webp` directly in `site/public/images/` → manually set `heroImage: "XX-YY.webp"` in `site/src/content/recipes/XX-YY.md` (filename only, no path prefix).

### Known Issues

- **07-10.2 recipe not appearing on site:** The `extract_index` regex in `prepare-content.py` (line 111) only matches `XX-YY` with optional lowercase letter suffixes (`[a-z]*`). The `.2` version suffix in `07-10.2` is not supported. This recipe needs a manual site content file or a regex fix to support numeric sub-versions.

---

## Image Lifecycle & Cleanup Policy

Images in `The Manual/` are working files. Once processed and confirmed in `site/public/images/`, they should be deleted from The Manual folder.

**Delete from `The Manual/` when:**

- Hero image: `recipes.json` shows `heroImageOptimized: true`
- Reference image: `recipes.json` shows `referenceImagesProcessed: true`

This applies equally to hero images (`XX-YY.webp`) and reference images (`XX-YYa.webp`, etc.).

**Canonical location for all processed images:** `site/public/images/`

The `.png` originals in The Manual may be kept until optimized, then deleted once `heroImageOptimized: true`. Reference the `recipes.json` registry as the source of truth for what has been processed.
