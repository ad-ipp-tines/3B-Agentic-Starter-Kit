# Set up Cursor or Claude Code for 3B

About 20 minutes per builder. A person does every step that involves a credential.

## 1. Connect to the tenant's MCP server (OAuth)

**Cursor (recommended): the official plugin**
1. Cursor → Settings → Plugins → search **"Tines 3B"**, or type `/add-plugin tines-3b` in chat ([listing](https://cursor.com/marketplace/tines-3b)).
2. Set the plugin variable `TINES_3B_MCP_URL` to `https://<your-tenant>/mcp`. On Teams, an admin can set it once for everyone.
3. Sign in when the browser opens. 3B uses OAuth with dynamic client registration, so there's no client ID to paste.

**Cursor (manual):** copy `.cursor/mcp.json.example` to `.cursor/mcp.json` (gitignored) and set your tenant:

```json
{ "mcpServers": { "tines-3b": { "type": "http", "url": "https://<your-tenant>/mcp" } } }
```

**Claude Code:** open your tenant's **Settings → MCP** page and copy the Claude Code snippet. It's typically:

```bash
claude mcp add --transport http tines-3b https://<your-tenant>/mcp
```

Then complete sign-in from the `/mcp` menu inside a session.

**Check it:** ask the agent to list the 3B spaces you can see. Then run `3b-readiness` to record the full tool list.

> Use OAuth for anyone who builds: service-account tokens can explore and run, but can't edit or publish. Never put a token in a committed file.

## 2. Install Tines' official skills (pinned)

```bash
scripts/bootstrap.sh skills          # installs tines/skills at the tag in skills.lock (needs gh 2.90+)
```

Without gh 2.90 or later, the fallback is `npx skills add tines/skills`. That installs from the default branch, which means unpinned; note the version in your readiness report. The Cursor plugin also installs the skills from the default branch the first time it's used.

## 3. Install the 3B CLI (optional, for scripted runs)

The documented install and sign-in flows differ, so check `3b --help` after installing:
- docs: `curl -fsSL https://<your-tenant>/cli/install.sh | sh`, then `3b configure`;
- official skill: `curl --proto '=https' --tlsv1.2 -fsSL https://sh.3b.dev/cli/install.sh | sh`, then `3b auth login --host <your-tenant-host>`.

Then confirm with `3b spaces`. A person runs these commands; the guard hook stops agents from piping installers into a shell.

## 4. Get the repositories

1. Create the engagement repository from `kit/engagement-repo-template/`, and copy in the kit's skills, subagents and hooks:
   ```bash
   scripts/bootstrap.sh engagement ../<customer>-3b-engagement
   ```
2. Inside it, clone the space repository into `space/`. That's the GitHub repository your space syncs to (GitSync), or the space's own Git URL.
3. Open the engagement repository folder in Cursor or Claude Code. Type `/` and check that the `3b-*` skills are listed.

## 5. Hooks

`.claude/settings.json` (Claude Code) and `.cursor/hooks.json` (Cursor) run `scripts/hooks/guard.py` before shell and MCP calls. Cursor also imports Claude Code hooks when its third-party import setting is on (the default), so the guard may run twice. That's harmless.

## Troubleshooting

| Symptom | Fix |
|---|---|
| No 3B tools listed | Reconnect from the MCP settings and complete the browser sign-in again |
| `push_live` refused | The space syncs with Git: open a pull request (or use `sync_git`), and a person merges |
| "Unauthorized" after a day | Personal API keys expire after 24 hours. Use OAuth for building and a service account for automation |
| Skills missing in Cursor | Check `.claude/skills/` exists in the opened folder; Cursor loads it for compatibility |
