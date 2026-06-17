# Café Athena — Brand Guidelines

**Status:** Complete — Phase 1 brand build
**Last Updated:** 2026-06-11

---

## §1 — Overview & Brand Identity

### Mission Statement

Café Athena bridges the gap between professional culinary technique and the home kitchen. It is a tool for home cooks who want to cook at a higher level — learning the principles that make food work, and applying them to recipes of their own.

### Brand Promise

Every recipe and technique in Café Athena comes with the knowledge to make it your own.

### Positioning Statement

For home cooks who want more than a recipe list, Café Athena is a technique-forward resource organized around understanding — not output. Most recipe content online is built for speed and sharing. This is built around principles: what makes a dish work, and how to carry that across your whole kitchen.

### Core Values

**Craft over shortcut.**
There are faster ways to do most things in this book. We don't take them by default. Craft means choosing the method that builds skill and produces the better result — stock from bones, pasta shaped by hand, a sauce finished properly. A cook who knows the right way can always choose the shortcut consciously. The goal is to make that a choice, not a limitation.

**Curiosity first.**
The best cooks ask why before they ask how long. Café Athena is written for readers who want to understand why pasta water works in a sauce, what emulsification means for texture, where the Maillard reaction actually matters. Curiosity is the engine that turns a recipe into a skill. The book is written to feed it.

**Food is personal.**
This project started as one person organizing recipes he was actually cooking, for someone he actually cooked for. That origin is still visible in the book: nothing here is included for trend or aesthetic. It's included because it's worth cooking — and because the person it was cooked for would have wanted seconds.

**Honesty about difficulty.**
Café Athena doesn't pretend stocks take 20 minutes or that croissants are a weeknight project. Recipes are framed with honest time and effort expectations because a cook who is misled loses confidence, not just a Tuesday evening. Honesty about difficulty is also honesty about reward: the things that take longer are worth it, and we say so plainly.

**Skills compound.**
The book is organized the way a professional kitchen operates: technique first, then stations, then building blocks. What you learn in Chapter 1 applies in Chapter 7. What you build in Chapter 10 shows up everywhere. A reader who finishes this book is not where they started — and the book is designed so that's not an accident.

**Built for the kitchen, not the shelf.**
Café Athena is a digital-first project, designed to be used at the counter on a phone — not read once and set aside. Mobile-first isn't just a technical decision; it's a belief about how culinary knowledge should travel. It should be in your pocket when you need it, ready the moment you start cooking.

### Brand Archetype

**The Sage — a relationship with the material, not the teacher.**

The Sage creates conditions for understanding — not just instruction. In Café Athena, knowledge isn't transferred from author to reader; it's encountered through the work itself. The reader builds a relationship with the craft: with heat, with salt, with time, with structure. The voice doesn't tell you what to think about a technique — it shows you how the technique thinks, and lets you arrive at the understanding yourself. The outcome isn't a set of completed recipes. It's culinary enlightenment: a cook who sees the logic behind food and doesn't need to be told twice.

---

## §2 — Author & Brand Story

### The Author

I didn't learn to cook in a classroom. I learned the way most home cooks do — at family tables, in friends' kitchens, by watching and tasting and making things badly until I made them better. For most of my adult life, cooking has been part of how I live rather than what I do professionally. My work is in business development and marketing, with a technical background and a serious interest in AI. Café Athena is where those two lives intersect.

My culinary education, such as it is, came from books and obsessive watching. Escoffier was a revelation the first time I read him — not the recipes, which are period pieces, but the structure underneath them: the logic of a kitchen as a system. Keller's rigor. Jean-Pierre's warmth. Marco Pierre White's conviction that cooking is a discipline, not a performance. Gordon Ramsay at his most technical, before it became television. Brian Langston and Max Miller of Tasting History for reminding me that food has a past worth knowing. I've been learning from all of them for years, and I still am.

What I cook, I cook for my wife Athena. That is where the name came from. For a while, I was posting dinner photos on Facebook and Instagram under "Tonight at Café Athena" — casual, a few words, whatever we were having. The name felt right before there was any plan around it.

### How the Project Started

The actual catalyst was a problem, not a vision. I had years of recipes in too many places: handwritten cards, photos on my phone, a large OneNote archive, documents scattered across drives. None of it was usable while standing at the stove. My first idea was simple — organize everything into OneNote, use an iPad at the counter. Then we got a Samsung Smart Fridge with a large display screen built into the door. The iPad approach didn't work with it.

The fridge became a forcing function. I needed something that would display cleanly on a large screen, be accessible without a dedicated device, and hold up as a real reference. I was also in the middle of developing my AI skills, and I had Claude Code. I started with a Chef agent and three modes of interaction — recipe development, formatting, technique education. The agent wrote and organized content; I directed, reviewed, and refined. The cookbook grew from that loop.

What began as a personal organization tool became a manuscript — organized around how professional kitchens operate, with technique at the front, station work through the middle, and the building blocks at the back. Then it became a published Astro website. Then it became a brand.

### Why It Matters

The project is named for Athena, and that origin is still visible in the book. Nothing in it was included for trend, aesthetic, or algorithm. Every recipe is something I've cooked, something I cook, or something I'm working toward. The test for anything going into The Manual is honest: would I actually make this? Would it be worth her time at the table?

