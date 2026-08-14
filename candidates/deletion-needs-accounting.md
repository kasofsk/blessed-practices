---
name: deletion-needs-accounting
title: Deletion is reviewed by accounting, because the usual gates go green
scope: documentation
altitude: mid
portability: universal
confidence: medium
status: candidate
evidence:
  - ".chug/tasks/check-molt.sh — a vanished landed-slice claim, a doc that lost its last referrer, a deletion that was not eligible, a deleted path still cited from a non-doc file with no stub, a shed with no ledger line"
  - "job #576 — every mechanical gate green while four load-bearing sentences were missing"
rationale: >
  Every quality gate in this system detects a document saying something wrong.
  Shedding produces documents that say something less, which is invisible to all
  of them. The answer — ask accounting questions instead — is a genuinely new
  move.
related: [shed-the-corpus-at-milestones, a-check-that-cannot-run-exits-distinctly, human-approval-only-where-no-gate-can-judge]
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

## Derivation

The accounting gate's five questions were derived from exactly this reasoning,
and the first shed validated it: the four sentences the reviewer restored were
invisible to every path, constant, link and row check, because none of them
named a path, a constant, a link or a row.
