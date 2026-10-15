# The visual tour

_Twelve diagrams, one idea each, in the order a new builder meets them. Every diagram links to the file that is the source of truth; where a diagram and its source disagree, the source wins and this page is the bug. 3B facts come from the public docs and Tines' official skills; anything unconfirmed is in [`VERIFY.md`](VERIFY.md)._

Time: 30 minutes. Audience: anyone new to the kit: customer builders, platform owners, security reviewers, CSEs, and the AI agents that will enhance it.

---

## 1. Three repositories, three jobs

The kit is the reusable layer. Each customer gets an **engagement repository** (specs, fixtures, runbooks, onboarding records, agent configuration) with their **space repository** cloned inside it. The space repository is Git-synced to the 3B space and holds workflows only, because 3B treats every top-level folder there as a workflow and rejects executables, symlinks and submodules.

```mermaid
flowchart TB
    subgraph KIT["3B-Agentic-Starter-Kit: the reusable layer (this repository)"]
        direction LR
        K1["AGENTS.md + CLAUDE.md<br/>short rules both editors load"]
        K2[".claude/skills/<br/>9 onboarding skills: what, when, how to prove it"]
        K3[".claude/agents/<br/>onboarding-lead · solution-architect · builder · reviewer"]
        K4["scripts/hooks/guard.py<br/>wired by .claude/settings.json and .cursor/hooks.json"]
        K5["kit/templates/<br/>kit/engagement-repo-template/"]
        K6["tenant-skills/enterprise-conventions/<br/>one rule set for editors and for 3B"]
        K7["evals/ · docs/ · prompts/ · skills.lock"]
    end
    subgraph ENG["acme-3b-engagement: the customer's engagement repository (example)"]
        direction LR
        E1["onboarding/<br/>profile · progress · readiness · backlog · guide"]
        E2["specs/ · fixtures/ · runbooks/"]
        E3["AGENTS.md · .claude/ · .cursor/<br/>copied in by bootstrap.sh"]
        E4["space/<br/>a gitignored clone of the space repository"]
    end
    subgraph SPACE["acme-3b-soc: the space repository, Git-synced (example)"]
        direction LR
        S1["one top-level folder per workflow"]
        S2["Step/ config.toml · Dockerfile · code<br/>tests/step-tests/"]
        S3["main = Live · any other branch = a draft"]
    end
    K5 -- "scripts/bootstrap.sh engagement" --> E3
    E4 -- "git clone into space/" --> S1
    S3 <-- "GitSync through a GitHub App" --> T["The 3B space"]
```

**Read next:** [`README.md`](../README.md), [`decisions/0004-git-is-source-of-truth.md`](decisions/0004-git-is-source-of-truth.md), [`../kit/engagement-repo-template/README.md`](../kit/engagement-repo-template/README.md).

---

## 2. MCP meets 3B in three directions

The kit uses all three. Direction A is how builders work from day one. Direction B is phase 4, read-only tools first. Direction C is how an agent in a workflow reaches a vendor's tools without ever holding a credential.

```mermaid
flowchart LR
    subgraph CLIENTS["AI clients"]
        ED["Cursor · Claude Code · Codex<br/>(a builder, signed in)"]
        AS["Claude · other assistants<br/>(the customer's users)"]
    end
    subgraph T["Tines 3B tenant"]
        M["A · Tenant MCP server<br/>/mcp · Streamable HTTP"]
        W["B · A workflow route step<br/>/name/mcp · route_type api<br/>route_auth space, tenant or sso"]
        S["C · A workflow step<br/>+ an MCP server connector"]
    end
    V["Vendor MCP server<br/>(EDR, ticketing, identity …)"]
    ED -- "OAuth: explore, run, build, publish<br/>service-account token: explore and run only" --> M
    AS -- "platform-run OAuth 2.1:<br/>discovery, registration, consent, tokens" --> W
    S -- "OAuth, bearer or SSO route;<br/>auth injected by the connector" --> V
    M -. "every change audit-logged as MCP;<br/>push_live refused in Git-synced spaces" .-> M
```

