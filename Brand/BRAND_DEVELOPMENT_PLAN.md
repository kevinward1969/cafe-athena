# Café Athena — Brand Development Plan

**Status:** Phase 1 starting
**Last Updated:** 2026-06-11
**Tracking:** See `BRAND_TODO.md` for task-level progress

---

## Overview

This plan covers the full first-phase brand build for Café Athena — from identity foundation through visual system and into marketing activation. Work is sequenced by dependency: strategy must precede voice, voice must precede copy, visual identity must precede asset generation.

**End state:** A complete `BRAND_GUIDELINES.md`, author identity in all three formats, two audience personas, a visual system spec, and a briefed Visual Director Gem capable of producing on-brand assets beyond cookbook images.

---

## Surface Assignments

| Surface | Responsible For |
|---------|----------------|
| **Brand Manager** (Claude Desktop) | Strategy, positioning, author identity, voice & tone, personas, written guidelines sections |
| **Visual Director Gem** (Gemini Gem 2) | Visual asset generation — cookbook images (current scope) + brand asset concepts (new scope) |
| **Technical Director** (Claude Code) | Site copy implementation, template builds, deploy |
| **Claude Code** (orchestration) | Plan tracking, cross-phase coordination, file management |

---

## Phase 1 — Brand Foundation

**Goal:** Define the strategic core — what Café Athena is, who it's for, and what it stands for. Everything downstream depends on this.

**Deliverables:**
- Mission statement
- Brand promise (one sentence)
- Positioning statement (formal)
- Core values (3–5, with definitions)
- Brand archetype

**Primary surface:** Brand Manager
**Resources to load:** `dm_2019_key_brand_elements.pdf`, `core_values_worksheet.docx`, `positioning_statement_worksheet.docx`
**Output file:** `BRAND_GUIDELINES.md` §1 (Overview & Brand Identity)

---

## Phase 2 — Author Identity

**Goal:** Establish Kevin Ward as the credible, specific voice behind the book. Not a generic food blogger — a person with a real culinary point of view.

**Deliverables:**
- Author backstory (long-form narrative)
- Author bio — long version (250–300 words, site/press)
- Author bio — short version (2–3 sentences, site blurb)
- Author bio — social versions (per-platform character limits: Instagram, YouTube, Pinterest, Facebook)
- Author photo brief (for Visual Director or external photography)

**Primary surface:** Brand Manager
**Resources to load:** `Developing Your Personal Brand.docx`
**Output files:** `Author/bio-long.md`, `Author/bio-short.md`, `Author/bio-social.md`

---

## Phase 3 — Audience Personas

**Goal:** Define who Café Athena is actually for — specific people, not demographics. Personas drive voice, copy tone, content priorities, and channel selection.

**Deliverables:**
- Persona 1: The Serious Home Cook (primary)
- Persona 2: The Culinary Curious (secondary)
- Each persona: name, demographics, goals, pain points, content consumption habits, why they'd find Café Athena, what would lose them

**Primary surface:** Brand Manager
**Resources to load:** `buyer_persona_template.xlsx`
**Output files:** `Personas/persona-serious-home-cook.md`, `Personas/persona-culinary-curious.md`

---

## Phase 4 — Voice & Tone

**Goal:** Define two distinct registers — how Café Athena writes inside the book vs. how it speaks in marketing contexts. These are different tones for different jobs.

**Deliverables:**
- Manuscript register spec (authority, craft, warmth — for cookbook copy)
- Acquisition register spec (welcoming, curious, accessible — for site/social)
- 5–8 writing examples per register (do/don't pairs)
- Forbidden phrases list

**Primary surface:** Brand Manager
**Output file:** `BRAND_GUIDELINES.md` §5–6 (Voice & Tone sections)

---

## Phase 5 — Visual Identity

**Goal:** Establish the complete visual system: color, typography, photography standards, and asset specs. This phase also expands the Visual Director Gem's brief to cover brand assets beyond cookbook images.

**Deliverables:**
- Full color palette (primary, secondary, neutral, functional) with hex values
- Typography system — display, body, accent (web + print)
- Logo/wordmark brief (for external design or Firefly concept generation)
- Photography standards (already partially defined in Visual Director Gem; formalize here)
- Visual asset spec for social templates
- Updated Visual Director Gem brief to cover brand asset modes

**Primary surface:** Brand Manager (spec) + Visual Director Gem (generation)
**Output files:** `BRAND_GUIDELINES.md` §3–4, `Creative/visual-system.md`, updated Visual Director Gem instructions

---

## Phase 6 — Brand Guidelines Completion

**Goal:** Assemble all phase outputs into the complete `BRAND_GUIDELINES.md`. The document becomes the single reference for all brand decisions.

**Deliverables:**
- Complete `BRAND_GUIDELINES.md` — all 10 sections from stub outline
- Internal QA against brand scorecard

**Primary surface:** Brand Manager + Claude Code
**Resources to load:** `brand_strategy_scorecard.xlsx`
**Output file:** `BRAND_GUIDELINES.md` (complete)

---

## Phase 7 — Marketing Activation Handoff

**Goal:** Hand the completed brand system off to the marketing layer. This phase triggers the open items in `Marketing/MARKETING_STATUS.md`.

**Deliverables:**
- Site copy rewrites (hero, about, CTAs) using acquisition register
- Social channel setup (Instagram, Pinterest, YouTube — per `Marketing/Social/channels.md`)
- Social post templates (per platform)
- About page / author section

**Primary surface:** Brand Manager (copy) + Technical Director (site implementation)
**Dependency:** Phases 1–6 complete

---

## Dependencies Map

```
Phase 1 (Foundation)
  └── Phase 2 (Author Identity)     ← can run in parallel with Phase 3
  └── Phase 3 (Personas)            ← can run in parallel with Phase 2
      └── Phase 4 (Voice & Tone)    ← requires both Phase 1 and Phase 3
          └── Phase 5 (Visual)      ← requires Phase 1; can partially run with Phase 4
              └── Phase 6 (Guidelines Complete)
                  └── Phase 7 (Marketing Activation)
```

**Phases 2 and 3 can run in parallel.** All other phases are sequential.

---

## Key References

| File | Purpose |
|------|---------|
| `Resources/INDEX.md` | Which reference docs to load for each phase |
| `BRAND_TODO.md` | Task-level tracking (this plan's execution layer) |
| `BRAND_STATUS.md` | High-level status — updated at phase completion |
| `Marketing/MARKETING_STATUS.md` | Phase 7 activation tracker |
| `Agents/AGENT_CHANGELOG.md` | Log any agent updates triggered by this work |
