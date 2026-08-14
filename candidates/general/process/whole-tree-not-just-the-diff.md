---
type: Blessed Practice
title: "Cheap checks run whole-tree, not only over the diff"
description: "If a check is cheap enough, run it over the whole tree on every change."
status: draft
tags:
  - bucket/general
  - scope/process
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Diff-scoping is the reflex, and it is wrong for anything cheap. The failures
  here are all of the same shape: a change in one area invalidates a claim in
  another, and only a whole-tree pass connects them.
---

**Rule.** If a check is cheap enough, run it over the whole tree on every
change. Diff-scoping is a performance optimisation and should be justified by a
measurement, not assumed.

**Why.** The interesting violations are cross-cutting: a rename in code
falsifies a claim in a document nobody touched; a deleted file orphans
references elsewhere. A diff-scoped check cannot see either. And once the tree
is clean, whole-tree is the only mode that keeps it clean.

**How to apply.** Measure the check whole-tree. Under a second or so, make it
unconditional. Where the tree is not yet clean, run as a ratchet — judge only
what the diff adds — and record the debt, then convert to whole-tree the moment
the debt is cleared.

**Does not apply when.** The check is inherently relational to the change
(ordering, authorship, what this diff edits).

## Where this comes from

The whole-tree decision for one checker is recorded with its cause: the claims
it resolves are made by every kind of change, and one change orphaned ten
references that a narrowly-scoped version never saw. A separate lint shows the
full arc — it ran as a ratchet while debt existed, and moved to whole-tree the
moment one change cleared it.

## Related

- [Cannot-run and passed must not print the same](a-check-that-cannot-run-exits-distinctly.md)
- [Fix the class, and sweep the tree for its other instances](sweep-the-class-not-the-instance.md)
- [Order gates cheapest-first and diff-aware](gates-are-cheap-first.md)
