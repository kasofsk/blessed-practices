---
type: Blessed Practice
title: "Corrections are appended, dated, and name their job"
description: "A correction is a new dated section naming the change that wrote it, what it corrects, and what evidence changed the answer."
status: draft
tags:
  - bucket/general
  - scope/documentation
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  The mechanism that makes an append-only body survivable. It also creates an
  unusually good audit trail: what was believed, when, on what evidence, and
  what replaced it.
---

**Rule.** A correction is a new dated section naming the change that wrote it, what
it corrects, and what evidence changed the answer. It never edits the text it
corrects.

**Why.** The reader needs to know both what is true now and why the earlier
answer looked right — that is what stops the same wrong turn being taken again.
A silent edit erases the second half.

**How to apply.** Head the section with the date and the change that made it. State the superseded
claim verbatim, then the new one, then the evidence: host, command, tree state,
output. Point the head at the correction. Where a correction supersedes an
earlier correction the same day, say so rather than leaving two.

**Does not apply when.** The text is in a mutable head — edit it in place.

## Where this comes from

One correction records a proof on two platforms with host, operating system,
tree state and command for each. Another shows why the discipline matters: a
correction recorded a plausible diagnosis as established fact, a reviewer
refuted it from the code, and because the change's whole product was a record
— half of it going into an append-only body — it had to be right before it
could merge.

## Related

- [A mutable head over an append-only body](mutable-head-append-only-body.md)
- [Date every measurement, and name the host it was taken on](date-the-measurement.md)
- [Report verification as commands and outputs, not as adjectives](../process/verification-is-reported-with-its-command.md)
