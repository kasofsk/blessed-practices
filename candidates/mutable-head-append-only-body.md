---
name: mutable-head-append-only-body
title: A mutable head over an append-only body
scope: documentation
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "design #415 D2 — the head is rewritten to current truth whenever anything changes; the body is append-only"
  - "jobs #436, #445, #461, #473 — reviews that explicitly leave append-only bodies alone and gate only on the head"
  - "job #461 — a false sentence in an appended body 'freezes as a permanently wrong account'"
rationale: >
  The structural answer to the conflict between 'docs must be current' and
  'decisions must not be rewritten after the fact'. It is the most reusable idea
  in this project's documentation architecture.
related: [present-tense-prose-is-a-claim, corrections-are-appended-and-dated, rejected-alternatives-are-part-of-the-record]
---

**Rule.** A decision document has two parts. The head states current truth and
is rewritten whenever anything changes. The body is the argument as it was made
and is never rewritten — only appended to, with dated corrections.

**Why.** Rewriting an argument to match the outcome destroys the reasoning that
future readers need in order to know whether the decision still applies. Leaving
the head stale makes the document actively misleading. The split gets both.

**How to apply.** Put status, current state and the slice table in the head, and
bound the head explicitly so a reviewer can tell which half a line is in. Never
edit below the line; append a dated correction naming the job. When the body
turns out to be wrong, say so in a correction — do not fix it in place.

**Does not apply when.** The document is a reference page, which holds no
history and is rewritten freely.

## Derivation

This is design #415 D2, and its enforcement shows up in almost every later
review: findings are routinely scoped as "design-doc bodies are NOT findings —
append-only body, correctly left alone", while the same reviewer blocks on one
head sentence.
