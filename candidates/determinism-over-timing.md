---
name: determinism-over-timing
title: Wait on the observable, never on the clock
scope: testing
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #229 — a trace test that synchronised on a state write while the effect it asserted was emitted just afterwards; 'nondeterministic and will flake — the exact failure the brief calls out as worse than no trace'"
  - "job #343 — a fixed sleep covering a whole stage transition, unlike its siblings which covered a single event"
  - "The test harness's default wait is set below the core's scan interval so a wait fails loudly instead of being rescued"
rationale: >
  Flaky tests in an orchestrator are indistinguishable from real intermittent
  bugs, which is the worst possible property. The corpus contains both the
  standard sleep-based flake and a subtler one — waiting on a signal emitted
  before the effect under test.
related: [assertions-that-can-fail, bounded-and-loud, no-vacuous-assertions]
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

## Derivation

Job #229's reviewer traced the race precisely: the state write happens before
the trailing effect is recorded, the test's wait resolves on the write, "so
whether the effect is in the snapshot depends on the scheduler". The committed
fixture reflected an early capture, so the test would flip on any run where the
actor got there first.