The cookbook is built for home cooks who want more than a recipe list — who want to understand why something works, carry that understanding into their own kitchen, and cook at a higher level without pretending to be a chef. That is exactly who I am. I am writing the book I needed.

---

## §3 — Typography

### Type System Overview

Café Athena uses a two-font system: a classical serif for display and a contemporary sans-serif for body. The pairing is deliberate — it is not trendy, and it does not look like a food blog.

---

### Display Font: Cormorant Garamond

**Use for:** H1–H4 headings, pull quotes, recipe titles, chapter names, large display text, the site wordmark.

**Character:** Old-style editorial serif with visible calligraphic origins. Cormorant Garamond reads as authoritative without being formal — it has warmth in its letterforms, a quality shared with original Garamond but with more display presence at large sizes. At heading scale, it signals a book, not a website. That is the correct signal for Café Athena.

**Weights in use:**

- `font-weight: 400` (Regular) — subheadings, pull quotes, recipe titles at body-adjacent scale
- `font-weight: 500` (Medium) — primary headings, chapter names, display use (this is the site default per `global.css`)
- `font-weight: 600` (SemiBold) — reserved for emphasis within a heading context; use sparingly
- `font-weight: 700` (Bold) — not used. Cormorant Garamond Bold at display size reads as heavy; the brand does not shout.

**Notes on Cormorant Garamond at scale:** At very small sizes (below 14px), Cormorant Garamond's thin strokes become fragile. Do not use it for body copy, metadata, or captions. It is a display font. Below H4, hand off to Inter.

---

### Body Font: Inter

**Use for:** Body copy, recipe method steps, ingredient lists, metadata (date, category, keyword labels), UI elements (navigation, buttons, form labels), captions, footnotes.

**Character:** Geometric humanist sans-serif designed specifically for screen legibility. Inter is neutral in personality — it does not impose itself. That is its job here: clear transmission of information at reading scale without competing with Cormorant Garamond's editorial voice.

**Weights in use:**

- `font-weight: 400` (Regular) — all body copy, method steps, ingredient lists
- `font-weight: 500` (Medium) — metadata labels, UI element text, inline callouts
- `font-weight: 600` (SemiBold) — section labels, button text, navigation items
- `font-weight: 700` (Bold) — used sparingly for inline emphasis within body copy only

---

### The Pairing Rationale

Cormorant Garamond + Inter is a classic editorial-to-utility pairing. The serif says *craft, time, attention*. The sans-serif says *clarity, function, efficiency*. Together they describe exactly what Café Athena is: a book that takes the material seriously and also intends to be used at the counter while something is on the stove.

The pairing communicates without language: when you see Cormorant Garamond, you are in editorial territory — this is knowledge, context, the author's voice. When you see Inter, you are in operational territory — this is instruction, this is the information you act on. The fonts map to the two registers of the book.

---

### Web Implementation

Both fonts are served via Google Fonts. The `@theme` block in `site/src/styles/global.css` defines them as CSS custom properties:

```css
--font-heading: "Cormorant Garamond", serif;
--font-body: "Inter", sans-serif;
```

Fallback stacks are implicit in the CSS keyword: `serif` and `sans-serif`. No custom fallback stacks are defined — acceptable for this project since both fonts load reliably in the target environment (modern browsers, Samsung Smart Fridge browser).

A system monospace font (`font-mono`) is used in limited UI contexts — recipe index numbers, code-adjacent display. It is not a named brand font and should not appear in designed brand materials.

---

### What Not to Use

- **No other serif fonts.** Do not substitute Playfair Display, Lora, EB Garamond, or any other serif. If Cormorant Garamond is unavailable, fall back to the system serif — do not substitute a visually similar web font.
- **No other sans-serif fonts.** Do not substitute Outfit, DM Sans, Nunito, or trend-facing geometric sans-serifs. If Inter is unavailable, fall back to the system sans-serif.
- **No decorative or script fonts.** Never. Not for recipe titles, not for the wordmark, not for social graphics. The brand is editorial, not artisanal-market-chalkboard.
- **No Cormorant Garamond in body copy.** It is not designed for extended reading at 16px. This is a hard rule.
- **No mixing weights casually.** Weight choices are functional. Using Bold Cormorant Garamond for decorative emphasis violates the type system's intent.

---

## §4 — Color Palette

### Palette Overview

The Café Athena palette is built on a deliberate tension: warm, editorial tones drawn from parchment, old paper, and olive oil — set against a cool near-navy as the primary dark. This is not an oversight. The tension is structural.

The warm tones (cream, parchment, olive-gold) carry the editorial and culinary identity. They feel like a well-used cookbook, a kitchen table, candlelight. The cool dark (charcoal) carries authority and precision. It does not feel domestic. The combination produces a brand that is approachable without being soft, and authoritative without being cold. That is the exact register Café Athena needs to occupy.

---

### Primary Darks

**Charcoal** `#1a1a2e`

- CSS variable: `--color-charcoal`
- Semantic role: Primary dark — text on light backgrounds, page framing, headers
- Usage: Default body text color, heading color, primary background for dark-mode contexts, navigation
- Character: Near-navy, not warm. This is the most important thing to understand about the palette. `#1a1a2e` has a blue-violet undertone — it reads as authoritative, almost archival. It is closer to midnight ink than to charcoal or espresso. This choice anchors the whole palette toward the cool-authority pole.

**Charcoal Light** `#2d2d44`

