---
type: Blessed Practice
title: "An automated change is gated on the health of what it changed"
description: "After an automated change to a running system, assert that the system can do its work — not merely that its processes answer."
status: draft
tags:
  - bucket/general
  - scope/operations
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  A self-deploying system needs its deploys to be self-verifying, and the
  interesting part is what the gate asserts: not that the process is up, but
  that the system can do work.
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

## Where this comes from

The gate asserts an alive-node count and non-zero capacity across those nodes,
treating unknown capacity as not-capacity rather than as capacity. Its records
show it firing repeatedly against a system whose processes answered a health
endpoint while no capacity was registered at all — the exact state a plain
liveness check calls healthy.

## Related

- [A multi-leg operation reports every leg, including the ones it skipped](deploy-legs-report-skipped.md)
- [Announce exactly what ran — never a tier you did not execute](../process/announce-exactly-what-ran.md)
- [Prefer a loud refusal to a silent degradation](../architecture/refuse-loudly.md)
