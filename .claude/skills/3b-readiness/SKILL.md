---
name: 3b-readiness
description: Checks whether a customer's Tines 3B tenant and builders are ready to start building — access model, spaces and groups, GitSync to GitHub, connectors, AI provider, the editor's MCP connection and the tools it exposes, the CLI, pinned official skills, network and audit. Read-only; produces a readiness report and a gap list with owners. Use in onboarding phase 0, or when asked to check setup, access or MCP connectivity.
compatibility: Cursor or Claude Code; Tines 3B
---

# 3B readiness check

Read-only. You inspect and ask. You never create spaces, groups, connectors, keys or GitHub apps: you list what a person needs to do. Setup steps are in `docs/04-setup-cursor-and-claude-code.md`.

## Checks

Run these in order. Record each result in the profile and in the report.

1. **Identity and access.** SSO and provisioning mode. One space per team with one group granting access. Who holds the push-live, network-creator and connector-admin permissions.
2. **GitSync.** For each production space: is it synced to a repository in the customer's GitHub through the GitHub App, with `main` as the default branch and branch protection requiring a review? A customer GitHub admin installs the app. Separately: does an engagement repository exist (created from `kit/engagement-repo-template/`), with the space repository cloned at `space/`?
3. **MCP connection.** Is the editor connected to `<tenant origin>/mcp`, through the official Cursor plugin or the Settings → MCP snippet, with **OAuth**? Service-account tokens can't build or publish. Then **list the tools it exposes** and record each one in the profile as `read`, `run`, `build` or `publish`. Only tools on this list may be used by name later. Smoke test: list the spaces you can see.
4. **Official skills.** Which `tines/skills` version is loaded? Compare it with `skills.lock`. The Cursor plugin installs from the default branch, so the versions may differ: note it.
5. **CLI (optional, for scripted runs).** Ask the person to sign in; the documented flows differ (`3b configure` in the docs, `3b auth login --host <tenant-host>` in the skill), so they should check `3b --help`. Then `3b spaces`. The key never enters this session.
6. **Connectors.** For the first use case: is each connector created, granted to the space's group, and tested? Record names only. If an external MCP server is involved, does it have an "MCP server" connector?
7. **AI provider.** Which provider connector (3B is bring-your-own-model), the default model, and spend controls. Record the plan's Tines Units budget if known.
8. **Network.** Private systems behind a firewall? Is a tunnel network set up (needs the Network creator role; the token is shown once)?
9. **Audit.** Where audit logs go. MCP actions should appear attributed to the user.
10. **Automation identity.** Is a service account in place for any read and run automation? Personal API keys expire after 24 hours.

## Report

Write `onboarding/readiness.md` in the customer's engagement repository:

| Check | Result | Status (Available / Verify / blocked) | Owner (role) if blocked |
|---|---|---|---|

Then the gap list, ordered by what blocks the first workflow. End with: ready / not ready for phase 1.

## Rules

- Never ask for, print or store a secret, key or token.
- If the MCP connection fails or the tool list is empty, say so plainly. Don't guess tool names.
- Mark anything unconfirmed as Verify and add it to the customer's open items.
