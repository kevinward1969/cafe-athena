# Project Brief: Site IA & Taxonomy Upgrade

**Status:** Active Planning
**Initiated:** 2026-05-18
**Priority:** High — foundational to all future site growth

---

## Background & Goals

The Café Athena manuscript has grown to ~130 folios across 12 chapters. The current site
renders recipes strictly by folio number within each chapter section, with no filtering,
cross-linking, or family-level browsing. Research into best-practice recipe site IA
(see `Online Recipe & Cookbook Site Structures vs. cookbook.kevinward.com.md`) confirms
that the primary gap is not content — it is **metadata richness and discovery tooling**.

The existing infrastructure is closer to best practice than it appears:

| Best-practice axis | Current state |
|---|---|
| Cuisine | `cuisine:` field exists in `## Category` |
| Style/register | `style:` field exists in `## Category` |
| Dietary | `dietary:` field exists in `## Category` (optional) |
| Tags | `## Keywords` section exists in every folio |
| Family/subcategory | **Missing** — no field |
| Course/meal type | **Missing** — no field |
| Registry metadata | **Missing** — `recipes.json` tracks pipeline stages only |
| Site filters | **Not built** |
| Site index pages | **Not built** |
| Cross-links ("See Also") | **Not built** |
| Collection pages | **Not built** |

This project formalizes the taxonomy, backfills the manuscript, propagates metadata
through the registry and pipeline, then builds the site features that consume it.

---

## Taxonomy Directory

**Canonical location: `Guidance/Taxonomy.md`**

All controlled vocabulary for every indexing field lives in one file.
`Recipe-Format-Standard.md`, the Chef agent, and the Astro pipeline
all reference this file — nothing defines valid terms anywhere else.
This prevents drift as new recipes, chapters, or cuisines are added.

Fields are also validated against this file by `audit.py --sync-metadata`.

---

## Taxonomy Design

### Existing fields (keep, no changes)

```
cuisine: French | style: Pastry | dietary: Vegetarian
```

Full controlled vocabulary moved to `Guidance/Taxonomy.md`.

### New fields to add

#### `family:` (optional → required for Ch. 10–12, recommended elsewhere)

The subcategory within a chapter. Answers: *what kind of thing is this?*
Enables grouping within chapter landing pages and cross-reference lookup.

Format: appended to the Category line

```
cuisine: French | style: Pastry | family: Pastry Dough
```

#### `course:` (optional → recommended for Ch. 3–9)

The meal/service position. Answers: *when is this served?*
Most useful for finished-dish chapters. Components and technique folios
use `course: Component` or omit the field.

```
cuisine: French | style: Classical | family: Mother Sauce | course: Component
```

**`course:` controlled vocabulary:**
`Breakfast` · `Brunch` · `Lunch` · `Dinner` · `Dessert` · `Snack` · `Beverage` · `Component`

---

## Family Philosophy

Family vocabulary is **prescriptive, not just descriptive** — it should include
categories we will cook, not only categories we have. This future-proofs the taxonomy
and the site's filter UI.

**Family axis by chapter type:**

| Chapter type | Family axis | Rationale |
|---|---|---|
| Technique (Ch. 1–2) | Science domain / Skill type | Concepts, not proteins |
| Garde Manger (Ch. 3) | Form & presentation | The station organizes by form |
| Starch (Ch. 4) | Starch base | Bread vs. Pasta vs. Rice vs. Polenta |
| Protein brigade (Ch. 5–7) | **Protein/ingredient** | How people browse: "I have chicken" |
| Vegetable (Ch. 8) | Primary vegetable | Ingredient-first for plant dishes |
| Pâtissier (Ch. 9) | Pastry form | Cookie vs. Tart vs. Cake vs. Canelé |
| Building blocks (Ch. 10–12) | Type of component | Stock vs. Sauce vs. Dough vs. Cream |

---

## Family Vocabulary (Proposed — validate before writing to folios)

### Chapter 1 — The Lab (Technique Folios)

