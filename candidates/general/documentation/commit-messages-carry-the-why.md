---
type: Blessed Practice
title: "The commit message carries the why"
description: "The commit message explains why the change is shaped the way it is: what changed, why this shape, what was deliberately not done, and how it was verified."
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
  In this project the commit message is the primary durable record of reasoning,
  and it visibly works: reviewers cite commit bodies as evidence, and deviations
  argued there are accepted rather than reworked.
---

**Rule.** The commit message explains why the change is shaped the way it is:
what changed, why this shape, what was deliberately not done, and how it was
verified. The diff shows what; only the message can show why.

**Why.** Pull-request threads and chat transcripts do not persist and are not
searchable from the code. The commit is attached to the change forever and is
what a future reader reaches through blame.

**How to apply.** Structure it: a one-line subject naming the outcome, then what
changed by file or subsystem, then the reasoning for any non-obvious choice,
then verification with commands. Name the alternatives you rejected. Never
leave a work-in-progress message on a merged commit — amend it into a real one.

**Does not apply when.** The change is genuinely mechanical and its subject line
says everything.

## Where this comes from

The corpus this came from averages several hundred words of rationale per
merge, structured as what changed, why this shape, and how it was verified,
and reviewers routinely cite commit bodies as evidence when accepting a
deviation. One change amended a work-in-progress conflict-resolution message
into a real one specifically to satisfy the rule — the practice being enforced
on its own record-keeping.

## Related

- [Knowledge lives in docs; code carries pointers](docs-are-the-knowledge-store.md)
- [Record every deviation from the brief, with its reason](../process/deviation-is-recorded-not-silent.md)
- [Report verification as commands and outputs, not as adjectives](../process/verification-is-reported-with-its-command.md)
