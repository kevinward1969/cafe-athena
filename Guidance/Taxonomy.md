# Café Athena — Controlled Vocabulary & Taxonomy

**Version:** 1.0
**Last Updated:** 2026-05-18

This is the single source of truth for all indexing field values used across:

- Folio `## Category` sections (manuscript)
- `recipes.json` entries (registry)
- Astro built files (site pipeline)
- Agent instructions (Chef agent, Claude Code)

Add new terms here first. Never define valid values anywhere else.

---

## Fields & Controlled Vocabulary

### `cuisine:`

The regional or cultural origin of the dish. Use the most specific accurate term.

| Value | Use for |
|---|---|
| `French` | Classical French technique and tradition |
| `Italian` | Italian regional cooking |
| `Japanese` | Japanese culinary tradition (washoku and modern) |
| `Korean` | Korean culinary tradition |
| `Vietnamese` | Vietnamese culinary tradition |
| `Chinese` | Chinese regional cooking |
| `Greek` | Greek and Cypriot cooking |
| `Spanish` | Spanish and Catalan cooking |
| `Indian` | Indian subcontinent cooking |
| `Middle Eastern` | Levantine, Persian, Turkish, North African cooking |
| `Mexican` | Mexican and Central American cooking |
| `Thai` | Thai culinary tradition |
| `American` | American regional cooking (Southern, BBQ, Cajun, etc.) |
| `Mediterranean` | Dishes drawing from multiple Med. traditions |
| `Asian-Fusion` | Intentional cross-cultural Asian combination |
| `Global` | Technique or component with no single cultural origin |

---

### `style:`

The register, occasion, or culinary approach. Answers: *how is this positioned?*

| Value | Use for |
|---|---|
| `Classical` | Rooted in established tradition; codified technique |
| `Modern` | Contemporary reinterpretation or new method |
| `Rustic` | Informal, hearty, country-style |
| `Fine Dining` | Restaurant-polished; plating and precision matter |
| `Competition` | Built for competition judging: bold, precise, wow-factor |
| `Brunch` | Positioned for brunch service |
| `Weeknight` | Accessible, time-efficient, everyday cooking |
| `Pastry` | Pastry and confectionery context |
| `Technique Folio` | Technique or science folio (Ch. 1–2); not a recipe |

> **Not in style:** Service formats (Tapas, Mezze, Dim Sum, Family-Style, Tasting Menu)
> belong to Part IV — The Expo (Ch. 13–15). They describe how a menu is structured,
> not what an individual recipe is.

---

### `course:`

The meal position or service role. Answers: *when/how is this served?*

| Value | Use for |
|---|---|
| `Breakfast` | Morning meal |
| `Brunch` | Late morning; brunch service |
| `Lunch` | Midday meal |
| `Dinner` | Evening meal / main service |
| `Appetizer` | Starter; plated first course |
| `Amuse-Bouche` | Single-bite pre-starter |
| `Soup` | Soup course |
| `Salad` | Salad course |
| `Side` | Accompaniment; not a standalone main |
| `Dessert` | Sweet final course |
| `Snack` | Informal; not a meal course |
| `Beverage` | Drinks |
| `Component` | Building block; not served standalone (stocks, sauces, doughs, fillings) |

---

### `dietary:`

Dietary accommodations. Optional — include only if the recipe genuinely qualifies.
Do not add speculatively or with modifications in mind.

| Value | Use for |
|---|---|
| `Vegetarian` | No meat or fish; may include dairy and eggs |
| `Vegan` | No animal products |
| `Pescatarian` | No meat; fish and seafood permitted |
| `Gluten-Free` | No gluten-containing ingredients |
| `Dairy-Free` | No dairy |
| `Keto` | Low-carb, high-fat |

---

### `cluster:`

The subcategory within a chapter. Taxonomy philosophy and full vocabulary below.

**Philosophy:** Clusters are **prescriptive** — include categories for recipes we will
cook, not only recipes we currently have. Cluster axis varies by chapter type:

- Technique chapters (1–2): science domain or skill type
- Garde Manger (3): form and presentation
- Starch chapter (4): starch base
- Protein brigade (5–7): primary protein/ingredient
- Vegetable chapter (8): primary vegetable
- Pâtissier (9): pastry form
- Building block chapters (10–12): component type

---

#### Chapter 1 — The Lab

