#!/usr/bin/env python3
"""Package canonical Agent Skills into the Claude marketplace wrappers."""

from __future__ import annotations

import argparse
import filecmp
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
PLUGINS = ROOT / "plugins"


def skill_names() -> set[str]:
    return {
        directory.name
        for directory in SKILLS.iterdir()
        if directory.is_dir() and (directory / "SKILL.md").is_file()
    }


def plugin_names() -> set[str]:
    return {
        directory.name
        for directory in PLUGINS.iterdir()
        if directory.is_dir() and (directory / ".claude-plugin/plugin.json").is_file()
    }


def package(check: bool) -> int:
    canonical = skill_names()
    wrappers = plugin_names()
    if canonical != wrappers:
        missing_wrappers = sorted(canonical - wrappers)
        missing_skills = sorted(wrappers - canonical)
        if missing_wrappers:
            print(f"skills without Claude plugins: {', '.join(missing_wrappers)}")
        if missing_skills:
            print(f"Claude plugins without canonical skills: {', '.join(missing_skills)}")
        return 1

    drifted: list[str] = []
    for name in sorted(canonical):
        source = SKILLS / name / "SKILL.md"
        target = PLUGINS / name / "skills" / name / "SKILL.md"
        if check:
            if not target.is_file() or not filecmp.cmp(source, target, shallow=False):
                drifted.append(name)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)

    if drifted:
        print(f"Claude plugin packages are stale: {', '.join(drifted)}")
        print("run scripts/package_claude_plugins.py")
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail when a Claude plugin copy differs from its canonical skill",
    )
    return package(parser.parse_args().check)


if __name__ == "__main__":
    raise SystemExit(main())
