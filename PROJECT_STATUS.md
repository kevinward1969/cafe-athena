# Café Athena - Project Status & Active Context

Last Updated: 2026-04-15

## 🎯 Active Development

| Folio | Title | Status | Notes |
| :--- | :--- | :--- | :--- |
| **10-21** | Lemon Cream & Parmigiano Sauce | Completed | Indexed. |
| **04-16** | Definitive Guide to Egg Pasta | Completed | Indexed. |

## 📋 TODO

- **Full Manual Structure — Four-Part Arc**: The Manual has a confirmed four-part structure:

  | Part | Chapters | Theme |
  | :--- | :--- | :--- |
  | **Part I: The Academy** | Ch. 1–2 (The Lab, The Foundation) | Technique |
  | **Part II: The Brigade** | Ch. 3–9 (Garde Manger → The Pâtissier) | Cooking through the stations |
  | **Part III: The Larder** | Ch. 10–12 (Stocks & Sauces, Spice Blends, Les Fonds) | Building blocks |
  | **Part IV: The Expo** | Ch. 13–15 (Planning, Plating, Service) | Capstone — how it reaches the guest |

  Part IV is the narrative capstone: you enter through technique, cook through the brigade, build from the larder, and the whole thing culminates in service. Reads like a real culinary school curriculum.

- **Chapter 12 — Les Fonds** *(Structural Bases, Vessels & Platforms)*: Completes Part III. 15 entries complete: 12-01 Crispy Rice Platform, 12-02 Foundation Tart Dough (Six Variants), 12-03 Pâte Brisée, 12-04 Pâte à Choux, 12-05 Pâte Feuilletée, 12-06 Rough Puff Pastry, 12-07 Rich Yolk Pasta Dough, 12-08 Gnocchi 201, 12-09 Definitive Guide to Egg Pasta, 12-10 Quintessential Spinach Pasta, 12-11 Crème Pâtissière, 12-12 The Meringue Trinity, 12-13 Crème Chantilly, 12-14 The Composite Creams, 12-15 The Master Laminated Frico. Chapter 9 retains 09-07 and 09-09 as single-formula educational references pointing to 12-02. Next candidate: 12-16 Non-Fish Caviar (Seeds & Spheres) — in development.

- **Part IV: The Expo** *(Ch. 13–15)*: Narrative capstone of The Manual and a dedicated site section.
  - **Ch. 13 — Planning**: Menu engineering, course sequencing, ticket flow, timing
  - **Ch. 14 — Plating**: Composition, visual language, the architecture of the plate
  - **Ch. 15 — Service**: The handoff, hospitality, reading the room, pacing
  Content is editorial/instructional (not recipe folios). Needs: content plan, chapter scaffolding, site section design, nav integration.

---

## 🌅 On the Horizon

- **Home Page Copy — 3 Main Area Descriptions**: ✅ Completed 2026-04-08.
- **Glossary Letter Navigation Fix**: ✅ Completed 2026-04-08.
- **Academy Section Randomizer (Home Page)**: ✅ Completed 2026-04-08.
- **Featured Recipe Randomizer (Home Page)**: ✅ Completed 2026-04-08.
- **Food Critic / Food Writer Agent**: Create a new Claude Code agent for creative and marketing copy — editorial, journalistic, blog posts, social media. Separate surface from the Chef agent.
- **Section & Chapter Banner Images**: Full-bleed panoramic banners (~1920×380px WebP) for each section page and each chapter. Generated via Gemini Gem 2. See image briefs below. Implementation: add optional `bannerImage` prop to `SectionLayout.astro`. Naming: `banner-academy.webp`, `banner-brigade.webp`, `banner-larder.webp`, `banner-ch03.webp` … `banner-ch12.webp`. All placed in `site/public/images/`.

- **Glossary Pull**: ✅ Completed 2026-04-09 — all 127/127 recipes indexed.
- **Glossary Audit**: ✅ Completed 2026-04-14 — removed 13 duplicate entries, fixed alphabetization in C, D, P, and merged near-identical variants. Old monolithic `Café Athena - Glossary.md` deleted; split-file format is now canonical.

