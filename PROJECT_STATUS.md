# Café Athena - Project Status & Active Context

Last Updated: 2026-04-08

## 🎯 Active Development

| Folio | Title | Status | Notes |
| :--- | :--- | :--- | :--- |
| **10-21** | Lemon Cream & Parmigiano Sauce | Completed | Indexed. |
| **04-16** | Definitive Guide to Egg Pasta | Completed | Indexed. |

## 🌅 On the Horizon

- **Home Page Copy — 3 Main Area Descriptions**: ✅ Completed 2026-04-08.
- **Glossary Letter Navigation Fix**: ✅ Completed 2026-04-08.
- **Academy Section Randomizer (Home Page)**: ✅ Completed 2026-04-08.
- **Featured Recipe Randomizer (Home Page)**: ✅ Completed 2026-04-08.
- **Food Critic / Food Writer Agent**: Create a new Claude Code agent for creative and marketing copy — editorial, journalistic, blog posts, social media. Separate surface from the Chef agent.
- **Section & Chapter Banner Images**: Full-bleed panoramic banners (~1920×380px WebP) for each section page and each chapter. Generated via Gemini Gem 2. See image briefs below. Implementation: add optional `bannerImage` prop to `SectionLayout.astro`. Naming: `banner-academy.webp`, `banner-brigade.webp`, `banner-larder.webp`, `banner-ch03.webp` … `banner-ch11.webp`. All placed in `site/public/images/`.

- **Glossary Workflow**: Automated terminology extraction from recipes with duplicate prevention and A-Z sorting. Track progress via `glossaryPull` in `recipes.json` — 72 entries pending.
- **Glossary Audit**: Fixing structural issues, malformed headers, and alphabetization errors in the main glossary. Run after glossary pull backlog is cleared.

---

## 🔧 Site & Asset Maintenance

### Hero Image Progress

Hero image status is tracked per-recipe in `recipes.json` via `heroImage` and `heroImageOptimized` stages. Use `/sync-registry` to refresh.

**Next hero image batch:** 02-05, 02-06, 02-07 (The Larder, The Steward, Sanitation & HACCP)

---

### Glossary Pull — Missing Entries

Tracked in `recipes.json` via `glossaryPull` stage. **72 entries remaining** (Chapters 1–7, plus any new additions). Chapters 8–11 are complete.

Run `/glossary-pull [id]` for each pending entry. Check status with:

```
python3 -c "import json; d=json.load(open('recipes.json')); [print(r['id']) for r in d['recipes'] if not r['stages'].get('glossaryPull')]"
```

---

### Format Audit — Full Cookbook

Run `/format-audit Chapter N` across all chapters to validate every recipe and folio against `Recipe-Format-Standard.md`. Includes structural order, Mise En Place compliance, Keywords, and Category sections.

| Chapter | Status |
| :--- | :--- |
| Chapter 1 - The Lab | Pending |
| Chapter 2 - The Foundation | Pending |
| Chapter 3 - Garde Manger | Pending |
| Chapter 4 - The Mill | Pending |
| Chapter 5 - The Fishmonger | Pending |
| Chapter 6 - The Poulterer | Pending |
| Chapter 7 - The Butcher | Pending |
| Chapter 8 - The Field | Pending |
| Chapter 9 - The Pâtissier | Pending |
| Chapter 10 - Stocks & Mother Sauces | Pending |
| Chapter 11 - Spice Blends & Oils | Pending |

### PNG → WebP Optimization

Run `/recipe-hero-image optimize all` to convert all PNGs in chapter folders to WebP in one pass.

