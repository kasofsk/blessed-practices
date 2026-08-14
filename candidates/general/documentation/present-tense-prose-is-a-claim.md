---
type: Blessed Practice
title: "Present-tense prose about the tree is a factual claim"
description: "A sentence in the present tense about what the system does, what a gate checks, what a path holds or what a constant equals is a factual claim about the tree."
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
  This is the dominant defect class in the entire history — nearly a third of
  all rejections. Nothing else comes close, and it is not a code problem: it is
  prose making unchecked assertions about machinery.
---

**Rule.** A sentence in the present tense about what the system does, what a
gate checks, what a path holds or what a constant equals is a factual claim
about the tree. Check it or mark it. Do not write one you have not verified.

**Why.** Present-tense prose about machinery is trusted and acted on. A stale
claim is worse than silence: it sends the next author to build against something
that is not there, and it lets a reviewer accept it as an answer. In this
history it also compounds — one stale sentence is copied into three
operator-facing files before anyone re-checks the original.

**How to apply.** When you change behaviour, grep for prose describing the old
behaviour before you write the new prose. Write what the tree does, date any
measurement, and mark anything unbuilt in the sentence rather than describing it
as if it ran. Prefer naming the mechanism over restating its output.

**Does not apply when.** The sentence is explicitly historical or dated — past
tense is not a claim about today.

## Where this comes from

This is the largest defect class in the source retrospective by a wide margin
— 98 of 355 review rejections, more than any other cause. A representative
instance is a document saying nothing reads a file yet, in the very change
that made both halves of that sentence false while correcting the identical
sentence in a sibling file. The reviewers' phrasing recurs almost verbatim
across ten separate changes.

## Related

- [A change updates the docs it makes stale, in the same commit](docs-updated-in-the-same-commit.md)
- [A doc asserting another doc's status is the most fragile sentence you can write](cross-doc-state-claims.md)
- [An unenforced intention gets read as a statement of fact](../architecture/unenforced-intentions-become-believed-facts.md)
- [Marking is a syntax, and the markers are not interchangeable](mark-unbuilt-intent.md)