| Family | Folios |
|---|---|
| `Heat & Thermodynamics` | 01-01, 01-13 |
| `Salinity & Seasoning` | 01-02 |
| `Starch & Dough Science` | 01-03, 01-08, 01-09, 01-10 |
| `Emulsification & Bonding` | 01-04, 01-05, 01-06 |
| `Hydrocolloids & Gels` | 01-07, 01-12 |
| `Fermentation` | 01-15, 01-16, 01-17, 01-18, 01-19, 01-21 |
| `Preservation & Transformation` | 01-11, 01-20, 01-22, 01-23 |

### Chapter 2 — The Foundation (Technique Folios)

| Family | Folios |
|---|---|
| `Kitchen Management` | 02-01, 02-02, 02-03, 02-05, 02-06, 02-07 |
| `Skills` | 02-04 |

> `Skills` (not `Knife Skills`) — future-proofs for other skill folios beyond knife work.

### Chapter 3 — Garde Manger

| Family | Current Folios | Notes |
|---|---|---|
| `Mousse & Pâté` | 03-07, 03-08, 03-10, 03-12, 03-13 | |
| `Amuse-Bouche` | 03-01 | Kitchen-sent, table-presented |
| `Canapé` | 03-02, 03-14 | Passed/reception; finger food on a base |
| `Cold Plate` | 03-03, 03-04, 03-11 | Plated first course |
| `Tartare & Raw` | 03-05 | |
| `Salad` | 03-09 | |
| `Preserved & Pickled` | 03-06 | |
| `Charcuterie` | — | Future |

### Chapter 4 — The Mill

| Family | Folios |
|---|---|
| `Bread` | 04-01, 04-05, 04-11, 04-14 |
| `Rice` | 04-02, 04-03 |
| `Pasta` | 04-04, 04-08, 04-10, 04-13 |
| `Gnocchi` | 04-07 |
| `Polenta` | 04-06, 04-09 |
| `Grain & Legume` | 04-12 |

> `Rice` (not `Risotto`) — future-proofs for rice pilaf, fried rice, arroz, etc.
> Future additions: `Pizza`, `Flatbread`.

### Chapter 5 — The Fishmonger

*Protein-based families. Technique lives in Keywords.*

| Family | Current Folios | Future |
|---|---|---|
| `Mollusc` | 05-01 (scallops) | clams, mussels, oysters |
| `Finfish` | 05-02, 05-03, 05-04 | salmon, halibut, tuna, mackerel |
| `Crustacean` | — | shrimp, lobster, crab |
| `Cephalopod` | — | squid, octopus |
| `Cured & Smoked` | — | gravlax, smoked fish |

### Chapter 6 — The Poulterer

*Protein-based families. Technique lives in Keywords.*

| Family | Current Folios | Future |
|---|---|---|
| `Chicken` | 06-01, 06-02, 06-04, 06-05, 06-06 | — |
| `Duck` | 06-03 | — |
| `Turkey` | — | roast, confit |
| `Game Bird` | — | quail, pheasant, guinea fowl |
| `Egg` | — | standalone egg preparations |

### Chapter 7 — The Butcher

*Protein-based families. Technique lives in Keywords.*

| Family | Current Folios | Future |
|---|---|---|
| `Beef` | 07-01, 07-04, 07-05, 07-06, 07-07, 07-08, 07-09, 07-10, 07-11, 07-13 | — |
| `Pork` | 07-03, 07-12 | ribs, roast, shoulder |
| `Ground & Formed` | 07-02 | meatballs, sausage, burgers, kofta, gyro, shawarma |
| `Lamb` | — | rack, shoulder, leg |
| `Goat` | — | braise, stew |
| `Veal` | — | osso buco, scaloppine |
| `Wild Game` | — | venison, rabbit, bison |
| `Offal` | — | liver, kidney, sweetbreads |

> `Charcuterie` removed from Ch. 7. In classical brigade, charcuterie belongs to
> Garde Manger (Ch. 3). Cured items like 07-12 (Dehydrator Bacon) file under `Pork`.

### Chapter 8 — The Field

*Mix of ingredient groups and technique/form families. Grain removed — lives in Ch. 4.*