| Cluster | Notes |
|---|---|
| `Heat & Thermodynamics` | Thermal control, reverse sear, gradient techniques |
| `Salinity & Seasoning` | Salt science, equilibrium brining |
| `Starch & Dough Science` | Baker's percentages, dextrinization, brownie method, bread architecture |
| `Emulsification & Bonding` | Emulsions, hydrocolloids, sodium citrate, mantecatura |
| `Hydrocolloids & Gels` | Spherification, fluid gels, gelation |
| `Fermentation` | Microbial fermentation, kefir, sourdough taxonomy and stewardship, lacto-fermentation |
| `Preservation & Transformation` | Vacuum compression, blanch & press, oil clarification, lipid extraction |

---

#### Chapter 2 — The Foundation

| Cluster | Notes |
|---|---|
| `Kitchen Management` | Station setup, tools, equipment, larder, sanitation, stewardship |
| `Skills` | Knife mechanics and any other hands-on technique folios added later |

---

#### Chapter 3 — Garde Manger

| Cluster | Notes |
|---|---|
| `Mousse & Pâté` | Cold-set mousses, liver pâtés, vegetarian pâtés |
| `Amuse-Bouche` | Kitchen-sent, table-presented, single bite — chef's statement, not ordered |
| `Canapé` | Passed or displayed at reception/cocktail service; finger food on a base |
| `Cold Plate` | Composed cold plates served as a plated first course |
| `Tartare & Raw` | Raw preparations: tartare, crudo, ceviche |
| `Salad` | Dressed salads served as a standalone course |
| `Preserved & Pickled` | Fermented, pickled, compressed vegetable preparations |
| `Charcuterie` | Production recipes: terrines, pâtés en croûte, galantines, aspics, rillettes — the cold station's craft. Sausage-making lives in Ch. 7 (Pork). Boards and curated presentations live in the Expo (Ch. 13–15). |

---

#### Chapter 4 — The Mill

| Cluster | Notes |
|---|---|
| `Bread` | Leavened breads: sourdough, focaccia, baguette, buns |
| `Pasta` | Fresh and dried pasta dishes |
| `Rice` | Risotto, pilaf, fried rice, rice-based dishes |
| `Gnocchi` | Potato gnocchi, Parisian gnocchi (choux-based), gnudi |
| `Polenta` | Corn-based preparations: soft, set, fried |
| `Grain & Legume` | Bulgur, farro, beans, lentils, rice-and-beans dishes |
| `Pizza` | Pizza and flatbread (future) |
| `Flatbread` | Pita, naan, lavash, crêpes (future) |

---

#### Chapter 5 — The Fishmonger

| Cluster | Notes |
|---|---|
| `Finfish` | All fin fish: cod, bass, salmon, tuna, halibut, mackerel, swordfish |
| `Mollusc` | Scallops, clams, mussels, oysters |
| `Crustacean` | Shrimp, lobster, crab, langoustine (future) |
| `Cephalopod` | Squid, octopus, cuttlefish (future) |
| `Cured & Smoked` | Gravlax, smoked fish, salt cod preparations (future) |

---

#### Chapter 6 — The Poulterer

| Cluster | Notes |
|---|---|
| `Chicken` | All chicken preparations regardless of technique |
| `Duck` | Duck confit, duck breast, duck leg preparations |
| `Turkey` | Roast, confit, braise (future) |
| `Game Bird` | Quail, pheasant, guinea fowl, squab (future) |
| `Egg` | Standalone egg preparations not covered elsewhere (future) |

---

#### Chapter 7 — The Butcher

| Cluster | Notes |
|---|---|
| `Beef` | All beef cuts: ribeye, chuck, short rib, oxtail, skirt, ground |
| `Pork` | Pork steaks, belly, shoulder, ribs, tenderloin, bacon, cured pork |
| `Lamb` | Rack, shoulder, leg, ground (future) |
| `Goat` | Braise, stew, roast (future) |
| `Veal` | Osso buco, scaloppine, roast (future) |
| `Wild Game` | Venison, rabbit, bison, boar (future) |
| `Offal` | Liver, kidney, sweetbreads, tongue, tripe (future) |

> `Charcuterie` is NOT a Ch. 7 cluster. The Butcher processes and cooks meat;
> charcuterie craft (terrines, sausages, boards) belongs to Ch. 3 Garde Manger.
> Cured/smoked items like bacon (07-12) file under their protein (`Pork`).

---

#### Chapter 8 — The Field

