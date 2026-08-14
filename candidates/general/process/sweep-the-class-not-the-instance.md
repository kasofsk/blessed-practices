---
type: Blessed Practice
title: "Fix the class, and sweep the tree for its other instances"
description: "When you find a defect, name its class, search the whole tree for other instances, and fix them in the same change."
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
  The single most common cause of a third and fourth rework cycle here is fixing
  one instance of a defect whose siblings sit in adjacent files. Sweeping is
  cheap; the extra cycles are not.
---

**Rule.** When you find a defect, name its class, search the whole tree for
other instances, and fix them in the same change. State the search you ran and
what it returned.

**Why.** Defect classes cluster: the same sentence is copied into an operator
README, a runbook and a design head; the same guard is written twice with one
spelling. Fixing one leaves the others to be found one cycle at a time by
different reviewers.

**How to apply.** Turn the defect into a grep. Run it, list the hits, fix or
clear each, and record the swept-and-cleared set so the next reviewer does not
repeat the search. Where the class is mechanically checkable, consider a gate
instead — the sweep is the prototype for it.

**Does not apply when.** The instance is genuinely unique and you can show the
search is empty — which is the same work, so run it anyway.

## Where this comes from

One reviewer named the discipline explicitly after missing it the first time —
sweep the whole tree for the defect class rather than naming one instance —
and published both the two further instances found and the cleared list. The
counter-examples are three changes where the same stale sentence sat in three
operator-facing files and was corrected two at a time, costing a cycle each.

## Related

- [Cheap checks run whole-tree, not only over the diff](whole-tree-not-just-the-diff.md)
- [Present-tense prose about the tree is a factual claim](../documentation/present-tense-prose-is-a-claim.md)
