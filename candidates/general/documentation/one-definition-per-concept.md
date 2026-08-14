---
type: Blessed Practice
title: "One definition per concept, and a registry that says where"
description: "Each concept is defined in exactly one document."
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
  A concept explained in two places drifts in one of them, and the reader cannot
  tell which. The registry approach is stronger than a glossary because it
  routes rather than restates, so there is nothing to keep in sync.
---

**Rule.** Each concept is defined in exactly one document. A registry routes the
term to its owner. Every other document mentions the term freely and links to
the owner; it never defines it.

**Why.** Two definitions is two things to update and one of them will be missed.
A registry keeps the count at one without preventing anyone from talking about
the concept.

**How to apply.** Register a term only when the cost of a second definition is
real — a registry of a dozen rows that states its own admission criterion beats
a glossary of two hundred. Hold every document to the rule, including the
project instructions and prompt files: one line of gloss plus a link is a
mention, and a mention is free.

**Does not apply when.** The term is unregistered — then it is invisible to the
rule, however it is written.

## Where this comes from

The measurement that motivated it found two documents opening with a byte-
identical sentence defining the same central invariant and diverging in the
next clause. The registry that followed deliberately exempts no file, because
a file-level exemption would have covered exactly that instance.

## Related

- [A doc asserting another doc's status is the most fragile sentence you can write](cross-doc-state-claims.md)
- [Knowledge lives in docs; code carries pointers](docs-are-the-knowledge-store.md)
- [Mechanise the checkable half; route the rest to judgement](../process/mechanise-the-checkable-half.md)
