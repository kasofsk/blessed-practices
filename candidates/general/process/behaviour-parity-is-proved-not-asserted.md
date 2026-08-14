---
type: Blessed Practice
title: "A refactor proves parity; it does not assert it"
description: "A change that claims to preserve behaviour ships the evidence: a characterisation test or trace landed *before* the refactor and unchanged by it, or a line-by-line correspondence the reviewer can check."
status: draft
tags:
  - bucket/general
  - scope/process
  - altitude/high
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  The refactors that landed cleanly here all carried a mechanical parity
  argument, not a promise. The one that did not carried a real regression, found
  by a reviewer diffing expressions by hand.
---

**Rule.** A change that claims to preserve behaviour ships the evidence: a
characterisation test or trace landed *before* the refactor and unchanged by it,
or a line-by-line correspondence the reviewer can check.

**Why.** "No behaviour change" is the most common false claim in a refactor,
because the author has just spent hours convincing themselves the shapes are
equivalent. A pre-existing artifact that the refactor does not touch is the only
cheap proof.

**How to apply.** Land the characterisation artifact in its own commit first, so
its content cannot be tuned to the new code. Keep the refactor commit free of
changes to it. Where no such artifact exists, structure the diff so
correspondence is checkable — same ordering, same names, one concern per commit.

**Does not apply when.** The change deliberately alters behaviour — then say so
and test the new behaviour.

## Where this comes from

One refactor's review named the technique as the reason it passed: the
characterisation traces were landed in a separate preparatory commit and left
untouched by the extraction, so the unchanged traces are the parity proof. A
structurally similar refactor without that artifact was rejected for a single
assignment made unconditional where the original had been conditional.

## Related

- [Break it on purpose and watch the named case go red](../testing/assertions-that-can-fail.md)
- [Deciders return effects; interpreters perform them](../architecture/pure-decider-effects.md)
- [Regenerate golden artifacts; never hand-patch them](../testing/golden-artifacts-are-regenerated.md)
