# Prompt for Cursor (Tines laptop): continue building the kit

Paste everything below the line into Cursor's agent chat, opened at the root of a fresh clone of this repository.

Before you start, a person sets up four things:
- access to the private repository;
- the Tines 3B Cursor plugin, connected to a **sandbox** tenant with OAuth;
- gh 2.90 or later;
- a sandbox space Git-synced to a throwaway GitHub repository.

---

You're continuing work on the **3B Agentic Starter Kit**, a private repository that onboards enterprise teams onto Tines 3B with an agentic build method. Read these before doing anything: `README.md`, `AGENTS.md`, `PLAN.md`, `docs/03-agentic-architecture.md`, `docs/decisions/README.md`, `docs/02-availability.md` and `docs/VERIFY.md`. Follow `AGENTS.md` and `prompts/03-sync-protocol.md` at all times.

**Your milestones are M1 (verify on a sandbox tenant) and M3 (automated evals) in `PLAN.md`.** Work in small pull requests, one topic each, on branches named `cursor/<topic>`.

## Task 1: Close the VERIFY register (`docs/VERIFY.md`, V1–V8)

For each item:
1. Show me a short plan and wait for "yes".
2. Test it on the **sandbox** tenant only, with synthetic data.
3. Record the evidence: what you ran, what you saw, and a screenshot path or output excerpt with no secrets.
4. Update `docs/02-availability.md`, change the label, and remove the row from `docs/VERIFY.md`.
5. If V1 (the MCP tool list) closes, tighten `scripts/hooks/guard.py` to the exact publish, delete and access tool names, and add a test case to its docstring.

## Task 2: Dry-run the programme, phases 0–2, on the sandbox

Use a synthetic use case: "triage EDR alerts and open a ticket". Run the kit's own skills in order:
`/3b-onboard` → `3b-readiness` → `3b-discover` → `3b-spec` → `/3b-build-loop` → `3b-review` (in a new chat) → a person merges → `3b-operate`.

Create a scratch engagement repository with `scripts/bootstrap.sh engagement ../sandbox-engagement` and clone the sandbox space repository into its `space/`. Keep a friction log: every place a skill was unclear, wrong about 3B, or asked an unnecessary question. Fix the skills in this repository, one PR per skill, each citing the friction it fixes.

## Task 3: Run the golden tasks

Follow `evals/README.md` for every skill. Record the results in a PR description: pass rate per skill, failures and causes. Add scenarios for any failure mode you found in Task 2.

## Task 4: Write the walkthrough guide (`docs/guide/`)

Using the outline in `docs/guide/README.md`, write the chapters as Markdown, using the sandbox dry run as the worked example (synthetic data only). Use plain language, short sentences and second person. Put one Mermaid diagram where a picture helps. Label every 3B capability Available, Verify or Not available, with a public link. Open one PR per two or three chapters. 3B builds the interactive version of this guide (prompt 02) from these files, so keep headings stable.

## Task 5 (M3): Automate evals

Propose a design first and wait for "yes". Run trigger checks and code-graded scenarios headless (for example, a scripted Claude Code or Cursor CLI run against a sandbox engagement repository). Add a CI job that runs them on PRs that touch `.claude/skills/` or `skills.lock`. Record a no-skill baseline per skill.

## Rules

- Never push to `main`. Every PR passes `python3 scripts/validate.py` and gets a fresh-context review from the `reviewer` subagent, pasted into the PR. A person merges.
- Never commit customer names, people's names, tenant hostnames, tokens or real payloads. Sandbox only.
- Prefer Tines' official skills for how to build in 3B; never copy them into this repository.
- When the public docs and a skill disagree, record both in `docs/VERIFY.md` and test it.
- At the end of each session, add a short handoff to your last PR: what changed, what's next, open questions.
