---
type: Blessed Practice
title: "Keep declared intent and observed state in separate fields"
description: "When a value can be both requested and reported, store two values: what was asked for, and what was last observed."
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
  The design that resolved the source project's longest-running capacity
  confusion did it by refusing to collapse two meanings into one number. The
  resulting vocabulary — intent, observation, provenance, staleness — has been
  reusable everywhere since.
---

**Rule.** When a value can be both requested and reported, store two values:
what was asked for, and what was last observed. Every consumer names which one
it reads, and the acting path reads the observation.

**Why.** Collapsing them produces a number that is sometimes a wish and
sometimes a fact, with no way to tell which — so an operator cannot distinguish
"the node has not applied it yet" from "the node refused" from "the change never
reached it".

**How to apply.** Carry provenance and an observation timestamp beside the
observed value. Assert, executably, that the acting path never reads intent.
Make the reconciliation loop the only thing that pushes intent toward
observation, and give it a terminal state for a refusal so it stops re-pushing.

**Does not apply when.** The value is only ever asserted locally and applied
synchronously.

## Where this comes from

The design that resolved the source project's longest-running capacity
confusion did it by refusing to collapse a request and a report into one
number, adding provenance and an observation timestamp beside the observed
value. The one bug worth knowing about in such a scheme surfaced in its
interface: a staleness clock driven by activity stops exactly when the system
is idle, which is the failure case.

## Related

- [An architectural boundary that nothing checks is a comment](boundaries-are-asserted-not-documented.md)
- [An interface that cannot prove freshness must not imply it](../code/surface-staleness-in-the-ui.md)
- [One decision site per question](one-decision-site.md)
