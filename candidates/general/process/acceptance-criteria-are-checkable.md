---
type: Blessed Practice
title: "Acceptance criteria name an observation, not an intention"
description: "Every acceptance criterion is a specific observation someone can make: a command and its expected output, a file that must not exist, a string that must not appear in the tree."
status: draft
tags:
  - bucket/general
  - scope/process
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Criteria phrased as intentions are unfalsifiable and are routinely reported as
  met. Criteria phrased as observations force the implementer to produce the
  observation, which is most of the value.
---

**Rule.** Every acceptance criterion is a specific observation someone can make:
a command and its expected output, a file that must not exist, a string that
must not appear in the tree. "Works correctly" and "is documented" are not
criteria.

**Why.** An unobservable criterion is satisfied by assertion. The implementer
writes "done", the reviewer cannot cheaply refute it, and the failure surfaces
later at much higher cost.

**How to apply.** Prefer criteria you can express as a grep or a command exit.
Where the criterion is a negative ("nothing in the tree still says X"), give the
search. Where it is a measurement, give the command that produces the number.

**Does not apply when.** The judgement is genuinely human (is this argument
honest, is this doc readable) — then say that a human decides it, and route it
to one.

## Where this comes from

Several changes carried "the build is green" as an acceptance criterion and
failed on it repeatedly, because the earlier attempts never reached the stage
that runs it — so the criterion was predicted rather than observed. The lesson
reviewers drew was about phrasing: name the stage and the command, so the
implementer knows an observation has to be produced.

## Related

- [Break it on purpose and watch the named case go red](../testing/assertions-that-can-fail.md)
- [Report verification as commands and outputs, not as adjectives](verification-is-reported-with-its-command.md)
