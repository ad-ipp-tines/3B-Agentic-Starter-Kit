# The onboarding programme: phases and exit criteria

Each phase ends when a person signs off every criterion. The agent proposes; the person decides.

## Phase 0 · Readiness
- [ ] SSO in place, with the provisioning mode known.
- [ ] One space per team, each with one dedicated group.
- [ ] Who holds push-live, connector-admin, network-creator and API-key permissions is decided and written down.
- [ ] Each production space is Git-synced to a space repository in the customer's GitHub (GitHub App installed, default branch `main`, branch protection requiring a review).
- [ ] An engagement repository exists, created from `kit/engagement-repo-template/`, with the space repository cloned at `space/`.
- [ ] Builders' editors are connected to `<tenant origin>/mcp` with OAuth (Cursor plugin or Settings → MCP snippet). The `tools/list` result is recorded in the profile.
- [ ] Official skills installed at the version in `skills.lock`; the conventions skill drafted.
- [ ] Connectors for the first use case created, granted to the space's group, and tested.
- [ ] AI provider connector and default model set (if AI steps are planned).
- [ ] A tunnel set up for private systems (if needed).
- [ ] Audit log destination decided.
- [ ] A service account in place for read-and-run automation (personal API keys expire after 24 hours).

## Phase 1 · Discover
- [ ] 5–10 use cases in the backlog, scored for value, feasibility and risk, each with an `agentic_fit`.
- [ ] The top use case has a spec with fixtures and expected results, merged to the engagement repository.
- [ ] The workflow owner (role) signed off the spec in its pull request.

## Phase 2 · First workflow
- [ ] Built on a branch from the spec, with step tests for every step.
- [ ] Fixtures pass end to end on the draft.
- [ ] A fresh-session review scorecard passes on the pull request.
- [ ] A person merged it; Live moved, and the step tests passed at push-live.
- [ ] A runbook exists, and the owner knows how to read runs and errors.

## Phase 3 · Agentic
- [ ] A use case with real judgment in it, justified in the spec (why AI, which shape).
- [ ] AI or agent steps with a strict output schema validated downstream, allowed actions, a token budget, and a person's approval on every consequential action.
- [ ] An eval set of 20+ realistic cases; pass rate and cost per run recorded.
- [ ] Review passed and merged by a person.

## Phase 4 · MCP
- [ ] Every builder uses the 3B MCP server from their editor, acting as themselves.
- [ ] Where the customer wants it: one workflow serving read-only MCP tools behind `space` or `sso` route auth, tested with the MCP Inspector and about 10 evaluation questions.
- [ ] Where an agent needs a vendor's tools: an MCP server connector, with only the needed tools used.
- [ ] A person approved every server, its tools and who can call them.

## Phase 5 · Operate and scale
- [ ] Autofix and autotune proposals reviewed in a fresh session before a person merges them.
- [ ] A weekly review of failures, Tines Units and AI spend, owned by a role.
- [ ] The conventions skill imported into the spaces with auto-sync, and installed in builders' editors.
- [ ] A handover guide delivered (`3b-handover`); the customer ships the next workflow without the CSE.