**Read next:** [`05-mcp-with-3b.md`](05-mcp-with-3b.md), [`decisions/0011-mcp-direction-policy.md`](decisions/0011-mcp-direction-policy.md), [`../.claude/skills/3b-mcp/SKILL.md`](../.claude/skills/3b-mcp/SKILL.md).

---

## 3. The onboarding programme: six phases, each with an exit a person signs

`3b-onboard` walks the phases in order and stops at the first one whose exit criteria aren't all met. Nothing skips phase 0: every later phase depends on access, GitSync, connectors and the recorded MCP tool list.

```mermaid
flowchart LR
    P0["0 · Readiness<br/>access · GitSync · MCP over OAuth<br/>connectors · AI provider"]
    P1["1 · Discover<br/>ranked backlog → signed-off spec"]
    P2["2 · First workflow<br/>deterministic · step tests · Live"]
    P3["3 · Agentic<br/>AI only where judgment is needed"]
    P4["4 · MCP<br/>editors on MCP · tools served safely"]
    P5["5 · Operate and scale<br/>weekly review · conventions · handover"]
    P0 -->|"tools/list recorded,<br/>first connectors tested"| P1
    P1 -->|"owner approves the spec PR"| P2
    P2 -->|"PR merged, step tests<br/>green at push-live"| P3
    P3 -->|"eval set scored,<br/>approvals in place"| P4
    P4 -->|"tool list approved"| P5
    P5 -.->|"next use case"| P1
```

| Phase | Kit skills | Typical length |
|---|---|---|
| 0 | `3b-readiness` | week 1 |
| 1 | `3b-discover`, `3b-spec` | weeks 1–2 |
| 2 | `3b-build-loop`, `3b-review`, `3b-operate` | weeks 2–3 |
| 3 | `3b-spec`, `3b-build-loop`, `3b-review` | weeks 4–6 |
| 4 | `3b-mcp` | weeks 5–8 |
| 5 | `3b-operate`, `3b-handover` | weeks 8–12 |

**Read next:** [`06-onboarding-programme.md`](06-onboarding-programme.md), [`../.claude/skills/3b-onboard/references/programme.md`](../.claude/skills/3b-onboard/references/programme.md).

---

## 4. The build loop: one workflow, from a spec to a pull request

A person asks. The builder, the only subagent that writes to `space/`, shows a plan, waits for a yes, builds on a branch using Tines' `building-workflows` skill, tests, and opens a pull request. The guard hook runs whether or not the model agrees.

```mermaid
sequenceDiagram
    autonumber
    actor P as Builder (a person)
    participant E as Editor session (Cursor or Claude Code)
    participant B as builder subagent
    participant H as guard.py (hook)
    participant S as space/ checkout
    participant T as 3B tenant (MCP tools, 3b CLI)
    participant G as GitHub (space repository)
    P->>E: /3b-build-loop specs/edr-alert-triage.md
    E->>B: build this one workflow
    B->>P: numbered plan: steps, connectors, step tests, fixtures
    P->>B: yes
    B->>S: git switch -c build/edr-alert-triage
    B->>S: edit steps per building-workflows (templates, config.toml, Dockerfile)
    B->>T: run each changed step
    T-->>B: outputs, executions, logs
    B->>S: add tests/step-tests: happy · malformed · duplicate
    B->>T: fixtures end to end on the draft branch
    T-->>B: results compared with the spec's expected results
    B->>G: push the branch, open a pull request with the results
    Note over H: every shell and MCP call passes guard.py first, push_live, deletes, grants and keys are denied
    B-->>E: report + pull request link
    E->>P: ask for a fresh-context review
```

