# Café Athena — Controlled Vocabulary & Taxonomy

**Version:** 1.1
**Last Updated:** 2026-05-20

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
| `Middle Eastern` | Multi-tradition Middle Eastern dishes; use a sub-cuisine below when the origin is specific |
| `Turkish` | Turkish culinary tradition (sub-cuisine of Middle Eastern) |
| `Lebanese` | Lebanese culinary tradition (sub-cuisine of Middle Eastern) |
| `Persian` | Persian/Iranian culinary tradition (sub-cuisine of Middle Eastern) |
| `Moroccan` | Moroccan culinary tradition (sub-cuisine of Middle Eastern) |
| `North African` | Broader North African cooking not specific to Morocco (sub-cuisine of Middle Eastern) |
| `Mexican` | Mexican and Central American cooking |
| `Latin American` | Caribbean and South American cooking (Puerto Rican, Dominican, Cuban, Colombian, etc.) |
| `Thai` | Thai culinary tradition |
| `American` | Multi-regional American cooking; use a sub-cuisine below when the origin is specific |
| `Southern` | American Southern cooking (sub-cuisine of American) |
| `Cajun` | Cajun and Creole cooking (sub-cuisine of American) |
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
| `Modernist` | Molecular gastronomy and modernist techniques: spherification, fluid gels, hydrocolloids, precision chemistry |
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

### `family:`

The subcategory within a chapter. Taxonomy philosophy and full vocabulary below.

**Philosophy:** Families are **prescriptive** — include categories for recipes we will
cook, not only recipes we currently have. Family axis varies by chapter type:

- Technique chapters (1–2): science domain or skill type
- Garde Manger (3): form and presentation
- Starch chapter (4): starch base
- Protein brigade (5–7): primary protein/ingredient
- Vegetable chapter (8): primary vegetable
- Pâtissier (9): pastry form
- Building block chapters (10–12): component type

---

#### Chapter 1 — The Lab

| Family | Notes |
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

| Family | Notes |
|---|---|
| `Kitchen Management` | Station setup, tools, equipment, larder, sanitation, stewardship |
| `Skills` | Knife mechanics and any other hands-on technique folios added later |

---

#### Chapter 3 — Garde Manger

| Family | Notes |
|---|---|
| `Mousse & Pâté` | Cold-set mousses, liver pâtés, vegetarian pâtés |
| `Amuse-Bouche` | Kitchen-sent, table-presented, single bite — chef's statement, not ordered |
| `Canapé` | Passed or displayed at reception/cocktail service; finger food on a base |
| `Cold Plate` | Composed cold plates served as a plated first course — includes tartare, crudo, ceviche |
| `Salad` | Dressed salads served as a standalone course |
| `Preserved & Pickled` | Fermented, pickled, compressed vegetable preparations |
| `Charcuterie` | Production recipes: terrines, pâtés en croûte, galantines, aspics, rillettes — the cold station's craft. Sausage-making lives in Ch. 7 (Pork). Boards and curated presentations live in the Expo (Ch. 13–15). |

---

#### Chapter 4 — The Mill

| Family | Notes |
|---|---|
| `Bread` | Leavened breads: sourdough, focaccia, baguette, buns |
| `Pasta` | Fresh and dried pasta dishes |
| `Rice` | Risotto, pilaf, fried rice, rice-based dishes |
| `Polenta` | Corn-based preparations: soft, set, fried |
| `Grain & Legume` | Bulgur, farro, beans, lentils, rice-and-beans dishes |
| `Pizza` | Pizza and flatbread (future) |
| `Flatbread` | Pita, naan, lavash, crêpes (future) |

---

#### Chapter 5 — The Fishmonger

| Family | Notes |
|---|---|
| `Finfish` | All fin fish: cod, bass, salmon, tuna, halibut, mackerel, swordfish |
| `Mollusc` | Scallops, clams, mussels, oysters |
| `Crustacean` | Shrimp, lobster, crab, langoustine (future) |
| `Cephalopod` | Squid, octopus, cuttlefish (future) |
| `Cured & Smoked` | Gravlax, smoked fish, salt cod preparations (future) |

---

#### Chapter 6 — The Poulterer

