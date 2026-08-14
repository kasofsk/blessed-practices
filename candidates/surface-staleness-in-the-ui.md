---
name: surface-staleness-in-the-ui
title: An interface that cannot prove freshness must not imply it
scope: code
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #300 — a staleness clock that only ticked while something was running, so a node going silent on an idle fleet never flipped to stale, and the display asserted freshness"
  - "job #256 — a control that stranded rows in a permanent loading state when clicked while their data was in flight"
rationale: >
  Operator interfaces are read as evidence during incidents. A display that
  degrades to 'looks fine' exactly when the system is idle or broken is worse
  than one that shows nothing.
related: [separate-intent-from-observation, silent-filters-hide-rows, announce-exactly-what-ran]
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

## Derivation

Job #300's finding names both halves: the clock only advanced while something
was running, so a silent node never flipped to stale, and once its timestamp
advanced past the frozen clock the clamped display read "reported 0s ago" —
"idle is the capacity-failure case".
