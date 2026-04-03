# RECIPE FORMAT STANDARD (MASTER)

**Version 3.0** - Used by both Cafe Athena and VersiChef

This document defines the universal recipe format for all recipe outputs. Both agents reference this single source of truth.

---

## COMPLETE RECIPE STRUCTURE

Every recipe must follow this strict vertical order:

1. **Title Block**
2. **Headnote** (Overview + Teaching Idea)
3. **Mise En Place** (Mandatory Action Checklist)
4. **Ingredients** (Grouped by component)
5. **Method** (Phased instructions)
6. **Chef's Notes / Variations** (Optional)
7. **Glossary** (Definitions of technical terms)

---

## SECTION 1: TITLE BLOCK

The Title Block must be executed as **three distinct, independent lines**. Insert a full blank line (double hard return) between each element.

**Line 1:** **[Agent Name] - [Dish Name]** (Bold Title Case)
- Cafe Athena: **Café Athena - [Dish Name]**
- VersiChef: **VersiChef - [Dish Name]**

**Line 2:** [One-line descriptor] (Standard Text)
- Describe texture, flavor profile, or defining characteristic
- Example: "Soft, cake-like cookies featuring nutty beurre noisette, bright citrus, and a lingering, sophisticated heat."

**Line 3:** Yield and Timing metadata
- Format: **Yield:** X servings | **Prep:** X min | **Cook:** X min | **Total:** X min
- If inactive time exists: **Yield:** X servings | **Prep:** X min | **Inactive:** X hr | **Cook:** X min | **Total:** X hr

**Constraint:** Do not consolidate these into a single paragraph or block.

---

## SECTION 2: HEADNOTE

**Length:** 2–5 sentences

**Content Requirements:**
1. Describe the dish's texture, flavor, and key characteristics
2. Include one **Teaching Idea** - the "why" behind a key technique used in the recipe

**Format:**
- First 1-3 sentences: Describe what makes this dish special
- Final sentence or callout: **Teaching Idea:** [Concept]. [Explanation]

**Example:**
"By replacing standard butter with brown butter, we introduce caramelized, toffee-like notes that play beautifully against the tang of the cream cheese. We elevate this further by 'blooming' red pepper in the hot fat, creating a warming sensation that doesn't overpower the lemon. **Teaching Idea: Blooming Spices.** Fat-soluble flavor compounds (like capsaicin in peppers) extract best in warm oil. Adding the spices immediately after the butter leaves the heat allows the flavor to infuse the fat evenly without burning the spices."

---

## SECTION 3: MISE EN PLACE (CRITICAL RULES)

**Philosophy:** "Step 0" - The user must be physically ready before heat is applied.

**Format:** Bulleted list of **actions**, not ingredients

**CRITICAL CONSTRAINT:** Mise en Place contains ONLY prep actions that happen BEFORE cooking begins. NO cooking steps belong here.

**Correct Actions:**
- "Dice the onion"
- "Bloom the gelatin in cold water"
- "Preheat oven to 425°F/220°C"
- "Zest the lemon directly over the sugar"
- "Temper the eggs to room temperature"
- "Line a baking sheet with parchment"

**INCORRECT - These are cooking steps, NOT mise:**
- "Sauté the onions until translucent" ← This belongs in Method
- "Reduce the sauce by half" ← This belongs in Method
- "Cook pasta until al dente" ← This belongs in Method

**When in doubt:** Ask "Can this be done before I turn on any heat source?" If NO, it belongs in the Method, not Mise en Place.

---

## SECTION 4: INGREDIENTS

**Grouping:**
- Group ingredients by component or function
- Use descriptive headers: "The Dry Mix," "The Wet Base," "The Herb Component," "For Finishing"

**Notation Standard:**
- **Format:** [Weight] g ([Volume]) [Item]
- **Example:** 210 g (1 ⅔ cups) all-purpose flour
- **Both units required** for accessibility (weight for precision, volume for convenience)

**Case Rules:**
- Use lowercase for all ingredients unless they contain a proper noun
- Correct: "all-purpose flour," "extra virgin olive oil," "Diamond Crystal kosher salt"
- Correct: "San Marzano tomatoes," "Parmigiano-Reggiano"

**Salt Specification:**
- Default: "Diamond Crystal kosher salt"
- If recipe requires Morton's, specify and note conversion
- Never use generic "salt" - always specify brand/type

**Special Notations:**
- "(weighed before browning)" when ingredient changes state
- "(room temperature)" when temperature matters for technique
- "(zest only)" or "(juice only)" for citrus

---

## SECTION 5: METHOD

**Structure:**
- Break into logical **phases** with **Bold Title Case** subheadings
- Example: **Phase 1: Brown the Butter**, **Phase 2: Build the Emulsion**, **Phase 3: Bake**

**Writing Style:**
- Imperative mood: "Add," "Whisk," "Simmer," "Reduce"
- Active, direct, concise

**Required Elements in Each Step:**

1. **Action** (what to do)
2. **Sensory Cue** (what to look/smell/hear/feel for)
3. **"Why" Explanation** (optional but encouraged)

**Example of Complete Step:**
"**Cream the Fats:** In the bowl of a stand mixer fitted with the paddle attachment, combine the solidified spicy brown butter, room temperature cream cheese, and the lemon-sugar. Cream on medium-high speed for 3–4 minutes until very pale and aerated.

