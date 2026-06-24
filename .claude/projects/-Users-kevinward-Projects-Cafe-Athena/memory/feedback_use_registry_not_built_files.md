---
name: feedback_use_registry_not_built_files
description: Use recipes.json to check recipe pipeline status — don't read built files in site/src/content/recipes/
metadata:
  type: feedback
---

When assessing whether a built recipe file (site/src/content/recipes/XX-YY.md) should be committed or is pipeline-complete, check The Manual/recipes.json first — it has the authoritative stage flags (deployed, heroImageOptimized, etc.).

**Why:** Reading the built file itself is indirect and slower. recipes.json is the single source of truth for per-recipe state.

**How to apply:** Any time a question arises about recipe pipeline status, open recipes.json rather than the built output file.
