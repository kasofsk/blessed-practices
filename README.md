# blessed-practices

Blessed code practices stored as portable Agent Skills and published through
thin client-specific packaging.

Each practice is a plain Markdown file at `skills/<name>/SKILL.md`. Its YAML
frontmatter provides the portable name and load trigger; its body is the
practice. There is exactly one copy of every practice, and every install route
serves that file.

Each practice is published as its own Claude plugin containing a single skill,
so you can install exactly the ones you want. Claude loads a practice when the
work in front of it matches the skill's description — no need to invoke them by
hand.

## Install in Claude Code

```
/plugin marketplace add kasofsk/blessed-practices
/plugin install layering@blessed-practices
```

Then browse and install the rest from the `/plugin` menu, or install by name:

```
/plugin install domain-modelling@blessed-practices
```

## Install in Codex

Ask Codex to install one or more canonical skill paths from this repository.
For example:

```text
Install skills/layering and skills/domain-modelling from
https://github.com/kasofsk/blessed-practices
```

Codex discovers the installed practices from their ordinary `SKILL.md`
frontmatter. No Codex-specific copy of the practice is required.

## Practices

### general

| Plugin | Skill | Practice |
|--------|-------|----------|
| [comments-describe-the-code](plugins/comments-describe-the-code) | `comments-describe-the-code:comments-describe-the-code` | Comments describe the code itself, not the prompt or conversation that produced it — and a long justifying comment is a smell pointing at the code. |
| [dependencies](plugins/dependencies) | `dependencies:dependencies` | Use the package manager; never hand-edit the manifest. |
| [domain-modelling](plugins/domain-modelling) | `domain-modelling:domain-modelling` | The language, aggregates as consistency boundaries, entities and values, illegal states, where behaviour lives, persistence. |
| [fix-the-assumption-not-the-hack](plugins/fix-the-assumption-not-the-hack) | `fix-the-assumption-not-the-hack:fix-the-assumption-not-the-hack` | When a feature invalidates an assumption the design rests on, rethink the pattern rather than land a tweak. |
| [idiomatic-by-default](plugins/idiomatic-by-default) | `idiomatic-by-default:idiomatic-by-default` | Take the ecosystem's standard path unless there's an articulable reason not to. |
| [illegal-states-unrepresentable](plugins/illegal-states-unrepresentable) | `illegal-states-unrepresentable:illegal-states-unrepresentable` | Model data so invalid combinations cannot be constructed; parse loose external shapes into precise variants at the boundary. |
| [layering](plugins/layering) | `layering:layering` | Which way dependencies point, what each layer owns, what may cross a boundary, ports and adapters. |
| [modular-and-layered-code](plugins/modular-and-layered-code) | `modular-and-layered-code:modular-and-layered-code` | Architect so a future agent can act at a single layer — strict tested contracts, pure logic, impurity at the edges. |
| [push-back-and-verify-assumptions](plugins/push-back-and-verify-assumptions) | `push-back-and-verify-assumptions:push-back-and-verify-assumptions` | Push back on wrong premises, state assumptions explicitly, and stop rather than build something plausibly correct. |
| [comments-describe-the-code](skills/comments-describe-the-code) | `comments-describe-the-code:comments-describe-the-code` | Comments describe the code itself, not the prompt or conversation that produced it — and a long justifying comment is a smell pointing at the code. |
| [dependencies](skills/dependencies) | `dependencies:dependencies` | Use the package manager; never hand-edit the manifest. |
| [domain-modelling](skills/domain-modelling) | `domain-modelling:domain-modelling` | The language, aggregates as consistency boundaries, entities and values, illegal states, where behaviour lives, persistence. |
| [fix-the-assumption-not-the-hack](skills/fix-the-assumption-not-the-hack) | `fix-the-assumption-not-the-hack:fix-the-assumption-not-the-hack` | When a feature invalidates an assumption the design rests on, rethink the pattern rather than land a tweak. |
| [idiomatic-by-default](skills/idiomatic-by-default) | `idiomatic-by-default:idiomatic-by-default` | Take the ecosystem's standard path unless there's an articulable reason not to. |
| [layering](skills/layering) | `layering:layering` | Which way dependencies point, what each layer owns, what may cross a boundary, ports and adapters. |
| [modular-and-layered-code](skills/modular-and-layered-code) | `modular-and-layered-code:modular-and-layered-code` | Architect so a future agent can act at a single layer — strict tested contracts, pure logic, impurity at the edges. |
| [push-back-and-verify-assumptions](skills/push-back-and-verify-assumptions) | `push-back-and-verify-assumptions:push-back-and-verify-assumptions` | Push back on wrong premises, state assumptions explicitly, and stop rather than build something plausibly correct. |
| [write-the-present-not-the-diff](skills/write-the-present-not-the-diff) | `write-the-present-not-the-diff:write-the-present-not-the-diff` | Say what is true now; don't narrate the correction or apologize for the claim it replaced. |

`layering` and `domain-modelling` are a pair — the first is the structure, the
second is the content — but each stands alone.

## Reading the practices without installing

Every practice is a plain Markdown file at
`skills/<name>/SKILL.md`. The YAML frontmatter tells a compatible agent when to
load it; the body is the practice.

## Packaging

There is none. Each marketplace entry points at the repository root and names
the one skill directory it publishes:

```json
{
  "name": "layering",
  "source": "./",
  "version": "1.0.0",
  "skills": ["./skills/layering"]
}
```

Claude Code installs the entry as a single-skill plugin, so `skills/<name>/SKILL.md`
is the only copy of a practice that exists. Run `scripts/validate.py` after
editing the catalog; it checks frontmatter, registration, and that every entry
resolves to a real skill.

## Contributing

See [CLAUDE.md](./CLAUDE.md) for the repo layout, the versioning rule that gates
client updates, and how to add a practice.

## License

[MIT](./LICENSE)
