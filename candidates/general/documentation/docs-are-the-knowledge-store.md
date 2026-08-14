---
type: Blessed Practice
title: "Knowledge lives in docs; code carries pointers"
description: "The knowledge a comment would carry goes in a document; the code carries at most a two-sentence doc comment pointing at it."
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
  A radical rule with a clear argument: comments are scattered by construction,
  nobody reviews them as a body, and an agent reading the tree cannot tell a
  current comment from a stale one. The corpus supports the argument — several
  rejections are about comments that contradicted the code beside them.
---

**Rule.** The knowledge a comment would carry goes in a document; the code
carries at most a two-sentence doc comment pointing at it. Rationale goes in the
commit message.

**Why.** Documents are intentional and organised: one place to look, one place
to update, and a maintenance process. Comments are none of those — they drift
silently, they are never reviewed as a body, and their staleness is invisible.

**How to apply.** When you want to write a paragraph in the source, write it in
the module's notes page and leave a pointer. Keep the module header —
accepts, emits, guarantees, spec section — as the in-tree surface. Treat doc
comments as prose held to the same standard as any doc: they go stale, and they
are covered by the same same-commit rule.

**Does not apply when.** The comment is a machine-read directive, which is not
prose — put its justification on the directive line.

## Where this comes from

The argument is specific and was tested: comments are scattered by
construction, nobody reviews them as a body, and a reader cannot distinguish a
current one from a stale one. In the source corpus they were wrong often
enough to mislead reviewers — pointing at renumbered specification sections,
describing behaviour a later change had inverted.

## Related

- [No comments except doc comments, capped at two sentences](../code/comments-are-banned-docs-are-not.md)
- [One definition per concept, and a registry that says where](one-definition-per-concept.md)
- [The commit message carries the why](commit-messages-carry-the-why.md)
