---
name: read-modify-write-reads-again
title: Re-read before you write back
scope: architecture
altitude: low
portability: universal
confidence: high
status: candidate
evidence:
  - "job #291 — a clone taken before a helper that persists a derived value, written back after it"
  - "job #72 — an in-memory index updated by insertion only, never pruned on edit"
rationale: >
  The concrete, greppable form of the single-writer rule. It is worth stating
  separately because the violating code looks completely ordinary and passes
  every type check.
related: [single-writer-per-record, one-decision-site]
---

**Rule.** If you clone a record, call anything that may persist a change, and
then write your clone back, you have overwritten that change. Re-read after the
call, or move your mutation inside the site that owns it.

**Why.** Helper functions that refresh derived state are exactly the ones you
call in the middle of a mutation, and they are invisible at the call site. The
overwrite is silent, and if the record's new state is terminal nothing ever
recomputes it.

**How to apply.** Prefer mutating through the owning function over
clone-mutate-put. Where clone-put is unavoidable, keep the window free of calls,
and add a test that asserts the derived value survives the compound operation.

**Does not apply when.** No path in the window writes the record — which you
should be able to state, not assume.

## Derivation

Job #291's reviewer wrote the failing sequence explicitly, including why nothing
self-heals: the state written was terminal, so no later pass recomputed the
value that had just been clobbered.
