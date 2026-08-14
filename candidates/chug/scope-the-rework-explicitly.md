---
type: Blessed Practice
title: "A verdict says what to change and what not to touch"
description: "Every rejecting verdict has two parts: what is accepted and must not change, and what must change."
status: draft
tags:
  - bucket/chug
  - scope/process
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
sources:
  - resource: https://github.com/kasofsk/chuggernaut
    title: "Chuggernaut — the platform this practice was derived from"
evidence:
  - "job #366 — 'Everything else in this change is correct and in scope. Do not re-do the rest.'"
  - "job #457 — 'do not rework the test change, the new correction section, the D3/D8/slice-2 rows or the proofs section'"
  - "job #314 — a verdict opening with an explicit what_is_right list before its findings"
rationale: >
  The best reviews in this corpus all share one habit that the worst lack: an
  explicit accepted list. It shortens the next cycle and prevents the fixer from
  churning code that already passed — which is itself a common source of new
  findings.
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

## Where this comes from

Reviews using this shape converge in one or two cycles; the same reviewers,
reviewing without it, produce cycles where the second attempt breaks something
the first got right. Job #393 cycle 2 is the explicit statement of the
discipline: "what I did this cycle that I should have done in cycle 1 is sweep
the WHOLE tree for the same defect class instead of naming one instance".

## Related

- [A rejection names the rule it rejects under](../general/process/verdict-names-the-rule.md)
- [Rework builds on the previous attempt; it does not restart it](branch-preserved-across-rework.md)
- [The rework brief carries the evidence, not just the verdict](rework-context-carries-the-evidence.md)
