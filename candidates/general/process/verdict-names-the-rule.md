---
type: Blessed Practice
title: "A rejection names the rule it rejects under"
description: "Every blocking finding cites the rule, criterion or ticket item it violates, by name or number, and quotes the clause."
status: draft
tags:
  - bucket/general
  - scope/process
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Naming the rule makes the verdict auditable and the rule improvable. An
  unnamed rejection is an opinion; a named one can be argued with, cited, or
  used as evidence that the rule needs changing.
---

**Rule.** Every blocking finding cites the rule, criterion or ticket item it
violates, by name or number, and quotes the clause. Findings with no citable
basis are advisory and labelled as such.

**Why.** The citation is what lets the fixer know whether to comply or to argue,
and what lets the rule set evolve — a rule cited in twenty rejections is
working; a rule never cited is decoration.

**How to apply.** Cite the rule and the acceptance criterion together where both
apply. Where the basis is judgement rather than a rule, say "non-blocking
observation" and do not fail on it. When you find yourself inventing a rule to
justify a block, that is a signal to propose the rule instead.

**Does not apply when.** The finding is a plain correctness bug — the code being
wrong is its own basis.

## Where this comes from

Rejections in the source retrospective routinely cite a numbered rule, quote
the clause and point at the line. The rules cited most often — update the
documents your change makes stale, and present-tense prose is a factual claim
— are also the ones later mechanised into automated checks, which is what a
citation count is good for.

## Related

- [Practices are numbered, tiered, injectable, and carry their why](blessed-practices-are-numbered-and-cited.md)
