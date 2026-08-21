# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

An **agent-agnostic practice library** published as a Claude Code plugin
marketplace and directly installable as Agent Skills. The repo is the
marketplace `blessed-practices`; each entry in the catalog publishes exactly one
practice as a single-skill plugin. The point of the one-practice-per-plugin
split is that a user installs only the practices they want.

## Layout

```
skills/<practice>/SKILL.md               # the practice — the only copy that exists
.claude-plugin/marketplace.json          # the catalog: one entry per published practice
scripts/validate.py                      # frontmatter, registration, and entry wiring
README.md                                # human-facing practice table (keep in sync with the catalog)
```

The plugin name, the skill directory name, and the frontmatter `name` are all the
same slug, so the skill surfaces as `<practice>:<practice>`.

**There is no packaging step and no generated tree.** Every catalog entry sets
`"source": "./"` — the marketplace root — and names the single skill directory it
publishes:

```json
{
  "name": "layering",
  "source": "./",
  "version": "1.0.0",
  "description": "…",
  "skills": ["./skills/layering"]
}
```

For an entry whose `source` resolves to the marketplace root, a declared `skills`
path *replaces* the default `skills/` scan rather than adding to it, so each
plugin exposes exactly its own practice. Installing one practice copies the
whole repository root into the plugin cache — roughly 70 KB, all of it text —
while loading only the declared skill, so the cost is disk, never context.

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
The version lives in `.claude-plugin/marketplace.json`, in the entry's `version`
field. Edit a practice without bumping its version and clients keep the old text
forever.

- **patch** (`1.0.0 → 1.0.1`) — wording or a clarification within a practice.
- **minor** (`1.0.0 → 1.1.0`) — substantive new guidance added to a practice.
- **major** (`1.x → 2.0.0`) — renaming the skill, or reversing existing guidance.

## Procedures

### Edit an existing practice

1. Edit `skills/<practice>/SKILL.md`.
2. **Bump that plugin's `version`** in `.claude-plugin/marketplace.json`.
3. If the practice's scope changed, update the catalog `description` and the
   README row together.
4. Validate: `scripts/validate.py` and
   `python3 -m json.tool .claude-plugin/marketplace.json >/dev/null`.

### Add a new practice

1. `skills/<slug>/SKILL.md` with `name` and `description` frontmatter.
2. **Register it** in `.claude-plugin/marketplace.json` with `name`, `source`
   (`"./"`), `version` (`1.0.0`), `description`, and `skills`
   (`["./skills/<slug>"]`). A plugin absent from the catalog is not published —
   clients cannot see it.
3. Add a row to the README table under the right category heading.

Categories (`general`, and any added later) are **README headings only**, not a
directory level. `skills/` stays flat, and plugin names must be unique across the
whole marketplace.

### Cross-references between practices

Practices are installed independently, so a sibling may be absent. Never link to
another practice by relative path — that path does not resolve once installed.
Name it instead: "the **layering** practice (`layering@blessed-practices`)".

### Test locally

```sh
scripts/validate.py                        # catalog wiring
claude plugin validate .                   # marketplace manifest
```

To exercise a real install without touching your own plugin config, point Claude
Code at a scratch config directory:

```sh
CLAUDE_CONFIG_DIR=$(mktemp -d) claude plugin marketplace add ./
```

Then install the practice from that marketplace and check
`claude plugin details <practice>` reports `Skills (1)`.

### Publish

Commit on a branch (never straight to `main`), push, open a PR. After merge:

```
/plugin marketplace update blessed-practices
/plugin install <practice>@blessed-practices
```

## Conventions

- **Keep two things in sync** on every change: the `marketplace.json` entry
  (version + description) and the README table.
- Practices are written as prose that states a rule and its cost, not as checklists.
- Branch for changes; finish commit messages with the project's `Co-Authored-By` trailer.