**Read next:** [`../.claude/skills/3b-build-loop/SKILL.md`](../.claude/skills/3b-build-loop/SKILL.md), [`../.claude/agents/builder.md`](../.claude/agents/builder.md), [`decisions/0008-git-to-build-mcp-for-context-cli-to-run.md`](decisions/0008-git-to-build-mcp-for-context-cli-to-run.md).

---

## 5. The ship path: from pull request to Live

Live moves only when a person merges to `main`. 3B then runs the step tests at push-live, and a failing test blocks the release. Autofix and autotune proposals come back as branches and go through the same review.

```mermaid
flowchart LR
    BR["Branch build/name<br/>a draft in 3B"] --> PR["Pull request<br/>spec link · step-test and fixture results"]
    PR --> RV["Fresh-context review<br/>3b-review scorecard"]
    RV -->|"ready"| MG["A person merges to main"]
    RV -->|"top three fixes"| BR
    MG --> LIVE["Live moves<br/>3B runs the step tests at push-live"]
    LIVE -->|"a test fails"| BLOCK["Release blocked"]
    LIVE --> OPS["Operate<br/>runbook · failures · weekly review"]
    OPS -.->|"autofix or autotune branch"| RV
    AG["An agent calls push_live over MCP"] -. "refused by 3B in Git-synced spaces,<br/>and denied by guard.py" .-> MG
```

**Read next:** [`decisions/0007-people-approve-the-irreversible.md`](decisions/0007-people-approve-the-irreversible.md), [`decisions/0009-step-tests-and-evals-are-acceptance.md`](decisions/0009-step-tests-and-evals-are-acceptance.md), [`../.claude/skills/3b-operate/SKILL.md`](../.claude/skills/3b-operate/SKILL.md).

---

## 6. Skills: what stays resident, what loads on demand

Progressive disclosure keeps the context small. `AGENTS.md` is always loaded and stays under 200 lines. Every procedure is a skill, about 100 tokens each until it's used. Tines' official skills teach *how* to build in 3B; the kit's teach *what*, *when* and *how to prove it*; the conventions skill carries the customer's own rules into the editor and into 3B.

```mermaid
flowchart TB
    subgraph ALWAYS["Always in context"]
        A["AGENTS.md<br/>the non-negotiables and how to start"]
    end
    subgraph ONDEMAND["Loaded when relevant"]
        direction LR
        R["3b-onboard<br/>the router"]
        K["Kit skills<br/>readiness · discover · spec · build-loop<br/>review · mcp · operate · handover"]
        C["enterprise-conventions<br/>the customer's rules"]
    end
    subgraph OFFICIAL["Tines official skills, pinned in skills.lock"]
        direction LR
        O1["building-workflows<br/>the format spec"]
        O2["building-agents"]
        O3["mcp-builder · mcp-client"]
        O4["workflow-discovery · workflow-operations<br/>workflow-review · workflow-volume-design"]
    end
    A --> R --> K
    K -- "names the official skill to load" --> O1
    K --> O2
    K --> O3
    K --> O4
    C -. "also imported into each 3B space from Git, auto-sync on" .-> IP["3B in-product agent"]
```

**Read next:** [`decisions/0001-compose-official-skills.md`](decisions/0001-compose-official-skills.md), [`decisions/0002-skills-over-one-big-prompt.md`](decisions/0002-skills-over-one-big-prompt.md), [`decisions/0012-same-skills-in-editor-and-product.md`](decisions/0012-same-skills-in-editor-and-product.md).

---

## 7. Who may do what: trust boundaries

Two subagents read, one writes on a branch after a yes, and a short list of actions belongs to people only. The guard hook enforces the last row; it doesn't rely on the model remembering.

```mermaid
flowchart LR
    L["onboarding-lead<br/>plans, delegates, keeps the log"]
    subgraph READ["Read-only subagents"]
        SA["solution-architect<br/>tenant inventory · vendor docs · options"]
        RV["reviewer<br/>scorecard · verdict"]
    end
    subgraph WRITE["Writes, on a branch, after a person's yes"]
        B["builder<br/>edits in space/ · step tests · pull request"]
    end
    subgraph PEOPLE["People only"]
        M["merge to main: Live moves"]
        C["connectors · access grants<br/>API keys · tunnels"]
        PUB["publish or push_live · delete"]
    end
    L --> SA
    L --> B
    L --> RV
    RV -- "verdict" --> M
    B -. "guard.py denies" .-> PUB
    B -. "guard.py denies" .-> C
```

