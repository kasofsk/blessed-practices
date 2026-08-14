---
name: terminal-means-terminal
title: Terminal states are terminal, and nothing self-heals after them
scope: architecture
altitude: mid
portability: universal
confidence: medium
status: candidate
evidence:
  - "job #291 — a wrong value written during the transition to a terminal state is permanent"
  - "job #167 — a late container exit for a revoked job drove a code path that expected live state and panicked the single-threaded core"
rationale: >
  Terminality is usually treated as a property of the state machine. In practice
  it is a property of the recovery story: anything wrong at the moment of
  transition is wrong forever, and any late event arriving afterwards must be
  dropped deliberately.
related: [single-writer-per-record, restart-reconciliation-is-first-class, refuse-loudly]
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

## Derivation

The 2026-07-23 outage is the record: a revoked job's orphaned container exited,
the exit walked the full verdict path, and a routine that expects live execution
state panicked the core loop. One revoked job took down the platform. The fix
was a single guard at the exit funnel plus a regression test that holds a run
open across a revoke.
