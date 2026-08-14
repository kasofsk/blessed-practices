---
type: Blessed Practice
title: "No comments except doc comments, capped at two sentences"
description: "Source files carry doc comments only, each at most two sentences, plus machine-read directives."
status: draft
tags:
  - bucket/general
  - scope/code
  - altitude/mid
  - portability/universal
  - confidence/medium
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  The most aggressive rule in the set, and the one most worth reviewing
  deliberately. The evidence for it is real — comments in this corpus were
  wrong often — but the cost is also real, and adopting it needs a decision
  rather than a default.
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

## Where this comes from

One change removed every non-documentation comment from a large codebase and
hoisted the rationale worth keeping into a per-module notes page. Its review
found the one thing worth knowing about such a sweep: a two-line safety
comment was half-deleted, leaving a truncated sentence that no lint could
catch. The motivating defect class is separate — around ten comments pointing
readers at a renumbered specification section, every copy inheriting the same
off-by-one.

## Related

- [Knowledge lives in docs; code carries pointers](../documentation/docs-are-the-knowledge-store.md)
- [Present-tense prose about the tree is a factual claim](../documentation/present-tense-prose-is-a-claim.md)
- [The commit message carries the why](../documentation/commit-messages-carry-the-why.md)