---

## 🔧 Site & Asset Maintenance

### Hero Image Progress

Hero image status is tracked per-recipe in `recipes.json` via `heroImage` and `heroImageOptimized` stages. Use `/sync-registry` to refresh.

**Hero image status (2026-04-09):** 84/127 complete. Pending: 07-13, 08-04–08-06, 09-01–09-11 (all), 10-01–10-23, 11-01–11-05.

---

### Format Audit — Full Cookbook

Run `/format-audit Chapter N` across all chapters to validate every recipe and folio against `Recipe-Format-Standard.md`. Includes structural order, Mise En Place compliance, Keywords, and Category sections.

> **Note:** Chapters 1 and 2 are entirely Technique Folios — they do not contain recipes. The format audit for these chapters uses folio-specific checks only (Glossary, Keywords lowercase, Category, dual temperatures). Recipe-specific sections (Mise En Place, Ingredients, Method) do not apply and should not be flagged. See `Guidance/Recipe-Format-Standard.md` — Technique Folio Format section.

| Chapter | Type | Status |
| :--- | :--- | :--- |
| Chapter 1 - The Lab | Technique Folios (19) | ✅ Complete (2026-04-10) |
| Chapter 2 - The Foundation | Technique Folios (7) | ✅ Complete (2026-04-10) |
| Chapter 3 - Garde Manger | Recipes | ✅ Complete (2026-04-11) |
| Chapter 4 - The Mill | Recipes | ✅ Complete (2026-04-11) |
| Chapter 5 - The Fishmonger | Recipes | ✅ Complete (2026-04-10) |
| Chapter 6 - The Poulterer | Recipes | ✅ Complete (2026-04-10) |
| Chapter 7 - The Butcher | Recipes | ✅ Complete (2026-04-10) |
| Chapter 8 - The Field | Recipes | ✅ Complete (2026-04-10) |
| Chapter 9 - The Pâtissier | Recipes | ✅ Complete (2026-04-09) |
| Chapter 10 - Stocks & Mother Sauces | Recipes | ✅ Complete (2026-04-09) |
| Chapter 11 - Spice Blends & Oils | Recipes | ✅ Complete (2026-04-09) |
| Chapter 12 - Les Fonds | Recipes | ✅ Complete (2026-04-14) |

### PNG → WebP Optimization

✅ Complete (2026-04-09) — 0 PNGs remaining in The Manual.

### Hero Image Generation — Missing Entries (43 total)

Use `/recipe-hero-image [index]` for each. Ch. 9 (zero coverage) is highest priority.

