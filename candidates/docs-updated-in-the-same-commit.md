---
name: docs-updated-in-the-same-commit
title: A change updates the docs it makes stale, in the same commit
scope: documentation
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/style.md Tier 2 rule 5 — cited by name in dozens of rejections"
  - ".chug/tasks/review-docs-updated.md — a blocking evaluator on every code and web job"
  - "jobs #413, #518, #522 — each rejected for exactly one un-updated sentence, everything else accepted"
rationale: >
  The single most-cited rule in the corpus. Its power comes from the timing
  clause: not 'keep docs current' but 'in the same commit', which makes it
  checkable and makes the obligation land on the author with the context.
related: [present-tense-prose-is-a-claim, the-landing-job-owns-the-doc-update, sweep-the-class-not-the-instance]
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

## Derivation

Job #413 is the archetype: a substantial, correct, fully tested change rejected
on a single missing table row in a specification section that enumerates what
the change added. The reviewer's closing line — "fix that one row and this
passes; please do not touch anything else" — is why the rule is cheap to comply
with and expensive to ignore.
