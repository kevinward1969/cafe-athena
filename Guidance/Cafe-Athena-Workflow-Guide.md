**CAFÉ ATHENA — WORKFLOW GUIDE**

Strategic methodology for dish development, technical documentation, and site publishing.

---

**WORKFLOW A: THE NEW RECIPE CYCLE (LAB TO PUBLICATION)**

* **PHASE 1: DRAFTING (MODE 1).** Initiate a chat to begin development of a new concept. The AI iterates on technique, variables, flavor profiles, and structure.
* **PHASE 2: REFINING.** Use iterative passes to lock in temperatures, ratios, equipment, and method. Resolve food science questions here.
* **PHASE 3: FINALIZING.** Say "Finalize" or "Ready for Manual" to exit Mode 1. The AI confirms completion criteria before advancing.
* **PHASE 4: FORMATTING (MODE 2).** The AI scans the live chapter directory, assigns the next XX-YY index, generates the complete manuscript-ready recipe with Keywords and Category sections, and runs a built-in clarity audit — fixing any forward references, ambiguous parentheticals, unlisted method ingredients, or multi-action steps before outputting the final draft.
* **PHASE 5: WRITING TO DISK.** The AI writes the formatted file directly to the correct chapter folder in `The Manual/` and updates `Cafe-Athena-The-Manual-Current-Version.md`.
* **PHASE 6: PUBLISHING TO SITE.** Run `/pipeline [index]` in Claude Code. The pipeline handles registration, clarity audit, image prompt generation, format audit, keyword/category pull, glossary pull, hero image check, build, deploy, and all tracking updates in a single command.

---

**WORKFLOW B: THE LEARNING/FOLIO CYCLE (THE MASTERCLASS)**

