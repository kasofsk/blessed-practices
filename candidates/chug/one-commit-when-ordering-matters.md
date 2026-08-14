---
type: Blessed Practice
title: "When a gate reads commit order, ship one commit"
description: "If any gate derives meaning from commit timestamps or commit membership, keep the branch to one commit — or make every commit that touches a subject also touch the docs that name it."
status: draft
tags:
  - bucket/chug
  - scope/process
  - altitude/low
  - portability/project
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
sources:
  - resource: https://github.com/kasofsk/chuggernaut
    title: "Chuggernaut — the platform this practice was derived from"
evidence:
  - "jobs #449, #453, #468, #469, #495, #531 — branches failing the staleness gate purely because a later commit touched a file an earlier commit's doc names"
  - "job #449 cycle 3 — the blocker cleared by squashing to a single commit"
rationale: >
  Six separate jobs lost a cycle to the same mechanical trap. It is entirely
  avoidable and entirely non-obvious, which is exactly what a blessed practice
  is for.
---

**Rule.** If any gate derives meaning from commit timestamps or commit
membership, keep the branch to one commit — or make every commit that touches a
subject also touch the docs that name it.

**Why.** Ordering-sensitive gates compare the newest commit per path. A branch
that lands a doc edit and then, in a later commit, changes a file that doc names
is flagged even though both are in the same change. Rework commits make this
near-certain, because they touch code after the docs were written.

**How to apply.** Squash before submitting when the branch has been reworked.
Where a second commit is unavoidable, use the gate's own attestation mechanism —
an assertion of attention that survives a rebase, written into a tracked file
rather than a commit trailer.

**Does not apply when.** No gate reads commit structure — then commit however
you like.

## Where this comes from

Job #449's cycle-2 blocker was derived by the reviewer from the two commits'
timestamps and the docs' path claims; cycle 3 cleared it by squashing. Job #453
then reproduced it in the other direction — a correct prose fix committed alone,
newer than the three docs beside it, re-opened the same block.

## Related

- [A change updates the docs it makes stale, in the same commit](../general/documentation/docs-updated-in-the-same-commit.md)
- [Clear an attention gate with an assertion of attention, not a timestamp](../general/documentation/assertion-of-attention-over-timestamp.md)
- [Rework builds on the previous attempt; it does not restart it](branch-preserved-across-rework.md)
