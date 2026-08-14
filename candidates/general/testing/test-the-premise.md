---
type: Blessed Practice
title: "Test the premise, not only the behaviour"
description: "Where a check exists because of an external fact, assert that fact in the suite too."
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
  An unusual and generalisable move: assert the reason the check exists, not
  just the check's output. It makes the test self-documenting and gives a future
  maintainer a principled way to delete it.
---

**Rule.** Where a check exists because of an external fact, assert that fact in
the suite too. If the fact ever stops holding, the suite says so and the check
can be removed on evidence rather than on guesswork.

**Why.** Checks accumulate and nobody dares delete them, because the reason they
exist is not written down anywhere testable. Pinning the premise converts "we
think this is still needed" into a measurement.

**How to apply.** Add a case asserting the external behaviour — this tool
accepts this input, these two implementations disagree, this API returns this
shape. Name it so its purpose is obvious. Say in the header that the gate is
deleted, not tuned, if the premise case ever fails.

**Does not apply when.** The premise is a stable specification rather than an
observed quirk.

## Where this comes from

One suite asserts that the standard syntax checker accepts its failing fixture
and that two shells disagree about it, so the gate's justification is itself
under test and its removal condition is mechanical rather than a matter of
nerve. The header states the consequence: if the premise case ever fails, the
gate is deleted, not tuned.

## Related

- [A test must be able to observe what its name claims](no-vacuous-assertions.md)
- [An architectural boundary that nothing checks is a comment](../architecture/boundaries-are-asserted-not-documented.md)
- [Break it on purpose and watch the named case go red](assertions-that-can-fail.md)
