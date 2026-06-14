# Café Athena — Visual System

**Status:** Logo delivered — three variants complete
**Last Updated:** 2026-06-11

---

## Delivered Logo Files

| File | Use |
|------|-----|
| `Brand/Logo/logo-black.svg` | Primary mark — charcoal (`#1a1a2e`) on light/parchment backgrounds |
| `Brand/Logo/logo-color.svg` | Accent mark — olive gold (`#c9a96e`) on dark/charcoal backgrounds |
| `Brand/Logo/logo-white.svg` | Reverse mark — white on dark or photographic backgrounds |

All three files are fully outlined (text converted to paths). No font dependencies. Source file: `Brand/Logo/Cafe Athena - The Manual - Logo.ai`

**Structure:** "Café Athena" in Cormorant Garamond Bold / horizontal rule / "THE MANUAL" in Inter Black. All elements outlined as vectors.

---

## Part 1 — Logo & Wordmark Brief

### What the Mark Must Communicate

Café Athena is a culinary cookbook with a specific character: editorial, craft-driven, warm but authoritative. The mark needs to communicate all of this simultaneously — and do it without being generic.

The name itself does a lot of work. "Café" signals a place: intimate, European, food-serious without being a temple. "Athena" is classical — the name carries weight, myth, a woman who represents wisdom and craft. Together they are not precious, not rustic, not trendy. They are deliberate.

The mark must read as:

- **Editorial** — this is a book, a reference, a considered work. Not a food blog.
- **Craft-focused** — the work here is made by hand, cooked with attention, written with care. The mark should feel made, not generated.
- **Warm** — approachable, personal, the kind of thing you'd encounter at a bistro table rather than in a design portfolio.
- **Authoritative** — not aggressive, not institutional, but the mark of something that knows what it is.

It should hold up in two contexts: as a wordmark in a browser tab and page header, and as a stamp-like element on a cookbook cover or social graphic.

---

### Wordmark Direction: Cormorant Garamond

The heading font is the natural candidate for the wordmark. Cormorant Garamond in Medium weight (500) already reads as the brand's editorial voice. The question is whether to use the font straight as a set wordmark, or to introduce a subtle typographic treatment that distinguishes the logo from a heading.

**Recommended approach:** Set "Café Athena" in Cormorant Garamond at display scale. Apply one deliberate typographic decision to distinguish it from a standard heading — the ligature treatment on "Caf**é**", the letter-spacing, or a fine rule between "Café" and "Athena" acting as a divider. Nothing decorative. The mark's quality should come from what you choose not to do, not from ornament added.

The subtitle "The Manual" may appear below in Inter at small scale, tracked wide — this establishes the editorial hierarchy (name above, reference label below) and mirrors how a printed cookbook title page works.

---

### Whether a Symbol is Needed

A standalone symbol (icon/mark separate from the wordmark) is not needed at this stage. The reasons:

1. The project has one author and one site. The contexts where a symbol-only mark is necessary — app icons, embroidered hats, contexts where text can't appear — are not current use cases.
2. A symbol risks introducing design decisions (what does a Corinthian helmet look like at 32px? how do you make an olive branch not feel like a spa brand?) that are hard to get right and easy to get wrong.
3. Cormorant Garamond at display scale is already a mark. The letterforms have enough presence that the wordmark functions as identity.

**Recommendation:** Wordmark only at launch. Revisit a companion symbol if and when print, merchandise, or a standalone app icon creates a genuine need.

---

### Style References to Avoid

These are the wrong directions. Encountering any of these in a direction should be a stop signal.

**Generic food blogger aesthetic** — sun, fork, wheat sheaf, anything that could also be the logo for a meal-prep subscription box. This brand is not that.

**White-space minimalism** — thin-weight geometric type on white, a lot of air, a single lowercase wordmark. This reads as a design portfolio or a DTC brand. It is incompatible with the editorial warmth the brand requires.

**Rustic farmhouse** — chalkboard textures, distressed type, anything that evokes a farmers' market sign or a mason jar label. The brand is bistro, not barn.

**Mythological illustration** — no Athena helmets, no owls as symbols, no classical columns. The name Athena is personal; it belongs to Kevin's wife. Turning it into a classical mythology reference is both wrong in origin and visually exhausted.

**Chef-coded imagery** — no crossed knives, no chef's hat, no toque. This brand is home cook by origin and identity. Professional technique, yes. Professional kitchen signifiers, no.

---

### Format & File Requirements (Future Delivery)

When the wordmark is produced, deliver:

- **SVG** — primary format, scalable, suitable for web and print
- **PNG** — 2x resolution at 400px wide, transparent background, for social media and document use
- **Dark version** (charcoal `#1a1a2e` on transparent) — primary web use
- **Light version** (parchment `#faf7f2` or white on transparent) — use on dark backgrounds
- **Olive gold version** (`#c9a96e` on transparent) — limited use for special contexts

No raster-only delivery. The wordmark must be vector-native.

---

## Part 2 — Social Template Visual Specs