| Family | Current Folios | Future |
|---|---|---|
| `Salad & Dressed` | 08-04, 08-05 | herb salads, dressed grain salads |
| `Mash & Purée` | 08-03 | mousseline, smooth veg preparations |
| `Tuber` | 08-06, 08-10 | sweet potato, sunchoke, taro, yuca, yam |
| `Root Vegetable` | — | carrot, parsnip, celeriac, beet, turnip |
| `Stuffed` | 08-08 | stuffed peppers, cabbage rolls |
| `Roasted & Grilled` | 08-02, 08-07 | squash, corn ribs, charred veg |
| `Mushroom` | 08-01 | all fungi |
| `Steamed & Braised` | 08-09 | butter-braised greens, delicate veg |
| `Leafy Green` | — | spinach, chard, kale (future) |
| `Legume` | — | lentils, chickpeas, beans (future) |
| `Tomato & Nightshade` | — | eggplant, peppers (future) |
| `Allium` | — | onion, leek, fennel (future) |
| `Brassica` | — | cauliflower, broccoli, sprouts (future) |

### Chapter 9 — The Pâtissier

| Family | Folios | Notes |
|---|---|---|
| `Brownie & Bar` | 09-01, 09-06 | |
| `Cookie` | 09-02, 09-03 | 09-03 pending replacement with Lemon Blackberry Tart |
| `Small Cake & Pastry` | 09-04 | Canelé; future: financier, madeleine, kouglof |
| `Posset & Panna Cotta` | 09-05 | Future: panna cotta, bavarian |
| `Tart` | — | Future: 09-03 Lemon Blackberry Tart |
| `Choux` | — | Future |
| `Frozen Dessert` | — | Future |
| `Confection` | — | Future |

### Chapter 10 — Stocks & Mother Sauces

| Family | Folios | Notes |
|---|---|---|
| `Stock` | 10-01, 10-17 | |
| `Mother Sauce` | 10-03, 10-08, 10-15, 10-16, 10-18 | |
| `Derivative Sauce` | 10-04, 10-05, 10-06, 10-10, 10-11, 10-19 | |
| `Cold Blended Sauce` | 10-02, 10-14, 10-20 | Pesto, salsa di noci — replaces `Pesto` family |
| `Compound Butter` | 10-07, 10-22 | |
| `Emulsion` | 10-09, 10-25 | Stable emulsions only |
| `Ragù & Meat Sauce` | 10-13 | Bolognese is a ragù |
| `Dipping Sauce` | 10-23, 10-24 | |
| `Cream Sauce` | 10-12, 10-21 | |
| `Pan Sauce` | — | Future |
| `Jus & Reduction` | — | Future |
| `Salsa & Fresh Sauce` | — | Future |
| `Vinaigrette` | — | Future |

### Chapter 11 — Spice Blends & Oils

| Family | Folios | Notes |
|---|---|---|
| `Herb Oil` | 11-01 | Chlorophyll-stabilized fresh herb oils |
| `Specialty Salt` | 11-02, 11-03, 11-04 | Smoked, flavored, crystallized, ash |
| `Wet Paste` | 11-05 | Nashville fire paste, harissa |
| `Dry Spice Blend` | 11-06 | Spice-forward dry blends |
| `Infused Oil` | — | Garlic, chili, aromatic oils (future) |
| `Dry Herb Blend` | — | Za'atar, herbes de Provence, fines herbes (future) |
| `Fresh Herb Blend` | — | Gremolata, persillade, chermoula (future) |
| `Spice Rub` | — | Dry rubs for smoking/grilling (future) |
| `Vinegar & Acid` | — | Flavored vinegars, shrubs (future) |

### Chapter 12 — Les Fonds

| Family | Folios |
|---|---|
| `Platform & Vessel` | 12-01, 12-15, 12-16 |
| `Pastry Dough` | 12-02, 12-03, 12-04, 12-05, 12-06 |
| `Pasta Dough` | 12-07, 12-08, 12-09, 12-10 |
| `Cream & Filling` | 12-11, 12-12, 12-13, 12-14 |
| `Garnish & Component` | 12-17, 12-20, 12-22 |
| `Batter & Coating` | 12-18, 12-19, 12-21 |
| `Caramel & Sugar` | 12-23 |

---

## Data Flow

