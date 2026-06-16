# The Expo — Project Tracker

**Status:** Active (started 2026-06-16)
**Plan origin:** Technical Director architecture session, 2026-06-16
**Last Updated:** 2026-06-16

> **Scope note:** this is the *single* working document for all Expo work — architecture, decisions, open questions, and the build checklist all live here, not split across `IDEAS.md`/`PROJECT_STATUS.md`. `PROJECT_STATUS.md` holds only a one-line pointer while this is active. On completion, the durable process knowledge (commands, agents, skills) graduates to `Guidance/Cafe-Athena-Workflow-Guide.md` as a new workflow, and this file is retired — see **Lifecycle** below.

---

## Folder Structure

The Expo is editorial/blog content, not manuscript content — it does not live under `The Manual/`.

```
Expo/                      ← this project, top-level, sibling to Brand/ and Marketing/
├── EXPO_TODO.md            ← this file
├── Posts/                  ← finalized source markdown, flat, pipeline-ready
├── Drafts/                 ← research notes, half-written essays, not yet pipeline-ready
└── expo.json                ← registry (Phase 4) — NOT under The Manual/recipes.json
```

**Why not mirror all of The Manual's machinery (chapters, full taxonomy, format-audit):** that tooling exists because recipe *bodies* have dozens of repeated structural sections (Mise, Method, Yield...) across 175+ entries, and consistency at that scale needs automated enforcement. Expo post bodies don't have that — they're freeform narrative/instructional prose, nothing to format-audit against.

**Correction (2026-06-16):** categories and tags/keywords are *not* an exception to this — they are exactly the kind of repeated structure recipes already have (their `## Keywords` / `## Category` sections), and Expo needs an equivalent generation mechanism, not ad hoc manual tagging. See **Categories & Tags** below — the tag mechanism reuses the recipe keyword-pull approach directly.

---

## Lifecycle Convention (applies here, proposed project-wide)

Per Kevin's clarification (2026-06-16):