**Read next:** [`../.claude/agents/`](../.claude/agents/), [`decisions/0005-one-orchestrator-few-subagents.md`](decisions/0005-one-orchestrator-few-subagents.md), [`decisions/0006-fresh-context-review.md`](decisions/0006-fresh-context-review.md).

---

## 8. The guard hook, decision by decision

One script, two editors. Claude Code calls it as a `PreToolUse` hook on Bash and every MCP tool; Cursor calls it before shell and MCP execution, fail-closed for MCP. Until the 3B MCP tool list is published, MCP tools are matched by name pattern.

```mermaid
flowchart TD
    IN["A tool call from the agent<br/>(shell command or MCP tool)"] --> Q1{"MCP tool name matches<br/>delete · destroy · remove · purge<br/>push_live · promote · publish<br/>grant · revoke · api_key · rotate<br/>secret · credential · connector_*?"}
    Q1 -->|"yes"| DENY["Deny: exit 2<br/>tell the person to do it in the 3B UI"]
    Q1 -->|"no"| Q2{"Shell command matches<br/>3b apps connect or disconnect<br/>THREE_B_API_KEY · git push --force<br/>curl piped to a shell · rm -rf /?"}
    Q2 -->|"yes"| DENY
    Q2 -->|"no"| ALLOW["Allow: exit 0"]
    DENY --> SHOW["The editor shows the reason to the agent and the person"]
```

**Read next:** [`../scripts/hooks/guard.py`](../scripts/hooks/guard.py), [`../.claude/settings.json`](../.claude/settings.json), [`../.cursor/hooks.json`](../.cursor/hooks.json), [`VERIFY.md`](VERIFY.md) items V1 and V7.

---

## 9. Quality: five layers, graded by code first

"It looks right" is how AI-built work fails. Each layer catches a different class of mistake, and the first two are native to 3B.

```mermaid
flowchart BT
    ST["1 · Step tests<br/>per step · hermetic, no network · byte-for-byte<br/>run automatically at push-live"]
    FX["2 · Fixtures<br/>per workflow · end to end on a draft<br/>happy · malformed · duplicate"]
    EV["3 · AI evals<br/>20+ real cases per AI step<br/>pass rate and cost per run recorded"]
    RV["4 · Fresh-context review<br/>15-row scorecard against the spec"]
    GT["5 · Kit golden tasks<br/>per skill · trigger checks + scenarios<br/>re-run on every skills.lock bump"]
    ST --> FX --> EV --> RV --> GT
```

**Read next:** [`08-quality-and-evals.md`](08-quality-and-evals.md), [`../.claude/skills/3b-review/references/scorecard.md`](../.claude/skills/3b-review/references/scorecard.md), [`../evals/README.md`](../evals/README.md).

---

## 10. AI inside a workflow: the model reasons, a person approves, the workflow executes

When a use case needs judgment, the AI step recommends from an allow-list and emits strict JSON. A deterministic step validates it, a person approves anything consequential, and only an approved request triggers the side effect.

```mermaid
sequenceDiagram
    autonumber
    participant IN as Trigger (route or cron)
    participant N as normalize_input
    participant AI as summarize_and_recommend (AI)
    participant V as validate_output
    participant AP as request_approval
    actor O as Workflow owner (a person)
    participant X as execute_action
    IN->>N: event
    N->>AI: cleaned fields, everything the model reads is untrusted data
    AI-->>V: JSON per the output schema: severity, recommendation from the allow-list
    V->>V: schema valid? recommendation allowed? otherwise a structured error and stop
    V->>AP: proposal + a plain-language risk line
    AP->>O: approve or deny
    O-->>AP: approve
    AP->>X: the approved request only
    X-->>O: result, logged with stable ids and no secrets
```