```
Folio ## Category section   ←── source of truth (human-edited)
        │
        ├── prepare-content.py extracts → Astro built file frontmatter
        │       (cuisine, style, dietary, family, course)
        │
        └── /register-recipe writes → recipes.json entry
                (cuisine, style, dietary, family, course, keywords[])
                        │
                        └── audit.py --sync-metadata backfills existing entries
```

### recipes.json entry — proposed new schema

```json
{
  "id": "12-11",
  "title": "Crème Pâtissière",
  "chapter": 12,
  "chapterName": "Les Fonds",
  "type": "recipe",
  "cuisine": "French",
  "style": "Classical",
  "family": "Cream & Filling",
  "course": "Component",
  "keywords": ["crème pâtissière", "pastry cream", "filling", "tart"],
  "dietary": null,
  "added": "2026-04-04",
  "stages": { ... },
  "audit": { ... }
}
```

---

## Phased Implementation Plan

### Phase 1 — Taxonomy Definition ✅ COMPLETE (2026-05-18)

- [x] Identify gaps in current Category fields
- [x] Design `family:` and `course:` fields (renamed from `cluster:`)
- [x] Draft family vocabulary for all chapters
- [x] Establish family philosophy (prescriptive; ingredient-based for brigade chapters)
- [x] Create `Guidance/Taxonomy.md` — canonical controlled vocabulary
- [x] Review and validate family assignments (Kevin)
- [x] Update `Guidance/Recipe-Format-Standard.md` v3.3 — add new fields, reference Taxonomy.md
- [x] Vocabulary removed from `Recipe-Format-Standard.md` (lives in Taxonomy.md only)

### Phase 1.5 — Agent & Workflow Updates ✅ COMPLETE (2026-05-18)

- [x] Canonical master v1.7 — Category format updated (4 fields + Taxonomy.md ref); recipe structure order corrected; section numbers fixed
- [x] Claude Desktop v1.9 — Category format and structure item 10 updated
- [x] `format-audit.md` — vertical order fixed (Ingredients before Mise); Category checks updated for all 4 fields; technique folio spec corrected
- [x] Gemini Gem 1 — no change needed (defers to Recipe-Format-Standard.md attachment)
- [x] `CLAUDE.md` — no change needed (pipeline docs update deferred to Phase 4)

### Phase 2 — Manuscript Backfill ✅ COMPLETE (2026-05-18)

