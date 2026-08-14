---
type: Blessed Practice
title: "Clear an attention gate with an assertion of attention, not a timestamp"
description: "When a gate exists to make someone look at something, let them clear it by asserting that they looked — naming what they looked at — rather than by performing the mechanical act the gate measures."
status: draft
tags:
  - bucket/general
  - scope/documentation
  - altitude/mid
  - portability/universal
  - confidence/medium
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  A subtle and generalisable idea: when a gate is a proxy for a human action,
  let the human assert the action rather than perform the proxy. The
  rebase-survivability reasoning is a second, independent lesson.
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
every conflict resolution rewrites commits.

**Does not apply when.** The mechanical act is the point, not a proxy.

## Where this comes from

The mechanism was added with both halves of its reasoning recorded: the
printed remedy names the assertion rather than the mechanical act, because
committing a document unchanged satisfies a timestamp without satisfying the
purpose; and it is written into a tracked file rather than a commit message,
because a rebase that squashes or re-authors commits destroys the latter
silently.

## Related

- [Mechanise the checkable half; route the rest to judgement](../process/mechanise-the-checkable-half.md)
- [Suspect is not wrong — publish a reading list, block almost nowhere](staleness-is-suspect-not-wrong.md)
