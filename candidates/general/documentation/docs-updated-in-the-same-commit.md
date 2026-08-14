---
type: Blessed Practice
title: "A change updates the docs it makes stale, in the same commit"
description: "The commit that changes behaviour also changes every document the new behaviour makes false."
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
  The single most-cited rule in the corpus. Its power comes from the timing
  clause: not 'keep docs current' but 'in the same commit', which makes it
  checkable and makes the obligation land on the author with the context.
---

**Rule.** The commit that changes behaviour also changes every document the new
behaviour makes false. Not a follow-up ticket, not a later sweep — the same
commit.

**Why.** The author of the change is the only person who knows exactly which
sentences it falsifies, and they know it for about an hour. Deferring the doc
update means someone else re-derives it later from a diff, or nobody does.

**How to apply.** Before committing, grep the tree for the behaviour's names —
the symbol, the setting, the path, the old adjective — and read every hit.
Include doc comments in source files: they are prose too. Include operator
templates and runbooks, which are the most-read and least-grepped.

**Does not apply when.** The doc is an append-only historical record — then
annotate rather than rewrite, per mutable-head-append-only-body.

## Where this comes from

The most-cited rule in the source retrospective, and the archetype is
instructive: a substantial, correct, fully tested change rejected on a single
missing table row in the section that enumerates what the change added. The
reviewer's closing line — fix that one row and this passes, please do not
touch anything else — is why the rule is cheap to comply with and expensive to
ignore.

## Related

- [Fix the class, and sweep the tree for its other instances](../process/sweep-the-class-not-the-instance.md)
- [Present-tense prose about the tree is a factual claim](present-tense-prose-is-a-claim.md)
