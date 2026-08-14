---
name: sweep-the-class-not-the-instance
title: Fix the class, and sweep the tree for its other instances
scope: process
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "job #393 cycle 2 — a reviewer swept every count-prose hit in the tree and found exactly two more, closing the class"
  - "job #478, #495, #497 — the same stale sentence corrected in one or two of three sibling files, each miss costing another cycle"
  - "job #501 — a gate written for the class of shell divergence rather than the one spelling that failed"
rationale: >
  The single most common cause of a third and fourth rework cycle here is fixing
  one instance of a defect whose siblings sit in adjacent files. Sweeping is
  cheap; the extra cycles are not.
related: [scope-the-rework-explicitly, whole-tree-not-just-the-diff, present-tense-prose-is-a-claim]
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

## Derivation

Job #393's cycle-2 review names the discipline and its result: the whole-tree
sweep for stale count-prose found exactly two further instances, both in files
the change already edited, and the reviewer published the cleared list. Jobs
#478, #495 and #497 are the counter-examples — the same sentence in three
operator-facing files, corrected two at a time.
