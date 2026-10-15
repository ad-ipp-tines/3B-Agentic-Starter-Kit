# The 3B onboarding guide

_The walkthrough a new builder, platform owner or CSE reads first. It explains the kit in the order you'll use it, with one worked example throughout: a synthetic EDR alert-triage workflow taken from spec to Live. Diagrams live in the [visual tour](../00-visual-tour.md); this guide links to them rather than repeating them._

**Status:** chapters are being written (milestone M2 in [`PLAN.md`](../../PLAN.md)). Until then, the reading paths below point at the reference pages that already exist.

---

## Start here, by role

| You are | Read, in order | Time |
|---|---|---|
| **A builder new to 3B** | [What 3B is](../01-what-is-3b.md) → [visual tour](../00-visual-tour.md) §1, 4, 5, 9 → [setup](../04-setup-cursor-and-claude-code.md) → the `3b-build-loop` skill | 45 min |
| **A platform owner** | [visual tour](../00-visual-tour.md) §1, 3, 7, 12 → [setup](../04-setup-cursor-and-claude-code.md) §1–4 → [programme](../06-onboarding-programme.md) → [governance](../07-enterprise-governance.md) | 40 min |
| **A security reviewer** | [visual tour](../00-visual-tour.md) §2, 7, 8, 10 → [MCP with 3B](../05-mcp-with-3b.md) → [governance](../07-enterprise-governance.md) → [guard.py](../../scripts/hooks/guard.py) → [availability](../02-availability.md) | 40 min |
| **A CSE running the programme** | everything above, then [the demo](../../demo/README.md), [the decisions](../decisions/README.md) and [`PLAN.md`](../../PLAN.md) | 2 h |
| **An AI agent enhancing the kit** | [`AGENTS.md`](../../AGENTS.md) → [sync protocol](../../prompts/03-sync-protocol.md) → the prompt for your editor in [`prompts/`](../../prompts/) | — |

**Fifteen minutes only?** Read the [visual tour](../00-visual-tour.md) §1, 4 and 5, then the [availability page](../02-availability.md). You'll know where things live, how a change ships, and what's confirmed.

---

## Chapters

Each chapter is one phase or one concept, uses the worked example, labels every 3B capability **Available**, **Verify** or **Not available** with a public link, and ends with a short "check yourself".

| # | Chapter | Covers | Diagrams | Status |
|---|---|---|---|---|
| 1 | **Why this method** | What prompting alone gets you, what the gates add, the pros in plain terms, where Workbench-style in-product building fits | tour §4, §5 | planned |
| 2 | **The pieces** | Official skills vs kit skills vs conventions; subagents; hooks; the three repositories | tour §1, §6, §7 | planned |
| 3 | **Setup** | Editor + MCP over OAuth; pinned skills; CLI; engagement repository + `space/` | tour §12 | planned (reference: [setup](../04-setup-cursor-and-claude-code.md)) |
| 4 | **Phase 0 · Readiness** | A worked readiness report; the MCP tool list; GitSync; the one-group-per-space rule | tour §3 | planned |
| 5 | **Phase 1 · Discover and spec** | A worked backlog; the agentic-fit ladder; the EDR alert-triage spec and fixtures | tour §11 | planned (reference: [`demo/scenario/`](../../demo/scenario/)) |
| 6 | **Phase 2 · Build to Live** | Branch, step tests, fixtures on the draft, pull request, scorecard, merge, step tests at push-live. Screenshots of each gate | tour §4, §5, §9 | planned |
| 7 | **Phase 3 · Adding AI safely** | Choosing a shape; output schemas; approvals; the eval set; cost per run | tour §10 | planned |
| 8 | **Phase 4 · MCP** | Editors on MCP; serving read-only tools from a workflow; calling a vendor's MCP server | tour §2 | planned (reference: [MCP with 3B](../05-mcp-with-3b.md)) |
| 9 | **Phase 5 · Operate and hand over** | Runbooks; autofix review; the weekly review; conventions in every space; the handover guide | tour §5 | planned |
| 10 | **Reference** | Status labels; decision records; the VERIFY register; glossary | — | planned (reference: [decisions](../decisions/README.md), [VERIFY](../VERIFY.md)) |

---

## How the guide is written

- **Who writes it.** Cursor on the Tines laptop, following Task 4 in [`prompts/01-cursor-continue-building.md`](../../prompts/01-cursor-continue-building.md), using the sandbox dry run as the worked example. 3B builds the interactive version, **Launchpad**, from these Markdown files ([`prompts/02-3b-build-onboarding-guide.md`](../../prompts/02-3b-build-onboarding-guide.md)), so headings stay stable once published.
- **Voice.** Plain language, short sentences, second person. Engineering, not marketing.
- **Examples.** Synthetic only: the EDR alert-triage scenario in [`demo/scenario/`](../../demo/scenario/). No customer names, people, tenant hostnames or real payloads.
- **Truth.** Every 3B claim carries a status label and a public link. Anything unconfirmed goes to [`VERIFY.md`](../VERIFY.md), not into a chapter.
- **Review.** Each chapter lands by pull request after a fresh-context review, like everything else in the kit.

## Conventions for a chapter

```markdown
# N. Title

_One-line summary. Time: X minutes._

## What you'll do
## Walkthrough (numbered, with the exact commands and prompts)
## What just happened (the concept, with a link to the tour diagram)
## Pros you can point at (one line each)
## Check yourself (3 questions)
```
