---
type: Blessed Practice
title: "Design for the mixed-version window, because you are always in one"
description: "Assume both versions are running simultaneously."
status: draft
tags:
  - bucket/general
  - scope/operations
  - altitude/high
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  A system that deploys itself across a heterogeneous estate is never uniformly
  versioned. The source retrospective treats the mixed window as the normal
  operating condition, which changes how every wire and script change is
  reviewed.
---

**Rule.** Assume both versions are running simultaneously. Every wire change,
script change and configuration change states what the older side does when it
meets the newer one, and the answer is never "silently ignores the difference".

**Why.** Rollouts take minutes to days across an estate, and failures cluster
there. The default behaviour of an older component meeting a newer message is to
drop what it does not understand — which is fine for an addition and catastrophic
for a semantic change.

**How to apply.** Ask, for every field and flag: what does the previous version
do with this? Where it would drop meaning, add a guard that converts the drop
into a named failure. Keep the old path byte-identical where you can, and pin
that with a golden. Expect error branches to be busiest during the window and
check their messages there.

**Does not apply when.** The deploy is atomic across every participant.

## Where this comes from

One review credits the decision in its own terms: an additive field plus a
guard that turns the older side's silent semantic drop into a named failure,
better than a constant nothing compares. The cost of not thinking about the
window appears elsewhere in the same corpus — a routine reply from an older
peer produced a confidently wrong operator instruction on every task it
touched.

## Related

- [An error names one cause and one action, and only when it is that cause](../code/errors-name-the-actionable-thing.md)
- [Prefer a loud refusal to a silent degradation](../architecture/refuse-loudly.md)
- [Wire changes are additive, epoch-gated, and tolerated by N-1](../architecture/additive-wire-evolution.md)