| Family | Notes |
|---|---|
| `Chicken` | All chicken preparations regardless of technique |
| `Duck` | Duck confit, duck breast, duck leg preparations |
| `Turkey` | Roast, confit, braise (future) |
| `Game Bird` | Quail, pheasant, guinea fowl, squab (future) |
| `Egg` | Standalone egg preparations not covered elsewhere (future) |

---

#### Chapter 7 — The Butcher

| Family | Notes |
|---|---|
| `Beef` | All beef cuts: ribeye, chuck, short rib, oxtail, skirt |
| `Pork` | Pork steaks, belly, shoulder, ribs, tenderloin, bacon, cured pork |
| `Lamb` | Rack, shoulder, leg (future) |
| `Goat` | Braise, stew, roast (future) |
| `Veal` | Osso buco, scaloppine, roast (future) |
| `Wild Game` | Venison, rabbit, bison, boar (future) |
| `Offal` | Liver, kidney, sweetbreads, tongue, tripe (future) |
| `Ground & Formed` | Meatballs, sausage, burgers, kofta, gyro (lamb/beef), shawarma (lamb) — protein secondary to form |

> `Charcuterie` is NOT a Ch. 7 family. The Butcher processes and cooks meat;
> charcuterie craft (terrines, sausages, boards) belongs to Ch. 3 Garde Manger.
> Cured/smoked items like bacon (07-12) file under their protein (`Pork`).
> Chicken gyro/shawarma files under Ch. 6 `Chicken`.

---

#### Chapter 8 — The Field

Families are organized by primary ingredient. Technique is secondary — it belongs in keywords.

| Family | Notes |
|---|---|
| `Tuber` | Starchy underground veg: potato, sweet potato, sunchoke, taro, yuca, yam |
| `Root Vegetable` | Lower-starch roots: carrot, parsnip, celeriac, beet, turnip, radish |
| `Squash & Gourd` | Spaghetti squash, butternut, delicata, zucchini, pumpkin |
| `Corn` | Corn ribs, elotes, charred corn, corn-forward vegetable preparations |
| `Stalk & Shoot` | Asparagus, artichoke, celery, fennel stalks |
| `Mushroom` | All fungi: king trumpet, porcini, cremini, mixed mushroom preparations |
| `Leafy Green` | Spinach, chard, kale, escarole, grape leaves, dolma |
| `Allium` | Onion, leek, fennel, shallot as the primary |
| `Brassica` | Cauliflower, broccoli, Brussels sprouts, cabbage |
| `Tomato & Nightshade` | Tomato, eggplant, pepper as the primary |
| `Legume` | Lentils, chickpeas, white beans as the primary |
| `Grain Salad` | Grain-forward salads in a vegetable context: tabbouleh, kisir, herb-grain salads |

---

#### Chapter 9 — The Pâtissier

| Family | Notes |
|---|---|
| `Brownie & Bar` | Brownies, blondies, bar cookies |
| `Cookie` | All dropped, rolled, or piped cookies |
| `Cake` | Layer cakes, sheet cakes, bundt (future) |
| `Small Cake & Pastry` | Canelé, financier, madeleine, kouglof, friand — individually portioned baked items |
| `Tart` | Tarts and tartlets; shell sourced from Ch. 12 |
| `Choux` | Éclairs, profiteroles, Paris-Brest, choux au craquelin (future) |
| `Custard & Baked Cream` | Baked egg-set cream preparations: crème brûlée, pot de crème, clafoutis, flan |
| `Posset & Panna Cotta` | Set creams: posset, panna cotta, bavarian (future) |
| `Frozen Dessert` | Ice cream, sorbet, semifreddo (future) |
| `Bread Pudding` | Custard-soaked bread desserts (future) |
| `Confection` | Truffles, bonbons, caramels, nougat (future) |

---

#### Chapter 10 — Stocks, Sauces & Condiments