- CSS variable: `--color-charcoal-light`
- Semantic role: Secondary dark — subtle UI depth, layered backgrounds, panel backgrounds in dark contexts
- Usage: Card borders in dark contexts, secondary navigation backgrounds, hover states on dark surfaces, depth layering on the charcoal base
- Character: The same cool near-navy family, lifted slightly. Used to create depth without introducing a new hue.

---

### Warm Tones

**Parchment** `#faf7f2`

- CSS variable: `--color-parchment`
- Semantic role: Page background — the default canvas
- Usage: Full-page background color. The primary surface. Everything is read against this.
- Character: Not white. Not off-white. Warmer and slightly more aged — paper that has been used, not paper from a ream. This single choice places the brand decisively in the editorial tradition.

**Cream** `#f5f0e8`

- CSS variable: `--color-cream`
- Semantic role: Card and panel backgrounds
- Usage: Recipe cards, sidebar panels, inset content blocks, glass-panel UI elements. Slightly darker than parchment — creates contrast to lift cards off the page without reaching for a border.
- Character: The same warm family as parchment, a step richer. The two are close enough to read as the same palette family; different enough to create visual separation.

**Divider** `#e0d8cc`

- CSS variable: `--color-divider`
- Semantic role: Borders, rule lines, structural dividers
- Usage: Horizontal rules between sections, card borders, table borders, any structural line that needs to separate without interrupting. Not used as a fill color.
- Character: The darkest of the warm tones — still clearly in the parchment family but with enough contrast against cream and parchment backgrounds to read as a line.

---

### Accent

**Olive Gold** `#c9a96e`

- CSS variable: `--color-olive-gold`
- Semantic role: Primary accent — CTAs, interactive labels, highlights, the brand's warm color
- Usage: Call-to-action buttons, active navigation indicators, link hover states, recipe category labels, any element that needs to say "this is actionable or notable." This is the brand's warmest color and its only saturated accent on light backgrounds.
- Character: Not orange, not yellow, not brown. Olive gold occupies the tonal space between aged honey and warm olive oil — it is both culinary and editorial. It reads as expensive without being precious.
- **Accessibility note:** `#c9a96e` on `#faf7f2` (parchment) produces a contrast ratio of approximately 2.8:1 — below the WCAG AA minimum of 4.5:1 for normal text. Do not use olive gold for body text or small labels. It is approved for large display text (18px+ or 14px+ bold), icons, decorative rules, and UI elements where text contrast requirements do not apply. For interactive text links, pair olive gold with a visible underline or weight increase to compensate for contrast.

**Olive Dark** `#a8873f`

- CSS variable: `--color-olive-dark`
- Semantic role: Hover and active state for olive gold
- Usage: Button hover state, active link state, pressed state for any olive-gold interactive element. Never used as a standalone accent — always in relation to olive gold.
- Character: The same hue, deeper. Still warm, still within the olive-oil family, but clearly a state change.

---

### Supporting

**Burgundy** `#6b2737`

- CSS variable: `--color-burgundy`
- Semantic role: Accent support — currently underused, status: defined but deferred
- Usage intent: Chapter color coding (specifically The Butcher, Ch. 7, and French bistro contexts), alert or error states in UI, pull-quote backgrounds, decorative rules in print contexts. The color maps to red wine and raw beef — it is the correct color for Chapter 7's visual identity.
- Current status: The color exists in the CSS palette and appears in templates, but has no systematic deployment. **Decision deferred to Phase 6** — when site chapter branding is addressed, burgundy will be formalized as the accent color for The Butcher chapter. Until then, do not introduce it into new UI contexts without deliberate intent.
- Character: Dark, warm red. Not a fire-engine red, not a pink-adjacent mauve — this is the color of reduced red wine in a cast iron pan. It is the most emotionally charged color in the palette and should be used with corresponding restraint.

**Smoke** `#6b6b7b`

- CSS variable: `--color-smoke`
- Semantic role: Secondary text, metadata, subdued UI
- Usage: Dates, categories, bylines, placeholder text, secondary navigation labels, any text that needs to be present but not primary. The typographic workhorse for everything that is not the main voice on the page.
- Character: A cool grey — notably it shares the blue-violet undertone of charcoal. Smoke is not a warm grey. This is another expression of the palette's cool-authority pole, applied at text scale.

---

### The Palette's Central Tension

The warm tones (parchment, cream, olive-gold) and the cool darks (charcoal, smoke) do not neutralize each other. They create a productive friction. Warm editorial vs. cool authority is the visual expression of what the book is: approachable craft with intellectual structure underneath.

A pure warm palette would read as a food blog. A pure cool-dark palette would read as a design portfolio. The tension between them produces something that reads as a serious culinary reference that is still warm to be near. Every layout decision in the brand should maintain this tension. When in doubt: warm surfaces, cool type.

---

## §5 — Voice & Tone: Manuscript Register

### Register Spec

The Manuscript Register is the voice inside the book — headnotes, technique explanations, method steps, glossary entries. It assumes the reader is already committed: they're at the counter, or they're reading to prepare for when they will be. The job of this register is to transmit understanding, not instructions.

Write as someone who has worked through the material and found the logic in it. Explain the why before or alongside the how — not after, and not as a footnote. A headnote isn't a story. It's a brief for the cook: what to understand about this dish before the hands go in. A technique explanation isn't a procedure. It's a description of what the technique is actually doing and why it does it.

