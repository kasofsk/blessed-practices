---
type: Blessed Practice
title: "Resolve record conflicts by keeping both, in landing order"
description: "When two branches append independent records to the same file, the resolution is the union in landing order — never a choice between them."
status: draft
tags:
  - bucket/general
  - scope/process
  - altitude/mid
  - portability/project
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Nine consecutive jobs resolved the same class of conflict the same way, and
  each commit message re-derived the reasoning from scratch. That is a practice
  waiting to be written down.
---

**Rule.** When two branches append independent records to the same file, the
resolution is the union in landing order — never a choice between them. When
they both rewrite a summary, merge the summary so it is true of both landings,
rather than taking one side's list.

**Why.** Appended records are statements about different events; neither
invalidates the other, so choosing loses history. Summaries are the opposite:
each side wrote a sentence true of its own landing only, so keeping either one
leaves the file asserting a falsehood about the other.

**How to apply.** Body: concatenate, ordered by merge order, separated as the
file's own convention separates them. Head: rewrite to current truth naming both
landings. Scratch files whose semantics are "lines this diff adds" have no
precedence question at all — take the union and say why.

**Does not apply when.** The two changes genuinely contradict — then it is a
decision, and it belongs to a human, not to the merge.

## Where this comes from

Nine consecutive changes resolved the same class of conflict identically and
re-derived the reasoning each time. The compact statement: a scratch file
whose semantics are the lines a change adds has no precedence question at all,
so there is nothing to reconcile between the sides — only to keep. Summaries
are the opposite case, because each side wrote a sentence true only of its own
landing.

## Related

- [A mutable head over an append-only body](../documentation/mutable-head-append-only-body.md)
- [Corrections are appended, dated, and name their job](../documentation/corrections-are-appended-and-dated.md)