| File | Chapter | Status |
| :--- | :--- | :--- |
| 01-01.png | Chapter 1 | Pending |
| 01-02.png | Chapter 1 | Pending |
| 01-03.png | Chapter 1 | Pending |
| 01-04.png | Chapter 1 | Pending |
| 01-05.png | Chapter 1 | Pending |
| 03-01.png | Chapter 3 | Pending |
| 03-03.png | Chapter 3 | Pending |
| 03-04.png | Chapter 3 | Pending |
| 03-05.png | Chapter 3 | Pending |
| 05-01.png | Chapter 5 | Pending |
| 05-02.png | Chapter 5 | Pending |
| 06-01.png | Chapter 6 | Pending |
| 06-03.png | Chapter 6 | Pending |
| 06-04.png | Chapter 6 | Pending |
| 07-01.png | Chapter 7 | Pending |
| 07-02.png | Chapter 7 | Pending |
| 07-03.png | Chapter 7 | Pending |
| 07-04.png | Chapter 7 | Pending |
| 07-05.png | Chapter 7 | Pending |
| 07-06.png | Chapter 7 | Pending |
| 07-07.png | Chapter 7 | Pending |
| 07-08.png | Chapter 7 | Pending |
| 07-09.png | Chapter 7 | Pending |

### Hero Image Generation — Missing Entries (~85 total)

Use `/recipe-hero-image [index]` for each. Chapters with zero coverage are highest priority.

