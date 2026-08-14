---
type: Blessed Practice
title: "Reserve human approval for what no gate and no reader can judge"
description: "Put a human approval step only where the failure mode is invisible to both a gate and a reading reviewer."
status: draft
tags:
  - bucket/chug
  - scope/process
  - altitude/high
  - portability/universal
  - confidence/medium
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
sources:
  - resource: https://github.com/kasofsk/chuggernaut
    title: "Chuggernaut — the platform this practice was derived from"
evidence:
  - "design #533 — the one job type ending in a human approval, because the failure it most likely dies of names no path, constant or link and has no signature in a diff"
  - "job #548 — the accounting gate that mechanises the checkable half, leaving the human the rest"
rationale: >
  A deliberate, argued placement of the human in exactly one place. The
  reasoning generalises: the human is for the judgements that leave no
  mechanical trace, and putting them anywhere else wastes the scarcest resource
  in the loop.
---

**Rule.** Put a human approval step only where the failure mode is invisible to
both a gate and a reading reviewer. Everywhere else, mechanise or delegate to a
reader.

**Why.** Human attention is the bottleneck in an agent-driven system. Spending
it on things a script can decide makes the loop slower without making it safer;
withholding it from the judgements only a person can make is where real damage
happens.

**How to apply.** Name the failure the human is there to catch, and check that
it genuinely leaves no signature: no path, no constant, no link, no diff shape.
If it does leave one, write the gate instead. Order the human step last, after
everything mechanical has passed, so their time is spent on a candidate that is
otherwise ready.

**Does not apply when.** The action is irreversible or outward-facing —
confirmation there is about authority, not judgement, and is always warranted.

## Where this comes from

Design #533 argues the placement explicitly: the shedding job type's most likely
failure is a rejected alternative deleted along with the implemented design, and
"a shed rejected alternative names no path, constant or link and has no
signature in a diff". Everything that does leave a signature became the
accounting gate instead.

## Related

- [Deletion is reviewed by accounting, because the usual gates go green](../general/documentation/deletion-needs-accounting.md)
- [Reviewers read; gates run](reviewers-read-they-do-not-run.md)
- [Write the summary for whoever has to judge it, close calls first](the-work-summary-is-for-the-approver.md)
