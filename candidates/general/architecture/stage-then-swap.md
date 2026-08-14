---
type: Blessed Practice
title: "Build aside, then swap atomically"
description: "Produce the new artifact beside the live one under a distinct name, verify it, then make it live with a single rename or retag."
status: draft
tags:
  - bucket/general
  - scope/architecture
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Every live-update path in this system converged independently on the same
  shape. That convergence is the argument for stating it as a practice rather
  than rediscovering it per subsystem.
---

**Rule.** Produce the new artifact beside the live one under a distinct name,
verify it, then make it live with a single rename or retag. Deletion of the old
artifact happens after the swap, best-effort.

**Why.** The swap is the only step that can be observed half-done, and a rename
is the smallest such step available. A build that dies part-way then leaves
every live name exactly as it was, which is the property that makes retrying
safe.

**How to apply.** Name the staging artifact so a crashed run's leftovers are
identifiable and reclaimable. Verify the staged artifact by the criterion its
consumer uses — not the one the builder finds convenient. Prune leftovers under
an exit trap that preserves the original exit code.

**Does not apply when.** The target has no atomic replace primitive; then say
what the observable half-state is and how the consumer detects it.

## Where this comes from

Every live-update path in the source system converged independently on this
shape: build under temporary names, verify, then swap, with an exit trap
pruning leftovers while preserving the original exit code. The convergence
across unrelated subsystems is the argument for stating it once rather than
rediscovering it per subsystem.

## Related

- [A multi-leg operation reports every leg, including the ones it skipped](../operations/deploy-legs-report-skipped.md)
- [Validate everything first, then mutate](validate-before-you-mutate.md)
