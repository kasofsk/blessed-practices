---
name: rejected-alternatives-are-part-of-the-record
title: The rejected alternatives are the part that cannot be re-derived
scope: documentation
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "Design reviews here routinely credit a document for stating a rejected option at its strongest before killing it"
  - "job #310 — 'rejected option A is stated at its strongest before being killed', cited as the mark of a decided rather than straddled question"
  - "design #533 — the shed a human approver most likely has to catch is a shed rejected alternative"
rationale: >
  The strongest consistent signal in the design-review corpus. Documents that
  price their alternatives get accepted; documents that only argue for their
  recommendation come back, even when the recommendation is right.
related: [decide-do-not-straddle, mutable-head-append-only-body, shed-the-corpus-at-milestones]
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

## Derivation

Review after review in this corpus praises the same property: "the options
section is honest — the asymmetry and the ownership inversion are real costs,
fairly stated", "rejected option A is stated at its strongest before being
killed". The complementary finding is just as consistent: documents that omit an
obvious competitor come back for it by name.
