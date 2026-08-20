#!/usr/bin/env python3
"""Validate canonical skills, Claude packages, and marketplace registration."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"{path}: missing YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ValueError(f"{path}: unterminated YAML frontmatter") from error
    values: dict[str, str] = {}
    for line in lines[1:end]:
        key, separator, value = line.partition(":")
        if separator and key in {"name", "description"}:
            values[key] = value.strip().strip('"')
    return values


def main() -> int:
    canonical: set[str] = set()
    for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        name = path.parent.name
        values = frontmatter(path)
        if values.get("name") != name:
            raise ValueError(f"{path}: frontmatter name must be {name!r}")
        if not values.get("description"):
            raise ValueError(f"{path}: description must not be empty")
        canonical.add(name)

    marketplace = json.loads(
        (ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8")
    )
    published = {plugin["name"] for plugin in marketplace["plugins"]}
    if canonical != published:
        raise ValueError(
            f"canonical skills {sorted(canonical)} do not match marketplace {sorted(published)}"
        )

    packaged = subprocess.run(
        [str(ROOT / "scripts/package_claude_plugins.py"), "--check"],
        check=False,
    )
    return packaged.returncode


if __name__ == "__main__":
    raise SystemExit(main())
