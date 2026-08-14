---
name: comments-are-banned-docs-are-not
title: No comments except doc comments, capped at two sentences
scope: code
altitude: mid
portability: universal
confidence: medium
status: candidate
evidence:
  - "docs/reference/style.md Tier 1"
  - "job #342 — the sweep that took the tree to zero non-doc comments"
  - "jobs #60, #79, #150 — findings where a comment contradicted the code beside it or pointed at the wrong specification section"
rationale: >
  The most aggressive rule in the set, and the one most worth reviewing
  deliberately. The evidence for it is real — comments in this corpus were
  wrong often — but the cost is also real, and adopting it needs a decision
  rather than a default.
related: [docs-are-the-knowledge-store, present-tense-prose-is-a-claim, commit-messages-carry-the-why]
---

**Rule.** Source files carry doc comments only, each at most two sentences, plus
machine-read directives. Longer prose goes in a document with a pointer from the
module header.

**Why.** Comments drift silently: nobody reviews them as a body of knowledge, and
a reader cannot tell a current one from a stale one. In this corpus they were
wrong often enough to mislead reviewers — pointing at renumbered specification
sections, describing behaviour a later change inverted.

**How to apply.** Put the module's contract in an inner doc comment — accepts,
emits, guarantees, spec section — and register it. Put rationale in the commit
message and per-module notes. Hold doc comments to the same same-commit update
rule as any other prose, since no doc gate reaches into source files.

**Does not apply when.** Adopting this wholesale in a codebase whose culture
depends on inline explanation — consider adopting only the "doc comments are
prose and go stale" half first.

## Derivation

Job #79's cycle-2 finding is the archetype: roughly ten comments across code,
types and the front end pointed a reader at the wrong specification section,
because the brief's own hint was off by one and every copy inherited it.
