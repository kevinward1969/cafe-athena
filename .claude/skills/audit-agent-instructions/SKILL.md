---
name: audit-agent-instructions
description: Audits all Café Athena AI agent instruction files for version sync, missing sections, and cross-platform consistency. Compares canonical .claude/agents/ masters against Claude Desktop and Gemini Gem secondary surfaces. Invoke when agent files are updated or when surfaces may have drifted.
---

# Audit Agent Instructions

Audit all Café Athena agent instruction surfaces for version skew, missing sections, and cross-platform drift.

## When to Use

- After updating any canonical `.claude/agents/*.agent.md` file
- Before a session-handoff commit that includes agent changes
- Periodically to catch drift between surfaces
- When behavior of Claude Desktop or Gemini sessions feels inconsistent with Claude Code

## Surface Map

| Canonical Master | Secondary Surfaces |
|---|---|
| `.claude/agents/Cafe Athena Chef.agent.md` | `Agents/Claude-Desktop/PROJECT_INSTRUCTIONS.md`, `Agents/Gemini-Gems/CAFÉ ATHENA - CHEF GEM INSTRUCTIONS.md` |
| `.claude/agents/Cafe Athena Brand Manager.agent.md` | `Agents/Claude-Desktop/BRAND_MANAGER_INSTRUCTIONS.md` |
| `.claude/agents/Cafe Athena Technical Director.agent.md` | `Agents/Claude-Desktop/TECHNICAL_DIRECTOR_INSTRUCTIONS.md` |
| `Agents/Gemini-Gems/CAFÉ ATHENA - VISUAL DIRECTOR GEM INSTRUCTIONS.md` | Standalone — no canonical; audit for internal quality only |

## Audit Protocol

### Phase 1 — Inventory

Read all files in the surface map in parallel. For each file record:
- Version number from header
- Date of last update
- Section headings present

### Phase 2 — Version Check

For each canonical master:
1. Extract its version number
2. Extract the version number from each secondary surface
3. Check whether the canonical's header comment references the correct secondary version (e.g., `currently v1.18`)
4. Flag any skew: canonical ahead of secondary, or canonical's pointer stale

### Phase 3 — Section Comparison

Compare secondary surfaces to their canonical master. Flag:

**CRITICAL — blocks correct behavior:**
- A section present in canonical that is entirely absent from secondary AND is load-bearing for the agent's core task (e.g., Mode 2 Output Protocol step missing, Stop Points missing)
- A constraint that is present in canonical but absent from secondary (safety blocks, HACCP rules, format-standard refresh step)

**MODERATE — degrades quality:**
- Skills tables missing from secondary (agent won't proactively invoke skills)
- Session start files missing (agent starts without full context)
- Propagation rule missing from secondary (agent won't trigger version bumps)

**MINOR — informational:**
- Section exists in canonical but condensed in secondary (acceptable for platform-appropriate trimming)
- Wording differences that don't change behavior

**Platform-appropriate — do NOT flag:**
- Claude Desktop-specific sections (Do Not Repopulate Internal Memory, CLAUDE CODE HANDOFF block)
- Gemini-specific structures (version history tables, TOC, keyword-based mode detection)
- ECC skills absent from Desktop surfaces (not applicable in Claude Desktop)
- Standalone Gemini Gems with their own versioning

### Phase 4 — Report

Produce the audit report in this format:

```
Agent Instruction Audit
═══════════════════════════════════════

Surfaces audited: N files
Issues found: N critical / N moderate / N minor

CRITICAL
────────
[Agent name] — [surface file]
Issue: [description]
Fix: [exact change needed]

MODERATE
────────
[same format]

MINOR
─────
[same format]

CLEAN SURFACES
──────────────
[list surfaces with no issues]

Recommended actions (in priority order):
1. [action]
2. [action]
```

### Phase 5 — Apply Fixes (optional)

If the user confirms, apply all CRITICAL and MODERATE fixes directly:

1. Edit the secondary surface file
2. Bump the version number in the secondary surface header
3. Update the canonical master's secondary surface pointer to the new version
4. Add an entry to `Agents/AGENT_CHANGELOG.md`
5. Remind Kevin which Claude Desktop projects need a paste action

Do not apply MINOR fixes without explicit instruction.

## Known Platform Differences (Never Flag)

These differences between canonical and secondary surfaces are intentional:

**Chef — Claude Desktop only:**
- "Do Not Repopulate Internal Memory" clause — addresses Claude Desktop Project Memory feature
- `CLAUDE CODE HANDOFF` block after Mode 2 — triggers `/register-recipe` in Claude Code
- `/pipeline` listed as primary entry point — Desktop users run it in Claude Code

**Chef — Gemini Gem only:**
- Full version history table
- Table of Contents
- Keyword-based mode detection (Gemini doesn't do intent inference as reliably)
- Steelman check listed under Stop Points (structural difference, not behavioral)
- Own `v3.x` version series independent of canonical `v1.x`

**Brand Manager — Claude Desktop:**
- Resource library lists actual file paths instead of INDEX pointers (appropriate — Desktop can't read binary files the same way)
- ANTI-SYCOPHANCY and DECISION PROTOCOL sections condensed or absent (platform trimming)

**Technical Director — Claude Desktop:**
- ECC skills absent from skills table (not applicable in Desktop)
- `.claude/SKILLS_INDEX.md` absent from session start (not meaningful in Desktop)

## Version Bump Rule

After applying any fix to a secondary surface:
1. Bump the secondary surface version (e.g., `v1.17` → `v1.18`)
2. Update the canonical master's pointer comment to match (e.g., `currently v1.18`)
3. Add to `Agents/AGENT_CHANGELOG.md`:
   ```
   ## [Agent Name] vX.Y — YYYY-MM-DD
   - [what changed and why]
   ```
