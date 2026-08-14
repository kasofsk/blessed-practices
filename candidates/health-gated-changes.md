---
name: health-gated-changes
title: An automated change is gated on the health of what it changed
scope: operations
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #269 — a deploy health gate asserting a live dispatcher and a live fleet, with the empty-fleet case a failure"
  - "job #329 — the gate firing for real: a healthy dispatcher over an empty fleet, which would previously have passed"
rationale: >
  A self-deploying system needs its deploys to be self-verifying, and the
  interesting part is what the gate asserts: not that the process is up, but
  that the system can do work.
related: [refuse-loudly, deploy-legs-report-skipped, announce-exactly-what-ran]
---

**Rule.** After an automated change to a running system, assert that the system
can do its work — not merely that its processes answer. Bound the check, retry
within the bound, and fail the change if the assertion never holds.

**Why.** Process liveness is the easiest thing to check and the least
informative. A component that answers a health endpoint while no capacity is
registered is exactly the state a deploy can produce and the state that looks
healthy on every dashboard.

**How to apply.** Pick an assertion that requires the whole path: capacity
registered and non-zero, a dependency reachable, a queue draining. State the
window and the interval and justify them. Treat the empty case as a failure,
explicitly, since it is the one an unconfigured system produces.

**Does not apply when.** The change is genuinely inert until an operator acts.

## Derivation

Job #269's gate asserts an alive-node count and non-zero capacity across those
nodes, treating unknown capacity as not-capacity. Job #329's records show it
firing repeatedly against a live dispatcher with no worker registered — the
exact state the earlier liveness check would have called healthy.
