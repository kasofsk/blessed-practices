---
name: stale-base-is-not-an-authoring-failure
title: Distinguish a stale base from a bad attempt
scope: process
altitude: mid
portability: project
confidence: medium
status: candidate
evidence:
  - "job #464 — 'This is a stale-base problem, not an authoring one; rework cannot fix it'"
  - "job #372 cycle 2 — a rebase moved the base and inverted a correction the previous cycle had made true"
  - "job #443/#444 — conflict resolutions where both sides' records were kept, in job order"
rationale: >
  In a self-hosting system with many concurrent jobs, the base moves under a
  branch routinely. Treating a base-induced failure as an authoring failure
  sends the wrong instruction to the fixer and can make the change worse.
related: [escalate-when-the-brief-is-unsatisfiable, merge-conflicts-keep-both-records, one-commit-when-ordering-matters]
---

**Rule.** When a finding is caused by the branch's base rather than by the
change, say so and name the remedy: rebase, wait for a dependency, or re-cut the
ticket. Do not phrase it as a defect in the work.

**Why.** The two have opposite fixes. Reworking the change against a bad base
produces churn and can invert a correction that was accurate when written. And a
brief written against a tree the branch does not have cannot be satisfied by
editing the branch.

**How to apply.** Establish the base commit and check whether the cited symbols,
lines and sections exist there. If they do not, report the base and stop. After
any rebase, re-verify the claims the previous cycle made — a rebase can falsify
a correction without touching it.

**Does not apply when.** The branch simply failed to rebase when it should have
— that is an authoring failure, and worth saying.

## Derivation

Job #372's cycle-2 review is the clearest case: all four prior findings were
fixed, and then "the rebase moved the base onto a tree that rewrote the
referenced document — and the correction now asserts the opposite of the tree it
would merge into". The work was right; the base moved.