**Read next:** [`03-agentic-architecture.md`](03-agentic-architecture.md) §3, [`decisions/0003-deterministic-first.md`](decisions/0003-deterministic-first.md), the spec template §5–6 in [`../kit/templates/workflow-spec.md`](../kit/templates/workflow-spec.md).

---

## 11. A change's journey across the two repositories

The spec lands in the engagement repository and the owner approves it there. The build lands in the space repository and a person merges it there. Fixtures cross over at test time; the runbook is written after Live.

```mermaid
flowchart LR
    subgraph ENG["Engagement repository"]
        SP["specs/edr-alert-triage.md"] --> SPR["Spec pull request<br/>the owner approves"]
        FX["fixtures/edr-alert-triage/<br/>happy · malformed · duplicate"]
        RB["runbooks/edr-alert-triage.md"]
    end
    subgraph SPACE["Space repository, cloned at space/"]
        WF["edr-alert-triage/<br/>steps + tests/step-tests"] --> BPR["Build pull request<br/>results + review scorecard"]
    end
    SPR -- "build from the spec" --> WF
    FX -. "run on the draft branch" .-> WF
    BPR -->|"a person merges"| LIVE["Live in 3B"]
    LIVE -- "3b-operate" --> RB
```

**Read next:** [`decisions/0004-git-is-source-of-truth.md`](decisions/0004-git-is-source-of-truth.md), [`../.claude/skills/3b-spec/SKILL.md`](../.claude/skills/3b-spec/SKILL.md).

---

## 12. Day one: from nothing to `/3b-onboard`

What a platform owner and a CSE do before the first build session. Every step that touches a credential is done by a person; the kit never sees a key.

```mermaid
sequenceDiagram
    autonumber
    actor P as Platform owner + CSE
    participant T as 3B tenant
    participant GH as GitHub
    participant K as The kit
    participant E as Engagement repository
    participant ED as Editor (Cursor or Claude Code)
    P->>T: SSO · one group per space · connectors · AI provider · audit destination
    P->>GH: install the 3B GitHub App · create the space repository · protect main
    P->>T: GitSync the production space to that repository
    P->>K: scripts/bootstrap.sh skills (tines/skills at the pinned tag)
    P->>K: scripts/bootstrap.sh engagement ../acme-3b-engagement
    K-->>E: templates · kit skills · subagents · hooks · conventions skill
    P->>E: git clone the space repository into space/
    P->>ED: Tines 3B plugin (Cursor) or the Settings → MCP snippet, sign in with OAuth
    P->>ED: open the engagement repository, run /3b-onboard
    ED->>T: 3b-readiness lists the MCP tools and records them
```

**Read next:** [`04-setup-cursor-and-claude-code.md`](04-setup-cursor-and-claude-code.md), [`../scripts/bootstrap.sh`](../scripts/bootstrap.sh), [`../.claude/skills/3b-readiness/SKILL.md`](../.claude/skills/3b-readiness/SKILL.md).

---

## Check yourself

1. Where does a workflow's code live, and why can't the spec live next to it? *(Diagram 1, 11)*
2. Which credential can call the 3B MCP build and publish tools, and what can a service-account token do? *(Diagram 2)*
3. Why does the programme never skip phase 0? *(Diagram 3)*
4. Name the only subagent that writes to `space/`, and the two things it can never do. *(Diagrams 4, 7)*
5. What happens when an agent calls `push_live` in a Git-synced space? Name both controls. *(Diagrams 5, 8)*
6. Which layer catches a changed expected output that nobody confirmed? *(Diagram 9)*
7. In an AI step, what sits between the model's recommendation and the side effect? *(Diagram 10)*
8. Which steps on day one involve a credential, and who performs them? *(Diagram 12)*
