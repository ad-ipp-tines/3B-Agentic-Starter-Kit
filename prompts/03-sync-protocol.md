# Sync protocol: how people and agents work on this repository together

GitHub is the single source of truth. Three kinds of contributor share it:

| Contributor | Works where | Branch prefix |
|---|---|---|
| The CSE | Any machine | `cse/<topic>` |
| Cursor agent | Tines laptop, sandbox tenant | `cursor/<topic>` |
| 3B agent | Sandbox space, Git-synced repository (Launchpad) | `3b/<topic>` in that repository |

## Every session

1. **Pull first:** `git switch main && git pull`, then branch.
2. **One topic per branch and per PR.** Small PRs merge; big ones rot.
3. **Before opening a PR:** `python3 scripts/validate.py` passes, and a fresh-context review (the `reviewer` subagent or a new chat with `3b-review`) is pasted into the PR.
4. **The PR description ends with a handoff:**
   ```
   Changed: …
   Next: …
   Open questions: …
   VERIFY updates: …
   ```
5. **A person merges.** Nobody pushes to `main`.

## Keeping truth current

- A PR that changes a 3B fact updates `docs/02-availability.md` (with a source) or adds a row to `docs/VERIFY.md`.
- A PR that bumps `skills.lock` re-runs the golden tasks and reports the results.
- A PR that changes how the kit works adds or updates an ADR in `docs/decisions/`.
- A PR that completes a milestone updates the table in `PLAN.md`.

## Conflicts

Rebase on `main`. If two PRs change the same skill, the second author resolves the conflict and re-runs that skill's golden tasks.

## Never

- Commit secrets, tokens, `external_id` values, customer names, people's names, tenant hostnames or real payloads.
- Copy Tines' official skills into this repository; pin them in `skills.lock`.
- Present a Verify or Not-available capability as a feature.