The Sage archetype governs tone: the knowledge appears in the work, not from above. Don't tell the reader what the dish tastes like or how they'll feel. Don't praise the recipe. Let the technique speak.

Be direct about difficulty. Be specific about why something matters. Never skip the structural explanation to get to the step. Never repeat structural explanation already given elsewhere in the book — cross-reference and move on.

The register works for Persona 1 (don't over-explain; do connect to principle), Persona 3 (show the structure so she can use it forward), and Persona 2 (be readable, not clinical — she'll go deep if the writing earns it).

**Voice markers:** active construction, present tense for instruction, specific over general, technical terms used correctly and introduced when first needed, no hedging, no decorative prose.

---

### Do / Don't Pairs — Manuscript Register

---

**Pair 1**

DON'T: "Cook the onions over medium heat until they soften, about 8–10 minutes."

DO: "Cook the onions over medium heat until they lose their rawness and begin to turn translucent — 8 to 10 minutes. You're driving off moisture and beginning to convert the sugars. The next stage, where they start to color and sweeten further, is caramelization. Stop here if you want them neutral; go further if you want the sweetness to register in the dish."

*Principle: The step without the why is just a timer. Name what is happening and why the cook is stopping where they are.*

---

**Pair 2**

DON'T: "Season to taste with salt and pepper."

DO: "Season with salt. Taste. You're looking for the point where the flavors of the dish sharpen and become legible without tasting of salt itself — a threshold, not a quantity. Pepper is a separate decision: add it here only if the dish is going to cool before serving, since pepper blooms in heat and loses its edge in resting food."

*Principle: "Season to taste" is a placeholder, not an instruction. It teaches nothing and helps no one who doesn't already know.*

---

**Pair 3**

DON'T: "Make sure not to overcrowd the pan, or the food will steam instead of sear."

DO: "Work in batches if the pan is crowded. Surface contact and dry heat are what produces the Maillard crust; add too much protein at once and you lower the pan temperature below the threshold and the moisture you're trying to drive off accumulates instead. The result is braised meat in its own water, not a sear."

*Principle: "Will steam instead of sear" tells the cook what will happen but not why. The underlying physics — temperature drop, moisture accumulation — gives Persona 3 something to apply in other contexts.*

---

**Pair 4**

DON'T: "This is a great dish for a dinner party — it can be made ahead and reheated!"

DO: *(nothing — remove this sentence entirely.)*

*Principle: Promotional framing has no place in the manuscript register. The reader is cooking, not deciding whether to cook. Serving-occasion commentary belongs in the acquisition register, if anywhere.*

---

**Pair 5**

DON'T: "Don't be intimidated by this step — it's easier than it looks."

DO: "The fold here is decisive. Work quickly: the batter deflates if you linger, and once lost, that structure doesn't come back. Two or three passes, not ten."

*Principle: "Don't be intimidated" is condescension dressed as reassurance. Persona 1 reads it as noise. Tell the cook what to do and why it matters — that is the actual reassurance.*

---

**Pair 6**

DON'T: "Feel free to experiment with different herbs and spices to make this dish your own."

DO: "The herb here is structural, not decorative: its job is to cut the richness and bring definition to a dish that would otherwise be flat. Tarragon works. So does chervil, at about half the volume. Dill changes the character significantly — more eastern, less bistro. The structural role stays the same; the flavor register shifts."

*Principle: "Make it your own" is an empty invitation. Give Persona 3 the structural reasoning and she'll make it her own without being told to.*

---

**Pair 7**

DON'T: "Reduce the sauce until it reaches the right consistency."

DO: "Reduce until the sauce coats the back of a spoon and a line drawn through it holds — roughly 40% of original volume for a veal jus, though the fat content of the stock you're using will affect where this lands. Taste as it reduces: the salt concentrates, so adjust only after the reduction is complete."

*Principle: "Right consistency" is defined by experience, not instruction. Persona 1's core frustration is vague endpoints. Give the test, give the reference point, give the variable that affects it.*

---

**Pair 8**

DON'T: "This technique takes some practice, but once you get the hang of it, you'll wonder how you ever cooked without it."

DO: *(nothing — cut the sentence. If there is something genuinely useful to say about the learning curve, say it specifically: "The first attempt will feel mechanical. By the third, the hand motion becomes automatic.")*

*Principle: "You'll wonder how you ever cooked without it" is a marketing sentence. The manuscript register doesn't sell. It teaches.*

---

## §6 — Voice & Tone: Acquisition Register

### Register Spec

The Acquisition Register is the voice outside the book — site copy, social posts, the About page, any context where the reader hasn't yet committed. It addresses someone who is curious but skeptical, considering whether this resource is for them.

The register is honest, specific, and unhurried. It doesn't try to close. It describes what the thing actually is and lets that description do the work. Persona 2's trust threshold is high and her detector for manufactured content is finely calibrated — one AI-sounding phrase, one breathless oversell, and she's gone. Persona 3 is equally unforgiving.

Write as if you're describing the book to someone you respect who asked you directly. Be concrete about what it is and isn't. Acknowledge difficulty where it exists. Don't perform enthusiasm — if something is worth spending time on, say why. Let the specifics do the selling.

