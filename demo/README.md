# The demo: a small POC that takes one 3B workflow from idea to Live, with the kit

_Twenty-five minutes, one sandbox tenant, one synthetic use case. The audience sees the same request built twice: once as a plain prompt to 3B's in-product agent, once with the kit. Then they watch the guard refuse an unsafe action, a person merge, and 3B run the step tests at push-live._

**Audience:** the CSE team first. Then a customer's builders and security lead, with the same run of show.

**The claim, in one line:** 3B already writes the code. The kit adds the system around it that makes the result reviewable, tested, governed and repeatable, and it does that with the editor the builder already uses.

---

## 1. The POC

| | |
|---|---|
| **Use case** | EDR alert arrives by webhook → normalise → ignore duplicates → check the indicator against a block list → set a priority → open a ticket |
| **Why this one** | Everyone understands it, it has a consequential side effect (the ticket), it needs idempotency, and it stays deterministic, so the contrast is about method, not about AI |
| **Spec** | [`scenario/spec-edr-alert-triage.md`](scenario/spec-edr-alert-triage.md) |
| **Fixtures** | [`scenario/fixtures/edr-alert-triage/`](scenario/fixtures/edr-alert-triage/): `happy.json`, `malformed.json`, `duplicate.json` |
| **Plain-prompt beat** | [`scenario/plain-prompt.md`](scenario/plain-prompt.md) |
| **Talk track** | [`talk-track.md`](talk-track.md) |
| **Stretch** | Phase 3 in five minutes: add `summarize_alert (AI)` with an output schema; the ticket step stays deterministic |

Everything is synthetic. The block list is a short static file inside the step; no vendor API is called. The ticket goes to the sandbox's ticketing connector if one exists, otherwise to a named volume `tickets` so the demo has no external dependency.

---

## 2. Run of show

| Min | Beat | What the room sees | The pro you point at |
|---|---|---|---|
| 0–2 | **Frame** | One slide: the three repositories (tour §1). "3B writes the code. Here's what we put around it." | — |
| 2–6 | **Plain prompt** | In a scratch space, paste the plain prompt into the in-product agent. Let it build. Open the result. | It works once. Then point: no spec, no duplicate handling, no step tests unless asked, the ticket step unguarded, no review, nothing in git |
| 6–8 | **Where we are** | In the engagement repository: `/3b-onboard`. It reports phase 2 and routes to the build loop. | The programme knows where you are; one next step, with an owner |
| 8–10 | **The spec is the contract** | Open the spec PR (merged in prep): trigger, steps, idempotency, expected results, step tests to write. | The owner approved what gets built before anything was built |
| 10–17 | **The build loop** | `/3b-build-loop specs/edr-alert-triage.md`. Plan → "yes" → branch in `space/` → steps built with `building-workflows` → step tests → fixtures on the draft → PR opened with results. | Plan before act; one branch per workflow; tests written during the build, not after; the PR carries the evidence |
| 17–18 | **The guard** | Ask the agent: "push it live." Two refusals: guard.py denies, and 3B itself refuses `push_live` in a Git-synced space. | Must-never rules are enforced, not remembered |
| 18–21 | **Fresh review** | New chat: `3b-review`. The scorecard lands on the PR; one Fix row (planted: a missing duplicate step test on the twin branch, or a real one). Builder fixes it. | The builder never grades its own work |
| 21–23 | **Merge → Live** | A person merges. Watch 3B run the step tests at push-live. Send `happy.json` to the Live route; the ticket appears. Send `duplicate.json`; nothing happens. | Live moves only on a human merge; the platform re-checks; idempotency is real |
| 23–25 | **Close** | The engagement log, the runbook stub, and the numbers: minutes to Live, step tests, fixtures, first-pass verdict. "Same request. The method changed, not the model." | Repeatable: the next workflow follows the same path without us |

**Stretch (+5 min):** `/3b-spec` adds `summarize_alert (AI)` as a single-request step with a strict schema and an allow-listed `recommended_priority`. Show that the ticket step validates the JSON and that priority stays a recommendation. The point: AI where judgment helps, deterministic where it matters.

---

## 3. Prep, the day before

Do readiness properly once; the demo then runs on rails.

- [ ] **Sandbox tenant and space.** A space `demo-soc`, Git-synced to a throwaway GitHub repository with `main` protected (one review required). A second scratch space for the plain-prompt beat, not Git-synced.
- [ ] **Engagement repository** created with `scripts/bootstrap.sh engagement ../demo-3b-engagement`; the space repository cloned at `space/`; the spec and fixtures from `scenario/` copied in and the spec PR merged.
- [ ] **Editor** connected over OAuth (Cursor plugin or Settings → MCP snippet); `3b-readiness` run; the MCP tool list recorded in `onboarding/profile.yaml`.
- [ ] **Official skills** installed at the `skills.lock` tag; version noted.
- [ ] **Connectors.** A ticketing connector granted to the space if available; otherwise confirm the volume fallback in the spec.
- [ ] **Dry run** the whole build loop once. Time it. Fix any skill friction before the demo, not during.
- [ ] **Twin branch** `build/edr-alert-triage-twin`, pre-built to the PR stage with one planted gap (no duplicate step test). If the live build runs long, cut to it at minute 15.
- [ ] **Backup recording** of the dry run, in case the tenant or the network misbehaves.
- [ ] **Screens.** Editor left, 3B right, GitHub PR in a tab. Font large. Secrets never on screen; the OAuth sign-in happens before the audience arrives.

---

## 4. What to measure (and say out loud)

| Measure | Target for the demo | Why it matters to a customer |
|---|---|---|
| Minutes from `/3b-build-loop` to the PR | ≤ 8 | Speed with the gates on |
| Step tests written | 3 per step, all green at push-live | Regression safety from day one |
| Fixtures passing on the draft | 3 of 3 | The spec's expected results are real |
| First-pass review verdict | "ready" after one fix | Review catches things; the loop converges |
| Human approvals | 2 (plan, merge) | Exactly the two that matter |
| Agent attempts at an irreversible action | 1, denied | The guard works in front of people |

---

## 5. If something goes wrong

| Symptom | Do |
|---|---|
| The agent has no 3B tools | Re-add the MCP entry, sign in again; meanwhile narrate from the twin branch |
| The build loop stalls past minute 15 | Cut to the twin branch at its PR stage; keep the review and merge beats live |
| Step tests fail at push-live | Good: that's the control working. Show the blocked release, fix on the branch, merge again |
| The ticketing connector errors | The spec's fallback writes the ticket to the `tickets` volume; show it there |
| OAuth session lapsed | Sign in again off-screen; never paste a token |
| The room wants AI now | Run the stretch beat; keep the ticket step deterministic and say why |

---

## 6. After the demo

- Ask the CSE team: which beat would land hardest with your customers, and which gate would they push back on?
- Record the measures above in [`PLAN.md`](../PLAN.md) under M1, with the friction log from the dry run.
- Every friction point becomes a skill fix by pull request.

## 7. The second demo, later: the kit builds its own onboarding

Once chapters exist in `docs/guide/`, run [`prompts/02-3b-build-onboarding-guide.md`](../prompts/02-3b-build-onboarding-guide.md) live: 3B builds **Launchpad**, the interactive onboarding walkthrough, from the kit's own Markdown, behind SSO, through the same spec → branch → tests → PR → merge path. Ten minutes, and the kit has onboarded itself.
