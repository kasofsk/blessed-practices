---
name: prove-with-a-ladder
title: Prove a capability with a ladder of rungs, each one falsifiable
scope: process
altitude: mid
portability: universal
confidence: medium
status: candidate
evidence:
  - "job #395 — a proof job climbing numbered rungs against real infrastructure, each rung asserting one platform fact"
  - "job #417 — a proof whose scripts had two fail-open defects that would have let it report success without proving anything"
  - "The identity proof job's negative rung asserts a capability by declaring none and showing nothing is minted"
rationale: >
  A repeatable shape for establishing that something works end to end against
  real systems, with the crucial property that a failing rung is visible rather
  than skipped — including a deliberate negative rung.
related: [assertions-that-can-fail, a-denial-with-no-control, self-skip-loudly]
---

**Rule.** To establish an end-to-end capability, write a ladder: numbered rungs,
each asserting one fact, each able to fail independently, with a summary that
cannot report success unless every rung passed. Include at least one negative
rung that proves the mechanism is off when it should be.

**Why.** End-to-end proofs are where fail-open defects hide, because the happy
path is long and the summary is written by the same script. A ladder makes each
step attributable and makes the negative case a first-class result.

**How to apply.** Assert the platform facts the rung depends on before asserting
the outcome. Make the summary derive from the rung results, not from reaching
the end. Bound each rung in wall-clock time. Record the run with its host, date
and tree state.

**Does not apply when.** The capability is already covered by a lower-tier test.

## Derivation

Job #417's review found two fail-open defects that "would let the proof report
PASS without proving anything", and job #395's found a summary that
"contradicts itself on every failing run". Both are the same structural risk:
the ladder's report was not derived from the ladder's results.