| Index | Title | Chapter | Status |
| :--- | :--- | :--- | :--- |
| 02-01 | The Kitchen Cockpit (Station Management) | Ch. 2 | Pending |
| 02-02 | The Kit (Analog Tools) | Ch. 2 | Pending |
| 02-03 | The Machine Shop (Electrics) | Ch. 2 | Pending |
| 02-04 | Knife Mechanics (The Geometry of the Cut) | Ch. 2 | Pending |
| 02-05 | The Larder (Inventory & Storage) | Ch. 2 | Pending |
| 02-06 | The Steward (Care & Maintenance) | Ch. 2 | Pending |
| 02-07 | Sanitation & HACCP (The Defense) | Ch. 2 | Pending |
| 03-02 | Mini Boursin & Bacon Meatballs | Ch. 3 | Pending |
| 03-06 | Vacuum-Infused Market Pickles | Ch. 3 | ✅ Deployed |
| 03-07 | Silky Chicken Liver Mousse | Ch. 3 | ✅ Deployed |
| 03-08 | Sous Vide Chicken Liver Mousse | Ch. 3 | ✅ Deployed |
| 03-09 | Winter Citrus & Shaved Fennel Salad | Ch. 3 | ✅ Deployed |
| 03-10 | Velvet Mushroom Mousse | Ch. 3 | ✅ Deployed |
| 03-11 | Double Deviled Eggs (Le Jambon) | Ch. 3 | ✅ Deployed |
| 03-12 | Deviled Ham & Cognac Mousse | Ch. 3 | ✅ Deployed |
| 03-13 | Calf Liver & Duck Fat Mousse | Ch. 3 | ✅ Deployed |
| 04-01 | 80:20 Poolish-Sourdough Baguettes | Ch. 4 | Pending |
| 04-02 | Risotto alla Milanese | Ch. 4 | Pending |
| 04-03 | Risotto of White Mushrooms | Ch. 4 | Pending |
| 04-04 | Stabilized Cacio e Pepe | Ch. 4 | Pending |
| 04-05 | The Rich Yolk Pasta Dough (Laminated) | Ch. 4 | Pending |
| 04-06 | High-Hydration Focaccia (The 85% Method) | Ch. 4 | Pending |
| 04-07 | Pressure-Gelatinized Polenta | Ch. 4 | Pending |
| 04-08 | Parisian Gnocchi (Pâte à Choux) | Ch. 4 | Pending |
| 04-09 | Calabrian Chili & Red Pepper Cavatappi | Ch. 4 | Pending |
| 04-10 | Pressure-Gelatinized Polenta (The BBQ Pitmaster) | Ch. 4 | Pending |
| 04-11 | Gnocchi 201 (The Master Doughs) | Ch. 4 | Pending |
| 04-12 | Pasta e Patate (Napoli Style) | Ch. 4 | Pending |
| 04-13 | Same-Day Sourdough Discard Focaccia | Ch. 4 | Pending |
| 04-14 | The Companion Louisiana-Style Black Beans & Rice | Ch. 4 | Pending |
| 04-15 | Prosciutto Balanzoni | Ch. 4 | Pending |
| 04-16 | The Definitive Guide to Egg Pasta | Ch. 4 | Pending |
| 04-17 | The Quintessential Spinach Pasta | Ch. 4 | Pending |
| 04-18 | Sourdough Hybrid Spoon Buns | Ch. 4 | Pending |
| 06-02 | Wafu Wedding Soup (Kyoto Spice) | Ch. 6 | Pending |
| 06-05 | Louisiana Blackened Chicken Pasta | Ch. 6 | Pending |
| 06-06 | Modern Chicken Pot Pie (Velouté Method) | Ch. 6 | Pending |
| 07-10 | The Competition Red Texas-Style Chili | Ch. 7 | Pending |
| 07-10.2 | The Competition Red Texas-Style Chili (v2) | Ch. 7 | Pending |
| 07-11 | Pressure-Braised Chuck Roast | Ch. 7 | Pending |
| 07-12 | Dehydrator Bacon (Four Ways) | Ch. 7 | Pending |
| 08-01 | King Trumpet Scallops & Celeriac Mousseline | Ch. 8 | Pending |
| 08-02 | Roasted Spaghetti Squash Pomodoro Rustico | Ch. 8 | Pending |
| 08-03 | Velvet Root Vegetable Mash | Ch. 8 | Pending |
| 08-04 | St. Louis Style Kisir (Red Hot Bulgur) | Ch. 8 | Pending |
| 08-05 | Modern Tabbouleh (The Acid Cutter) | Ch. 8 | Pending |
| 08-06 | Onion Potato Crisps | Ch. 8 | Pending |
| 09-01 | Brown Butter & Miso-Caramel Truffle Brownies | Ch. 9 | Pending |
| 09-02 | Spicy Brown Butter & Lemon Cheesecake Cookies | Ch. 9 | Pending |
| 09-03 | Sesame Tuile Cylinders | Ch. 9 | Pending |
| 09-04 | Pâte à Choux (The Steam Dough) | Ch. 9 | Pending |
| 09-05 | Pâte Feuilletée (Classic Puff Pastry) | Ch. 9 | Pending |
| 09-06 | Pâte Brisée (Classic Shortcrust) | Ch. 9 | Pending |
| 09-07 | Pâte Sucrée (Sweet Tart Dough) | Ch. 9 | Pending |
| 09-08 | Rough Puff Pastry (Demi-Feuilletée) | Ch. 9 | Pending |
| 09-09 | Pâte Sablée (Rich Shortbread Crust) | Ch. 9 | Pending |
| 09-10 | Spicy Brown Butter & Lemon Cheesecake Cookies (v2) | Ch. 9 | Pending |
| 09-11 | Brandy-Infused Canelés de Bordeaux | Ch. 9 | Pending |
| 10-01 | High-Pressure White Chicken Stock | Ch. 10 | Pending |
| 10-02 | Vibrant Basil Pesto (Genovese) | Ch. 10 | Pending |
| 10-03 | Sauce Béchamel (Mother Sauce No. 1) | Ch. 10 | Pending |
| 10-04 | Sauce Mornay (Enriched Cheese Sauce) | Ch. 10 | Pending |
| 10-05 | Classic Beurre Rouge | Ch. 10 | Pending |
| 10-06 | Classic Beurre Blanc | Ch. 10 | Pending |
| 10-07 | Master Compound Butter (Beurre Composé) | Ch. 10 | Pending |
| 10-08 | Sauce Hollandaise (Mother Sauce No. 5) | Ch. 10 | Pending |
| 10-09 | Master Mayonnaise (The Cold Mother) | Ch. 10 | Pending |
| 10-10 | Classic Remoulade | Ch. 10 | Pending |
| 10-11 | Classic Tartar Sauce | Ch. 10 | Pending |
| 10-12 | Cultured Crème Fraîche | Ch. 10 | Pending |
| 10-13 | Classic Ragù alla Bolognese | Ch. 10 | Pending |
| 10-14 | Capuliato Siciliano (Sun-Dried Tomato Pesto) | Ch. 10 | Pending |
| 10-15 | Sauce Tomate (Mother Sauce No. 4) | Ch. 10 | Pending |
| 10-16 | Sauce Velouté (Mother Sauce No. 2) | Ch. 10 | Pending |
| 10-17 | Pressure-Roasted Brown Stock (Fond Brun) | Ch. 10 | Pending |
| 10-18 | Sauce Espagnole (Mother Sauce No. 3) | Ch. 10 | Pending |
| 10-19 | Classic Demi-Glace | Ch. 10 | Pending |
| 10-20 | Ligurian Salsa di Noci (Toasted Walnut Pesto) | Ch. 10 | Pending |
| 10-21 | Lemon Cream & Parmigiano Sauce | Ch. 10 | Pending |
| 10-22 | Beurre Noisette (The Toasted Butter) | Ch. 10 | Pending |
| 10-23 | The Asian Dipping Sauce Collection | Ch. 10 | Pending |
| 11-01 | Vibrant Green Herb Oil | Ch. 11 | Pending |
| 11-02 | Quick-Process Smoked Salt | Ch. 11 | Pending |
| 11-03 | Sodium Acetate (Salt & Vinegar Crystals) | Ch. 11 | Pending |
| 11-04 | Burnt Allium Ash Salt | Ch. 11 | Pending |
| 11-05 | Nashville Fire Paste (Lipophilic Heat) | Ch. 11 | Pending |

