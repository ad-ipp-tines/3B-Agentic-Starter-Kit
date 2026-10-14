#!/usr/bin/env python3
"""Repository checks for the 3B Agentic Starter Kit.

Runs locally (`python3 scripts/validate.py`) and in CI. Standard library only.

Checks:
  1. Every skill in .claude/skills/<name>/SKILL.md has YAML frontmatter with a
     `name` that matches its folder, a lowercase-hyphen name of 64 chars or fewer,
     and a non-empty `description` of 1024 chars or fewer.
  2. Every SKILL.md body stays under 500 lines (progressive disclosure: move
     detail into references/ files that load only when needed).
  3. Relative markdown links inside skills, agents and docs resolve to real files.
  4. Every subagent in .claude/agents/*.md has `name` and `description`.
  5. Every eval file in evals/golden-tasks/ names a skill that exists.
  6. No secret-looking strings anywhere in tracked text files.
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / ".claude" / "skills"
TENANT_SKILLS = ROOT / "tenant-skills"
AGENTS = ROOT / ".claude" / "agents"
EVALS = ROOT / "evals" / "golden-tasks"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\((?!https?://|mailto:|#)([^)#\s]+)(?:#[^)]*)?\)")
SECRET_RES = [
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}"),
    re.compile(r"\bxox[abpr]-[A-Za-z0-9-]{10,}"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"(?i)authorization:\s*bearer\s+(?!<|\$|\{)[A-Za-z0-9._-]{24,}"),
]
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".py", ".sh", ".toml", ".txt", ".example"}

errors: list[str] = []


def frontmatter(path: pathlib.Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{rel(path)}: missing YAML frontmatter")
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        errors.append(f"{rel(path)}: unterminated frontmatter")
        return {}, text
    meta: dict[str, str] = {}
    for line in text[4:end].splitlines():
        m = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if m:
            meta[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return meta, text[end + 4 :]


def rel(path: pathlib.Path) -> str:
    return str(path.relative_to(ROOT))


def check_links(path: pathlib.Path, body: str) -> None:
    for target in LINK_RE.findall(body):
        if not (path.parent / target).resolve().exists():
            errors.append(f"{rel(path)}: broken link -> {target}")


def check_skills() -> set[str]:
    names: set[str] = set()
    if not SKILLS.is_dir():
        errors.append(".claude/skills/ is missing")
        return names
    for skill_md in sorted(list(SKILLS.glob("*/SKILL.md")) + list(TENANT_SKILLS.glob("*/SKILL.md"))):
        folder = skill_md.parent.name
        meta, body = frontmatter(skill_md)
        name, desc = meta.get("name", ""), meta.get("description", "")
        if name != folder:
            errors.append(f"{rel(skill_md)}: name '{name}' must match folder '{folder}'")
        if not NAME_RE.match(name) or len(name) > 64:
            errors.append(f"{rel(skill_md)}: name must be lowercase-hyphen, at most 64 chars")
        if not desc or len(desc) > 1024:
            errors.append(f"{rel(skill_md)}: description must be 1-1024 chars")
        if len(body.splitlines()) > 500:
            errors.append(f"{rel(skill_md)}: body over 500 lines; move detail into references/")
        check_links(skill_md, body)
        for ref in skill_md.parent.rglob("*.md"):
            if ref != skill_md:
                check_links(ref, ref.read_text(encoding="utf-8"))
        names.add(name)
    return names


def check_agents() -> None:
    for agent_md in sorted(AGENTS.glob("*.md")):
        meta, body = frontmatter(agent_md)
        if not meta.get("name") or not meta.get("description"):
            errors.append(f"{rel(agent_md)}: subagent needs name and description")
        check_links(agent_md, body)


def check_evals(skill_names: set[str]) -> None:
    for task in sorted(EVALS.glob("*.yaml")):
        m = re.search(r"^skill:\s*([a-z0-9-]+)\s*$", task.read_text(encoding="utf-8"), re.M)
        if not m:
            errors.append(f"{rel(task)}: missing 'skill:' line")
        elif m.group(1) not in skill_names:
            errors.append(f"{rel(task)}: skill '{m.group(1)}' does not exist")


def local_denylist() -> list[re.Pattern[str]]:
    """Terms that must never appear (internal names, customer names). Kept OUT of git on purpose."""
    path = ROOT / ".hygiene-denylist.local"
    if not path.exists():
        return []
    lines = [l.strip() for l in path.read_text(encoding="utf-8").splitlines()]
    return [re.compile(l, re.I) for l in lines if l and not l.startswith("#")]


def check_docs_and_secrets() -> None:
    deny = local_denylist()
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix not in TEXT_SUFFIXES and path.name not in {"AGENTS.md", "CLAUDE.md"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if path.suffix == ".md" and ".claude" not in path.parts:
            check_links(path, text)
        for pattern in SECRET_RES:
            if pattern.search(text):
                errors.append(f"{rel(path)}: secret-looking string ({pattern.pattern[:24]}...)")
        if path.name == ".hygiene-denylist.local":
            continue
        for pattern in deny:
            if pattern.search(text):
                errors.append(f"{rel(path)}: matches a local denylist term (see .hygiene-denylist.local)")


def main() -> int:
    skill_names = check_skills()
    check_agents()
    check_evals(skill_names)
    check_docs_and_secrets()
    if errors:
        print("FAIL")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK: {len(skill_names)} skills, {len(list(AGENTS.glob('*.md')))} agents, "
          f"{len(list(EVALS.glob('*.yaml')))} eval files checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
