# Café Athena — Brand Development Plan

**Status:** Phase 8 complete — all three social channels live with first content posted
**Last Updated:** 2026-06-28
**Tracking:** See `BRAND_TODO.md` for task-level progress

---

## Overview

This plan covers the full brand build for Café Athena — from scope definition through visual system and into marketing activation. Work is sequenced by dependency: scope must precede strategy, strategy must precede persona, persona and strategy must precede voice, voice must precede identity copy.

**End state:** A complete `BRAND_GUIDELINES.md`, a defined project scope, author identity written in the correct voice for the correct audience, a full visual system, and a briefed Visual Director Gem capable of producing on-brand assets beyond cookbook images.

---

## Surface Assignments

| Surface | Responsible For |
|---------|----------------|
| **Brand Manager** (Claude Desktop) | Strategy, positioning, author identity, voice & tone, personas, written guidelines sections |
| **Visual Director Gem** (Gemini Gem 2) | Visual asset generation — cookbook images (current scope) + brand asset concepts (new scope) |
| **Technical Director** (Claude Code) | Site copy implementation, template builds, deploy |
| **Claude Code** (orchestration) | Plan tracking, cross-phase coordination, file management |

---

## Phase 1 — Project Scope Definition

**Status: Complete ✓**

**Goal:** Define what Café Athena is and is not before any brand strategy is written. Everything downstream — positioning, voice, author bios, social copy — depends on a clear answer to "what is this thing?"

**Deliverables:**

- Scope statement — what the project covers (chapters, content types, technique range) ✓
- Out-of-scope statement — what it explicitly does not cover ✓
- Format and delivery definition — digital-first, how it is used, what it is not (not a blog, not a social account, not a restaurant guide) ✓
- Problem/solution statement — the specific problem it solves for the reader ✓

**Primary surface:** Brand Manager
**Output file:** `Brand/BRAND_SCOPE.md` — complete 2026-06-24

---

## Phase 2 — Brand Foundation

**Status: Complete ✓**

**Goal:** Define the strategic core — what Café Athena stands for. Informed by the scope definition.

**Deliverables:**

- Mission statement ✓
- Brand promise ✓
- Positioning statement ✓
- Core values (6 written) ✓
- Brand archetype ✓

**Output file:** `BRAND_GUIDELINES.md` §1

**Note:** May require minor revision once Phase 1 scope document is written, to ensure positioning reflects the defined scope precisely.

---

## Phase 3 — Audience Personas

**Status: Complete ✓ — cross-check deferred**

**Goal:** Define who Café Athena is actually for. Personas drive voice, copy tone, content priorities, and channel selection.

**Deliverables:**

- Persona 1: The Serious Home Cook ✓
- Persona 2: The Culinary Curious ✓
- Persona 3: The Kitchen Experimenter ✓
- Cross-check all personas against positioning statement ← deferred, not yet done

**Output files:** `Personas/persona-serious-home-cook.md`, `Personas/persona-culinary-curious.md`, `Personas/persona-kitchen-experimenter.md`

---

## Phase 4 — Voice & Tone

**Status: Complete ✓**

**Goal:** Define two distinct registers — how Café Athena writes inside the book vs. how it speaks in marketing contexts.

**Deliverables:**

- Manuscript register spec ✓
- Acquisition register spec ✓
- 8 do/don't pairs — manuscript register ✓
- 8 do/don't pairs — acquisition register ✓
- Forbidden phrases list (21 entries) ✓

**Output file:** `BRAND_GUIDELINES.md` §5–6

---

## Phase 5 — Author Identity

**Status: Complete ✓**

**Goal:** Establish Kevin Ward as the credible, specific voice behind the book. Bios are written in the acquisition register voice (Phase 4) and speak to the defined personas (Phase 3). This phase comes after voice and personas — not before — so the copy reflects both.

**Deliverables:**

- Author backstory (long-form narrative) ✓ — in `BRAND_GUIDELINES.md` §2
- Author bio — long version (250–300 words, site/press) ✓ — `Author/bio-long.md` — v1.0 2026-06-28
- Author bio — short version (2–3 sentences, site blurb) ✓ — `Author/bio-short.md` — v1.0 2026-06-28
- Author bio — social versions (per-platform, per acquisition register) ✓ — `Author/bio-social.md` — v1.0 full revision 2026-06-28 (all four platforms: Instagram, YouTube, Pinterest, Facebook)
- Author photo brief ✓ — `Author/photo-brief.md`
- Solo author headshot — still needed (specs in photo brief)

