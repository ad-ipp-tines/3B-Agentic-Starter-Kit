# 0012. The same conventions in the editor and in the product

- **Status:** Accepted
- **Context:** Builders will work in three places: Cursor or Claude Code, the 3B in-product agent, and MCP clients steering the in-product agent. If each place follows different rules, the workflows drift. 3B skills are Agent Skills bundles. Custom skills can be created in the UI or imported from Git, with resync and an optional auto-sync. The limits are 500 files, 5 MB per file and 25 MB per bundle ([use skills in 3B](https://docs.3b.tines.com/en/articles/15886505-use-skills-to-give-tines-3b-new-expertise)). Editors load the same Agent Skills format ([agentskills.io](https://agentskills.io/specification)).
- **Decision:** the customer's conventions live in **one skill bundle**, started from `tenant-skills/enterprise-conventions/`:
  - naming;
  - route auth defaults;
  - idempotency;
  - logging;
  - AI step rules;
  - approvals.

  That bundle is imported into the 3B spaces from Git with auto-sync, and installed in builders' editors from the same repository. A change to a convention is a pull request against that one bundle.
- **Why:** one source of rules, enforced wherever building happens. Skills load progressively, so the cost is small until a convention is relevant ([Anthropic, Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)).
- **Consequences:** the conventions skill must be written in Agent Skills format with no editor-only features. Whether a bundle's scripts run identically in 3B and in an editor is **Verify**: keep the conventions skill instruction-only.
- **Revisit when:** 3B or the editors diverge from the Agent Skills spec.
