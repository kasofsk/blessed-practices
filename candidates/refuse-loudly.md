---
name: refuse-loudly
title: Prefer a loud refusal to a silent degradation
scope: architecture
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/style.md Tier 3 — a control that reports success and does nothing is worse than no control"
  - "job #6 — a launch failure propagated as an error left the task Running forever and the job looking healthy"
  - "job #137 — a broker permission gap made dynamic worker registration silently no-op in production"
rationale: >
  The most damaging failures in this history are not crashes; they are
  operations that reported success and did nothing. A refusal is a ticket; a
  silent no-op is an outage discovered days later by inference.
related: [unenforced-intentions-become-believed-facts, errors-name-the-actionable-thing, fail-closed-allow-lists]
---

**Rule.** When a component cannot do what it was asked, it says so, by name, at
the moment of the request. It never proceeds with the capability quietly
dropped, and it never reports success for a partial result.

**Why.** Silent degradation is read as success by every consumer, including the
humans reading dashboards. The cost of a loud refusal is a failed request; the
cost of a silent one is a false belief that spreads.

**How to apply.** Prefer refusing at declaration time (config validation) over
refusing at use time, and refusing at use time over dropping. A boot that cannot
serve its declared capability refuses to boot rather than serving on without it.
Every refusal names the setting, the value and the node.

**Does not apply when.** The degraded mode is genuinely the product decision —
then it is a documented mode with its own observable state, not a fallback.

## Derivation

Job #6's finding is the pattern in miniature: a launch failure was `?`-propagated,
so the task stayed Running and "the job sits in Evaluation looking healthy —
exactly the wedged state the brief was filed to fix". Job #137's is the
production version: an announce the broker denied, so a whole feature no-op'd on
the real fleet while every test passed against an open server.
