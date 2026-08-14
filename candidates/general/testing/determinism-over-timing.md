---
type: Blessed Practice
title: "Wait on the observable, never on the clock"
description: "Synchronise on the observable the assertion depends on, not on time and not on a proxy signal that fires earlier."
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
  Flaky tests in an orchestrator are indistinguishable from real intermittent
  bugs, which is the worst possible property. The corpus contains both the
  standard sleep-based flake and a subtler one — waiting on a signal emitted
  before the effect under test.
---

**Rule.** Synchronise on the observable the assertion depends on, not on time
and not on a proxy signal that fires earlier. Bound every wait, and set the
bound below any background interval that could rescue it.

**Why.** A sleep encodes a guess about a machine you do not control. A proxy
signal encodes a guess about ordering inside the component under test — and when
that ordering changes, the test does not fail, it flakes. And a wait bounded
above a background retry interval passes for the wrong reason, hiding the very
stall it was written to catch.

**How to apply.** Wait for the last thing the assertion needs, not the first
thing that indicates progress. Where the component writes state and then emits
an effect, wait on the effect. Choose timeouts by reference to the system's own
intervals and say why in a comment on the constant.

**Does not apply when.** The property under test is itself temporal — then the
timing is the assertion, and it should be stated as one.

## Where this comes from

A trace test synchronised on a state write while the effect it asserted was
emitted immediately afterwards, so whether the assertion saw it depended on
the scheduler — and the committed fixture reflected an early capture, so the
test would flip on any run where the other side won. A second instance: a
fixed sleep covering an entire phase transition, where its siblings covered a
single event. A third: a harness whose default wait was deliberately set below
a background retry interval, so a stall fails loudly instead of being rescued.

## Related

- [A test must be able to observe what its name claims](no-vacuous-assertions.md)
- [Break it on purpose and watch the named case go red](assertions-that-can-fail.md)
- [Everything is bounded, and the bound is loud](../architecture/bounded-and-loud.md)
