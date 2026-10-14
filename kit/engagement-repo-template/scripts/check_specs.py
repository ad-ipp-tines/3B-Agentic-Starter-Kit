#!/usr/bin/env python3
"""Checks every spec in specs/ before it can be merged. Standard library only.

- Required sections exist and aren't left as TBD
- fixtures/<workflow-name>/ has happy.json, malformed.json and duplicate.json, each valid JSON
- No secret-looking strings in specs, fixtures or runbooks
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REQUIRED = ["## 1. Purpose", "## 2. Trigger", "## 3. Inputs", "## 4. Steps", "## 6. Side effects and approvals",
            "## 7. Expected results", "## 9. Step tests", "## 10. Rollout"]
BASE_FIXTURES = ["happy.json", "malformed.json", "duplicate.json"]
SECRETS = [re.compile(p) for p in (r"\bsk-[A-Za-z0-9_-]{20,}", r"\b3b_sk_[A-Za-z0-9]{8,}", r"\bgh[pousr]_[A-Za-z0-9]{30,}",
                                   r"\bxox[abpr]-[A-Za-z0-9-]{10,}", r"external_id=[A-Za-z0-9_-]{8,}",
                                   r"-----BEGIN [A-Z ]*PRIVATE KEY-----")]


def main() -> int:
    errors: list[str] = []
    specs = sorted(p for p in (ROOT / "specs").glob("*.md") if p.name != "README.md")
    for spec in specs:
        text = spec.read_text(encoding="utf-8")
        for heading in REQUIRED:
            if heading not in text:
                errors.append(f"{spec.name}: missing section '{heading}'")
        if re.search(r"\bTBD\b", text):
            errors.append(f"{spec.name}: contains TBD")
        fx = ROOT / "fixtures" / spec.stem
        for name in BASE_FIXTURES:
            f = fx / name
            if not f.exists():
                errors.append(f"{spec.name}: missing fixtures/{spec.stem}/{name}")
                continue
            try:
                json.loads(f.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                errors.append(f"fixtures/{spec.stem}/{name}: invalid JSON ({e.msg})")
    for folder in ("specs", "fixtures", "runbooks", "onboarding"):
        for path in (ROOT / folder).rglob("*"):
            if path.is_file() and path.suffix in {".md", ".json", ".yaml", ".yml"}:
                body = path.read_text(encoding="utf-8", errors="ignore")
                if any(p.search(body) for p in SECRETS):
                    errors.append(f"{path.relative_to(ROOT)}: secret-looking string")
    if errors:
        print("FAIL")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK: {len(specs)} specs checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
