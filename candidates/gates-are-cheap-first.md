---
name: gates-are-cheap-first
title: Order gates cheapest-first and diff-aware
scope: process
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "Reading reviewers run at stage 0; the executing gate runs at stage 1 only on what they accept"
  - ".chug/tasks/ci.sh — pure-shell gates run before the diff-aware compile stages, so a docs-only change is still gated and gates in seconds"
  - "job #258 — a whole-repo duplication check runs unconditionally because it costs about 30ms"
rationale: >
  A gate ordering that puts the slow stage last is obvious; what this repo adds
  is that cheap whole-tree gates should be unconditional, because scoping them
  to the diff is what let a code job orphan references a scoped gate never saw.
related: [reviewers-read-they-do-not-run, whole-tree-not-just-the-diff, every-gate-has-a-test-suite]
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

## Derivation

This project's gate script runs eight pure-shell gates before its diff-aware
compile stages, so a documentation-only change is still fully gated and finishes
in seconds. The whole-tree decision is recorded with its reason: a scoped
doc-facts gate would not have seen the ten orphaned references a code job left
behind.
