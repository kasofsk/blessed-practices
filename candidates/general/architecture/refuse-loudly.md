---
type: Blessed Practice
title: "Prefer a loud refusal to a silent degradation"
description: "When a component cannot do what it was asked, it says so, by name, at the moment of the request."
status: draft
tags:
  - bucket/general
  - scope/architecture
  - altitude/high
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  The most damaging failures in this history are not crashes; they are
  operations that reported success and did nothing. A refusal is a ticket; a
  silent no-op is an outage discovered days later by inference.
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

## Where this comes from

Two instances anchor this. A launch failure propagated as an error rather than
recorded as a failure left the record running forever, so the work sat looking
healthy — the exact wedged state the fix was filed to remove. And a missing
transport permission made an entire feature a no-op in production while every
test passed against a permissive local server.

## Related

- [An error names one cause and one action, and only when it is that cause](../code/errors-name-the-actionable-thing.md)
- [An unenforced intention gets read as a statement of fact](unenforced-intentions-become-believed-facts.md)
- [Grants are allow-lists, fail-closed, refused at three layers](fail-closed-allow-lists.md)
