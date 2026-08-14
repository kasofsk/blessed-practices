---
name: test-the-premise
title: Test the premise, not only the behaviour
scope: testing
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #501 — the suite pins the premise as well as the behaviour: the syntax checker accepts the broken fixture, and the two shells disagree about it, so the gate is deleted rather than tuned if the divergence disappears"
  - "job #497 — a claimed capability whose enabling condition was destroyed by an unrelated teardown before it could be used"
rationale: >
  An unusual and generalisable move: assert the reason the check exists, not
  just the check's output. It makes the test self-documenting and gives a future
  maintainer a principled way to delete it.
related: [assertions-that-can-fail, no-vacuous-assertions, boundaries-are-asserted-not-documented]
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

## Derivation

Job #501's suite asserts that the standard syntax checker accepts the failing
fixture and that two shells disagree about it — so the gate's justification is
itself under test, and its removal condition is mechanical.
