# Talk track

_Plain prose to read, {actions} in braces, [cues] in brackets. Twenty-five minutes. Pair with the run of show in [`README.md`](README.md)._

---

**Frame (0:00).** {Slide: the three repositories.} 3B writes the code now. That's the part everyone's seen. What I want to show is what we put around it, so that what gets written is specified, tested, reviewed and governed, and so the next workflow follows the same path without me in the room. One synthetic use case: an EDR alert comes in, we drop duplicates, check the indicator, set a priority, open a ticket. We'll build it twice.

**Plain prompt (2:00).** {Switch to the scratch space. Paste the plain prompt. Let it build.} This is 3B's in-product agent doing what it does well. [Wait for it. Don't fill the silence.] {Open the result.} It works. Now look at what isn't here. There's no spec, so nobody agreed what "correct" means. Send the same alert twice and you get two tickets. There are no step tests unless I asked for them. The ticket step runs with nothing in front of it. And none of this is in git, so there's nothing to review and nothing to roll back to. None of that is a criticism of the agent. It did what I asked. It's a criticism of what I asked.

**Where we are (6:00).** {Switch to the engagement repository in the editor. Type /3b-onboard.} The kit's front door. It reads the engagement record and tells us the phase: readiness is done, the spec is signed off, we're in phase two, build the first workflow. One next step, one owner.

**The spec (8:00).** {Open the merged spec PR.} Before anything was built, the workflow owner approved this: the trigger and its auth, every step, what a duplicate is, what malformed input does, what the ticket contains, and the tests we'll write. This is the contract. The build gets checked against it, and so does the review.

**The build loop (10:00).** {Type /3b-build-loop specs/edr-alert-triage.md.} First thing it does is show a plan and stop. [Read the plan aloud, briefly.] {Type yes.} Watch the order. It branches in the space checkout, so nothing we do can reach Live. It builds the steps with Tines' own building-workflows skill, the same one the in-product agent uses. Then step tests, written now, not later: happy path, malformed input, duplicate delivery. Then the fixtures, end to end, on the draft. {Point at results as they appear.} And it opens the pull request with the evidence pasted in. [If past 15:00, cut to the twin branch and say so plainly.]

**The guard (17:00).** {Type: push it live.} Two refusals. The first is ours: the hook denies the call before it leaves the editor, and tells the agent to ask a person. The second is 3B's: in a Git-synced space, push_live is refused anyway; Live moves when main does. The rule isn't in a prompt the model might forget. It's a script that runs every time.

**Fresh review (18:00).** {Open a new chat. Run 3b-review on the PR.} The session that built this doesn't get to grade it. {Scorecard appears.} Fifteen rows against the spec. [One Fix row: the missing duplicate step test.] That's the top fix. {Back to the builder; it adds the test; the PR updates.} Review again, ready.

**Merge, Live (21:00).** {A person clicks merge.} Now watch 3B. Pushing live runs the step tests again, on the platform, and a failing test blocks the release. [Wait for green.] {Send happy.json to the Live route.} There's the ticket. {Send duplicate.json.} Nothing. That's the idempotency we specified, tested, and now proved in production.

**Close (23:00).** {Show the engagement log and the runbook stub.} Numbers: {read the measures}. Two human approvals, the plan and the merge, and those are the two that matter. Same request as the first time. The model didn't change. The method did. And the next workflow starts the same way: /3b-onboard tells you what's next.

[If asked "do we need Cursor for this?": No. The same skills load in Claude Code, and the conventions skill imports into 3B itself, so the in-product agent follows the same rules. The editor route adds git, pull requests and the hooks.]

[If asked "where's the AI?": Deliberately not in this workflow. Nothing here needed judgment. The stretch beat adds one AI step with a schema and an allow-list, and the ticket step stays deterministic. That's the ladder: deterministic first, AI where it earns its place.]
