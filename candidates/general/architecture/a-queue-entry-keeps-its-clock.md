---
type: Blessed Practice
title: "A re-queued item keeps its original clock"
description: "When an item goes back on a queue, it carries its original enqueue time and its original priority."
status: draft
tags:
  - bucket/general
  - scope/architecture
  - altitude/low
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Two independent findings in one job, both the same mistake: a value that
  encodes 'how long has this been waiting' was recomputed by a path that only
  meant to re-insert. It is a small rule with a large failure — starvation that
  never escalates.
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

## Where this comes from

One change carried both halves of this mistake. The re-queue path stamped a
fresh timestamp unconditionally, so an item that repeatedly lost a race for
capacity restarted its own starvation clock and could never trip the backstop
that existed to catch it. Separately, the restart path rebuilt the queue
sorted by timestamp alone, discarding the priority ordering — reintroducing
the inversion the feature had just fixed, in the window where restarts are
most frequent.

## Related

- [Every in-flight state has a restart arm](restart-reconciliation-is-first-class.md)
- [Everything is bounded, and the bound is loud](bounded-and-loud.md)
