---
type: Blessed Practice
title: "Rework builds on the previous attempt; it does not restart it"
description: "A rework cycle continues the same branch."
status: draft
tags:
  - bucket/chug
  - scope/process
  - altitude/high
  - portability/project
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
sources:
  - resource: https://github.com/kasofsk/chuggernaut
    title: "Chuggernaut — the platform this practice was derived from"
evidence:
  - "job #54 — the change from reset-on-re-entry to preserve-on-re-entry, so a rework cycle keeps the agent's commits"
  - "43% of jobs with tasks in this history needed at least one rework cycle; 86 needed three or more"
rationale: >
  Rework is the normal path, not the exception, so its economics dominate. The
  decision to preserve the branch across cycles is the single largest efficiency
  change in the corpus, and it also changes what a reviewer should write.
---

**Rule.** A rework cycle continues the same branch. The previous attempt's
commits stay; the fixer applies the findings on top. Nothing resets to the base.

**Why.** Discarding accepted work to fix one finding throws away the majority of
the value of the cycle and reintroduces defects the reviewer already cleared. It
also makes the second review a full review rather than a delta review.

**How to apply.** Create the branch on first entry only; on re-entry, if it
exists, leave it alone. Have the reviewer's verdict distinguish what is accepted
from what must change, and have the fixer touch only the second. Where commit
ordering matters to a gate, squash rather than reset.

**Does not apply when.** The previous attempt is fundamentally misdirected — then
say so explicitly and ask for a restart, rather than achieving it by side effect.

## Where this comes from

Job #54's brief made the change and named the cost it removes: the old path
"discards the agent's prior commits every rework". Branch existence
discriminates first entry from re-entry, so no extra parameter was needed —
which is also why the bug was easy to reintroduce and worth pinning.

## Related

- [A verdict says what to change and what not to touch](scope-the-rework-explicitly.md)
- [The rework brief carries the evidence, not just the verdict](rework-context-carries-the-evidence.md)
- [When a gate reads commit order, ship one commit](one-commit-when-ordering-matters.md)
