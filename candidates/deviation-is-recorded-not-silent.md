---
name: deviation-is-recorded-not-silent
title: Record every deviation from the brief, with its reason
scope: process
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "job #296 — a field-naming deviation recorded in the commit body and accepted"
  - "job #330 — a storage-layer deviation argued in the commit message and precedented, and accepted for that reason"
  - "job #461 — a rule change made during rework and not recorded, rejected because the record would have frozen as false"
rationale: >
  Deviations are usually right. What makes them expensive is being silent: the
  reviewer discovers a difference and cannot tell whether it is a decision or an
  oversight, so it becomes a finding either way.
related: [the-ticket-is-the-contract, commit-messages-carry-the-why, corrections-are-appended-and-dated]
---

**Rule.** When you implement something other than what the brief specified, say
so in the commit message and in the durable record: what the brief asked, what
you did, and why. Never deliver a silent difference.

**Why.** The reviewer's job is to compare the change against the brief. An
unexplained difference costs a cycle at best. A stated one is usually accepted
in the same review, because the reasoning is right there to judge.

**How to apply.** A short "deviates from the brief" paragraph in the commit
body: the requirement, the implemented behaviour, the reason, and whether the
brief's version remains desirable later. If the deviation changes a documented
rule, update the doc in the same commit.

**Does not apply when.** The difference is cosmetic and unobservable.

## Derivation

Job #330's storage deviation was accepted explicitly because it was "argued in
the commit message and precedented" — keeping a git read off the single-threaded
actor was judged right on its merits, and the argument was available to judge.
Job #461 is the inverse: a rule was changed during rework and the appended
record still said no rule changed, which "freezes as a false record of what this
job did".
