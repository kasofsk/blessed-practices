---
type: Blessed Practice
title: "A doc asserting another doc's status is the most fragile sentence you can write"
description: "Avoid asserting another document's implementation status."
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
  A distinct sub-class of stale prose worth its own card because the falsifying
  change is usually in a different document than the false sentence, so the
  author never sees it.
---

**Rule.** Avoid asserting another document's implementation status. When you
must, link to the row that owns the answer rather than restating it — and when
you land something, sweep every doc that names it.

**Why.** Status claims propagate: a design cites a sibling's phase as
unimplemented to justify its own scope, and three documents later the citation
is load-bearing. The landing that falsifies them all happens in a fourth place.

**How to apply.** Keep status in exactly one place per subject — the plan's own
status table — and link to it. When landing, search for the plan's identifier and for
the subject's name, and read every head that names it. Expect three hits when
you predicted one.

**Does not apply when.** The claim is dated and framed as history.

## Where this comes from

Three sibling documents made the same claim about a phase being unimplemented.
One change falsified all three; it corrected two and missed the third, which
is the characteristic shape — the sentence that goes false lives in a
different file from the change that falsifies it. Another document called a
slice proposed thirty lines above its own table row saying it had landed.

## Related

- [A mutable head over an append-only body](mutable-head-append-only-body.md)
- [Present-tense prose about the tree is a factual claim](present-tense-prose-is-a-claim.md)
