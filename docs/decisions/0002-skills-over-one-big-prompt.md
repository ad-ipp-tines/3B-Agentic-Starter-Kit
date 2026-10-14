# 0002. Skills and a short AGENTS.md, not one big prompt

- **Status:** Accepted
- **Context:** An onboarding spans readiness, discovery, specs, builds, MCP, reviews, operations and handover. Putting all of that in one instruction file would load thousands of tokens into every session, most of them irrelevant to the task at hand.
- **Decision:** `AGENTS.md` holds only the non-negotiables and how to start (under 200 lines). Every procedure is an [Agent Skills](https://agentskills.io/specification) skill in `.claude/skills/`. Each `SKILL.md` stays under 500 lines, with detail in `references/` one level deep. `CLAUDE.md` is a one-line import of `AGENTS.md`. Skills with side effects set `disable-model-invocation: true`, so they run only when a person calls them.
- **Why:** context is a finite attention budget, and only about 100 tokens per skill stay resident until it's used ([Anthropic, context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents); [Agent Skills spec](https://agentskills.io/specification)). Cursor loads `.claude/skills/` and reads `AGENTS.md`; Claude Code reads `CLAUDE.md` ([Cursor skills](https://cursor.com/docs/context/skills), [Claude Code memory](https://code.claude.com/docs/en/memory)). That gives one copy for both editors.
- **Consequences:** skills must have precise descriptions, because the description is what triggers them. `scripts/validate.py` enforces names, description length and file size.
- **Revisit when:** either editor drops `.claude/skills/` compatibility.