- [x] Add `family:` and `course:` to all existing folio `## Category` sections
- [x] All 152 folios updated via `scripts/backfill-taxonomy.py` (0 warnings, 0 skips)
- [x] Ch. 1–2: `family:` only (no `course:` — concept doesn't map to technique folios)
- [x] Ch. 3–8: `family:` + `course: Dinner`
- [x] Ch. 9: `family:` + `course: Dessert`
- [x] Ch. 10–12: `family:` + `course: Component`
- [ ] Verify Chef agent uses new fields correctly on first new folio after update

### Phase 3 — Registry Update ✅ COMPLETE (2026-05-18)

- [x] Add `cuisine`, `style`, `family`, `course`, `keywords[]`, `dietary` fields to
      `recipes.json` schema (`_meta.fields` description block added)
- [x] Update `/register-recipe` workflow to capture and write all new fields
- [x] Write `audit.py --sync-metadata` mode: reads each folio's Category/Keywords,
      populates missing fields in corresponding `recipes.json` entry (fast, no LLM)
      Also supports `--dry-run` to preview changes before writing.
- [x] Run `--sync-metadata` across all 152 entries — all populated

### Phase 4 — Pipeline Update ✅ COMPLETE (2026-05-19)

- [x] Updated `prepare-content.py` — `extract_metadata()` now extracts `family` and `course`; frontmatter template updated
- [x] Updated `site/src/content.config.ts` — `family` and `course` added to schema
- [x] Build verified clean — 152 pages, 3 filters indexed, 0 errors
- [x] `RecipeLayout.astro` Props interface updated; `[...slug].astro` passes all five Category fields
- [x] Landing pages (`larder`, `brigade`, `academy`) need no changes — they don't use Category fields
- [x] `CLAUDE.md` pipeline documentation updated (lines 193–194)

### Phase 5 — Site Features ✅ PARTIALLY COMPLETE (2026-05-19)

#### 5a — Filter UI ✅ COMPLETE

- [x] Pagefind filter index extended: `family` and `course` added to `data-pagefind-filter` in `RecipeLayout.astro` (4 filters total: cuisine, style, family, course)
- [x] ⌘K search modal: collapsible "Browse by family & course" filter chip panel — 38 chips across 6 groups (Proteins & Seafood, Starches, Sauces & Building Blocks, Pastry & Sweets, Technique, Course)
- [x] Filter-only browsing works (no text query required); OR within group, AND between groups; active count badge; Clear button; resets on modal close

#### 5b — Recipe Index Pages ✅ COMPLETE

- [x] `/categories` — visual index of all 40 families organized in 7 groups; dark 16:9 cards with hero images, 3-column grid, group headers in Cormorant serif
- [x] `/categories/[family]` — 40 static pages generated at build time; card grid (with images) or list fallback; hero banner with family name and recipe count; back navigation
- [x] `site/src/utils/taxonomy.ts` — `familyToSlug()`, `CATEGORY_GROUPS`, `NAV_CATEGORY_GROUPS`
- [x] Nav: hover tooltips on Academy/Brigade/Larder; "Categories" nav item with dark mega-menu dropdown (6 groups, "Browse all →" link); added to mobile nav and footer
- [x] Home page: "Browse by Category" section added to reference area (4 groups, pill-style links with counts)
- [x] Deployed to cookbook.kevinward.com (2026-05-19)

#### 5c — Cross-Links ("See Also") — Not yet built

- Add optional `## See Also` section to recipe format standard
- Format: `[XX-YY Title]` list (3–5 entries max)
- `prepare-content.py` resolves IDs to titles and URLs at build time
- `recipes.json` enables agent-assisted suggestions

#### 5d — Collection Pages — Not yet built

- Curated thematic groupings (e.g., "Core Café Athena Menu," "Full Brunch Service")
- Low priority until cross-links are complete

---

## Open Questions

1. ~~**`course:` for technique folios**~~ — **RESOLVED 2026-05-19**: omitted for Ch. 1–2. Concept doesn't map cleanly to technique folios; no `course:` field written.

2. ~~**`family:` for Ch. 1**~~ — **RESOLVED 2026-05-19**: science families validated and backfilled across all 23 Lab folios.

3. **PB tart crust** — new 12-25 folio or Variant 7 in 12-02? Decision deferred with tart work.

4. **`See Also` authoring** — manual (Chef agent adds during Mode 2 formatting) or semi-automated (`audit.py` suggests based on shared family/keywords)? Deferred until 5c is prioritized.

5. ~~**Filter UI approach**~~ — **RESOLVED 2026-05-19**: Pagefind native metadata filters used for ⌘K search modal. No custom JS islands needed.

6. **Taxonomy content gaps** — RecipeTinEats comparison identified browsable categories we don't yet have recipes for: Lamb, Eggs, Soups-as-dish, Asian Noodles, Breakfast. Taxonomy structure is correct; these are content gaps to fill with future folios.

---

## On-Hold Work (Tart Recipe Arc)

Deferred until Phase 2–3 are complete so new folios are registered correctly.

| Item | Status | Notes |
|---|---|---|
| 12-24 Foundation Curd | On hold | Lemon base; citrus variants. Earns Ch.12 as multi-use building block. |
| 12-11 update | On hold | Add lemon-flavored crème pâtissière variant |
| 09-03 Lemon Blackberry Tart | On hold | Replaces cookie v2 duplicate; references 12-02 (shell) and 12-24 (curd) |
| PB tart crust | On hold | 12-02 variant vs. new 12-25 folio — decision pending |
| 09-03 duplicate resolution | On hold | Current 09-02 (v1) and 09-03 (v2) are identical cookie recipe |

---

## Reference

- `Guidance/Taxonomy.md` — **canonical controlled vocabulary** (all valid field values)
- `Guidance/Recipe-Format-Standard.md` — format spec; references Taxonomy.md for vocab
- `recipes.json` — registry to be extended in Phase 3
- `site/scripts/prepare-content.py` — pipeline to be updated in Phase 4
- `site/src/content.config.ts` — Astro schema to be updated in Phase 4
- `Online Recipe & Cookbook Site Structures vs. cookbook.kevinward.com.md` — IA research
