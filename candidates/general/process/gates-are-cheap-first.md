---
type: Blessed Practice
title: "Order gates cheapest-first and diff-aware"
description: "Run gates in ascending cost."
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
  A gate ordering that puts the slow stage last is obvious; what this repo adds
  is that cheap whole-tree gates should be unconditional, because scoping them
  to the diff is what let a code job orphan references a scoped gate never saw.
---

**Rule.** Run gates in ascending cost. Anything cheap enough to run on every
change runs unconditionally and whole-tree; expensive stages are gated on the
paths the diff touches, and say which stages they skipped.

**Why.** Fast feedback is the point, but scoping a cheap gate to the diff buys
nothing and loses whole-tree coverage. The expensive stage is where scoping
pays, and that is also where an unannounced skip is most misleading.

**How to apply.** Measure each gate; if it is under a second whole-tree, make it
unconditional. Derive the expensive stages' triggers from path globs and print
which stages ran and which did not. Never let "no relevant paths changed" print
the same as "passed".

**Does not apply when.** The cheap gate is inherently diff-scoped (a
staleness ordering check over the docs a branch edits).

## Where this comes from

The source project runs eight sub-second whole-tree checks before its path-
triggered compile stages, so a documentation-only change is still fully gated
and finishes in seconds. The whole-tree decision is recorded with its cause: a
change in one area orphaned ten references elsewhere that a diff-scoped
version of the same check never saw.

## Related

- [A gate is code, so it has tests, and the tests are discovered](every-gate-has-a-test-suite.md)
- [Cheap checks run whole-tree, not only over the diff](whole-tree-not-just-the-diff.md)
