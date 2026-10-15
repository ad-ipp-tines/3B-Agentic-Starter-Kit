# The plain-prompt beat

Run this in a **scratch space that is not Git-synced**, in 3B's in-product agent, with no kit skills imported. It's the fair baseline: 3B's agent doing what it does well.

## The prompt

```text
Build a workflow that receives EDR alerts on a webhook, checks the file hash against a block list, sets a priority, and opens a ticket with the details.
```

Let it finish. Don't steer it.

## What to point at (be fair; name what's good first)

| Good | Missing, and why it matters |
|---|---|
| A working route step with `route_auth = "space"` by default | **No spec.** Nobody agreed what "correct" means, so nobody can say whether this is right |
| Reasonable step split; the block-list check works on the first run | **No idempotency.** Send the same alert twice: two tickets. EDRs redeliver |
| Readable code from `building-workflows` | **No step tests** unless you asked. Nothing stops the next change from breaking this one |
| A ticket is created | **Nothing in front of the side effect.** No validation of what goes into the ticket, no approval for anything consequential later |
| | **Not in git.** No pull request, no review, no diff, no rollback point |
| | **No runbook, no owner.** When it fails at 2 a.m., nobody knows what it was for |

## The line

"None of that is the agent's fault. It did what I asked. The kit changes what gets asked, and checks what comes back."