1. **`IDEAS.md`** — ideas not yet realized, or not yet completely acted on. Nothing active belongs here.
2. **`PROJECT_STATUS.md`** — work in progress, *or* existing/already-built systems with a functional status worth tracking. Not purely "pending."
3. **Working detail, while active** — consolidates into one tracker file per initiative (this file, for Expo) — not fragmented across `IDEAS.md`/`PROJECT_STATUS.md`/elsewhere. `PROJECT_STATUS.md` carries only a one-line pointer to it.
4. **On completion** — the durable "how it works" knowledge (commands, agents, skills, pipeline mechanics) gets written up as a new workflow section in `Guidance/Cafe-Athena-Workflow-Guide.md`, PHASE-style, matching Workflows A–D. The detailed tracker file is retired; `PROJECT_STATUS.md` keeps whatever ongoing functional-status line still applies (per #2) rather than dropping the system from view entirely.

Short version added to `CLAUDE.md` so it applies beyond Expo, not just here.

---

## Locked Architecture Decisions

- **Naming:** the content type is "Expo" throughout, not generic "posts" — collection name, folder names, registry, and scripts all use `expo`.
- **Content collection:** new `expo` collection in `site/src/content.config.ts`, separate from `recipes`. Recipes are untouched — they keep their existing chapter/section/taxonomy architecture; no categories needed there.
- **Site source folder:** `site/src/content/expo/` for built blog content. `site/src/content/recipes/` stays exactly as is.
- **Manuscript-side source folder:** `Expo/Posts/` (flat) — see Folder Structure above. The Astro glob loader pattern (`**/*.md`) is already recursive, so a future split into year/month subfolders (if weekly+ cadence makes flat unwieldy) requires zero pipeline changes — accommodated for free, not a separate build task.
- **URL structure:** flat `/expo/[slug]` — confirmed, no date-based permalinks (`/2026/06/slug`). Date-based permalinks are discouraged in current SEO practice (longer URLs, no ranking benefit, visually signals "old"). Routes: `site/src/pages/expo.astro` (landing) + `site/src/pages/expo/[...slug].astro` (post pages).
- **Pipeline:** sibling script `site/scripts/prepare-expo.py` reading from `Expo/Posts/` (not a `prepare-content.py` extension — different clean/copy logic, different image-naming pattern). Called from `deploy.sh` after the recipe prep step.
- **Registry:** `Expo/expo.json` — own lightweight schema (id/slug, title, date, stages: written/heroImage/deployed). Separate from `The Manual/recipes.json` to avoid touching the working recipe pipeline scripts (`audit.py`, `/format-audit`, `/sync-registry` all assume recipe-shaped entries).
- **Commands (proposed naming, confirm when built):** `/register-expo` and `/sync-expo-registry`, mirroring `/register-recipe` and `/sync-registry`.
- **Cross-linking:** `relatedRecipes[]` authored once on the Expo post. Recipe → post direction is a reverse lookup computed in `[...slug].astro`'s `getStaticPaths` (not a second hand-maintained field).
- **Search/SEO:** Pagefind needs no new config — matching `data-pagefind-*` attributes on the Expo body, plus a `sectionLabel()` case for `/expo/` URLs in `BaseLayout.astro`'s search JS. Expo pages use `Article`/`BreadcrumbList` JSON-LD (not `Recipe`).

---

## Categories & Tags

### What's used in the wild (researched 2026-06-16)

WordPress/food-blog convention, confirmed across multiple sources:

- **Categories** = broad, hierarchical, structural/navigational. Best practice caps hierarchy at 2–3 levels and keeps the total list small.
- **Tags** = granular, cross-cutting, recurring details readers browse by. Best practice: never create a tag you expect to use once. Never give a tag the same name as a category.
- IACP splits food blogging into **Narrative Culinary** (essay/story-driven) vs. **Recipe-Based**. Useful as a reference point, but per Kevin's direction below, the Expo's actual category axis is neither of these — it's about preparation/learning format.

### Category direction — preparation & learning (per Kevin, 2026-06-16)

Categories are organized around the *kind of instructional content*, not editorial theme. Examples given:

- **"This 4-Course Meal Prep"** — a full menu/course prep and execution walkthrough, sequencing multiple recipes together.
- **"Baguette Walkthrough"** — a timed walkthrough of a single recipe's execution: actions and timing, not the full technical detail already covered in the recipe folio. May be paired with video.

**Open question carried into the worked-example pass:** where does a narrative/historical piece (the Ortolan essay, the original test case) fit in a prep/learning-oriented category scheme? Either it gets its own category (e.g. "Story & Tradition") alongside the prep-focused ones, or it's reclassified as something else entirely. Not resolved — flag for the worked-example pass, don't guess.

**Revised seed list (draft, still needs the worked-example pass before Phase 7):**

1. **Meal Prep Walkthroughs** — multi-recipe, full-menu execution and sequencing (e.g. "The 4-Course Meal Prep")
2. **Recipe Walkthroughs** — single-recipe, timed action/sequence focus, video-pairing candidate (e.g. "Baguette Walkthrough")
3. **Story & Tradition** — narrative/historical pieces (e.g. Ortolan) — *unconfirmed fit, see open question above*

### Tags/keywords — reuse the recipe keyword-pull mechanism (per Kevin, 2026-06-16)

Correction from the earlier draft of this doc: tags are a repeated structure exactly like recipe Keywords, and should be generated the same way, not hand-authored against a manually maintained index. Two-part method:

1. **Generation method mirrors `/keyword-pull`** (see `.claude/commands/keyword-pull.md`) — read the Expo post, generate comma-separated terms covering technique, themes, references, equipment, etc., the same way recipe Keywords are generated. New command: `/expo-keyword-pull`.
2. **Inherit from related recipes.** Pull the existing `keywords[]` already on each recipe in the post's `relatedRecipes[]` (recipes already have these via their own `/keyword-pull`) and merge them into the post's tag set. A post about 06-12 Quail automatically picks up relevant terms already established on that recipe — no need to re-derive them from scratch or keep two vocabularies in sync by hand.

Recipe `Category` (the `cuisine`/`style`/`family`/`course`/`dietary` controlled-vocabulary assignment) does **not** carry over — that's recipe-architecture-specific and already confirmed out of scope for Expo. Only the *Keywords* generation method transfers.

- **No category/tag name collisions** — a tag must never duplicate a category name.
- **Format:** categories Title Case, tags lowercase-hyphenated.

---

## Agent Ownership — Who Writes Expo Content

**Resolved 2026-06-16:** going with the structured plan — the dedicated **Café Athena Content Writer & Social Media Manager Agent** (per `The Manual/IDEAS.md`, "Site, Agent, & Tooling"), not a Brand Manager interim handoff. Kevin is building this agent and finishing `Brand/BRAND_GUIDELINES.md` in parallel with Expo infra, rather than waiting for the literal Phase 7 trigger sequence (social channels live + content calendar started) to complete first. Reason this Expo session ran first: figuring out the technical structure surfaces concrete requirements for what the agent's "blog writing mode" needs to produce — see **Notes for the Future Writing Agent** below.

`CLAUDE.md`'s AI surface table should get a row for this agent once it exists — not done yet, do it when the agent is actually built, per the Documentation Lifecycle convention (don't document a system before it's real).

---

## Notes for the Future Writing Agent

Pulled from `Brand/BRAND_DEVELOPMENT_PLAN.md`, `Brand/BRAND_GUIDELINES.md`, and `Brand/Personas/*.md` (2026-06-16) — concrete signal that should inform the agent's design, not just the Expo infra.

### Voice register — open question, not mine to resolve

`BRAND_GUIDELINES.md` defines two registers: **Manuscript** (§5 — authority, craft, warmth; for in-book content) and **Acquisition** (§6 — welcoming, curious, accessible, skeptical-newcomer-facing; for site/social). Neither maps cleanly onto Expo:

- A Story & Tradition piece (Ortolan) reads like in-book companion content — arguably Manuscript register — but the explicit reason Expo exists is also to "drive search traffic from outside the cookbook audience" (original `IDEAS.md` framing), which is Acquisition register's job.
- Recipe/Meal Prep Walkthroughs are practical and instructional — closer to Acquisition's plain, concrete, unhurried voice — but they're teaching technique depth, which is Manuscript's territory.

**Likely needs a third register, or explicit per-category register mapping** (e.g. Story & Tradition → Manuscript-leaning, Walkthroughs → Acquisition-leaning). This is a brand/voice decision, not a technical one — flagging for whoever builds the agent, not deciding it here.

### The non-negotiable, from all three personas

All three audience personas (`Brand/Personas/persona-*.md`) independently flag the same failure mode: writing or video that *reads as produced* rather than *understood*. Direct signal:

- **Persona 2 (Culinary Curious):** "sensitive to AI-sounding prose and generic phrasing — she clicks away when something sounds manufactured." "Content that skips the why."
- **Persona 3 (Kitchen Experimenter):** "can feel the difference between a recipe tested in a real kitchen... and one produced for a content calendar." This is a direct, specific risk for a content-calendar-driven agent — the agent has to produce calendar-cadence output without it reading as calendar-cadence output.
- **Persona 1 (Serious Home Cook):** on video specifically — "The camera follows his hands. The narration doesn't stop to explain why he's doing it that way. The skill is visible but not transferable." This is the exact failure mode a "Recipe Walkthrough" video pairing must avoid — narrate the why, not just the action.

**Action:** the `avoid-ai-writing` skill (already an auto-trigger for `The Manual/` prose per `CLAUDE.md`) should extend to Expo content once the agent exists — add it to the auto-trigger table at that point.

### Two video systems exist — don't conflate them

`BRAND_GUIDELINES.md` §8 already defines an **Educational/Companion Content (Lane 2)** system: NotebookLM-generated infographics/slide decks/video overviews from Technique Folios, in a specific Victorian/editorial illustrated style, naming pattern `edu-[folio-id]-*`, stored in `The Manual/Educational/`. This is AI-generated explainer media from folio *text* — a different production pipeline from whatever "might also accompany a video" means for a Recipe Walkthrough post (which reads more like an actual filmed/produced cooking demonstration). Keep these distinct when the agent's scope is defined — don't let Lane 2's existing conventions get assumed onto Expo's walkthrough video concept without a deliberate decision.

### Asset naming already anticipated Expo

`BRAND_GUIDELINES.md` §9 already reserves `section-expo.webp` as a valid section-landing image name, alongside `academy`/`brigade`/`larder` — confirms "Expo" as the established name predates this session and the `expo.astro` landing page (Phase 2) should follow this existing naming spec for its hero/landing image.

---

## Open / Parked — Needs a Design Pass Before Build

- **Blog Categories** — revised seed list above (Meal Prep Walkthroughs / Recipe Walkthroughs / Story & Tradition); still needs a worked-example pass, including resolving whether narrative pieces like Ortolan fit this scheme, before the `category` field and `/expo/category/[category].astro` route are built.

---

## Related Task — Done (was tracked separately, not Expo scope)

- **Recipe JSON-LD gap — ✅ done 2026-06-16.** Added `Recipe` + `BreadcrumbList` JSON-LD via new `site/src/utils/recipeSchema.ts`, wired through `[...slug].astro` → `RecipeLayout.astro` → `BaseLayout.astro`. Parses `## Ingredients`/`## Method` from the raw markdown body at build time. Verified via `npm run build`: 143/175 recipes get full `Recipe` schema (rich-result eligible); the other 32 fall back to `BreadcrumbList`-only — 30 are technique folios (correct, no Recipe schema applies) and 2 (`10-25`, `11-12`) are "collection folios" using custom sub-build headings instead of flat Ingredients/Method, which don't parse with the current regex. Graceful fallback by design — emitting partial/broken schema fails Google's validation, so those 2 just don't get Recipe rich-result eligibility yet. Revisit if full coverage matters; not blocking anything.

---

## Phased Build Checklist

### Phase 1 — Content model ✅ done 2026-06-16

- [x] Add `expo` collection to `site/src/content.config.ts` (schema: title, slug, date, excerpt, heroImage, relatedRecipes[], chapterPart, tags[] — category field held per Open Items above)
- [x] Create `site/src/content/expo/` with one placeholder post (hand-written frontmatter, bypassing the pipeline for this test) — `placeholder-post.md`
- [x] Create `Expo/Posts/` and `Expo/Drafts/` (empty, `.gitkeep`-tracked per repo convention)
- [x] Verified via `npm run build` — 259 pages built clean, `expo` collection schema parses with no errors, recipe build unaffected (no `/expo` route yet — that's Phase 2)

### Phase 2 — Routing

- [ ] Build `site/src/pages/expo/[...slug].astro` (model on `[...slug].astro`'s `getStaticPaths`, sort by `date` descending)
- [ ] Build `site/src/pages/expo.astro` landing page (reverse-chron card grid — new simple layout, not `SectionLayout`)
- [ ] Add "Expo" nav link to `BaseLayout.astro` (desktop + mobile + footer)

### Phase 3 — Cross-linking

- [ ] Render `relatedRecipes[]` on the Expo post page (lookup via `getEntry('recipes', id)`)
- [ ] Reverse-lookup query in `[...slug].astro`'s `getStaticPaths` + "From the Expo" block in `RecipeLayout.astro`

### Phase 4 — Pipeline

- [ ] `site/scripts/prepare-expo.py` (reads `Expo/Posts/`)
- [ ] `Expo/expo.json` registry
- [ ] `/register-expo`, `/sync-expo-registry` slash commands
- [ ] Wire into `site/scripts/deploy.sh`

### Phase 5 — Search & SEO

- [ ] Pagefind `data-pagefind-*` attributes on Expo body
- [ ] `sectionLabel()` case for `/expo/` in `BaseLayout.astro` search JS
- [ ] `Article` + `BreadcrumbList` JSON-LD on Expo pages
- [ ] Metadata per `fixing-metadata` conventions (title format, OG image, `og:type: article`)

### Phase 6 — Tags/keywords (can run parallel to Phase 4/5)

- [ ] `/expo-keyword-pull` command, modeled on `.claude/commands/keyword-pull.md`
- [ ] Wire in keyword inheritance from each `relatedRecipes[]` entry's existing `keywords[]`
- [ ] `tags[]` field on schema
- [ ] `/expo/tag/[tag].astro` archive route

### Phase 7 — Categories (blocked on design pass — see Open Items)

- [ ] Work up category examples (Meal Prep Walkthrough, Recipe Walkthrough, and resolve where Story & Tradition/Ortolan fits)
- [ ] Add `category` field to schema
- [ ] `/expo/category/[category].astro` archive route

### Phase 8 — Validation

- [ ] Full build + deploy dry run with placeholder content
- [ ] Confirm search, cross-links, nav all work end to end
- [ ] Swap placeholder for real first post once Chef delivers 06-12 Quail + Ortolan essay

### Phase 9 — Graduation (on completion)

- [ ] Write up "Workflow E: The Expo Editorial Cycle" in `Guidance/Cafe-Athena-Workflow-Guide.md`, PHASE-style, naming the actual commands/agents/skills built
- [ ] Remove the `Expo` pointer row from `PROJECT_STATUS.md`
- [ ] Retire/archive this file
