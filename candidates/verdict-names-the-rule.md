---
name: verdict-names-the-rule
title: A rejection names the rule it rejects under
scope: process
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "Reviewers in this corpus routinely reject by naming a numbered style rule, e.g. 'Tier 2 #5, the docs-update half'"
  - "job #258 — a rejection naming the Tier 1 rule and the specific line that violates it"
rationale: >
  Naming the rule makes the verdict auditable and the rule improvable. An
  unnamed rejection is an opinion; a named one can be argued with, cited, or
  used as evidence that the rule needs changing.
related: [scope-the-rework-explicitly, blessed-practices-are-numbered-and-cited, the-ticket-is-the-contract]
---

**Rule.** Every blocking finding cites the rule, criterion or brief item it
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

## Derivation

The habit is visible throughout: rejections in this corpus name Tier 1 and Tier
2 rules by number, quote the clause, and point at the line. The rules that get
cited most (docs updated in the same commit; present-tense prose is a claim) are
also the ones the project later mechanised into gates.
