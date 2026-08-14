---
name: no-vacuous-assertions
title: A test must be able to observe what its name claims
scope: testing
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #276 — a test asserting a contract the function under test never reads, passing identically with the opposite input"
  - "job #297 — an assertion that could not hold against the fake backend and would fail the moment the real one ran"
  - "job #302 — an invariant checker that ran but whose breaches were discarded because nobody drained the sink"
rationale: >
  A family of failures where the test infrastructure is present, the test is
  green, and nothing is actually being checked. Three distinct mechanisms in
  three jobs, all with the same signature.
related: [assertions-that-can-fail, lowest-tier-that-expresses-it, boundaries-are-asserted-not-documented]
---

**Rule.** Check that the test can observe the thing it names: the function under
test must read the input you are varying, the fixture must be able to produce
the state you assert, and the assertion must be reached and drained.

**Why.** Green is the default outcome of a test that observes nothing. The name
then documents coverage that does not exist, and the next author trusts it.

**How to apply.** Ask what would have to be true for this test to fail, and
construct it. Where a checker records findings for later, assert that the
findings were drained — "the checker runs but nobody asserts" is the same hole
one level up. Prefer deriving assertion sites from the API rather than adding
them by eye, so wrapped and multi-line call sites are not silently skipped.

**Does not apply when.** The test is a smoke test whose only claim is that
nothing panicked — name it that way.

## Derivation

Job #302 is the richest instance: an invariant checker was wired into sixteen
test files, but only single-line call sites got an assertion, so several whole
test functions recorded breaches that were silently discarded at teardown. Cycle
2 derived the call sites from the API's method names instead of by eye.
