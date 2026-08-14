---
type: Blessed Practice
title: "Terminal states are terminal, and nothing self-heals after them"
description: "Treat the transition into a terminal state as the last chance to be correct."
status: draft
tags:
  - bucket/general
  - scope/architecture
  - altitude/mid
  - portability/universal
  - confidence/medium
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Terminality is usually treated as a property of the state machine. In practice
  it is a property of the recovery story: anything wrong at the moment of
  transition is wrong forever, and any late event arriving afterwards must be
  dropped deliberately.
---

**Rule.** Treat the transition into a terminal state as the last chance to be
correct. Late events for a terminal record are dropped at a single guard, before
any routing that assumes live state.

**Why.** Self-healing loops skip terminal records by design, so a defect
committed at that moment has no second chance. And an event arriving after
teardown will find half its context missing — if it is routed anyway, the
failure lands in the wrong place, at worst taking down the component.

**How to apply.** Put the drop-late-events guard at the funnel, not in each
consumer. Assert the negative space: no transition out of the terminal state,
and no handler reachable for a record that is in one. Test by holding a run open
across a revoke.

**Does not apply when.** The terminal state is re-openable by an operator — then
it is not terminal, and its re-entry path needs the same reconciliation as any
other.

## Where this comes from

A record was terminated while one of its containers was still alive. The
container's exit was then routed through the full verdict path, which reached
code expecting live execution state and panicked the single-writer core — one
terminated unit of work took down the whole platform. The fix was a single
guard at the exit funnel plus a regression test that holds a run open across
the termination.

## Related

- [Every in-flight state has a restart arm](restart-reconciliation-is-first-class.md)
- [One writer per record class](single-writer-per-record.md)
- [Prefer a loud refusal to a silent degradation](refuse-loudly.md)