| Index | Title | Chapter |
| :--- | :--- | :--- |
| 07-13 | Individual Beef Wellington | Ch. 7 |
| 08-04 | St. Louis Style Kisir (Red Hot Bulgur) | Ch. 8 |
| 08-05 | Modern Tabbouleh (The Acid Cutter) | Ch. 8 |
| 08-06 | Onion Potato Crisps | Ch. 8 |
| 09-01 | Brown Butter & Miso-Caramel Truffle Brownies | Ch. 9 |
| 09-02 | Spicy Brown Butter & Lemon Cheesecake Cookies | Ch. 9 |
| 09-03 | Sesame Tuile Cylinders | Ch. 9 |
| 09-04 | Pâte à Choux (The Steam Dough) | Ch. 9 |
| 09-05 | Pâte Feuilletée (Classic Puff Pastry) | Ch. 9 |
| 09-06 | Pâte Brisée (Classic Shortcrust) | Ch. 9 |
| 09-07 | Pâte Sucrée (Sweet Tart Dough) | Ch. 9 |
| 09-08 | Rough Puff Pastry (Demi-Feuilletée) | Ch. 9 |
| 09-09 | Pâte Sablée (Rich Shortbread Crust) | Ch. 9 |
| 09-10 | Spicy Brown Butter & Lemon Cheesecake Cookies (v2) | Ch. 9 |
| 09-11 | Brandy-Infused Canelés de Bordeaux | Ch. 9 |
| 10-01 | High-Pressure White Chicken Stock | Ch. 10 |
| 10-02 | Vibrant Basil Pesto (Genovese) | Ch. 10 |
| 10-03 | Sauce Béchamel (Mother Sauce No. 1) | Ch. 10 |
| 10-04 | Sauce Mornay (Enriched Cheese Sauce) | Ch. 10 |
| 10-05 | Classic Beurre Rouge | Ch. 10 |
| 10-06 | Classic Beurre Blanc | Ch. 10 |
| 10-07 | Master Compound Butter (Beurre Composé) | Ch. 10 |
| 10-08 | Sauce Hollandaise (Mother Sauce No. 5) | Ch. 10 |
| 10-09 | Master Mayonnaise (The Cold Mother) | Ch. 10 |
| 10-10 | Classic Remoulade | Ch. 10 |
| 10-11 | Classic Tartar Sauce | Ch. 10 |
| 10-12 | Cultured Crème Fraîche | Ch. 10 |
| 10-13 | Classic Ragù alla Bolognese | Ch. 10 |
| 10-14 | Capuliato Siciliano (Sun-Dried Tomato Pesto) | Ch. 10 |
| 10-15 | Sauce Tomate (Mother Sauce No. 4) | Ch. 10 |
| 10-16 | Sauce Velouté (Mother Sauce No. 2) | Ch. 10 |
| 10-17 | Pressure-Roasted Brown Stock (Fond Brun) | Ch. 10 |
| 10-18 | Sauce Espagnole (Mother Sauce No. 3) | Ch. 10 |
| 10-19 | Classic Demi-Glace | Ch. 10 |
| 10-20 | Ligurian Salsa di Noci (Toasted Walnut Pesto) | Ch. 10 |
| 10-21 | Lemon Cream & Parmigiano Sauce | Ch. 10 |
| 10-22 | Beurre Noisette (The Toasted Butter) | Ch. 10 |
| 10-23 | The Asian Dipping Sauce Collection | Ch. 10 |
| 11-01 | Vibrant Green Herb Oil | Ch. 11 |
| 11-02 | Quick-Process Smoked Salt | Ch. 11 |
| 11-03 | Sodium Acetate (Salt & Vinegar Crystals) | Ch. 11 |
| 11-04 | Burnt Allium Ash Salt | Ch. 11 |
| 11-05 | Nashville Fire Paste (Lipophilic Heat) | Ch. 11 |
| 12-02 | Foundation Tart Dough (Six Variants) | Ch. 12 |
| 12-03 | Pâte Brisée (Classic Shortcrust) | Ch. 12 |
| 12-04 | Pâte à Choux (The Steam Dough) | Ch. 12 |
| 12-05 | Pâte Feuilletée (Classic Puff Pastry) | Ch. 12 |
| 12-06 | Rough Puff Pastry (Demi-Feuilletée) | Ch. 12 |
| 12-07 | The "Rich Yolk" Pasta Dough (Laminated) | Ch. 12 |
| 12-08 | Gnocchi 201 (The Master Doughs) | Ch. 12 |
| 12-09 | The Definitive Guide to Egg Pasta | Ch. 12 |
| 12-10 | The Quintessential Spinach Pasta | Ch. 12 |

---

## 🖼 Banner Image Briefs

Full-bleed panoramic banners (~1920×380px WebP). Style: editorial food photography, desaturated/grayscale, cinematic aspect ratio (~5:1). Generated via Gemini Gem 2. Place in `site/public/images/`.

### Section Banners

