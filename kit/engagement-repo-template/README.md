# <Customer codename> · Tines 3B engagement

This repository is where your team and your coding agents plan, specify, test and record work on Tines 3B. Your workflows themselves live in the **space repository**, which is Git-synced with your 3B space and cloned here at `space/`.

| Path | What it is |
|---|---|
| `onboarding/` | Profile, progress log, readiness report, use-case backlog, handover guide |
| `specs/` | One spec per workflow, the contract each build is checked against |
| `fixtures/` | Synthetic end-to-end test inputs per workflow |
| `runbooks/` | How to run and fix each live workflow |
| `space/` | Your space repository (gitignored here; it has its own history and pull requests) |
| `AGENTS.md` | Rules your coding agents follow |
| `.claude/`, `.cursor/` | Agent skills, subagents and guard hooks from the 3B Agentic Starter Kit |
| `kit/` | Templates, the kit's availability and VERIFY pages, setup and MCP references, and the pinned `skills.lock`, copied in by bootstrap |

## Set up once

1. Create this repository from the kit's `kit/engagement-repo-template/`, then run `scripts/bootstrap.sh engagement <path-to-this-repo>` from the kit. That copies in the skills, subagents and hooks.
2. Clone your space repository into `space/`. Use the GitHub repository your space syncs to (preferred), or the space's own Git URL from the 3B docs.
3. Connect your editor to your tenant's MCP server with OAuth: the Tines 3B plugin for Cursor, or the snippet on your tenant's Settings → MCP page for Claude Code.
4. Open this folder in Cursor or Claude Code and run `/3b-onboard`.

## How a change happens

1. A spec change, as a pull request here. The workflow owner approves it.
2. A build on a branch in `space/`, with step tests, ending in a pull request on the space repository.
3. A fresh-context review of that pull request.
4. A person merges, which moves Live. 3B runs the step tests again at push-live.
