# The onboarding programme

Six phases, each ending with exit criteria a person signs off. **The canonical checklist is [`programme.md`](../.claude/skills/3b-onboard/references/programme.md)**; this page, the success-plan template and the router's table are summaries of it, and `3b-onboard` tracks where you are.

| Phase | The customer gets | Typical length | Kit skills |
|---|---|---|---|
| 0 · Readiness | Safe access: SSO, spaces and groups, GitSync, editors on MCP, connectors, AI provider | Week 1 | `3b-readiness` |
| 1 · Discover | A ranked backlog and a signed-off spec for the first workflow | Week 1–2 | `3b-discover`, `3b-spec` |
| 2 · First workflow | One deterministic workflow live through a reviewed PR, with step tests and a runbook | Week 2–3 | `3b-build-loop`, `3b-review`, `3b-operate` |
| 3 · Agentic | One AI-assisted workflow with schema, guardrails, approvals and a scored eval set | Week 4–6 | `3b-spec`, `3b-build-loop`, `3b-review` |
| 4 · MCP | Builders on MCP from their editors; optionally one workflow serving tools to their AI assistants | Week 5–8 | `3b-mcp` |
| 5 · Operate and scale | Weekly reviews, conventions in every space, a handover guide; the team ships alone | Week 8–12 | `3b-operate`, `3b-handover` |

## Roles (RACI)

| Activity | Customer platform owner | Workflow owner | Builders | Security reviewer | CSE |
|---|---|---|---|---|---|
| Access, spaces, GitSync, connectors | A/R | C | I | C | C |
| Backlog and priorities | C | A | C | I | R |
| Spec sign-off | I | A | R | C (routes, approvals) | R |
| Build and step tests | I | C | A/R | I | R (pairing) |
| Review and merge to Live | C | A | R | C (public routes, MCP) | R (review) |
| Operations and weekly review | A | R | R | I | C |

## Principles for running sessions

- **Their hands on the keyboard.** The customer's builders drive the editor agent; the CSE coaches.
- **One workflow at a time,** start to finish, before the next one.
- **Show the gates working.** Let a step test fail on purpose once, so the team sees the safety net.
- **Write things down.** Decisions go in `onboarding/progress.md` with reasons, because the next builder wasn't in the room.