The personal origin of the project is an asset in this register: a real kitchen, a real person it was cooked for, a real problem it solved. Lead with that over any credential or production value. "A culinary education disguised as a cookbook" is closer to the truth than "your go-to cooking resource."

The register earns trust rather than requesting it. It speaks to what Persona 2 and Persona 3 actually want — understanding, not just recipes — and it does so without promising more than the book delivers.

**Voice markers:** concrete nouns over abstract ones, short declarative sentences for key claims, no superlatives, no promises the book can't keep, no simulated warmth, human rhythm over copywriting cadence.

---

### Do / Don't Pairs — Acquisition Register

---

**Pair 1**

DON'T: "Unlock your culinary potential with expert techniques and delicious recipes!"

DO: "A cookbook organized around why food works — not just how to follow a recipe, but how to understand what the recipe is doing."

*Principle: "Unlock your potential" is an abstraction that promises nothing specific. Say what the thing actually is.*

---

**Pair 2**

DON'T: "Whether you're a beginner or an experienced cook, there's something here for everyone."

DO: "Built for cooks who already know their way around a kitchen and want the next layer — the technique context that explains why something works, not just that it does."

*Principle: "Something for everyone" defines nobody and signals generic content. Both Persona 1 and Persona 2 will read it as a red flag. Define the actual audience.*

---

**Pair 3**

DON'T: "Easy weeknight meals the whole family will love."

DO: *(This phrase does not appear in Café Athena copy, ever. The book does not make this promise. See Forbidden Phrases.)*

*Principle: Promises the book cannot keep destroy trust before it's built. Persona 2 has been burned by this exact phrase. Persona 1 will leave immediately.*

---

**Pair 4**

DON'T: "Dive into a world of flavor with our carefully curated collection of recipes!"

DO: "Ninety-some recipes and technique folios, organized the way a professional kitchen operates — technique first, then stations, then building blocks. Start anywhere. It connects."

*Principle: "World of flavor" and "carefully curated" are noise. Specific details about the actual contents are more persuasive than any amount of enthusiasm.*

---

**Pair 5**

DON'T: "Kevin's passion for cooking shines through in every recipe."

DO: "Kevin cooks for his wife Athena. Every recipe in this book has been through their kitchen — nothing was included for trend or aesthetic."

*Principle: "Passion shines through" is a template sentence. The actual origin story — real kitchen, real person, real test — is more specific, more honest, and more compelling.*

---

**Pair 6**

DON'T: "Join our community of food lovers and elevate your cooking today!"

DO: "The site is the cookbook — built to display on a refrigerator screen, readable at the counter with one hand. Start with the technique sections if you're learning from scratch. Start with the station chapters if you want to cook."

*Principle: "Join our community" is boilerplate. Persona 2 reads it as a mailing list pitch. Describe what the thing is and how to use it.*

---

**Pair 7**

DON'T: "With step-by-step instructions and helpful tips, even complex dishes are achievable!"

DO: "Some of what's in this book takes time. The pâte brisée takes practice. The stock takes hours. None of it is hidden — the recipes say what they need."

*Principle: "Even complex dishes are achievable!" is a false reassurance that signals the book is going to minimize difficulty. The actual promise — honesty about what things cost — is more trustworthy.*

---

**Pair 8**

DON'T: "Transform your cooking with these game-changing techniques!"

DO: "The technique sections explain the principle, then you see it applied across the recipes that follow. By the time you've cooked through a chapter, the principle isn't something you know about — it's something you've done."

*Principle: "Game-changing" is a superlative that has lost all meaning. Describe the actual mechanism of how the learning works.*

---

### Forbidden Phrases

These phrases are banned from all Café Athena copy regardless of register. Each entry is a specific phrase or class of phrase, with one-line reasoning.

---

**"Weeknight friendly"** — promises a speed and ease the book does not deliver and would not want to; Persona 2 has been burned by this phrase specifically.

**"Elevate your cooking"** — abstract superlative with no referent; signals marketing copy, not culinary authority.

**"Game-changer" / "game-changing"** — overused intensifier that has become noise; says nothing specific about anything.

**"Unlock [your potential / the secret to / the flavor]"** — infomercial register; incompatible with the Sage archetype.

**"Delicious"** — a writer's failure to describe what something tastes like; replace with the actual quality being named.

**"Amazing"** — same as above; meaningless intensifier.

**"Simple" / "easy" (as category labels)** — these are false promises when applied to technique-forward content; use specific time and effort framing instead.

**"Step-by-step"** — implies hand-holding; Persona 1 reads this as a signal that the resource isn't for serious cooks.

**"Even beginners can…"** — condescending in one direction while also misrepresenting the audience.

**"The whole family will love…"** — not the audience, not the promise, not the brand.

**"Passion for food / cooking"** — template phrase; replace with specifics about the actual project and its origin.

**"Carefully curated"** — filler modifier; if the selection needs justification, explain the actual selection logic.

**"Food lover"** — vague audience descriptor that includes everyone and therefore no one.

**"Join our community"** — boilerplate marketing call-to-action with no genuine content; if there is a community, describe it specifically.

**"Trust me, it works"** — undermines the Sage archetype; the technique should demonstrate its own reliability.

**"Secret ingredient / secret technique"** — sensationalizes what should be explained plainly.

**"Restaurant-quality at home"** — overused promise; if the dish is genuinely at that level, describe it specifically rather than invoking the comparison.

