---
type: Blessed Practice
title: "One decision site per question"
description: "Each policy question is answered by exactly one function."
status: draft
tags:
  - bucket/general
  - scope/architecture
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Divergence between a decision and its report is a distinct bug class here: the
  system does the right thing and tells the operator something else. One
  decision site, consumed by both, removes it structurally.
---

**Rule.** Each policy question is answered by exactly one function. Everything
that acts on the answer, and everything that displays the answer, calls it.

**Why.** When the actor and the reporter compute the same thing separately, they
drift, and the drift is invisible until an operator debugs against the report.
The report then actively misleads, which is worse than having no report.

**How to apply.** Extract the predicate before you have two callers, not after.
When adding a display of an existing behaviour, wire the display to the
behaviour's own function rather than reconstructing it from inputs.

**Does not apply when.** The display is deliberately a different question (an
intent versus an observation) — in which case label both, per
separate-intent-from-observation.

## Where this comes from

One snapshot refreshed two of a record's three fields from live state, so the
operator-facing view and the scheduler disagreed about a machine until the
next restart — the system did the right thing and reported something else. A
later change fixed the shape prospectively by extracting the resolution so the
acting path and the reported snapshot could not diverge.

## Related

- [Deciders return effects; interpreters perform them](pure-decider-effects.md)
- [One resolver per lookup question](one-resolver-per-question.md)
- [One writer per record class](single-writer-per-record.md)
