---
name: scope-the-rework-explicitly
title: A verdict says what to change and what not to touch
scope: process
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #366 — 'Everything else in this change is correct and in scope. Do not re-do the rest.'"
  - "job #457 — 'do not rework the test change, the new correction section, the D3/D8/slice-2 rows or the proofs section'"
  - "job #314 — a verdict opening with an explicit what_is_right list before its findings"
rationale: >
  The best reviews in this corpus all share one habit that the worst lack: an
  explicit accepted list. It shortens the next cycle and prevents the fixer from
  churning code that already passed — which is itself a common source of new
  findings.
related: [branch-preserved-across-rework, rework-context-carries-the-evidence, verdict-names-the-rule]
---

**Rule.** Every rejecting verdict has two parts: what is accepted and must not
change, and what must change. Both are specific.

**Why.** Without the accepted list, a fixer treats the whole diff as suspect and
rewrites working code, generating fresh findings and fresh cycles. With it, the
delta review is a delta review.

**How to apply.** Lead with the accepted list, itemised by deliverable, so the
fixer can see the majority of the work is done. Then the findings, each with
file, line, the defect, and a concrete suggested fix. Where a finding is
non-blocking, say so and say why you are not blocking on it.

**Does not apply when.** Nothing is accepted — say that too, plainly, and
consider whether the job should be escalated instead of reworked.

## Derivation

Reviews using this shape converge in one or two cycles; the same reviewers,
reviewing without it, produce cycles where the second attempt breaks something
the first got right. Job #393 cycle 2 is the explicit statement of the
discipline: "what I did this cycle that I should have done in cycle 1 is sweep
the WHOLE tree for the same defect class instead of naming one instance".