**"This will change the way you cook forever"** — unmeasurable promise; Persona 3 reads it as a tell for shallow content.

**"Don't be intimidated"** — reassurance framed as condescension; replace with specific instruction that actually removes the difficulty.

**"Make it your own"** — an instruction without mechanism; replace with the structural information that makes variation actually possible.

**"Something for everyone"** — self-defeating audience claim; the book is for serious cooks and should say so.

**"Tried and tested"** — filler credentialing; of course the recipes were tested; this phrase exists only to fill space.

---

## §7 — Visual Asset System: Cookbook Photography

### Standard & Scope

All recipe hero images, chapter banner images, and section landing page images for Café Athena are generated and maintained by the Visual Director (Gemini Gem 2). This section establishes the brand-level standard. The Gem's full operational instructions — including input formats, chapter-specific rules, reference image anchors, and suppression lists — are the authoritative detail layer at `Agents/Gemini-Gems/CAFÉ ATHENA - VISUAL DIRECTOR GEM INSTRUCTIONS.md`.

The standard below is what every image must satisfy regardless of which mode produced it.

---

### Core Aesthetic Standard

**Warm editorial food photography.** Rich, moody, and approachable. Bistro cookbook, not fine dining catalog. Every image should feel like it was taken in a real kitchen or on a real table, not a sterile studio.

This description has legal weight in the brand: any image that reads as clinical, minimalist, or modern-magazine fails the standard, regardless of technical quality.

---

### Three Image Types

| Type | Filename pattern | Dimensions | Purpose |
|------|-----------------|------------|---------|
| Recipe Hero | `XX-YY.webp` | 1920×1080 (16:9) | Primary dish photograph, one per recipe |
| Chapter Banner | `banner-chXX.webp` | 1920×480 (4:1) | Header strip on chapter and section landing pages |
| Section Landing | `section-[name].webp` | 1920×1080 (16:9) | Full-width hero on Academy, Brigade, Larder, Glossary pages |

---

### Recipe Hero Rules

- **Surface:** Always warm wood. Dark rich tones for braises and French bistro; lighter rustic for grilled and smoked. Marble only for The Pâtissier (Ch. 9) and Les Fonds (Ch. 12).
- **Angle:** Low three-quarter, approximately 30–45° elevation. Never overhead. Eye-level only for large whole proteins on boards.
- **Depth of field:** Shallow. Hero element sharp; background softens naturally.
- **Lighting:** Warm, directional side light. Moody for braises. Brighter and more natural for grilled. Never flat, never flash.
- **Color palette in images:** Caramelized browns, burgundy wine reductions, seared char, golden fond. Earthy stoneware tones. Fresh herb greens as the only saturated accent. No cool tones, no stark whites.
- **Props:** Maximum three supporting elements. Approved list: red wine glass, torn crusty bread, grey or cream linen napkin, fresh herb garnish. Nothing else.
- **Vessels:** Stoneware or earthenware — stone-grey or cream glaze for braises and stews; flat stoneware plate for steaks and pan sauces. No bright white plates, fine china, or minimalist tableware.
- **No people.** Hands actively engaged with food or cookware are permitted.

---

### Chapter Banner Rules

Ultra-wide panoramic strip. Ingredient-focused or process-focused — not a plated finished dish. Show raw materials, tools, or a mid-process moment representing the chapter's domain. Dramatic raking side light. Surface varies by chapter character: marble for The Mill and The Pâtissier, dark wood for The Butcher and The Larder, dark slate for The Academy and The Fishmonger.

---

### Section Landing Rules

More editorial and cinematic than recipe heroes. Establishes atmosphere for an entire section. People and faces are permitted in action and process shots — keep framing tight on the action. Lighting range is wider: fire glow and high contrast for Brigade, cool precision for Academy, warm and rich for Larder, soft and even for Glossary.

---

### What Is Never Acceptable in Any Image

- Text, labels, or watermarks of any kind
- Logos or branded items
- AI-style unrealistic food: perfect symmetry, glowing sauces, hyper-saturated color, impossible garnish arrangements
- Cool tones or stark white backgrounds on recipe heroes
- Modern minimalist tableware (bright white plates, thin-rim ceramics, designer vessels)

---

## §8 — Visual Asset System: Educational / Companion Content

Lane 2 covers all educational and explanatory visual content — infographics, slide decks, video overviews, and briefing documents generated from Technique Folios. This content is distinct from recipe hero photography (Lane 1) in both purpose and aesthetic. Where Lane 1 makes food look worth cooking, Lane 2 makes technique worth understanding.

---

### Canonical Reference Examples

These three outputs, generated from Chapter 1 (The Lab) Technique Folios via NotebookLM Studio, establish the Lane 2 visual standard:

| Folio ID | Title | Mode |
|----------|-------|------|
| 01-01 — Thermodynamics & Heat Control | "The Three Engines of Heat" | Dark |
| 01-02 — Salinity & Equilibrium | "Salt: The Master of Water Management" | Light |
| 01-03 — Baker's Percentages & Hydration | "The Baker's Ratio: Mastering Hydration & Scaling" | Light |

When producing new educational content, these three are the visual reference point. New outputs should feel as if they belong in the same series.

---

### Style

**Victorian/editorial textbook illustrated.** Hand-drawn sketch-style diagrams, decorative scroll and border elements, structured multi-panel layout. The aesthetic sits between a serious culinary reference book and a historical scientific illustration. Not modern infographic. Not clinical diagram. Not social media template.

