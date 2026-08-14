---
type: Blessed Practice
title: "A numeric function-length cap, enforced"
description: "Cap function length with a number, enforced by the linter, so a function one line over the cap fails the build."
status: draft
tags:
  - bucket/general
  - scope/code
  - altitude/low
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Included as a candidate mainly for the reasoning attached to it: vague rules
  erode and numbers do not. The specific number matters less than the fact that
  there is one and a machine enforces it.
---

**Rule.** Cap function length with a number, enforced by the linter, so a
function one line over the cap fails the build.

**Why.** A function that fits on one screen can be reviewed as a unit. More
importantly, a numeric limit is the only kind that does not erode: "keep
functions short" is satisfied by any function its author considers short.

**How to apply.** Set the number in the lint configuration and deny the lint at
the workspace level. Land it as a ratchet with per-site markers for existing
violations. Resist per-file exemptions; splitting is nearly always available and
usually an improvement.

**Does not apply when.** The function is a flat exhaustive match or table whose
splitting would obscure it — those deserve a marked exception, not a raised cap.

## Where this comes from

The rule's own rationale names the outcome it exists to prevent: a central
file reached roughly 2,900 lines precisely because no numeric limit existed,
and the subsequent carve-out into pure functions was a multi-change project.
The number matters less than the fact that a machine enforces one.

## Related

- [Land a new rule as a ratchet, and make the debt greppable](../process/ratchet-dont-sweep.md)
- [Names are the index an agent navigates by](naming-is-the-index.md)
- [Zero duplication, because agent-written code clones readily](no-duplication-threshold.md)
