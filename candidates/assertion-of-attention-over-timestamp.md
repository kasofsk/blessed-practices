---
name: assertion-of-attention-over-timestamp
title: Clear an attention gate with an assertion of attention, not a timestamp
scope: documentation
altitude: mid
portability: universal
confidence: medium
status: candidate
evidence:
  - "job #471 — a re-read assertion added as the way to clear the staleness block, because re-touching the doc satisfies the ordering without satisfying the purpose"
  - "job #471 — written into a tracked file rather than a commit trailer, because a rebase destroys a trailer and every conflict rework rebases"
rationale: >
  A subtle and generalisable idea: when a gate is a proxy for a human action,
  let the human assert the action rather than perform the proxy. The
  rebase-survivability reasoning is a second, independent lesson.
related: [staleness-is-suspect-not-wrong, one-commit-when-ordering-matters, mechanise-the-checkable-half]
---

**Rule.** When a gate exists to make someone look at something, let them clear
it by asserting that they looked — naming what they looked at — rather than by
performing the mechanical act the gate measures.

**Why.** Every proxy can be satisfied without doing the thing. Committing a
document unchanged updates its timestamp and clears an ordering check while
satisfying none of its purpose. An explicit assertion is at least honest, and it
is auditable.

**How to apply.** Make the assertion per-item, not a blanket waiver, and read it
from the change itself rather than from accumulated file contents — otherwise
yesterday's assertion becomes a standing exemption. Prefer a mechanism that
survives a rebase: content in a tracked file beats a commit trailer, because
every conflict rework rewrites commits.

**Does not apply when.** The mechanical act is the point, not a proxy.

## Derivation

Job #471 added the assertion and both halves of its reasoning: the printed
remedy names the assertion rather than the re-touch "because committing the doc
unchanged satisfies the ordering without satisfying the purpose", and the file
form exists because "a squashed or re-authored commit destroys a trailer
assertion silently".
