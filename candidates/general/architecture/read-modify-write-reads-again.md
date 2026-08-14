---
type: Blessed Practice
title: "Re-read before you write back"
description: "If you clone a record, call anything that may persist a change, and then write your clone back, you have overwritten that change."
status: draft
tags:
  - bucket/general
  - scope/architecture
  - altitude/low
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  The concrete, greppable form of the single-writer rule. It is worth stating
  separately because the violating code looks completely ordinary and passes
  every type check.
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

## Where this comes from

A handler cloned a record, called a helper that recomputed and persisted a
derived value, then wrote its stale clone back — silently reverting the
recomputation. The reason it never healed is the part worth remembering: the
state being written was terminal, so no later pass recomputed anything.

## Related

- [One decision site per question](one-decision-site.md)
- [One writer per record class](single-writer-per-record.md)
