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

### Phase 1 — Taxonomy Definition *(current phase)*

- [x] Identify gaps in current Category fields
- [x] Design `family:` and `course:` fields
- [x] Draft family vocabulary for all chapters
- [x] Establish family philosophy (prescriptive; ingredient-based for brigade chapters)
- [x] Create `Guidance/Taxonomy.md` — canonical controlled vocabulary
- [ ] Review and validate family assignments (Kevin) — esp. Ch. 1, Ch. 9, Ch. 10
- [ ] Update `Guidance/Recipe-Format-Standard.md` — add new fields, reference Taxonomy.md
- [ ] Remove vocabulary from `Recipe-Format-Standard.md` (now lives in Taxonomy.md only)

### Phase 2 — Manuscript Backfill

- [ ] Add `family:` and `course:` to all existing folio `## Category` sections
- [ ] Priority order: Ch. 12 first, then Ch. 10–11, then Ch. 3–9, then Ch. 1–2
- [ ] Use `audit.py` batch detection + human approval (no LLM needed — regex extraction)
- [ ] Verify Chef agent uses new fields correctly on first new folio after update

### Phase 3 — Registry Update

- [ ] Add `cuisine`, `style`, `family`, `course`, `keywords[]`, `dietary` fields to
      `recipes.json` schema (update `_meta.stages` description block)
- [ ] Update `/register-recipe` workflow to capture and write all new fields
- [ ] Write `audit.py --sync-metadata` mode: reads each folio's Category/Keywords,
      populates missing fields in corresponding `recipes.json` entry (fast, no LLM)
- [ ] Run `--sync-metadata` across all existing entries after manuscript backfill

### Phase 4 — Pipeline Update

- [ ] Update `prepare-content.py` to extract `family:` and `course:` alongside
      existing `cuisine`, `style`, `dietary`
- [ ] Update `site/src/content.config.ts` schema to add `family` and `course` fields
- [ ] Run full build and verify fields appear correctly in built recipe files
- [ ] Update `site/src/pages/larder.astro` (and `brigade.astro`, `academy.astro`)
      to pass new fields through — no UI changes yet, just data plumbing

### Phase 5 — Site Features

These are independent and can be prioritized separately after Phase 4.

#### 5a — Filter UI

- Add filter controls (family, cuisine, course, dietary) to section landing pages
- Keep crawlable — server-rendered options, progressive enhancement for interactivity
- Pagefind already indexes content; combine with metadata filters for hybrid search

#### 5b — Recipe Index Pages

- Visual index: category cards linking to filtered views (one per chapter section)
- Text index: alphabetical list of all recipes, optionally grouped by family

#### 5c — Cross-Links ("See Also")

- Add optional `## See Also` section to recipe format standard
- Format: `[XX-YY Title]` list (3–5 entries max)
- `prepare-content.py` resolves IDs to titles and URLs at build time
- `recipes.json` enables agent-assisted suggestions: "find all Cream & Filling
  recipes in Ch. 12 for cross-linking from this tart folio"

#### 5d — Collection Pages

- Curated thematic groupings (e.g., "Core Café Athena Menu," "Full Brunch Service,"
  "Foundational Sauces")
- Implemented as static Astro pages referencing recipe IDs
- Low priority until 5a–5c are complete

---

## Open Questions

1. **`course:` for technique folios** — omit or use a standard value like `Technique`?
   Affects Ch. 1 and Ch. 2 where the concept doesn't map cleanly.

2. **`family:` for Ch. 1** — the science families above are proposed; Kevin should
   validate whether these match how he thinks about the Lab chapter.

3. **PB tart crust** — new 12-25 folio or Variant 7 in 12-02?
   Depends on whether it's a pressed/cookie crust (separate) or enriched pastry dough
   (variant). Decision deferred with tart work.

4. **`See Also` authoring** — manual (Chef agent adds during Mode 2 formatting) or
   semi-automated (audit.py suggests based on shared family/keywords)?

5. **Filter UI approach** — pure Pagefind metadata filters, or custom Astro islands?
   Pagefind supports metadata filtering natively; may be sufficient without custom JS.

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
