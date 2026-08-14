---
name: function-length-cap
title: A numeric function-length cap, enforced
scope: code
altitude: low
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/style.md Tier 1 — 70 lines, denied by the workspace lint table"
  - "The rule's own justification: a file reached roughly 2,900 lines precisely because no numeric limit existed"
rationale: >
  Included as a candidate mainly for the reasoning attached to it: vague rules
  erode and numbers do not. The specific number matters less than the fact that
  there is one and a machine enforces it.
related: [no-duplication-threshold, naming-is-the-index, ratchet-dont-sweep]
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

## Derivation

The rule's own rationale in this tree names the outcome it exists to prevent: a
central file reached roughly 2,900 lines "precisely because no numeric limit
existed", and the subsequent carve-out into pure deciders was a multi-job
project.
