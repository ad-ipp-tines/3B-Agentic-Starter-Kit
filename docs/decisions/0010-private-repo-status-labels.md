# 0010. Private repo, status labels, no internal or customer content

- **Status:** Accepted
- **Context:** 3B is new and moving fast. Some of what we know comes from internal enablement and engineering material, and some behaviour has only been observed, not documented. Customer engagements produce sensitive context.
- **Decision:**
  - **Private repo.** The repository is private.
  - **Status labels on every capability claim.** **Available** (public docs or verified on a tenant, with the source), **Verify** (seen, unconfirmed), or **Not available** (documented as unfinished or proposed). The register is `docs/VERIFY.md`.
  - **No internal material.** No internal-only material: engineering internals, internal component names, pricing internals, enablement notes. The kit describes behaviour, cites public sources, and says "verify in your tenant" otherwise.
  - **No customer content.** No customer names, people, tenant hostnames or real payloads. Filled-in templates live in the customer's own copy (`customers/` is gitignored).
  - **Scanning.** `scripts/validate.py` scans for secret patterns. A local, uncommitted denylist (`.hygiene-denylist.local`) holds terms that must never appear, so the denylist itself doesn't leak them.
- **Why:** skills that teach proposals as features break customer trust. Hidden context is discoverable, so never rely on it to keep secrets ([OWASP LLM Top 10 2026, LLM08](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)).
- **Consequences:** some useful observations stay as "verify in your tenant" until public docs or a tenant test confirm them. That's the price of being trustworthy.
- **Revisit when:** a public, shareable edition is wanted. Then cut a public branch containing only Available claims with public citations.
