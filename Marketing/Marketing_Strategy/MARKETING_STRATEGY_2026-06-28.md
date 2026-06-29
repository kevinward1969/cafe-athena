# Café Athena — Marketing Strategy

**Version:** 1.0
**Date:** 2026-06-28
**Status:** Active
**Aligned to:** `Brand/Scorecards/BRAND_STRATEGY_SCORECARD_2026-06-28.md`

---

## Executive Summary

This document is the execution layer under the Brand Strategy Scorecard (2026-06-28). It translates the four brand objectives into a concrete content system, channel strategy, and 90-day roadmap. The strategy is organized around a weekly content cycle that produces five distinct assets from two source types — technique folios and recipe folios — and distributes them across three channels.

Primary 90-day objectives: site traffic growth (GA4) and social following growth across Instagram, Pinterest, and YouTube. A Facebook Group community is planned for Phase 2, contingent on reaching 500–1,000 Instagram followers.

---

## §1 — Strategic Objectives

Derived from Brand Strategy Scorecard 2026-06-28. Numeric targets and timeframes live in the scorecard — not restated here.

| Scorecard Objective | Marketing Translation |
|---|---|
| Obj 1 — Audience Growth | Drive site sessions from social; build following on all three channels |
| Obj 2 — Brand Consistency | Every published asset passes voice and visual review before posting |
| Obj 3 — Content Pipeline | Weekly cadence: 1 EXPO post + 2 reels, produced 4 weeks in advance |
| Obj 4 — Positioning & Awareness | Technique-first content mix reinforces "organized around understanding" positioning |

---

## §2 — Content Strategy

### Weekly Cadence

Three pieces of content per week, sourced from two folio types.

| Content Piece | Source | Frequency |
|---|---|---|
| EXPO post | Recipe folio | 1 per week |
| Technique reel | Technique folio | 1 per week |
| Recipe reel | Brigade or Larder recipe folio | 1 per week |

Content is produced 4 weeks in advance and scheduled. EXPO post scheduling requires a publish-date feature in the Astro site — flagged as a Technical Director task (see §6).

---

### Technique Folio Content Stack

One technique folio produces four pieces of content.

| Asset | Source | Production Path | Destination |
|---|---|---|---|
| Video Overview | NotebookLM Studio | Direct upload | YouTube |
| Technique reel | Folio reference image + ZONOS2 voiceover | ZONOS2 → Firefly Kling 3.0 → Adobe Express | Instagram / YouTube Short / Pinterest |
| Infographic | NotebookLM Studio | Direct upload | Pinterest image pin |
| Slide deck / PDF | NotebookLM Studio | Upload as Document Pin | Pinterest Document Pin |

---

### Recipe Content Stack

One recipe folio produces two pieces of content.

| Asset | Source | Production Path | Destination |
|---|---|---|---|
| EXPO post | Recipe folio | Writing Director drafts; Kevin approves | Site (scheduled) → pushed to all social |
| Recipe reel | Recipe hero image + ZONOS2 voiceover | ZONOS2 → Firefly Kling 3.0 → Adobe Express | Instagram / YouTube Short / Pinterest |

---

## §3 — Channel Strategy

### Instagram (@cafeathena_themanual)

**Lead persona:** Persona 2 (The Culinary Curious) — discovery-oriented, visual first
**Secondary:** Persona 1 (The Serious Home Cook)

**Content mix:**
- Technique reels (1/week) — the differentiator; most food content is recipe-volume, not technique-forward
- Recipe reels (1/week) — Brigade and Larder; bridges technique to immediately cookable dishes
- EXPO post share (1/week) — link in bio; caption drives to site

**Voice:** Acquisition register (§6, BRAND_GUIDELINES.md) — concrete, unhurried, no superlatives.

---

### Pinterest (CafeAthenaTheManual)

**Lead persona:** Persona 3 (The Kitchen Experimenter) — project-minded, saves and returns
**Secondary:** Persona 1

**Content mix:**
- Infographic pin (1/week) — technique folio visual from NotebookLM; high save rate for educational content
- Document pin (1/week) — slide deck PDF uploaded natively; swipeable carousel format
- Video pin (1/week) — recipe reel repurposed from Instagram upload
- EXPO post pin (1/week) — linked to technique article on site

**Notes:** Pinterest is an evergreen channel — pins surface weeks or months after posting. Technique content (infographics, document pins) is the strongest long-term traffic driver here.

---

### YouTube (youtube.com/channel/UC8TEjsxUEezQnvg9KeR4pnA)

**Lead persona:** Persona 1 (The Serious Home Cook) + Persona 2

**Content mix:**
- Video Overview (1/week) — NotebookLM Studio full-length technique video
- YouTube Short (1/week) — recipe reel repurposed from Instagram upload (same 9:16 format)

---

### Facebook Group (Phase 2 — deferred)

Launch contingent on reaching 500–1,000 Instagram followers. A group launched without a seed audience goes quiet. When launched: community hub for technique discussion, recipe questions, and exclusive previews. Kevin as the primary voice. Revisit at Q3 2026 checkpoint.

---

## §4 — UTM Tracking

All links to cafeathenathemanual.com in any marketing asset require UTM parameters. Convention documented in Brand Manager instructions. Parameters: `utm_source`, `utm_medium`, `utm_campaign` (recipe/folio slug), `utm_content` (folio ID).

UTM mapping for technique folio content type is a pending task — complete before first technique folio post goes live.

**Known untracked asset:** 06-07 Chicken and Dumplings Facebook reel (2026-06-22) — posted without UTM. Traffic visible in GA4 under `/06-07` but source unattributed.

---

## §5 — 90-Day Roadmap

### Phase 1 — Establish Cadence (July 2026)

- Produce and schedule first 4 weeks of content (4 technique folios + 4 recipe reels + 4 EXPO posts)
- Complete UTM mapping for all content types
- Confirm EXPO scheduled publish feature (Technical Director)
- Confirm social media links in site footer (Technical Director)
- All reels: ZONOS2 voiceover, warm unhurried tone, ≤15 seconds

### Phase 2 — Build Content Bank (August 2026)

- Maintain 4-week advance content buffer at all times
- First technique folio full stack live (all 5 assets produced and published)
- Pinterest Document Pin workflow confirmed and operational
- Q3 checkpoint: review follower and session targets against scorecard

### Phase 3 — Community (September 2026)

- Evaluate Facebook Group readiness: Instagram at 500 followers?
- If yes: launch with seeded content (first 10 posts planned before launch day)
- If no: defer to Q4 checkpoint

---

## §6 — Open Infrastructure Items

| Item | Owner | Status |
|---|---|---|
| EXPO scheduled publishing | Technical Director | Needed before Phase 1 content bank can be scheduled |
| Social media links in site footer | Technical Director | Added to PROJECT_STATUS.md 2026-06-28 |
| UTM mapping — technique folio content type | Brand Manager | Complete before first technique folio post |

---

## §7 — Content Rules

1. No social content produced for a folio that isn't live on the site.
2. Every link to cafeathenathemanual.com carries UTM parameters.
3. Every caption reviewed against §6 Forbidden Phrases before posting.
4. Every reel voiceover reviewed against Male Marketing Voice 1 profile (warm, unhurried, no announcer cadence).
5. Every visual asset reviewed against brand palette (parchment, charcoal, olive-gold) before posting.
6. Content produced 4 weeks in advance — never scrambled day-of.
