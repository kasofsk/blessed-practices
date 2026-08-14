---
type: Blessed Practice
title: "Everything is bounded, and the bound is loud"
description: "Every loop has an iteration cap, every queue a depth limit, every wait a deadline."
status: draft
tags:
  - bucket/general
  - scope/architecture
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Bounding is well understood; what this history adds is that the bound must be
  in the dimension the failure occurs in, and that hitting it must produce a
  named, attributable event rather than a silent give-up.
---

**Rule.** Every loop has an iteration cap, every queue a depth limit, every wait
a deadline. Hitting a bound emits a named failure that says which bound, with
what value, and what the caller should do.

**Why.** In an orchestrator, an unbounded wait does not fail — it wedges, and a
wedged component looks healthy. The named failure is what turns an outage into
a ticket.

**How to apply.** Bound in the dimension that actually varies: wall clock for
anything that waits on another machine, iterations only for pure loops. Check
the bound *between* units of work so the stop point is attributable, and print
what was not reached. Give the bound a named constant with the unit in the name.

**Does not apply when.** The bound would be arbitrary and the operation is
already bounded by something real upstream — in which case say which upstream
bound contains it, and derive your constant from it rather than guessing.

## Where this comes from

One review rejected waits that counted iterations while the calls inside them
were unbounded: the loop counted, the calls hung, and the bound measured
nothing. A better example in the same corpus derived a new timeout from the
enclosing budget and refused any larger value at parse time — a bound that
cannot exceed the one containing it.

## Related

- [A re-queued item keeps its original clock](a-queue-entry-keeps-its-clock.md)
- [An error names one cause and one action, and only when it is that cause](../code/errors-name-the-actionable-thing.md)
- [Prefer a loud refusal to a silent degradation](refuse-loudly.md)
