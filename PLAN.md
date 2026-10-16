# Plan: from bootstrap to v1

## Why this repository exists

Tines 3B is code-first and MCP-native. AI writes the code, steps run as code, and editors act on the tenant through MCP. Building this way is fast, and it needs the same controls as any other code path to production. This kit turns that into a repeatable onboarding method for enterprise customers. It replaces our earlier Stories-oriented starter kit for 3B work (the Stories kit stays for Stories customers).

## Goals

1. A customer team ships its **first deterministic workflow to Live within three weeks**, through a reviewed PR with step tests.
2. By week six, the team ships **one AI-assisted workflow** with an eval set, guardrails and approvals.
3. Builders use **MCP from their editors** under their own permissions. Where it's useful, a workflow serves tools to the customer's AI assistants, safely.
4. The customer **runs the next workflow without us**: conventions installed, weekly review owned, handover guide delivered.

## Non-goals (v1)

- A multi-agent swarm, or autonomous publishing.
- Migrating Stories estates wholesale (the official `tines-export-to-3b` skill handles one-off rebuilds).
- A public edition (decided at M5; see ADR 0010).

## Milestones

| # | Milestone | Done when | Who |
|---|---|---|---|
| M0 | **Bootstrap** (this commit) | Rules, 9 skills, 4 subagents, guard hooks, templates, 12 ADRs, docs, evals, prompts; `validate.py` passes | CSE |
| M1 | **Verify on a sandbox tenant** | `docs/VERIFY.md` V1–V8 and V11–V14 closed. One end-to-end dry run of phases 0–2 on a sandbox (readiness → spec → build → PR → review → merge), which is also the demo dry run (`demo/README.md`). Kit fixes merged. Deferred review items done: trim `docs/03-agentic-architecture.md` §2 to concept / what / where, add a 15-line synthetic session transcript to `docs/04-setup-cursor-and-claude-code.md` | CSE + Cursor (Tines laptop), using `prompts/01-cursor-continue-building.md` |
| M2 | **Onboarding guide and Launchpad** | `docs/guide/` chapters written. A 3B webpage workflow ("Launchpad") that walks a team through the programme, behind SSO or space auth | 3B, using `prompts/02-3b-build-onboarding-guide.md`; reviewed by the CSE |
| M3 | **Automated evals** | Trigger checks and code-graded golden tasks run headless in CI. A no-skill baseline recorded for each skill | Cursor + CSE |
| M4 | **Pilot** | One customer team through phases 0–3. Time to first Live workflow measured. Lessons recorded as ADRs or skill changes | CSE + customer |
| M5 | **v1** | Pilot lessons folded in. Golden tasks at or above target. Decision on a public edition | CSE |

## Workstreams

| Workstream | What | Where |
|---|---|---|
| Product truth | Keep `docs/02-availability.md` current against the product updates and `skills.lock` | `docs/`, `skills.lock` |
| Method | Skills, subagents, hooks and templates | `.claude/`, `scripts/`, `kit/` |
| Quality | Golden tasks, rubric, CI | `evals/`, `.github/` |
| Enablement | The guide, the Launchpad, a demo script | `docs/guide/`, prompts |

## Risks

| Risk | Mitigation |
|---|---|
| 3B changes fast; skills go stale | Pin official skills; monthly availability review; golden tasks on every bump |
| MCP tool names unpublished | Discover per tenant (`3b-readiness`); guard by pattern until V1 closes |
| Over-engineering scares customers off (the lesson from the earlier kit) | Phase-gated programme; one workflow at a time; `3b-onboard` shows only the next step |
| Agents act beyond intent | Hooks, read-only subagents, people-only publishing, fresh review |
| Internal or customer data leaking into the kit | Private repo; status labels; `validate.py` secret scan plus a local denylist |

## Success measures

- Days from kickoff to first Live workflow (target: 15 working days or fewer).
- Share of Live workflows with step tests for every step (target: 100%).
- First-pass review verdicts "ready" (track the trend; it should rise as conventions settle).
- Open VERIFY items (target: zero for anything the skills rely on).