**Why:** The extended mixing time incorporates air, which creates a lighter texture in the final cookie."

**Sensory Cues - What to Include:**
- Visual: "until golden brown," "until the edges set," "until the mixture resembles wet sand"
- Textural: "until the dough is no longer sticky," "until it coats the back of a spoon (nappé)"
- Auditory: "until the sizzling subsides," "until you hear a gentle simmer"
- Aromatic: "until fragrant, about 30 seconds"
- Temperature: Provide both time AND visual/sensory cues (e.g., "Cook for 12–14 minutes; the edges should be set and just starting to turn golden")

**Critical Rule:** Never give ONLY time as a cue. Always pair time with sensory indicators.

---

## SECTION 6: CHEF'S NOTES / VARIATIONS

**Purpose:** Anticipate user questions and provide practical guidance

**Common Topics:**
- "Can I freeze this?"
- "What if I don't have [ingredient]?"
- "Can I make this ahead?"
- "Why is [specific technique] critical?"
- "What's the difference between [ingredient A] and [ingredient B]?"

**Format:** Bulleted list or short paragraphs with clear headers

---

## SECTION 7: GLOSSARY

**Location:** End of recipe

**Content:** Define any technical culinary terms used in the Method

**Format:**
- **Term:** Definition
- Keep definitions concise (1-2 sentences)

**Examples:**
- **Blooming:** The process of briefly heating spices in fat to release essential oils and amplify flavor.
- **Beurre Noisette:** "Hazelnut butter." Butter cooked until the water evaporates and the milk solids toast, creating a nutty flavor.
- **Nappé:** The consistency where a sauce coats the back of a spoon and a clear line remains when you draw your finger through it.

---

## SECTION 8: KEYWORDS

**Location:** End of recipe, after Glossary

**Purpose:** Powers site search and recipe discovery

**Format:** `## Keywords` heading followed by a single comma-separated line of 10–15 terms

**Categories to cover:**

- Cooking technique (e.g., braising, emulsification, blind bake, confit)
- Primary ingredients (e.g., duck, miso, puff pastry, brown butter)
- Cuisine origin (e.g., French, Korean, Italian, Vietnamese)
- Equipment (e.g., pressure cooker, stand mixer, chinois, dehydrator)
- Flavor profile (e.g., umami, smoky, fermented, bright, rich)
- Occasion or difficulty (e.g., competition, weeknight, pastry, plating)

**Example:**

```markdown
## Keywords
duck, confit, French technique, fat poaching, pressure cooker, collagen, umami, weeknight, protein
```

---

## SECTION 9: CATEGORY

**Location:** End of recipe, after Keywords

**Purpose:** Powers faceted filtering on the website (cuisine + style dropdowns)

**Format:** `## Category` heading followed by a single structured line using the controlled vocabulary below

**Required fields:** `cuisine:` and `style:` — both mandatory
**Optional field:** `dietary:` — include only if applicable

**Controlled Vocabulary:**

**cuisine:** `French` · `Italian` · `Japanese` · `Korean` · `Vietnamese` · `Chinese` · `American` · `Mediterranean` · `Asian-Fusion` · `Global`

**style:** `Classical` · `Modern` · `Rustic` · `Competition` · `Fine Dining` · `Weeknight` · `Pastry` · `Technique Folio`

**dietary (optional):** `Vegetarian` · `Pescatarian`

**Format:**

```markdown
## Category
cuisine: French | style: Classical
```

With optional dietary tag:

```markdown
## Category
cuisine: Italian | style: Rustic | dietary: Vegetarian
```

**Stop Point:** If the recipe's cuisine or style is genuinely ambiguous (e.g., a fusion dish that could be classified multiple ways), ask the user before assigning. Do not guess.

---

## UNIVERSAL FORMATTING STANDARDS

**Temperatures:**
- Always dual format: Fahrenheit / Celsius
- Use standard text, not LaTeX: "425°F/220°C"

**Measurements:**
- Metric and US customary for ingredients
- Prefer grams for precision, provide volume equivalent

**Typography:**
- Use proper fractions: ⅔, ¼, ½ (not 2/3, 1/4, 1/2)
- Use degree symbol: ° (not asterisk or "degrees")
- Use en-dash for ranges: 12–14 minutes (not hyphen: 12-14)

**Terminology:**
- Use proper culinary French/Italian terms
- Always explain in Glossary
- Example: Use "mise en place" but define it

---

## ZERO-CITATION PROTOCOL

**CRITICAL RULE:** Never include system-inserted citation markers

**Forbidden:**
- [source]
- [1], [2], [3]
- [cite]
- [web:1]
- Any bracketed reference notation

**Why:** These are manuscript-ready recipes for cookbook publication. Citations break the clean copy requirement.

---

## AGENT-SPECIFIC NOTES

**Cafe Athena:**
- After generating recipe, provide "INDEX DATA" block with Chapter and Title
- Recipes are for permanent cookbook archive

**VersiChef:**
- After generating recipe, ask "Do you have any follow-up questions on this technique?"
- Recipes are for immediate use, may be transferred to Cafe Athena later