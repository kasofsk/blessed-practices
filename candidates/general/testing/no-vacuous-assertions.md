---
type: Blessed Practice
title: "A test must be able to observe what its name claims"
description: "Check that the test can observe the thing it names: the function under test must read the input you are varying, the fixture must be able to produce the state you assert, and the assertion must be reached and drained."
status: draft
tags:
  - bucket/general
  - scope/testing
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  A family of failures where the test infrastructure is present, the test is
  green, and nothing is actually being checked. Three distinct mechanisms in
  three jobs, all with the same signature.
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

## Where this comes from

The richest instance: an invariant checker was wired into sixteen test files,
but only single-line call sites got an assertion, so several whole test
functions recorded breaches that were silently discarded at teardown — the
checker runs and nobody asserts. The fix derived the call sites from the API's
method names instead of finding them by eye.

## Related

- [An architectural boundary that nothing checks is a comment](../architecture/boundaries-are-asserted-not-documented.md)
- [Break it on purpose and watch the named case go red](assertions-that-can-fail.md)
- [New behaviour lands with a test at the lowest tier that can express it](lowest-tier-that-expresses-it.md)
