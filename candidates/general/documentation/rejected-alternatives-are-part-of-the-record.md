---
type: Blessed Practice
title: "The rejected alternatives are the part that cannot be re-derived"
description: "A decision document states each rejected alternative at its strongest, with its real costs, before rejecting it — and keeps that section forever."
status: draft
tags:
  - bucket/general
  - scope/documentation
  - altitude/high
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  The strongest consistent signal in the design-review corpus. Documents that
  price their alternatives get accepted; documents that only argue for their
  recommendation come back, even when the recommendation is right.
---

**Rule.** A decision document states each rejected alternative at its strongest,
with its real costs, before rejecting it — and keeps that section forever. The
recommendation concedes the column where an alternative wins.

**Why.** The implementation can be re-derived from the code. The reasons an
option was rejected cannot: they live only in the head of whoever considered it,
and they are exactly what someone will want when circumstances change. A
document that only argues one way is indistinguishable from one that never
considered the others.

**How to apply.** Give each option a real "for" case in its own terms. Name the
condition that would revive it — what would have to change for this to become
the right answer. When compacting later, this section is the last to go.

**Does not apply when.** There genuinely was no alternative, which is rarer than
it feels — say why.

## Where this comes from

Review after review in the source corpus praises the same property: the
options section is honest, the asymmetry and the ownership inversion are real
costs fairly stated, the losing option is put at its strongest before it is
killed. The complementary finding is equally consistent — documents omitting
an obvious competitor are sent back for it by name.

## Related

- [A design decides the central question](decide-do-not-straddle.md)
- [A knowledge corpus needs a shedding process, not only an appending one](shed-the-corpus-at-milestones.md)
- [A mutable head over an append-only body](mutable-head-append-only-body.md)
