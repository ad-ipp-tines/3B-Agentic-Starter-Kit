# Fresh-context review of the kit at bootstrap (2026-10-14)

Run by a read-only session that hadn't written the kit, against `docs/research/3b-public-research-2026-10.md`. Findings are summarised; the fixes landed in the follow-up pull request unless marked deferred.

## Verdict (as given)

The method is sound and smaller than most agentic kits. The product-truth discipline (status labels, availability table, VERIFY register) is unusual and mostly accurate. The hook was the weakest link: it missed the two shell paths that actually move Live and its Cursor branch was untested against a documented payload shape. The kit overclaimed what hooks enforce. Several CLI subcommands the skills lean on aren't publicly documented. Bootstrap produced a repository whose skills referenced files that weren't copied. Not customer-ready until the top fixes land and V1/V2/V7 close on a sandbox.

## Top findings and what changed

| # | Finding | Severity | Change |
|---|---|---|---|
| 1 | `guard.py` allowed `git push … main` and `gh pr merge`; "Live moves only when a person merges" rested on branch protection alone | High | Guard denies pushes to `main`/`master`, `gh pr merge`, merge API calls, `git merge`; `3b-readiness` checks branch protection and the push-live permission with negative tests |
| 2 | Hooks presented as the control; they live in builder-owned files and Cursor cloud agents skip MCP hooks | High | Reframed everywhere: 3B RBAC + branch protection enforce; hooks are defence in depth. Control matrix added to `docs/07-enterprise-governance.md` |
| 3 | Cursor hook branch: MCP detection depended on a `url` key; output keys unverified; `$CLAUDE_PROJECT_DIR` unset under Cursor import would deny everything | High | Detect MCP by `hook_event_name`; emit both key styles; `${CLAUDE_PROJECT_DIR:-.}`; `failClosed` on both hooks; V7 expanded |
| 4 | CLI subcommands (`spaces`, `runs`, `executions`, `output`, `logs`, `--type`, `--branch`) stated as fact; only `3b run --wait` is documented | High | Labelled examples to confirm; V11 added; `AGENTS.md` rule 10 |
| 5 | Bootstrap didn't copy the docs the skills cite; conventions path wrong | Med | Bootstrap copies availability, setup, MCP, VERIFY and `skills.lock` into `kit/`; references fixed; `validate.py` checks backtick repo paths |
| 6 | Untrusted-input rule missing from kit `AGENTS.md` and five skills | Med | Added (rule 9 and per-skill lines) |
| 7 | Profile had no field for the MCP tool list; spec had no re-run-safety flag | Med | `tenant.mcp_tools`, `source_control` block; spec §7 "Safe to re-run fixtures" (checked by `check_specs.py`) |
| 8 | `bootstrap.sh skills` exited 1 on gh < 2.90 | Med | `--allow-unpinned` fallback; README and setup docs say so |
| 9 | Phase table in four places, already drifting; mixed status vocabularies | Med | `programme.md` declared canonical; drift fixed; PR template vocabulary unified |
| 10 | Agents could run `npx skills add` (unpinned); customer-name denylist local-only | Med | Guard denies ad-hoc skill installs; `HYGIENE_DENYLIST` CI secret supported |
| 11 | Service accounts described as read-and-run; they can also ask the in-product agent to build | Med | Corrected; recommendation to scope them to non-production spaces |
| 12 | Step tests described as running before the PR; only push-live runs are documented | Med | Pre-PR gate is step runs + fixtures; V12 added |
| 13 | GitSync is GitHub-only; GitLab/ADO path has no PR gate | Low | Stated in availability, governance and readiness |
| 14 | Subagent frontmatter mixed editor dialects (`tools` vs `readonly`) | Med | `readonly` + `disallowedTools`, no `tools` allowlist; per-editor note; V14 |
| 15 | Route-auth sets inconsistent across skill, scorecard and docs | Low | Unified |
| 16 | Secret scan lacked `3b_sk_`; `check_specs.py` didn't require §8 or catch placeholders | Low | Fixed |
| 17 | Marketing register in README/PLAN; "about 20 minutes" omitted tenant prerequisites | Low | Reworded |
| 18 | Glossary missing; "push live / publish / merge" used interchangeably | Low | Ten-term glossary in `docs/01-what-is-3b.md` |
| — | `docs/03-agentic-architecture.md` §2 reads as a position paper; no synthetic session transcript in `docs/04-setup-cursor-and-claude-code.md` | Low | **Deferred to M1** |

## What the reviewer said to leave alone

1. The honesty layer: availability table, VERIFY register and status labels.
2. ADR 0004's two-repository layout and the constraint behind it.
3. The acceptance loop: spec template → `check_specs.py` → fixtures → step tests → 15-row scorecard → golden tasks with `should_not_trigger` and `must_not`.
