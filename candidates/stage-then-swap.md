---
name: stage-then-swap
title: Build aside, then swap atomically
scope: architecture
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #183 — images built under temporary tags and retag-swapped onto the live tag only after all of them complete"
  - "job #473 — the daemon swap became extract, install-by-rename, then ask the supervisor"
  - "job #537 §7 — teardown renames a directory aside before deleting it"
rationale: >
  Every live-update path in this system converged independently on the same
  shape. That convergence is the argument for stating it as a practice rather
  than rediscovering it per subsystem.
related: [validate-before-you-mutate, deploy-legs-report-skipped]
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

## Derivation

Job #183's rework built three images under `<tag>-refresh` and swapped only
after all three completed, with the exit trap pruning temp tags — a no-op after
a successful swap because the tags share an image id. Job #473 carried the same
shape into the native daemon install.
