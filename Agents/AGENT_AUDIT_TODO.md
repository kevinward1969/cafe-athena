# Agent Audit — Remediation Backlog

**Audit date:** 2026-06-10
**Audited by:** Café Athena Technical Director agent
**Status:** All tiers complete (Tiers 1–2: 2026-06-10, Tier 3: 2026-06-11).

Context: A full evaluation of the Café Athena multi-agent architecture was completed 2026-06-10. Kevin reported only minor problems in practice; the Gemini Gem generates the most revision cycles (expected for visuals). The findings below are ranked by impact.

---

## Tier 1 — Immediate (genuine failure modes)

These are live bugs in agent instructions that will silently produce wrong behavior.

### 1. Fix stale path in canonical Chef agent

**File:** `.claude/agents/Cafe Athena Chef.agent.md`
**Status:** ✅ Done 2026-06-10
**Problem:** The BUILT-IN WORKFLOWS section said "read the relevant file from `.agents/workflows/`" — this path does not exist. The correct path is `.claude/commands/`.
**Fix applied:** Replaced both occurrences in the canonical. Secondary surface was already correct. Bumped to v1.17, changelog updated.

---

### 2. Fix stale version reference in Chef canonical header

**File:** `.claude/agents/Cafe Athena Chef.agent.md`
**Status:** ✅ Done 2026-06-10
**Problem:** File header said Claude Desktop secondary was "currently v1.9" — it is actually v1.16.
**Fix applied:** Updated reference to v1.16 in the canonical header.

---

### 3. Update "Site Developer" → "Technical Director" in CLAUDE.md

**File:** `CLAUDE.md`
**Status:** ✅ Done 2026-06-10
**Problem:** Two stale "site developer" references in Key Files table descriptions and one in the Agent Propagation Rule table.
**Fix applied:** Updated all three occurrences to "Technical Director."

---

### 4. Clean up SKILLS_INDEX under Chef heading

**File:** `.claude/SKILLS_INDEX.md`
**Status:** ✅ Done 2026-06-10
**Problem:** Chef section included `astro`, `cafe-athena-site-dev`, `seo-aeo-schema-generator`, `fixing-metadata`, and `seo-images` — all belong exclusively to the Technical Director.
**Fix applied:** Removed all five from the Chef section. They remain correctly listed under the Technical Director section.

---

## Tier 2 — High Value (structural gaps worth fixing)

These don't fail silently but will produce sub-optimal agent behavior over time.

### 5. Add collection folio keyword range to Chef Mode 2

**File:** `.claude/agents/Cafe Athena Chef.agent.md` (and secondary)
**Problem:** The 8–20 keyword range for collection folios is documented in the changelog and in `format-audit.md` / `keyword-pull.md`, but not in the canonical Chef Mode 2 Output Protocol (step 8). An agent doing Mode 2 without reading the format standard will cap at 15 keywords for a collection folio, producing an audit failure.
**Fix:** Add a parenthetical to Mode 2 step 8 clarifying the range: "8–15 for standard recipe folios, 8–20 for collection folios."

---

### 6. Resolve Brand Manager Mode 2 / Mode 3 overlap

**File:** `.claude/agents/Cafe Athena Brand Manager.agent.md` (and secondary)
**Problem:** "Write social posts" triggers both Mode 2 (Marketing Execution) and Mode 3 (Content Creation). The completion criteria differ but the actual work is the same. The agent makes an arbitrary assignment.
**Fix:** Add a disambiguation rule. Suggested split: Mode 2 = strategy-level deliverables (campaigns, briefs, frameworks, plans); Mode 3 = specific content pieces (post copy, bio, headline, email). Apply this rule to both the trigger keywords and the completion criteria.

---

### 7. Add session handoff protocol to Brand Manager