---

## 🖼 Banner Image Briefs

Full-bleed panoramic banners (~1920×480px WebP). Cinematic aspect ratio (~4:1). Generated via Gemini Gem 2. Place in `site/public/images/`.

### Color Grade System

Each section has a distinct color grade that carries through all its chapter banners — functioning as visual wayfinding.

| Section | Chapters | Grade | Character |
| :--- | :--- | :--- | :--- |
| **The Academy** | Ch. 1–2 | **Cool silver-blue** — desaturated with a slight blue-grey cast | Clinical, precise, intellectual |
| **The Brigade** | Ch. 3–9 | **Warm copper-sepia** — confirmed in Photoshop mockup | Heat, craft, kitchen energy |
| **The Larder** | Ch. 10–11 | **Deep amber-gold** — richer and darker than Brigade, almost candlelit | Slow-cooked, foundational, pantry depth |

Generate each section as a batch with the same grade instruction to ensure consistency across all images in that section.

### Section Banners

| File | Subject | Mood |
| :--- | :--- | :--- |
| `banner-academy.webp` | Close-up: copper saucepan mid-emulsification, thermometer probe, or whisk pulling a ribbon of sauce — the science of cooking in motion | Precise, analytical, controlled |
| `banner-brigade.webp` | Wide shot across a kitchen pass or a row of plated dishes in sequence — the rhythm of professional service | Disciplined, energetic, serial |
| `banner-larder.webp` | Aromatics, stock bones, a bouquet garni, jars of preserved goods — infrastructure before the recipe begins | Quiet, foundational, abundant |

### Chapter Banners

| File | Chapter | Subject |
| :--- | :--- | :--- |
| `banner-ch01.webp` | Ch. 1 — The Lab | Flames under copper, bubbling reduction, a fluid gel setting — pure technique |
| `banner-ch02.webp` | Ch. 2 — The Foundation | Knives laid flat, mise en place grid, kitchen equipment arranged with precision |
| `banner-ch03.webp` | Ch. 3 — Garde Manger | A terrine sliced to reveal layers, or a cold platter of terrines and mousse |
| `banner-ch04.webp` | Ch. 4 — The Mill | Flour-dusted bench, fresh pasta draped over a rack, bread scoring |
| `banner-ch05.webp` | Ch. 5 — The Fishmonger | Whole fish on ice, or shellfish on a dark slate surface |
| `banner-ch06.webp` | Ch. 6 — The Poulterer | A whole duck or chicken, skin-on, with aromatics — raw and ready |
| `banner-ch07.webp` | Ch. 7 — The Butcher | Prime beef cross-section showing marbling, or butchery tools on a block |
| `banner-ch08.webp` | Ch. 8 — The Field | Root vegetables, fresh herbs, earthy tones — unpretentious and whole |
| `banner-ch09.webp` | Ch. 9 — The Pâtissier | Laminated dough layers, precision pastry work, clean white marble |
| `banner-ch10.webp` | Ch. 10 — Stocks & Mother Sauces | Five sauce vessels in a row, or a stock reducing to a dark glaze |
| `banner-ch11.webp` | Ch. 11 — Spice Blends & Oils | Spice blends in small bowls, oils catching light, dry ingredients arranged by hue |

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
