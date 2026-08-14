---
name: a-queue-entry-keeps-its-clock
title: A re-queued item keeps its original clock
scope: architecture
altitude: low
portability: universal
confidence: high
status: candidate
evidence:
  - "job #150 cycle 4 — an agent evaluator that lost the slot race re-deferred with a fresh timestamp, restarting the starvation clock on every attempt"
  - "job #150 cycle 4 — a restart re-sorted the queue by enqueue time alone, discarding priority"
rationale: >
  Two independent findings in one job, both the same mistake: a value that
  encodes 'how long has this been waiting' was recomputed by a path that only
  meant to re-insert. It is a small rule with a large failure — starvation that
  never escalates.
related: [bounded-and-loud, restart-reconciliation-is-first-class]
---

**Rule.** When an item goes back on a queue, it carries its original enqueue
time and its original priority. Only a genuinely new item stamps a new clock.

**Why.** Timeouts, fairness and starvation detection are all computed from that
timestamp. A path that restamps it converts an accumulating wait into a
sequence of short waits, so the backstop that exists to catch starvation never
fires — under load, exactly when it is needed.

**How to apply.** Make the re-queue path take the existing entry rather than
constructing one. If it must construct, thread the original timestamp
explicitly. On restart, reconstruct the queue by the same ordering key the live
path uses, not by timestamp alone.

**Does not apply when.** The retry is semantically a new request (a fresh user
action), not a resumption of the same wait.

## Derivation

Job #150 cycle 4 carried both halves. The deferral path did
`queued_at = now` unconditionally, so a churning-but-full fleet could reset the
escalation clock indefinitely; the restart path sorted by `queued_at`, which
"reintroduces exactly the priority inversion this ticket fixes, in the restart
window the spec stresses is frequent".