**File:** `.claude/agents/Cafe Athena Brand Manager.agent.md` (and secondary)
**Problem:** The Chef has a formal SESSION HANDOFF PROTOCOL triggered by "Handoff / Close out / Goodbye." The Brand Manager has no equivalent — status doc updates are listed as completion criteria for each mode, but there's no single trigger that ensures a git commit happens at session end. Brand work accumulates uncommitted.
**Fix:** Add a SESSION HANDOFF PROTOCOL section mirroring the Chef's. Trigger: "Handoff," "Close out," "Goodbye," "Save and wrap." Actions: update `Brand/BRAND_STATUS.md` and `Marketing/MARKETING_STATUS.md`, stage changes, commit with a conventional commit message.

---

### 8. Add explicit cross-agent redirect to Brand Manager

**File:** `.claude/agents/Cafe Athena Brand Manager.agent.md` (and secondary)
**Problem:** The Brand Manager has no stated redirect protocol. If a user asks it to write site hero copy and then implement it, it has no guidance on how to hand off to the Technical Director. The Chef's OUT-OF-SCOPE REDIRECT section is the model to follow.
**Fix:** Add an OUT-OF-SCOPE REDIRECT section listing: culinary content and recipe decisions → Chef; site implementation, deploy, pipeline → Technical Director; visual image generation → Visual Director Gem.

---

## Tier 3 — Nice to Have (low urgency)

### 9. Fix broken markdown table row in Visual Director Mode 3

**File:** `Agents/Gemini-Gems/CAFÉ ATHENA - VISUAL DIRECTOR GEM INSTRUCTIONS.md`
**Problem:** The section-specific guidance table in Mode 3 has a malformed header row (`| Mood | ---- ----` — extra space breaks the table). Cosmetic, but signals the section hasn't had a review pass.
**Fix:** Correct the table header formatting. While there, check whether Mode 3's per-section guidance is specific enough — it's lighter than Mode 1's chapter-by-chapter style table.
**Remember:** This file requires Kevin to manually paste updated content into the Gemini Gem 2 configuration after any edit.

---

### 10. Add fallback language for missing reference images in Visual Director

**File:** `Agents/Gemini-Gems/CAFÉ ATHENA - VISUAL DIRECTOR GEM INSTRUCTIONS.md`
**Problem:** Reference style images are described as "attached to this Gem" — a UI-side attachment that cannot be verified by the system. If the Gem is recreated or attachments are cleared, the reference images silently disappear with no fallback instruction.
**Fix:** Add a one-paragraph fallback: "If reference images are not attached, use the written style descriptions below as your sole visual anchor — do not interpolate a generic food photography style."
**Remember:** Manual paste required into Gemini Gem 2.

---

### 11. Fatten the Technical Director's Claude Desktop secondary surface

**File:** `Agents/Claude-Desktop/TECHNICAL_DIRECTOR_INSTRUCTIONS.md`
**Problem:** The condensed Claude Desktop format intentionally omits the skills table, system assets table, and propagation rules that make the canonical stronger. If the Desktop surface is ever used for agent or tooling work, it will lack those guardrails.
**Fix:** Evaluate whether the Desktop surface is ever used for Mode 3 (Agent & Tooling Development) work. If yes, port the skills table and propagation rules in condensed form. If Desktop is only used for site work, leave it thin — that's correct by design.

---

### 12. Add session handoff protocol to Technical Director

**File:** `.claude/agents/Cafe Athena Technical Director.agent.md` (and secondary)
**Problem:** Lower urgency than Brand Manager — the Technical Director already has strong git discipline in the deploy workflow. But for non-deploy sessions (agent work, component changes), there's no formal "Handoff" trigger to ensure commits are staged and pushed.
**Fix:** Add a lightweight SESSION HANDOFF PROTOCOL matching the Brand Manager fix above.

---

## Notes for the session that picks this up

- Tier 2 items (5–8) are all Brand Manager / Chef canonical edits — do them together; the propagation and changelog work is the same for all four.
- Tier 3 items (9–12) can be deferred indefinitely or done opportunistically when touching those files for another reason.
- All canonical agent edits require: version bump in the edited file + changelog entry in `Agents/AGENT_CHANGELOG.md` + port to the relevant secondary surface + remind Kevin to paste updated secondary into Claude Desktop project settings.
- Visual Director edits require Kevin to manually paste into Gemini Gem 2 configuration — flag this when actioning items 9 or 10.
