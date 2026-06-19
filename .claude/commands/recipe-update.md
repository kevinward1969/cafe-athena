---
description: Workflow for editing an already-deployed recipe or technique folio. Bumps version, sets needsRedeploy, re-runs affected pipeline stages, and prepares the entry for redeploy. Single entry point for any post-deploy content change.
---

# Recipe Update Workflow

Invoked with: `/recipe-update [id]`

Example: `/recipe-update 03-05`

Use this command any time a deployed recipe's folio content changes — corrections, additions, technique notes, restructuring. Do NOT use for pipeline-stage-only changes (e.g., adding a hero image to an undeployed recipe — use `/pipeline` for that).

---

## Phase 0 — Load Entry

1. Read `The Manual/recipes.json`. Find the entry with `"id": "[id]"`.
2. Confirm `stages.deployed: true`. If `deployed: false`, stop:
   > `[id] has not been deployed yet. Use /pipeline [id] instead.`
3. Read the folio file from `The Manual/`.
4. Print a one-line status:
   > `[id] — [title] | Version: [version] | Last deployed: [lastDeployed] | needsRedeploy: [true/false]`

---

## Phase 1 — Document the Change

Ask the user (or infer from context if already stated):

> What changed in this recipe? (e.g., "added grilling method note", "corrected bake temperature", "restructured Method phases")

Record the change description. It will be used in the version bump note and commit message.

---

## Phase 2 — Version Bump

Increment the minor version in recipes.json:
- `"1.0"` → `"1.1"`
- `"1.9"` → `"1.10"`
- `"2.3"` → `"2.4"`

Set `lastModified` to today's date.
Set `needsRedeploy: true`.

Do NOT set `lastDeployed` — that only updates after a successful deploy.

---

## Phase 3 — Stage Re-evaluation

Determine which pipeline stages may be invalidated by the change:

| Change type | Re-run? |
|---|---|
| Typo fix, phrasing correction | No stage resets needed |
| Added/removed ingredients or steps | Re-run clarityAudit, formatAudit |
| Added/removed Glossary terms | Re-run glossaryPull |
| Added/removed Keywords | Re-run keywordPull |
| Structural restructuring (sections added/removed) | Re-run clarityAudit, formatAudit, keywordPull, glossaryPull |

For each stage that needs re-running:
1. Set that stage flag to `false` in recipes.json
2. Run the appropriate audit or pull command
3. Reset the flag to `true` if clean

**Do not reset stages that are unaffected by the change.**

---

## Phase 4 — Clarity & Format Check

Regardless of change type, run a quick clarity audit if any Method steps were touched:

```bash
# Invoke Recipe Clarity Auditor agent on the folio
```

If issues found: display and stop. Resolve before continuing.
If clean: continue. Do not set `clarityAudit: false` unless the audit actually failed.

---

## Phase 5 — Registry Write

Write all updates to `The Manual/recipes.json`:
- `version` — incremented
- `lastModified` — today
- `needsRedeploy: true`
- Any stage flags that were reset and re-passed

---

## Phase 6 — Commit

Stage the folio file and `The Manual/recipes.json`. Commit with:

```
feat([id]): [brief description of change]
```

Example: `feat(03-05): add cross-reference link to beurre blanc`

Do NOT deploy in this workflow. The redeploy is handled separately — either by running `/pipeline [id]` (which will see `needsRedeploy: true` and skip to deploy) or by a batch redeploy session.

---

## Phase 7 — Handoff

Print a summary:

```
✓ [id] — [title]
  Version: [old] → [new]
  Changed: [description]
  Stages reset: [list or "none"]
  needsRedeploy: true — run /pipeline [id] or batch deploy when ready
```

---

## Update Rules

- **One commit per recipe update.** Do not bundle multiple recipe updates in one commit.
- **Never deploy in this workflow.** Redeploy is always a separate, explicit step.
- **Never reset a stage that wasn't affected.** Only invalidate what the change actually touches.
- **Always bump version on content changes.** Even a one-word correction is a version increment.
- **needsRedeploy stays true until deploy.sh confirms success.** The pipeline clears it.
