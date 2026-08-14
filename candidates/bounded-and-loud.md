---
name: bounded-and-loud
title: Everything is bounded, and the bound is loud
scope: architecture
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/style.md Tier 2 rule 3"
  - "job #395 — rung waits were iteration-bounded rather than wall-clock bounded, with unbounded calls inside them"
  - "job #150 — a starved launch could reset its own escalation clock and never escalate"
rationale: >
  Bounding is well understood; what this history adds is that the bound must be
  in the dimension the failure occurs in, and that hitting it must produce a
  named, attributable event rather than a silent give-up.
related: [a-queue-entry-keeps-its-clock, refuse-loudly, errors-name-the-actionable-thing]
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

## Derivation

Job #395's reviewer rejected iteration-bounded waits containing unbounded calls:
the loop counted, the calls hung, so the bound measured nothing. Job #384
derived a new timeout from the enclosing RPC budget and refused values above it
at parse time, which is the shape to copy — a bound that cannot exceed the one
containing it.
