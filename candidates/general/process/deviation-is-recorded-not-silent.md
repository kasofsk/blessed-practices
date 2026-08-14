---
type: Blessed Practice
title: "Record every deviation from the brief, with its reason"
description: "When you implement something other than what the ticket specified, say so in the commit message and in the durable record: what the ticket asked, what you did, and why."
status: draft
tags:
  - bucket/general
  - scope/process
  - altitude/high
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Deviations are usually right. What makes them expensive is being silent: the
  reviewer discovers a difference and cannot tell whether it is a decision or an
  oversight, so it becomes a finding either way.
---

**Rule.** When you implement something other than what the ticket specified, say
so in the commit message and in the durable record: what the ticket asked, what
you did, and why. Never deliver a silent difference.

**Why.** The reviewer's task is to compare the change against the ticket. An
unexplained difference costs a cycle at best. A stated one is usually accepted
in the same review, because the reasoning is right there to judge.

**How to apply.** A short "deviates from the ticket" paragraph in the commit
body: the requirement, the implemented behaviour, the reason, and whether the
ticket's version remains desirable later. If the deviation changes a documented
rule, update the doc in the same commit.

**Does not apply when.** The difference is cosmetic and unobservable.

## Where this comes from

A storage-layer deviation was accepted explicitly because it was argued in the
commit message and had a precedent — the reasoning was there to judge. The
inverse: a rule was changed during a rework cycle while the change's own
appended record still said no rule had changed, which would have frozen as a
permanently false account of what it did.

## Related

- [Corrections are appended, dated, and name their job](../documentation/corrections-are-appended-and-dated.md)
- [The commit message carries the why](../documentation/commit-messages-carry-the-why.md)