| Cluster | Notes |
|---|---|
| `Mushroom` | King trumpet, porcini, cremini, mixed mushroom preparations |
| `Squash` | Spaghetti squash, butternut, acorn, delicata |
| `Root Vegetable` | Celeriac, parsnip, turnip, carrot, beet |
| `Potato` | Potato in all forms: pavé, mash, crisp, roasted |
| `Corn` | Corn ribs, elotes, polenta (when in vegetable context) |
| `Grain & Bulgur` | Tabbouleh, kisir, dolma, grain salads |
| `Asparagus` | Asparagus preparations |
| `Leafy Green` | Spinach, chard, kale, escarole preparations (future) |
| `Legume` | Lentils, chickpeas, white beans as the primary (future) |
| `Tomato & Nightshade` | Tomato, eggplant, pepper as the primary (future) |
| `Allium` | Onion, leek, fennel, shallot as the primary (future) |
| `Brassica` | Cauliflower, broccoli, Brussels sprouts, cabbage (future) |

---

#### Chapter 9 — The Pâtissier

| Cluster | Notes |
|---|---|
| `Brownie & Bar` | Brownies, blondies, bar cookies |
| `Cookie` | All dropped, rolled, or piped cookies |
| `Cake` | Layer cakes, sheet cakes, bundt (future) |
| `Tart` | Tarts and tartlets; shell sourced from Ch. 12 |
| `Choux` | Éclairs, profiteroles, Paris-Brest, choux au craquelin (future) |
| `Canelé` | Canelés de Bordeaux |
| `Posset & Panna Cotta` | Set creams: posset, panna cotta, bavarian (future) |
| `Frozen Dessert` | Ice cream, sorbet, semifreddo (future) |
| `Bread Pudding` | Custard-soaked bread desserts (future) |
| `Confection` | Truffles, bonbons, caramels, nougat (future) |

---

#### Chapter 10 — Stocks & Mother Sauces

| Cluster | Notes |
|---|---|
| `Stock` | All stocks: white, brown, fish, vegetable |
| `Mother Sauce` | The five classic French mother sauces |
| `Derivative Sauce` | Sauces derived from mother sauces |
| `Pan Sauce` | Deglazing-based sauces (future) |
| `Pesto` | Nut-and-herb pounded or blended sauces |
| `Compound Butter` | Flavored butters: beurre composé, noisette |
| `Emulsion` | Cold emulsions: mayo, aioli, vinaigrette; warm: beurre blanc |
| `Ragù` | Slow-cooked meat sauces |
| `Dipping Sauce` | Table sauces and dipping preparations |
| `Cream Sauce` | Dairy-based finishing sauces |

---

#### Chapter 11 — Spice Blends & Oils

| Cluster | Notes |
|---|---|
| `Herb Oil` | Chlorophyll-stabilized herb oils |
| `Finishing Oil` | Infused oils for plating and flavor (future) |
| `Specialty Salt` | Smoked salts, flavored salts, crystallized acids |
| `Paste & Blend` | Spice pastes, dry rubs, compound seasonings |
| `Spice Rub` | Dry rubs for smoking and grilling (future) |

---

#### Chapter 12 — Les Fonds

| Cluster | Notes |
|---|---|
| `Platform & Vessel` | Crispy rice, tuile cylinders, frico — structural bases |
| `Pastry Dough` | Tart doughs, shortcrust, pâte à choux, puff, rough puff |
| `Pasta Dough` | Egg pasta, laminated pasta, spinach pasta, gnocchi doughs |
| `Cream & Filling` | Crème pâtissière, meringues, Chantilly, composite creams, curd |
| `Garnish & Component` | Caviar (seeds/spheres), confit tomatoes, garlic crisps |
| `Batter & Coating` | Dustings, dredges, panés, starch batters |
| `Caramel & Sugar` | Dry caramel, wet caramel, sugar work |

---

## Usage Notes

### Mandatory fields

Every finished recipe folio must have: `cuisine`, `style`, `cluster`, `course`
Technique folios (style: `Technique Folio`) may omit `course`.

### Optional fields

`dietary` — only if the recipe genuinely qualifies without modification.

### Adding new values

1. Add the term to this file with a description
2. Update `Guidance/Recipe-Format-Standard.md` if the field vocabulary is listed there
3. Commit with message: `chore(taxonomy): add [field] value "[term]"`
4. Do not use the new term in a folio until it is committed here

### Validation

`audit.py --sync-metadata` will flag any Category field values not found in this file.
