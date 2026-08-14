---
type: Blessed Practice
title: "An interface that cannot prove freshness must not imply it"
description: "Any display of live state shows its own freshness, and its freshness clock runs unconditionally."
status: draft
tags:
  - bucket/general
  - scope/code
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Operator interfaces are read as evidence during incidents. A display that
  degrades to 'looks fine' exactly when the system is idle or broken is worse
  than one that shows nothing.
---

**Rule.** Any display of live state shows its own freshness, and its freshness
clock runs unconditionally. A view that cannot determine state says so, rather
than rendering the last known value as current.

**Why.** Idle is the failure case: when placement is broken nothing runs, so a
clock driven by activity stops exactly when the operator needs it. A frozen
timestamp then reads as "reported just now", actively asserting the opposite of
the truth.

**How to apply.** Drive the freshness clock from time, not from activity. Clamp
carefully — a value that clamps to zero reads as fresh. Distinguish loading,
unknown, stale and absent as separate visual states, and make sure each is
reachable.

**Does not apply when.** The value is static by definition.

## Where this comes from

A staleness indicator's clock ran only while something was executing, so a
component going silent on an idle system never flipped to stale — and once its
timestamp advanced past the frozen clock, the clamped display read "reported
0s ago", asserting the opposite of the truth. Idle is the failure case: when
scheduling is broken, nothing runs.

## Related

- [A dropped row reads like a negative result](../process/silent-filters-hide-rows.md)
- [Announce exactly what ran — never a tier you did not execute](../process/announce-exactly-what-ran.md)
- [Keep declared intent and observed state in separate fields](../architecture/separate-intent-from-observation.md)