* **PHASE 1: TECHNICAL INQUIRY (MODE 3).** Request detailed technical education on a specific subject (e.g., fluid gels, baker's percentages, emulsification chemistry).
* **PHASE 2: TUTORIAL.** The AI provides the underlying science, ratios, formulas, and technique context.
* **PHASE 3: FOLIO CREATION.** Say "Convert to Folio" or "Ready to format." The AI scans the target chapter directory, assigns the next XX-YY index, and formats the content using `Technique_Folio_Template_v1.md`.
* **PHASE 4: WRITING TO DISK.** The AI writes the folio directly to the correct chapter folder and updates the master index.
* **PHASE 5: PUBLISHING TO SITE.** Same pipeline as Workflow A, Phase 6.

---

**WORKFLOW C: ADDING IMAGES**

Images follow a two-type system. The canonical location for all processed images is `site/public/images/` — chapter folder copies are working files only and are deleted once processed.

* **HERO IMAGES (one per recipe):**

  **Standard path:**
  1. Run `/recipe-hero-image [index]` — the AI reads the recipe frontmatter and headnote, builds a detailed Gemini image prompt, and presents it for approval.
  2. Take the prompt to Gemini (image generation), generate the image, and save as `{index}.png` into the chapter folder.
  3. Run `/recipe-hero-image optimize [index]` — converts the PNG to WebP (quality 85, max 1920×1080), deletes the original PNG, deploys, then deletes the WebP from the chapter folder.

  **Bypass path (pre-optimized):**
  If you have already optimized the image and placed the WebP directly into `site/public/images/`, tell Claude Code — it will skip the optimize step, update `The Manual/recipes.json`, deploy, and commit. No chapter folder involvement needed.

* **REFERENCE IMAGES (inline figures within the recipe body):**

  1. Run `/recipe-hero-image insert [index] "[position hint]" "[caption]"` — the AI inserts the `[ref:]` shortcode at the correct location in the source folio and assigns the next available letter.
  2. Save the corresponding image as `{index}{letter}.png` in the chapter folder.
  3. Optimize: `/recipe-hero-image optimize {index}{letter}`.

* **SHORTCODE SYNTAX** (in recipe body):

  ```
  [ref:12-07a | The laminated pasta dough at final thickness]
  ```

  The Astro build transforms this into a captioned `<figure>` element. The image must exist at `site/public/images/{index}{letter}.webp`, which the pipeline places there from the chapter folder.

* **BATCH OPTIMIZATION:**

  ```
  /recipe-hero-image optimize chapter-4
  /recipe-hero-image optimize all
  ```

---

**WORKFLOW D: SYSTEM INTEGRITY AND GLOSSARY MAINTENANCE**

* **GLOSSARY PULL.** After formatting any new recipe, run `/glossary-pull [index]` to extract glossary terms and merge them alphabetically into the split glossary files at `The Manual/Glossary/Café Athena  - Glossary [LETTER].md` (duplicates are skipped automatically).
* **GLOSSARY AUDIT.** Run `/audit-glossary` periodically to enforce strict `- Term: Definition` formatting, correct alphabetization, and remove duplicates.
* **FORMAT AUDIT.** Run `/format-audit [index]` or `/format-audit Chapter N` to validate recipe structure against `Recipe-Format-Standard.md`. Includes an authorization layer — the AI presents proposed changes before writing anything.
* **KEYWORD PULL.** Run `/keyword-pull [index]` to generate and append `## Keywords` and `## Category` sections to any recipe missing them.
* **MASTER INDEX.** `The Manual/Cafe-Athena-The-Manual-Current-Version.md` must stay current. The AI updates it as part of Mode 2 and Mode 3 output. If an entry is added manually, update this file immediately.

---

**WORKFLOW E: THE EXPO EDITORIAL CYCLE**

The Expo is editorial/blog content — instructional walkthroughs, narrative essays, and technique companion pieces — published at `/expo/[slug]`. It lives in `Expo/` (sibling to `Brand/` and `Marketing/`), not under `The Manual/`. Posts flow through their own pipeline before the site build.

* **PHASE 1: DRAFTING.** Author writes the post in `Expo/Drafts/` — research notes, rough prose, source references. Nothing here is pipeline-ready. Drafts stay in this folder until the author is satisfied with the substance.

* **PHASE 2: WRITING TO DISK.** When the draft is final, write the finished post to `Expo/Posts/[slug].md` with complete frontmatter:

  ```yaml
  ---
  title: "Post Title"
  date: "YYYY-MM-DD"
  excerpt: "One or two sentence summary for cards and meta description."
  heroImage: "filename.webp"        # omit if no hero image yet
  relatedRecipes: ["06-12", "07-04"]
  category: "Recipe Walkthroughs"   # see category list below
  tags: []                          # populated in Phase 3
  ---
  ```

  Valid categories: `Recipe Walkthroughs`, `Meal Prep Walkthroughs`, `Technique in Context`, `Ingredient Spotlight`, `Story & Tradition`, `Plating & Presentation`, `Menu & Service`.

  **Filename = URL slug.** The file's name (without `.md`) becomes the post's URL — e.g. `baguette-walkthrough.md` → `/expo/baguette-walkthrough`. Name the file what you want in the URL.

  Inline images in the post body use the shortcode: `[expo:filename.webp | caption text]` — the build pipeline transforms this into a captioned `<figure>` element. Naming convention for inline images: `expo-[slug]-[n].webp` (e.g. `expo-baguette-walkthrough-1.webp`).

* **PHASE 3: KEYWORD PULL.** Run `/expo-keyword-pull [slug]`. The command reads the post body, generates 8–15 tags covering techniques, themes, cultural references, key ingredients, and equipment, then merges in the `keywords[]` already on each recipe listed in `relatedRecipes[]`. **Stop point:** the proposed tag list is presented for confirmation before anything is written. Tags are lowercase-hyphenated (`beurre-blanc`, `mise-en-place`).

* **PHASE 4: REGISTRATION.** Run `/register-expo [slug]`. The command reads the post's `title` and `date` from frontmatter, checks whether the hero image exists, and presents the entry for confirmation before writing. **Stop point:** confirm before the entry is added to `Expo/expo.json`. The registry tracks three stages per post: `written`, `heroImage`, `deployed`.

* **PHASE 5: HERO IMAGE.** Place the optimized WebP at `site/public/images/[heroImage].webp`. Once placed, update `heroImage: true` in the post's entry in `Expo/expo.json`. The image must exist at this path before the build — the `prepare-expo.py` script does not copy hero images from `Expo/Posts/`; they go directly into `site/public/images/`. Inline images placed alongside the source file in `Expo/Posts/` are copied by the pipeline automatically.

* **PHASE 6: PUBLISHING.** Run `bash site/scripts/deploy.sh` from the repo root. The script runs in sequence: `prepare-content.py` (recipes) → `prepare-expo.py` (expo posts) → `npm run build` (Astro + Pagefind) → `rsync` to FastComet. After rsync confirms success, update `deployed: true` in the post's entry in `Expo/expo.json`. **Never report the post as live until rsync completes.** Commit and push after the registry is updated.

* **GOVERNANCE.** Run `/expo-tag-audit` periodically to check tag frequency across all posts, surface single-use candidates (potential clutter), and flag near-duplicate pairs (pluralization drift, separator inconsistency). Read-only — produces a report only, no writes. Run `/sync-expo-registry` if posts were added to `Expo/Posts/` outside the normal `/register-expo` flow — it reconciles the registry against the live directory without removing entries or resetting completed stages.
