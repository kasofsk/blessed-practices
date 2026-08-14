---
name: corrections-are-appended-and-dated
title: Corrections are appended, dated, and name their job
scope: documentation
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "The design corpus carries dozens of '## Correction — <date>, job #N' sections"
  - "job #457 — a correction recording what was proven, on which host, at which tree sha, with the command"
  - "job #456 — a correction rejected because the diagnosis it recorded was refuted by the tree"
rationale: >
  The mechanism that makes an append-only body survivable. It also creates an
  unusually good audit trail: what was believed, when, on what evidence, and
  what replaced it.
related: [mutable-head-append-only-body, date-the-measurement, verification-is-reported-with-its-command]
---

**Rule.** A correction is a new dated section naming the job that wrote it, what
it corrects, and what evidence changed the answer. It never edits the text it
corrects.

**Why.** The reader needs to know both what is true now and why the earlier
answer looked right — that is what stops the same wrong turn being taken again.
A silent edit erases the second half.

**How to apply.** Head the section with the date and job. State the superseded
claim verbatim, then the new one, then the evidence: host, command, tree state,
output. Point the head at the correction. Where a correction supersedes an
earlier correction the same day, say so rather than leaving two.

**Does not apply when.** The text is in a mutable head — edit it in place.

## Derivation

Job #457's correction records a proof on two platforms with host, OS, tree sha
and command for each. Job #456 shows why the discipline matters: a correction
recorded a plausible diagnosis as established fact, the reviewer refuted it from
the tree, and because "this job's whole product is a record, and half of it goes
into an append-only body, that has to be right before it merges".
