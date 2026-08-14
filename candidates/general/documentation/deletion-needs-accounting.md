---
type: Blessed Practice
title: "Deletion is reviewed by accounting, because the usual gates go green"
description: "When a change's product is removal, review it by accounting: what was removed, what referenced it, what replaced the reference, and what the ledger records."
status: draft
tags:
  - bucket/general
  - scope/documentation
  - altitude/mid
  - portability/universal
  - confidence/medium
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Every quality gate in this system detects a document saying something wrong.
  Shedding produces documents that say something less, which is invisible to all
  of them. The answer — ask accounting questions instead — is a genuinely new
  move.
---

**Rule.** When a change's product is removal, review it by accounting: what was
removed, what referenced it, what replaced the reference, and what the ledger
records. Do not rely on the checks that detect wrongness — removal does not
produce wrongness.

**Why.** Correctness checks resolve claims against the tree. A deleted claim
resolves trivially. So the whole gate suite goes green on a change that removed
the most important sentence in the corpus.

**How to apply.** Enumerate deletions explicitly and require a ledger line per
shed. Check eligibility (was this artefact licensed for deletion), referential
completeness (does anything still cite the deleted path, including non-document
files), and orphaning (did a surviving document lose its last referrer). Make an
unresolvable base exit distinctly — "nothing lost" and "never looked" must not
print the same.

**Does not apply when.** The removal is of dead code the compiler can prove
unused.

## Where this comes from

A set of five accounting questions was derived from exactly this reasoning:
correctness checks resolve claims against the code, and a deleted claim
resolves trivially, so the whole suite goes green on a change that removed the
most important sentence in the corpus. The first run validated it — four load-
bearing sentences were wrongly removed, and all four were invisible to every
path, constant, link and status check, because none of them named a path, a
constant, a link or a status.

## Related

- [A knowledge corpus needs a shedding process, not only an appending one](shed-the-corpus-at-milestones.md)
- [Cannot-run and passed must not print the same](../process/a-check-that-cannot-run-exits-distinctly.md)
