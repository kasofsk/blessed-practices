---
name: separate-intent-from-observation
title: Keep declared intent and observed state in separate fields
scope: architecture
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "design #293 — the observed-versus-intended split, with an asserted invariant that placement never reads intent"
  - "jobs #296, #297, #298 — the slices that implemented it, including provenance on both records"
rationale: >
  The design that resolved this project's longest-running fleet confusion did it
  by refusing to collapse two meanings into one number. The resulting vocabulary
  — intent, observation, provenance, staleness — has been reusable everywhere
  since.
related: [one-decision-site, boundaries-are-asserted-not-documented, surface-staleness-in-the-ui]
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

## Derivation

Design #293 §5a and its slices introduced the split with an ordering key, a
provenance field, and a UI that distinguishes converged, pending, stale,
rejected and unacknowledged. Job #300's review then found the one bug that
matters in such a scheme: a clock that stopped while the fleet was idle, so a
node going silent never flipped to stale — "idle is the capacity-failure case".
