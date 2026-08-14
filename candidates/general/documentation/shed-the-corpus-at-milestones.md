---
type: Blessed Practice
title: "A knowledge corpus needs a shedding process, not only an appending one"
description: "Periodically and deliberately remove knowledge that has stopped earning its place: heads compacted, fully-implemented designs deleted outright, every referrer repointed or stubbed."
status: draft
tags:
  - bucket/general
  - scope/documentation
  - altitude/high
  - portability/universal
  - confidence/medium
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Every other practice here adds text. Without a counterweight the corpus grows
  until nobody reads it, at which point its accuracy stops mattering. This is
  the only mechanism in the corpus designed to remove knowledge deliberately.
---

**Rule.** Periodically and deliberately remove knowledge that has stopped
earning its place: heads compacted, fully-implemented designs deleted outright,
every referrer repointed or stubbed. Shedding is a distinct kind of work with
its own review, not a side effect of other work.

**Why.** An append-only corpus grows without bound, and the practical failure is
not wrongness but unreadability — the reader stops reading, so the accuracy
nobody is checking stops mattering. Removal must be a first-class operation or
it never happens.

**How to apply.** Trigger on a milestone, not a threshold. Licence deletion
narrowly: only artefacts whose status says they are fully implemented, so the
knowledge is in the code. Repoint or stub every reference. Keep the rejected
alternatives — they are the part that cannot be re-derived.

**Does not apply when.** The corpus is small enough that nobody skips it.

## Where this comes from

The first deliberate shed of the source corpus took seven review cycles, and
its most instructive cycle restored four sentences earlier passes had removed:
provenance and authorship statements that named no mechanism and described no
behaviour, so every mechanical check was green while they were missing. That
is the failure mode the design predicted, observed on the first run.

## Related

- [A mutable head over an append-only body](mutable-head-append-only-body.md)
- [Deletion is reviewed by accounting, because the usual gates go green](deletion-needs-accounting.md)
- [Measure corpus growth; do not set a threshold for it](growth-is-measured-not-felt.md)
