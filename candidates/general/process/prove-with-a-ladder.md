---
type: Blessed Practice
title: "Prove a capability with a ladder of rungs, each one falsifiable"
description: "To establish an end-to-end capability, write a ladder: numbered rungs, each asserting one fact, each able to fail independently, with a summary that cannot report success unless every rung passed."
status: draft
tags:
  - bucket/general
  - scope/process
  - altitude/mid
  - portability/universal
  - confidence/medium
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  A repeatable shape for establishing that something works end to end against
  real systems, with the crucial property that a failing rung is visible rather
  than skipped — including a deliberate negative rung.
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

## Where this comes from

One end-to-end proof had two fail-open defects that would have let it report
success without proving anything; another had a summary that contradicted
itself on every failing run. Both are the same structural risk — the report
was not derived from the results — and both were caught by reading the script
rather than by running it.

## Related

- [A denial with no control identifies no mechanism](../testing/a-denial-with-no-control.md)
- [A test that cannot run says so; it never passes vacuously](../testing/self-skip-loudly.md)
- [Break it on purpose and watch the named case go red](../testing/assertions-that-can-fail.md)
