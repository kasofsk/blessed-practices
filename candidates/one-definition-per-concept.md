---
name: one-definition-per-concept
title: One definition per concept, and a registry that says where
scope: documentation
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/concepts.md — a routing table naming the owning doc for each registered term"
  - "design #415 M5 — two documents opened with the identical sentence defining the same concept and diverged immediately after"
  - "job #449 — the registry's own rows misdescribed in the doc that introduced them"
rationale: >
  A concept explained in two places drifts in one of them, and the reader cannot
  tell which. The registry approach is stronger than a glossary because it
  routes rather than restates, so there is nothing to keep in sync.
related: [cross-doc-state-claims, mechanise-the-checkable-half, docs-are-the-knowledge-store]
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

## Derivation

Design #415's measurement found the motivating case: two documents opening with
a byte-identical sentence defining the project's central invariant, diverging in
the next clause. The registry that followed deliberately excludes no file,
because the file exemption would have covered exactly that instance.