This is intentional: the illustrated style communicates that the content takes the subject seriously without taking itself seriously. It is approachable because it is hand-drawn; it is credible because it is organized.

---

### Color Modes

Lane 2 operates in two modes. Both are on-brand.

**Light Mode (primary)** — Used for Salt (01-02) and Baker's Ratio (01-03).

- Background: parchment/cream (`#faf7f2` / `#f5f0e8`)
- Text: charcoal (`#1a1a2e`)
- Accent: olive-gold (`#c9a96e`) for callout boxes, banners, highlights
- Decorative elements: warm earth tones, muted gold rules and borders

This mode reads as a page from a well-made reference book. Use for most technique content.

**Dark Mode (secondary)** — Used for Heat (01-01).

- Background: charcoal (`#1a1a2e`)
- Text: cream/parchment (`#f5f0e8`)
- Accent: olive-gold (`#c9a96e`) for titles and highlights
- Panel fills: `#2d2d44` (charcoal-light) for section separation

Dark mode signals intensity and precision — appropriate for technical content where the subject matter is about force, heat, or transformation. Use selectively; light mode is the default.

---

### Layout Principles

- Multi-panel structure: 2–3 columns for mechanism-level content, full-width strips for timing rules or comparison tables
- Each mechanism or concept gets its own panel — no stacking unrelated ideas in a single cell
- Visual hierarchy: title → core reframe (subtitle) → mechanism panels → practical takeaway
- Illustrated diagrams show what is happening inside the food, not just labels or steps
- Timing strips and comparison tables are accepted structural elements when the folio includes them

---

### Production Method

Lane 2 content is generated via NotebookLM Studio using structured prompts derived from Technique Folios. The `/notebooklm-folio-explainer` skill produces copy-paste-ready prompts for all four Studio output types (Video Overview, Infographic, Slide Deck, Briefing Doc) from any folio ID.

The Technique Folio is the source of truth. Do not invent mechanisms, comparisons, or data points not present in the folio source.

---

### What to Avoid

- Modern flat infographic aesthetic (bright colors, geometric icons, sans-serif only)
- Clinical or textbook-plain layout with no editorial craft
- AI-generated photorealistic illustrations that don't match the sketch style
- Mixing Lane 1 food photography with Lane 2 illustrated diagrams in the same asset

---

## §9 — Asset Naming & Specifications

This section is the practical reference for every visual asset produced for Café Athena. Any image added to the project — cookbook, educational, author, or social — follows the naming conventions below and is stored in the canonical location listed. The naming patterns here are derived from the live site architecture at `site/public/images/` and are already in active use.

---

### Naming Conventions

#### Logo Files

| File | Variant | Use |
|------|---------|-----|
| `Brand/Visual Identity/logo-black.svg` | Black | Primary — charcoal on light backgrounds |
| `Brand/Visual Identity/logo-color.svg` | Color | Olive gold on dark backgrounds |
| `Brand/Visual Identity/logo-white.svg` | White | Reverse — on dark or photographic backgrounds |

Source: `Brand/Visual Identity/Cafe Athena - The Manual - Logo.ai`
All SVG files are fully outlined (no font dependencies).

---

#### Cookbook Images (Lane 1)

**Recipe hero images**
Pattern: `XX-YY.webp`
XX = chapter number (zero-padded to two digits)
YY = recipe number within chapter (zero-padded to two digits)
Example: `07-10.webp` (Chapter 7, Recipe 10)

**Reference / process images**
Pattern: `XX-YYa.webp`, `XX-YYb.webp`, etc.
Lettered suffix for secondary images tied to the same recipe. Letters run a → b → c in production order.
Example: `07-10a.webp`, `07-10b.webp`

**Chapter banners**
Pattern: `banner-chXX.webp`
XX = chapter number (zero-padded)
Example: `banner-ch07.webp`

**Section landing images**
Pattern: `section-[name].webp`
Valid names: `academy`, `brigade`, `larder`, `expo`
Example: `section-academy.webp`

---

#### Educational Content (Lane 2)

**NotebookLM infographics**
Pattern: `edu-[folio-id]-infographic.webp`
folio-id follows the same XX-YY recipe index convention
Example: `edu-01-02-infographic.webp`

**NotebookLM slide deck exports**
Pattern: `edu-[folio-id]-slides-XX.webp`
XX = slide number (zero-padded), starting at 01
Example: `edu-01-02-slides-01.webp`, `edu-01-02-slides-02.webp`

**NotebookLM Video Overview and Briefing Doc outputs** — these are not image files and are not stored in the image directories. Video Overview exports are video files; Briefing Doc exports are PDFs. Store these in `The Manual/Educational/` under a subfolder matching the folio ID (e.g., `The Manual/Educational/01-02/`). No image naming convention applies.

---

#### Author Assets

**Author photographs**
Pattern: `author-[descriptor].webp`
Descriptor is one or two lowercase words describing context.
Examples: `author-headshot.webp`, `author-kitchen.webp`, `author-portrait.webp`

---

#### Social Media Assets

**Instagram posts**
Pattern: `social-ig-[id]-[descriptor].webp`
id = recipe or folio index (XX-YY); descriptor = one or two lowercase words
Example: `social-ig-07-10-hero.webp`, `social-ig-01-02-slide1.webp`