### Design Principle for Social

Social graphics are acquisition-register materials. They are the brand's first impression with someone who doesn't know it yet. The visual language must do two things simultaneously: be immediately recognizable as Café Athena, and not look like a content template.

The tension to maintain at social scale is the same as the site: warm editorial surfaces, cool authoritative type. The implementation has to account for platform-specific constraints.

---

### Color Usage at Social Scale

The full palette does not translate equally to small screens. Some colors that work at page scale require adjustment in social contexts.

**Use freely at social scale:**

- Olive gold `#c9a96e` — strong enough to read as an accent even at small size; use as border treatment, label background, or typographic highlight
- Parchment `#faf7f2` as background fill on text-overlay panels — works at social scale
- Charcoal `#1a1a2e` as type color on light backgrounds — high contrast, reliable at small size

**Use with care:**

- Charcoal light `#2d2d44` — close enough to charcoal that it reads as the same dark at small size; use only for depth layering, not as a distinct color beat
- Divider `#e0d8cc` as a border or rule — thin rules at social scale can disappear on mobile; minimum 2px stroke weight

**Avoid at social scale:**

- Burgundy `#6b2737` as a background fill — at small scale it reads as a generic dark red; it does not carry the brand's warmth in that context
- Smoke `#6b6b7b` as a dominant color — it greys out social graphics and signals low-energy content

---

### Typography at Social Scale

Cormorant Garamond at small sizes is a legibility risk. At 24px and below, the thin strokes in the regular and medium weights become fragile on mobile screens. Social templates must account for this.

**Rules for social typography:**

- Recipe names and headline text: Cormorant Garamond at 36px minimum on standard (1080×1080) templates. Below 36px, switch to Inter.
- Caption text, labels, metadata: Inter only, 14px minimum, weight 500 or 600.
- Never use Cormorant Garamond at less than 28px in any social context. The strokes fail.
- Letter-spacing on Cormorant Garamond display text: slight tracking increase (0.02–0.04em) improves legibility at social scale without breaking the editorial character.

---

### Image Treatment on Social

**Recipe hero photography is the primary social image source.** The 1920×1080 hero images are already produced to brand standard and carry the full visual identity. Social templates should use cropped or reframed versions of these images rather than purpose-built graphics wherever possible. This maintains consistency between what the site looks like and what social looks like.

**Cropping guidance by platform:**

| Platform | Format | Crop approach |
|----------|--------|---------------|
| Instagram (Feed) | 1:1 (1080×1080) | Center-weighted crop of the hero; keep the primary dish in frame |
| Instagram (Stories/Reels) | 9:16 (1080×1920) | Vertical crop; image in top 60%, text overlay in bottom 40% on parchment panel |
| Pinterest | 2:3 (1000×1500) | Vertical crop with text overlay at bottom; recipe name in Cormorant Garamond |
| YouTube Thumbnail | 16:9 (1280×720) | Direct crop from the hero; add recipe title text in upper-left with olive-gold accent |
| Facebook (Post) | 1.91:1 (1200×628) | Horizontal crop from hero; text overlay optional |

Custom graphics (no photography) are reserved for announcements, chapter launches, or content series headers — not standard recipe posts.

---

### Consistent Visual Elements Across All Social Posts

These elements must appear on every designed social graphic. They are what makes a Café Athena post recognizable before the viewer reads a word.

**Wordmark placement:** Upper-left corner, dark version on light backgrounds, light version on dark or image backgrounds. Small — this is a signature, not a headline.

**Olive gold accent:** Every social graphic should have at least one element in olive gold. This is the single most reliable brand marker at social scale. A thin border strip, a label background, a color-blocked text panel, a rule line — the specific form is flexible, the color must appear.

**Type hierarchy:** One line of Cormorant Garamond (large) + one line of Inter (small) is the template rhythm. Title in serif, category or chapter name in sans-serif below. This pairing should be recognizable across all platforms.

**No busy compositions:** Maximum three visual elements on any text-overlay graphic. The brand's restraint is as much of an identity signal as any specific color or font. Over-designed social graphics contradict the brand.

**No stock photography.** All imagery is either from the Café Athena hero image library or is purpose-shot to the Visual Director standard. No generic food photography from external sources, ever.

---

### Platform-Specific Notes

**Instagram:** The grid is a visual statement. Consistent warm tones across hero images (already produced to standard) will maintain cohesion without additional effort. Avoid text-heavy posts — let the photography lead.

**Pinterest:** Text overlays are expected and perform well. Recipe name in Cormorant Garamond, chapter or category in Inter, olive-gold accent strip. Parchment background panel at the bottom third of the image.

**YouTube:** Thumbnail legibility at very small size (phone notification) is the primary constraint. Recipe title must be readable at 200px wide. Inter SemiBold or Bold for any text that must survive small-size rendering; Cormorant Garamond only for secondary elements.

**Facebook:** Lower visual intensity environment. Standard recipe posts with minimal text overlay perform fine. Reserve designed graphics for announcements and chapter launches.