| File | Subject | Mood | Status |
| :--- | :--- | :--- | :--- |
| `banner-academy.webp` | Close-up: copper saucepan mid-emulsification, thermometer probe, or whisk pulling a ribbon of sauce — the science of cooking in motion | Precise, analytical, controlled | ✅ Live |
| `banner-brigade.webp` | Wide shot across a kitchen pass or a row of plated dishes in sequence — the rhythm of professional service | Disciplined, energetic, serial | ✅ Live |
| `banner-larder.webp` | Aromatics, stock bones, a bouquet garni, jars of preserved goods — infrastructure before the recipe begins | Quiet, foundational, abundant | ✅ Live |

### Chapter Banners

| File | Chapter | Subject | Status |
| :--- | :--- | :--- | :--- |
| `banner-ch01.webp` | Ch. 1 — The Lab | Flames under copper, bubbling reduction, a fluid gel setting — pure technique | ✅ Live |
| `banner-ch02.webp` | Ch. 2 — The Foundation | Knives laid flat, mise en place grid, kitchen equipment arranged with precision | ✅ Live |
| `banner-ch03.webp` | Ch. 3 — Garde Manger | Sweeping diagonal cold platter — pâté, mousse, tartare, smoked salmon, giardiniera on dark wood | ✅ Live |
| `banner-ch04.webp` | Ch. 4 — The Mill | Flour-dusted bench, fresh pasta draped over a rack, bread scoring | ✅ Live |
| `banner-ch05.webp` | Ch. 5 — The Fishmonger | Whole fish on ice, or shellfish on a dark slate surface | ✅ Live |
| `banner-ch06.webp` | Ch. 6 — The Poulterer | A whole duck or chicken, skin-on, with aromatics — raw and ready | ✅ Live |
| `banner-ch07.webp` | Ch. 7 — The Butcher | Prime beef cross-section showing marbling, or butchery tools on a block | ✅ Live |
| `banner-ch08.webp` | Ch. 8 — The Field | Root vegetables, fresh herbs, earthy tones — unpretentious and whole | ✅ Live |
| `banner-ch09.webp` | Ch. 9 — The Pâtissier | Laminated dough layers, precision pastry work, clean white marble | ✅ Live |
| `banner-ch10.webp` | Ch. 10 — Stocks & Mother Sauces | Five sauce vessels in a row, or a stock reducing to a dark glaze | ⬜ Pending |
| `banner-ch11.webp` | Ch. 11 — Spice Blends & Oils | Spice blends in small bowls, oils catching light, dry ingredients arranged by hue | ⬜ Pending |
| `banner-ch12.webp` | Ch. 12 — Les Fonds | Crisp vessels and platforms arranged on a dark slate — tuile cylinders, rice crisps, croustades, a parmesan crisp cup catching light | ⬜ Pending |

### Layout

Banner sits **between the page hero text and the chapter card grid** — not above the title. Acts as an atmospheric divider with real visual weight.

```
[ Navbar ]
[ Part II · The Brigade · subtitle ]   ← existing hero
[ ────── BANNER IMAGE ─────────────]   ← full-bleed, ~400–500px tall
[ Chapter card grid ]                  ← existing grid
```

Color grading: warm sepia/copper tone. Apply a subtle dark vignette on top and bottom edges so it transitions cleanly into the cream page background.

### Implementation Notes

- Add optional `bannerImage` prop to `SectionLayout.astro`
- Banner renders after the hero `<section>` and before the chapter card grid `<div>`
- Use `object-fit: cover`, no height constraint on mobile (let it breathe), cap at ~480px on desktop
- No gradient needed on top edge — page background flows naturally; subtle gradient on bottom edge only
- The `clean_dirs` pattern in `prepare-content.py` already preserves `section-*.webp` — extend to also preserve `banner-*.webp`
- Chapter banners: same placement within each chapter's listing section (between chapter heading and recipe list)

---

## 🧠 Strategic Context & Learnings

- **Filesystem Authority**: Always scan live directories for folio numbers.
- **Scaling Nuance**: Ingredients scale linearly; reduction times do NOT (surface area constraints).
- **Formula Trust**: Use established adaptive hydration rates for pasta.
- **Tool Awareness**: Antigravity is used for local project orchestration. If unsure of its capabilities, ask.
