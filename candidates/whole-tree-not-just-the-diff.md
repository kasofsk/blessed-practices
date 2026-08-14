---
name: whole-tree-not-just-the-diff
title: Cheap checks run whole-tree, not only over the diff
scope: process
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "The doc-facts gate runs whole-tree on every job because a code job orphaned references a diff-scoped gate never saw"
  - "job #342 — once the tree reached zero non-doc comments, the lint moved from ratchet to whole-tree"
rationale: >
  Diff-scoping is the reflex, and it is wrong for anything cheap. The failures
  here are all of the same shape: a change in one area invalidates a claim in
  another, and only a whole-tree pass connects them.
related: [gates-are-cheap-first, sweep-the-class-not-the-instance, a-check-that-cannot-run-exits-distinctly]
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

## Derivation

The whole-tree decision for the path checker is recorded with its cause: the
claims are made by every job type, and a code job orphaned ten references that a
docs-scoped gate never saw. The comment lint shows the ratchet-to-whole-tree
transition after the debt was cleared in one job.
