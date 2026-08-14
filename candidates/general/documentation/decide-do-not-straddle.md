---
type: Blessed Practice
title: "A design decides the central question"
description: "Identify the question the document exists to settle and settle it, in its own numbered decision, early."
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
  Design documents that defer their central question generate implementation
  jobs that rediscover it, badly, under time pressure. The corpus rewards
  deciding early and visibly, including deciding against an earlier document.
---

**Rule.** Identify the question the document exists to settle and settle it, in
its own numbered decision, early. Where the answer contradicts an earlier
document, say which one is retracted and on what grounds.

**Why.** An undecided design is a decision delegated to whoever implements first,
made without the analysis, and then treated as precedent. Deciding in the
document is what makes the analysis reusable.

**How to apply.** Number the decisions and give each a section arguing it.
Resolve inter-document contradictions in a decision zero, before the body, so a
reader does not spend the document wondering. State what would change the
decision, so the next reader knows when to revisit.

**Does not apply when.** The question genuinely needs a measurement you have not
taken — then the document's decision is what to measure, and it says so.

## Where this comes from

The praise is consistent across the design corpus this came from — "the
central question is decided, not straddled" opens more than one accepted
review — and so is its inverse. Two documents were rejected for describing an
option space without choosing, and one for resolving the same tension twice
with different answers. The strongest example resolves a contradiction between
two earlier documents in a decision zero, before its own argument begins.

## Related

- [Corrections are appended, dated, and name their job](corrections-are-appended-and-dated.md)
- [The rejected alternatives are the part that cannot be re-derived](rejected-alternatives-are-part-of-the-record.md)
