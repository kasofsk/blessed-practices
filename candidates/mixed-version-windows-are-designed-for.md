---
name: mixed-version-windows-are-designed-for
title: Design for the mixed-version window, because you are always in one
scope: operations
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "job #403 — an additive field plus a guard turning the older side's silent semantic drop into a named failure"
  - "job #381 — an error message that fired wrongly on every task on a node running the previous version"
  - "job #480 — a mixed fleet preserved deliberately: the older path left byte-for-byte unchanged"
rationale: >
  A self-deploying system with a heterogeneous fleet is never uniformly
  versioned. The corpus treats the mixed window as the normal operating
  condition, which changes how every wire and script change is reviewed.
related: [additive-wire-evolution, errors-name-the-actionable-thing, refuse-loudly]
---

**Rule.** Assume both versions are running simultaneously. Every wire change,
script change and configuration change states what the older side does when it
meets the newer one, and the answer is never "silently ignores the difference".

**Why.** Rollouts take minutes to days across a fleet, and failures cluster
there. The default behaviour of an older component meeting a newer message is to
drop what it does not understand — which is fine for an addition and catastrophic
for a semantic change.

**How to apply.** Ask, for every field and flag: what does the previous version
do with this? Where it would drop meaning, add a guard that converts the drop
into a named failure. Keep the old path byte-identical where you can, and pin
that with a golden. Expect error branches to be busiest during the window and
check their messages there.

**Does not apply when.** The deploy is atomic across every participant.

## Derivation

Job #403's reviewer credits the decision explicitly: an additive field plus a
guard "that turns the N-1 semantic drop into a named task failure — better than
a constant nothing compares". Job #381 is the cost of not thinking about the
window: a routine older-node reply produced a confidently wrong operator
instruction on every task.
