# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

An **agent-agnostic practice library** published as a Claude Code plugin
marketplace and directly installable as Agent Skills. The repo is the
marketplace `blessed-practices`; each subdirectory of `plugins/` is a generated
Claude wrapper containing exactly one canonical practice. The point of the
one-practice-per-plugin split is that a user installs only the practices they
want.

## Layout

```
skills/<practice>/SKILL.md                 # canonical portable practice
.claude-plugin/marketplace.json          # the catalog: one entry per published practice
plugins/<practice>/
  .claude-plugin/plugin.json             # { name, description } — no version field, see Versioning
  skills/<practice>/SKILL.md             # generated Claude package; do not edit
scripts/package_claude_plugins.py         # canonical skill -> Claude package
README.md                                # human-facing practice table (keep in sync with the catalog)
```

The plugin name, the skill directory name, and the frontmatter `name` are all the
same slug, so the skill surfaces as `<practice>:<practice>`.

**The top-level `SKILL.md` is the practice.** The plugin copy is generated
packaging, never another maintained source. Edit only
`skills/<practice>/SKILL.md` and run `scripts/package_claude_plugins.py`. Check
mode must pass before commit.

## The frontmatter is the load trigger

Claude decides whether to pull a practice into context from its `description`
alone, so the description is functional, not decorative. Write it in the third
person, lead with what the practice makes you do, then list concrete "Use when …"
triggers — the situations, file names, and phrasings that should summon it. A
description that only restates the title will never fire.

Avoid `": "` (colon-space) in a description unless the value is quoted; it is
unquoted YAML.

## Versioning — the rule that gates client updates

**Installed clients only pick up changes when the plugin's `version` increases.**
The version lives in `.claude-plugin/marketplace.json` (the per-plugin `version`
field); `plugin.json` carries no version. Edit a practice without bumping its
version and clients keep the old text forever.

- **patch** (`1.0.0 → 1.0.1`) — wording or a clarification within a practice.
- **minor** (`1.0.0 → 1.1.0`) — substantive new guidance added to a practice.
- **major** (`1.x → 2.0.0`) — renaming the skill, or reversing existing guidance.

## Procedures

### Edit an existing practice

1. Edit `skills/<practice>/SKILL.md`.
2. Run `scripts/package_claude_plugins.py`.
3. **Bump that plugin's `version`** in `.claude-plugin/marketplace.json`.
4. If the practice's scope changed, update the catalog `description`, the
   `plugin.json` `description`, and the README row together.
5. Validate: `scripts/validate.py` and
   `python3 -m json.tool .claude-plugin/marketplace.json >/dev/null`.

### Add a new practice

1. `skills/<slug>/SKILL.md` with `name` and `description` frontmatter.
2. `plugins/<slug>/.claude-plugin/plugin.json` — `{ "name": "<slug>", "description": "…" }`.
3. Run `scripts/package_claude_plugins.py` to create the packaged skill.
4. **Register it** in `.claude-plugin/marketplace.json` with `name`, `source`
   (`"./plugins/<slug>"`), `version` (`1.0.0`), and `description`. A plugin absent
   from the catalog is not published — clients cannot see it.
5. Add a row to the README table under the right category heading.

Categories (`general`, and any added later) are **README headings only**, not a
directory level. `plugins/` stays flat, and plugin names must be unique across the
whole marketplace.

### Cross-references between practices

Practices are installed independently, so a sibling may be absent. Never link to
another practice by relative path — that path does not resolve once installed.
Name it instead: "the **layering** practice (`layering@blessed-practices`)".

### Test locally

```sh
claude --plugin-dir ./plugins/<practice>   # load one practice from the checkout
/reload-plugins                            # after edits
```

### Publish

Commit on a branch (never straight to `main`), push, open a PR. After merge:

```
/plugin marketplace update blessed-practices
/plugin install <practice>@blessed-practices
```

## Conventions

- **Keep three things in sync** on every change: `SKILL.md`, the `marketplace.json`
  entry (version + description), and the README table.
- Never edit a packaged `plugins/*/skills/*/SKILL.md`; regenerate it.
- Practices are written as prose that states a rule and its cost, not as checklists.
- Branch for changes; finish commit messages with the project's `Co-Authored-By` trailer.
