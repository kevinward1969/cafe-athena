# Marketing Status

**Last Updated:** 2026-06-29
**Branch:** main

---

## Current Documents

| Document | Path |
|---|---|
| Active Marketing Strategy | `Marketing/Marketing_Strategy/MARKETING_STRATEGY_2026-06-28.md` |
| Marketing Calendar | `Marketing/Marketing_Strategy/MARKETING_CALENDAR_2026.md` |
| Content Registry | `Marketing/Marketing Content/marketing_content.json` |
| Campaign Copy & Text | `Marketing/Campaigns/[YYYY]/[Month]/` |
| Archived Strategies | `Marketing/Marketing_Strategy/archived/` |

## Naming Conventions

**Campaign folders** (folio-tied, week-scheduled): `W#-Mon##-[folio]-[descriptor]`
Example: `W1-Jul7-06-04-hot-chicken/`

**Ala carte folders** (no folio, no cadence): `Mon##-[type]-[descriptor]`
Example: `Jul18-fact-maillard-reaction/` · `Jul20-bio-athena-origin/` · `Jul25-review-xyz-restaurant/`

Ala carte types: `bio`, `review`, `fact`, `culture`

---

## Next Actions — Week 1 (July 7 deadline)

Work in this order. Do not start Week 2 until Week 1 is confirmed ready.

| # | Action | Who | Status |
|---|--------|-----|--------|
| 1 | Write EXPO post: *"Nashville Hot Chicken — The Technique Behind the Heat"* (folio 06-04) | Writing Director | 🔲 |
| 2 | Publish EXPO post to site with `publishDate: 2026-07-08` + configure GitHub Actions daily deploy | Technical Director | 🔲 |
| 3 | Produce 3 EXPO cover images (1080×1080 IG, 1000×1500 Pinterest, 1080×1080 YouTube) | Brand Manager | 🔲 |
| 4 | Produce Nashville Hot Chicken recipe reel — Firefly → voiceover → Adobe Express assembly (folio 06-04) | Kevin | 🔲 |
| 5 | Write copy + hashtags for technique reel and recipe reel (hook, caption, CTA for both) | Writing Director | 🔲 |

All five pieces feed into the same registry entry block: `marketing_content.json` entries `2026-07-07-*`. Update `stages` and `platforms` as each step completes.

## Pending Items

| Item | Status | Notes |
|---|---|---|
| UTM mapping — technique folio content type | 🔲 Pending | Complete before first technique folio post goes live |
| EXPO scheduled publishing | ✅ Built (2026-06-28) | `publishDate` field added to expo schema. Posts with a future date are excluded at build time. GitHub Actions daily deploy deferred — configure as Action #2 above. |

## Phase 7 — Completed Items

- [x] Rewrite hero subheadline (acquisition register) — `site/src/pages/index.astro`
- [x] Write About page copy — `site/src/pages/about.astro`
- [x] Standardize all CTAs to olive-gold (#c9a96e) — `site/src/pages/index.astro`
- [x] Fix Archive card legibility (contrast/saturation) — `site/src/layouts/SectionLayout.astro`
- [x] Enrich footer (social links, privacy policy, copyright, About link) — `site/src/layouts/BaseLayout.astro`
- [x] Instagram channel brief — `Marketing/Marketing Content/Social/brief-instagram.md`
- [x] Pinterest channel brief — `Marketing/Marketing Content/Social/brief-pinterest.md`
- [x] YouTube channel brief — `Marketing/Marketing Content/Social/brief-youtube.md`
- [x] Post templates — Instagram, Pinterest, YouTube — `Marketing/Marketing Content/Social/Templates/`

## Social Media

| Platform | Brief | Templates | Account | Status |
|----------|-------|-----------|---------|--------|
| Instagram | ✓ | ✓ | instagram.com/cafeathena_themanual | Live — first reel posted (06-07 Chicken and Dumplings, 2026-06-28) |
| Pinterest | ✓ | ✓ | pinterest.com/CafeAthenaTheManual | Live — first reel posted (06-07 Chicken and Dumplings, 2026-06-28) |
| YouTube | ✓ | ✓ | youtube.com/channel/UC8TEjsxUEezQnvg9KeR4pnA | Live — first Short posted (06-07 Chicken and Dumplings, 2026-06-28) |

## Protocols

- **UTM tracking (2026-06-22):** All site links in marketing assets (social posts, reels, bios, pins, emails) must use UTM parameters before posting. Convention: `utm_source` (platform), `utm_medium` (format), `utm_campaign` (recipe slug), `utm_content` (folio ID). Save tracked URL in `Marketing/Marketing Content/Social/Recipes/[recipe-id]/` with post metadata. See Brand Manager instructions for full spec.
- **Untracked posts:** 06-07 Chicken and Dumplings Facebook reel (2026-06-22) — posted without UTM. Traffic visible in GA4 under Pages and Screens → `/06-07` but source unattributed.

## Deferred

- Social proof ("trusted by X home cooks") — needs audience first
- Newsletter capture — revisit after social channels are established
- Facebook Group — Phase 2; launch when Instagram reaches 500–1,000 followers; Q3 2026 checkpoint