**Pinterest pins**
Pattern: `social-pin-[id]-[descriptor].webp`
Example: `social-pin-07-10-vertical.webp`

**YouTube thumbnails**
Pattern: `social-yt-[id]-[descriptor].webp`
Example: `social-yt-01-02-thumb.webp`

**Facebook posts**
Pattern: `social-fb-[id]-[descriptor].webp`
Example: `social-fb-07-10-feature.webp`

---

### File Specifications

All images are exported as WebP at 80% quality unless a specific platform requires JPEG. These dimensions are the canonical output specifications — never scale up from a smaller source.

| Asset type | Format | Dimensions | Ratio |
|---|---|---|---|
| Recipe hero | WebP, 80% | 1920×1080 | 16:9 |
| Section landing | WebP, 80% | 1920×1080 | 16:9 |
| Chapter banner | WebP, 80% | 1920×480 | 4:1 |
| Instagram (square) | WebP, 80% | 1080×1080 | 1:1 |
| Instagram (portrait) | WebP, 80% | 1080×1350 | 4:5 |
| Pinterest pin | WebP, 80% | 1000×1500 | 2:3 |
| YouTube thumbnail | WebP, 80% | 1280×720 | 16:9 |
| Facebook post | WebP, 80% | 1200×630 | 1.91:1 |

WebP is the required format for all assets stored in this project. JPEG is acceptable only where a platform explicitly rejects WebP at upload. Do not deliver JPEG by default.

---

### Storage Locations

| Asset category | Canonical location |
|---|---|
| All processed cookbook images (Lane 1) | `site/public/images/` |
| Educational image exports (Lane 2 infographics, slides) | `site/public/images/edu/` |
| Social media exports | `site/public/images/social/` |
| Author photographs | `site/public/images/` |
| Video and PDF exports (NotebookLM) | `The Manual/Educational/[folio-id]/` |

**The Manual/ is not a storage location for processed images.** Images in `The Manual/` are working files only — unprocessed originals awaiting Photoshop export. Once an image is processed and placed in `site/public/images/`, the working file in `The Manual/` should be deleted. The `The Manual/recipes.json` registry flags when this has been done (`heroImageOptimized: true`, `referenceImagesProcessed: true`).

The `edu/` and `social/` subdirectories under `site/public/images/` are the intended locations for Lane 2 and social assets. They are not yet populated but are established here as the canonical locations for when those channels become active.

---

## §10 — What This Document Does Not Cover

These guidelines define the Café Athena brand for digital publishing: voice, typography, color, visual identity, and asset standards for the cookbook site and its companion social and educational channels. The following topics are outside the scope of this document. They are named explicitly to prevent the guidelines from being misread as covering them.

---

**Print and publishing specifications.** Physical cookbook production requires CMYK color profiles, bleed and trim marks, print-safe type specifications, and paper stock considerations. The color palette documented in §4 is defined in HEX/RGB for screen use. CMYK equivalents are not provided here. If print publishing becomes relevant, a separate print style guide is required before pre-press work begins.

**Trademark and legal.** The brand name Café Athena, the wordmark, and any associated logo marks are brand assets. Questions of trademark registration, copyright notices on published content, usage rights for photography, and licensing of educational material are legal questions. Nothing in this document constitutes legal guidance. Consult qualified legal counsel before registering marks or establishing formal usage rights policies.

**Video production standards.** The Visual Director Gem (§7 reference: `Agents/Gemini-Gems/CAFÉ ATHENA - VISUAL DIRECTOR GEM INSTRUCTIONS.md`) covers still image generation for Lane 1 and Lane 2 outputs. Full video production — camera settings, lighting rigs, editing style guides, color grading for long-form video — is not defined here. The NotebookLM Video Overview format is handled as a Studio output, not a produced video, and falls within the Lane 2 standard. Original produced video will require a separate video production brief.

**Third-party platform UI.** This document defines content standards — what assets look like, what copy sounds like. It does not define how those assets display within social platform interfaces. Platform layout, algorithm-driven format recommendations, and UI changes made by Instagram, Pinterest, YouTube, or Facebook are outside our control and outside this document's scope.

**Merchandise and physical products.** No physical Café Athena products currently exist. When they do — printed books, merchandise, packaging — a product design addendum is required. The type system and color palette provide a starting point, but physical production has enough divergent requirements that it should not be extrapolated from these guidelines without a dedicated specification pass.

**Email design.** Newsletter and email template design are not covered here. Email templates should follow the color system (§4) and type system (§3), but email clients have their own rendering constraints that require a dedicated template specification. When email becomes an active channel, build the template spec from these guidelines rather than assuming the web implementation translates directly.

---

## Sections

1. Overview & Brand Identity *(§1 complete)*
2. Author & Brand Story *(§2 complete — backstory, long bio, short bio, social bios)*
3. Typography *(§3 complete)*
4. Color Palette *(§4 complete)*
5. Voice & Tone — Manuscript Register *(§5 complete)*
6. Voice & Tone — Acquisition Register *(§6 complete)*
7. Visual Asset System — Lane 1: Cookbook Photography *(§7 complete)*
8. Visual Asset System — Lane 2: Educational / Companion Content *(§8 complete)*
9. Asset Naming & Specifications *(§9 complete)*
10. What This Document Does Not Cover *(§10 complete)*