**Primary surface:** Brand Manager
**Resources to load:** `Developing Your Personal Brand.docx`
**Output files:** `Author/bio-long.md`, `Author/bio-short.md`, `Author/bio-social.md`

---

## Phase 6 — Visual Identity

**Status: Complete ✓**

**Goal:** Establish the complete visual system: color, typography, photography standards, and asset specs.

**Deliverables:**

- Color palette ✓
- Typography system ✓
- Logo/wordmark (delivered — three SVG variants) ✓
- Photography standards ✓
- Social template visual specs ✓
- §8 Visual Asset System: Educational/Companion Content ✓
- §9 Asset Naming & Specifications ✓
- Visual Director Gem brief expansion for brand asset modes ← deferred to when social channels are active

**Output files:** `BRAND_GUIDELINES.md` §3–4, §7–9, `Creative/visual-system.md`

---

## Phase 7 — Brand Guidelines Completion

**Status: Complete ✓ — scorecard review skipped**

**Goal:** Assemble all phase outputs into the complete `BRAND_GUIDELINES.md`. Revisit once Phase 5 (author bios) revisions are done.

**Deliverables:**

- All 10 sections complete ✓
- Full consistency QA ✓
- Brand strategy scorecard review ← skipped; complete before Phase 8 opens

**Primary surface:** Brand Manager + Claude Code
**Resources to load:** `brand_strategy_scorecard.xlsx`
**Output file:** `BRAND_GUIDELINES.md`

---

## Phase 8 — Marketing Activation

**Status: Complete ✓**

**Goal:** Hand the completed brand system off to the marketing layer.

**Deliverables:**

- Site copy rewrites (hero, about, CTAs) using acquisition register ✓
- Social channel setup (Instagram, Pinterest, YouTube) ✓
- Social post templates (per platform) ✓
- About page / author section ✓

**Primary surface:** Brand Manager (copy) + Technical Director (site implementation)
**Dependency:** Phases 1–7 complete

**Completed state:**

- Instagram live (instagram.com/cafeathena_themanual) — first reel posted (06-07 Chicken and Dumplings, 2026-06-28) ✓
- Pinterest live (pinterest.com/CafeAthenaTheManual) — first reel posted (06-07 Chicken and Dumplings, 2026-06-28) ✓
- YouTube live (youtube.com/channel/UC8TEjsxUEezQnvg9KeR4pnA) — first Short posted (06-07 Chicken and Dumplings, 2026-06-28) ✓
- Channel briefs written for all three platforms ✓
- Post templates exist for all three platforms ✓
- YouTube banner finalized and uploaded (`Brand/Social/YouTube/CafeAthenaTheManual-YouTubeBanner01.png`) ✓

**Deferred (Phase 8 follow-on):**

- Brand strategy scorecard review (`brand_strategy_scorecard.xlsx`) — skipped at Phase 7, still outstanding
- Visual Director Gem brief expansion for brand asset modes — activate when social channels need custom graphics beyond reel templates
- Cross-check personas against positioning statement — deferred from Phase 3

---

## Dependencies Map

```
Phase 1 (Scope Definition)
  └── Phase 2 (Brand Foundation)
  └── Phase 3 (Audience Personas)      ← can run in parallel with Phase 2
        └── Phase 4 (Voice & Tone)     ← requires Phase 2 + Phase 3
              └── Phase 5 (Author Identity)  ← requires Phase 4 + Phase 3
Phase 2 (Brand Foundation)
  └── Phase 6 (Visual Identity)        ← can run in parallel with Phases 3–5
        └── Phase 7 (Guidelines Complete)  ← requires all phases
              └── Phase 8 (Marketing Activation)
```

---

## Key References

| File | Purpose |
|------|---------|
| `Brand/BRAND_SCOPE.md` | Project scope definition — Phase 1 output, complete 2026-06-24 |
| `Resources/INDEX.md` | Which reference docs to load for each phase |
| `BRAND_TODO.md` | Task-level tracking |
| `BRAND_STATUS.md` | High-level status — updated at phase completion |
| `Marketing/MARKETING_STATUS.md` | Phase 8 activation tracker |
| `Agents/AGENT_CHANGELOG.md` | Log any agent updates triggered by this work |
