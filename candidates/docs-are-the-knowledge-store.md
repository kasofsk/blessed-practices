---
name: docs-are-the-knowledge-store
title: Knowledge lives in docs; code carries pointers
scope: documentation
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/style.md Tier 1 — no comments except doc comments, capped at two sentences"
  - "job #342 — the tree's non-doc comments deleted, with the rationale worth keeping hoisted into a per-module notes document"
  - "docs/implementation-notes.md — the destination for that rationale"
rationale: >
  A radical rule with a clear argument: comments are scattered by construction,
  nobody reviews them as a body, and an agent reading the tree cannot tell a
  current comment from a stale one. The corpus supports the argument — several
  rejections are about comments that contradicted the code beside them.
related: [comments-are-banned-docs-are-not, commit-messages-carry-the-why, one-definition-per-concept]
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

## Derivation

Job #342 removed every non-doc comment from the tree and hoisted the load-bearing
rationale into a notes document. The review found the one thing worth knowing
about such a sweep: a two-line safety comment was half-deleted, leaving a
truncated sentence that no lint could catch — the directive survived, the
justification did not.