| Family | Notes |
|---|---|
| `Stock` | All stocks: white, brown, fish, vegetable |
| `Mother Sauce` | The five classic French mother sauces |
| `Derivative Sauce` | Sauces derived from mother sauces; includes slow-cooked meat sauces (bolognese, ragù) |
| `Pan Sauce` | Deglazing-based sauces (future) |
| `Jus & Reduction` | Reduced stocks, wine reductions, natural meat juices (future) |
| `Cold Blended Sauce` | Pesto, chimichurri, salsa verde, romesco — oil-based, blended, served cold |
| `Compound Butter` | Flavored butters: beurre composé, noisette |
| `Emulsion` | Stable emulsions — cold: mayo, aioli, vinaigrette; warm: hollandaise, beurre blanc |
| `Dipping Sauce` | Table sauces and dipping preparations |
| `Cream Sauce` | Dairy-based finishing sauces |
| `Salsa & Fresh Sauce` | Raw or minimally cooked fresh sauces: pico, salsa cruda (future) |
| `Vinaigrette` | Dressed, oil-and-acid preparations served cold (future) |

---

#### Chapter 11 — Spice Blends, Oils & Pastes

| Family | Notes |
|---|---|
| `Herb Oil` | Chlorophyll-stabilized fresh herb oils: basil, parsley, chive |
| `Infused Oil` | Aromatics-, spice-, or allium-infused oils: garlic, chili, truffle (future) |
| `Dry Spice Blend` | Spice-forward dry blends: smoked red pepper blend, ras el hanout, baharat |
| `Dry Herb Blend` | Herb-forward dry blends: herbes de Provence, za'atar, Italian seasoning, fines herbes |
| `Fresh Herb Blend` | Fresh-herb preparations: gremolata, persillade, chermoula, salmoriglio |
| `Specialty Salt` | Smoked salts, flavored salts, crystallized acids, ash salts |
| `Wet Paste` | Wet spice pastes: Nashville fire paste, harissa, berbere paste |
| `Spice Rub` | Dry rubs for smoking, grilling, and crusting (future) |
| `Vinegar & Acid` | Flavored vinegars, shrubs, acidulated preparations (future) |

---

#### Chapter 12 — Les Fonds

| Family | Notes |
|---|---|
| `Platform & Vessel` | Structural bases and edible vessels: crispy rice, frico, tuile cylinders |
| `Pastry Dough` | Tart doughs, shortcrust, pâte à choux, puff, rough puff |
| `Pasta Dough` | Egg pasta, laminated pasta, spinach pasta |
| `Cream & Filling` | Crème pâtissière, meringues, Chantilly, composite creams, curds |
| `Garnish & Component` | Caviar (seeds/spheres), confit tomatoes, garlic crisps — finishing elements |
| `Batter & Coating` | Dustings, dredges, panés, starch batters, frying coatings |
| `Caramel & Sugar` | Dry caramel, wet caramel, toffee, sugar work |
| `Bread Component` | Breadcrumbs (pangrattato), croutons, panade, toasted bread elements |
| `Pickle & Quick Preserve` | Quick pickles, acidulated preparations, brined components used across recipes |
| `Glaze & Reduction` | Glazes, balsamic reductions, wine reductions used as finishing components |
| `Gel & Aspic` | Gelatin-set components: aspic, gelée, fluid gel used in plating or terrines |

---

## Usage Notes

### Mandatory fields

Every finished recipe folio must have: `cuisine`, `style`, `family`, `course`
Technique folios (style: `Technique Folio`) may omit `course`.

### Optional fields

`dietary` — only if the recipe genuinely qualifies without modification.

### Multiple values

One value per field — this is the forcing function that makes the taxonomy useful.
If a recipe feels like it belongs in two families, the vocabulary needs a better term,
or the nuance belongs in `keywords:`.

**Exception — `dietary:`** supports comma-separated values because dietary attributes
are orthogonal flags, not mutually exclusive categories:

```
dietary: Vegetarian, Gluten-Free
```

**`keywords:`** is the designed catch-all for cross-cutting attributes — technique
names, specific dish names, occasions, ingredient details, etc.

### Adding new values

1. Add the term to this file with a description
2. Update `Guidance/Recipe-Format-Standard.md` if the field vocabulary is listed there
3. Commit with message: `chore(taxonomy): add [field] value "[term]"`
4. Do not use the new term in a folio until it is committed here

### Validation

`audit.py --sync-metadata` will flag any Category field values not found in this file.
