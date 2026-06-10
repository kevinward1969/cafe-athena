# Café Athena — Skills Index

Maps skills to agents and trigger conditions. Agents read this on startup and invoke the matching skill when the task qualifies.

**Source key:**

- `✅ project` — installed in `.claude/skills/` (ready now)
- `✅ global` — installed in `~/.claude/skills/` (ready now)
- `✅ ecc` — `everything-claude-code:name` (ready now)
- `📦 antigravity` — in `/Users/kevinward/Projects/Shared Skills/antigravity-awesome-skills/` (copy to skills folder to activate)
- `📦 findskills` — in `/Users/kevinward/Projects/Shared Skills/FindSkills_AI/` (copy to skills folder to activate)

---

## Café Athena Chef

| Skill | Source | Invoke when… |
|-------|--------|-------------|
| `avoid-ai-writing` | ✅ project | Reviewing or editing any prose before committing |
| `astro` | ✅ project | Any file in `site/` — pages, layouts, content config, build errors |
| `cafe-athena-site-dev` | ✅ project | Site changes, deploys, image pipeline |
| `seo-aeo-schema-generator` | ✅ project | Adding structured data to recipe pages |
| `fixing-metadata` | ✅ project | Editing `<head>`, OG tags, site-wide metadata |
| `seo-images` | ✅ project | Hero image processing, `site/public/images/` audit |

---

## Café Athena Brand & Marketing Manager

| Skill | Source | Invoke when… |
|-------|--------|-------------|
| `brand-voice` | ✅ global | Developing or auditing voice/tone in `BRAND_GUIDELINES.md` |
| `audience-persona-builder` | ✅ global | Building any file in `Brand/Personas/` |
| `copywriting` | ✅ global | Writing conversion-focused copy (CTAs, email, site) |
| `landing-page-copywriter` | ✅ global | Hero copy, subheadlines, About page |
| `social-content` | ✅ global | Social posts, `Marketing/Social/Templates/` content |
| `marketing-psychology` | ✅ global | Making copy or CTA decisions |
| `marketing-strategy` | ✅ global | `Marketing/` planning documents |
| `competitive-landscape` | ✅ global | Positioning Café Athena against other food/cookbook brands |
| `seo-fundamentals` | ✅ global | SEO decisions in site copy or metadata |
| `seo-content-writer` | ✅ global | SEO-optimised copy for site pages |
| `avoid-ai-writing` | ✅ project | Before finalising any prose that will be published |
| `beautiful-prose` | ✅ global | About page, long-form brand prose, editorial copy |
| `logo-brand-identity-creator` | 📦 findskills | `Brand/Creative/` — logo rules, visual standards |
| `image-prompt-generator` | 📦 findskills | Generating Gemini image prompts for hero or social assets |
| `ux-copywriting` | 📦 findskills | Microcopy, button labels, error states, onboarding text |
| `copy-editing` | 📦 antigravity | Reviewing and tightening copy before it goes live |
| `seo-aeo-keyword-research` | 📦 antigravity | Keyword targeting and content strategy planning |
| `seo-aeo-meta-description-generator` | 📦 antigravity | Meta titles and descriptions for site pages |
| `keyword-extractor` | 📦 antigravity | Extracting SEO keywords from recipe or site content |
| `seo-aeo-blog-writer` | 📦 antigravity | The Expo editorial blog posts (when that section launches) |

---

## Café Athena Site Developer *(planned)*

