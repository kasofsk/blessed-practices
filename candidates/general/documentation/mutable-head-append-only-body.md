---
type: Blessed Practice
title: "A mutable head over an append-only body"
description: "A decision document has two parts."
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
  The structural answer to the conflict between 'docs must be current' and
  'decisions must not be rewritten after the fact'. It is the most reusable idea
  in this project's documentation architecture.
---

**Rule.** A decision document has two parts. The head states current truth and
is rewritten whenever anything changes. The body is the argument as it was made
and is never rewritten — only appended to, with dated corrections.

**Why.** Rewriting an argument to match the outcome destroys the reasoning that
future readers need in order to know whether the decision still applies. Leaving
the head stale makes the document actively misleading. The split gets both.

**How to apply.** Put status, current state and the status table in the head, and
bound the head explicitly so a reviewer can tell which half a line is in. Never
edit below the line; append a dated correction naming the change. When the body
turns out to be wrong, say so in a correction — do not fix it in place.

**Does not apply when.** The document is a reference page, which holds no
history and is rewritten freely.

## Where this comes from

The split's enforcement is visible in nearly every later review of the source
corpus: findings are routinely scoped as "the append-only body is correctly
left alone" while the same reviewer blocks on a single sentence in the head.
The reason the body is frozen is recorded too — a false sentence appended
there freezes as a permanently wrong account of what a change did.

## Related

- [Corrections are appended, dated, and name their job](corrections-are-appended-and-dated.md)
- [Present-tense prose about the tree is a factual claim](present-tense-prose-is-a-claim.md)
- [The rejected alternatives are the part that cannot be re-derived](rejected-alternatives-are-part-of-the-record.md)
