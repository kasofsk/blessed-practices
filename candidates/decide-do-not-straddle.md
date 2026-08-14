---
name: decide-do-not-straddle
title: A design decides the central question
scope: documentation
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "job #310 — 'The central question is decided, not straddled' as the review's first praise"
  - "jobs #293, #309, #372 — designs accepted for resolving a tension explicitly and early"
  - "job #313 — a design that resolves a contradiction between two earlier designs in its Decision 0, before anything else"
rationale: >
  Design documents that defer their central question generate implementation
  jobs that rediscover it, badly, under time pressure. The corpus rewards
  deciding early and visibly, including deciding against an earlier document.
related: [rejected-alternatives-are-part-of-the-record, corrections-are-appended-and-dated, the-ticket-is-the-contract]
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

## Derivation

The praise is consistent across the design corpus, and so is its inverse: two
documents in this history were rejected for describing an option space without
choosing, and one for resolving the same tension in two places with different
answers.