| Skill | Source | Invoke when… |
|-------|--------|-------------|
| `astro` | ✅ project | Any Astro site work — pages, layouts, routing, content collections |
| `cafe-athena-site-dev` | ✅ project | Site changes, deploy pipeline, image pipeline |
| `seo-aeo-schema-generator` | ✅ project | Adding structured data to recipe pages |
| `fixing-metadata` | ✅ project | `<head>`, OG tags, site-wide metadata |
| `seo-images` | ✅ project | Hero image optimization and audit |
| `everything-claude-code:architect` | ✅ ecc | Architecture decisions for the site or agent system |
| `everything-claude-code:blueprint` | ✅ ecc | Planning complex multi-session technical work |
| `everything-claude-code:agentic-engineering` | ✅ ecc | Building or modifying agents and pipelines |
| `everything-claude-code:autonomous-loops` | ✅ ecc | Designing autonomous agent loop patterns |
| `everything-claude-code:orchestrate` | ✅ ecc | Multi-agent orchestration and handoffs |
| `everything-claude-code:tdd` | ✅ ecc | Writing tests for pipeline scripts or site features |
| `everything-claude-code:e2e` | ✅ ecc | End-to-end testing of the Astro site |
| `everything-claude-code:security-review` | ✅ ecc | Security review of site or pipeline |
| `everything-claude-code:code-reviewer` | ✅ ecc | Production code review before major changes |
| `everything-claude-code:context-budget` | ✅ ecc | Diagnosing agent context window issues |
| `everything-claude-code:claude-api` | ✅ ecc | Claude API usage, prompt caching, SDK patterns |
| `everything-claude-code:doc-updater` | ✅ ecc | Updating codemaps and documentation |
| `everything-claude-code:mcp-server-patterns` | ✅ ecc | MCP server integrations |
| `everything-claude-code:deployment-patterns` | ✅ ecc | Deploy workflow design |
| `everything-claude-code:python-reviewer` | ✅ ecc | Reviewing pipeline scripts in `scripts/` |
| `tailwind-patterns` | 📦 antigravity | Tailwind CSS v4 — `global.css`, design tokens, component styles |
| `tailwind-design-system` | 📦 antigravity | Extending the design system — color tokens, component variants |
| `bash-scripting` | 📦 antigravity | Writing or modifying pipeline scripts |
| `bash-linux` | 📦 antigravity | macOS shell operations, deploy scripting |
| `prompt-engineering-patterns` | 📦 antigravity | Advanced agent prompt design and optimization |
| `tool-design` | 📦 antigravity | Designing tools for agent use |
| `agent-tool-builder` | 📦 antigravity | Building Claude Code tools and MCP integrations |
| `agent-prompt-chain-designer` | 📦 findskills | Designing multi-step agent prompt chains |
| `instructions-writer` | 📦 findskills | Writing agent instructions or slash command definitions |
| `indexing-issue-auditor` | 📦 antigravity | Technical SEO — crawl budget, indexing errors |
| `error-detective` | 📦 antigravity | Debugging errors in pipeline scripts or site build |
| `documentation-templates` | 📦 antigravity | Writing README files, API docs, code comments |
| `skill-suggester` | 📦 antigravity | Identifying new skill needs from recurring patterns |

---

## Café Athena Content Writer & Social Media Manager *(planned)*

| Skill | Source | Invoke when… |
|-------|--------|-------------|
| `social-content` | ✅ global | Writing social posts for any platform |
| `social-media-post` | ✅ global | Platform-optimized posts with hooks and hashtags |
| `content-marketer` | ✅ global | Content strategy and distribution planning |
| `copywriting` | ✅ global | Conversion-focused copy |
| `avoid-ai-writing` | ✅ project | Before publishing any content |
| `beautiful-prose` | ✅ global | Long-form editorial content for The Expo |
| `storytelling-mastery` | ✅ global | Narrative structure for editorial posts |
| `seo-content-writer` | ✅ global | SEO-optimised content for site pages |
| `seo-content-planner` | ✅ global | Content calendar and topic cluster planning |
| `everything-claude-code:content-engine` | ✅ ecc | Platform-native content systems, content calendars |
| `everything-claude-code:crosspost` | ✅ ecc | Distributing content across X, LinkedIn, Threads, Bluesky |
| `everything-claude-code:article-writing` | ✅ ecc | Long-form articles, guides, newsletter issues |
| `seo-aeo-blog-writer` | 📦 antigravity | The Expo blog posts |
