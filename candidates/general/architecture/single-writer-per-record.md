---
type: Blessed Practice
title: "One writer per record class"
description: "For each class of record, exactly one component may write it, and that component writes it from one place."
status: draft
tags:
  - bucket/general
  - scope/architecture
  - altitude/high
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Every recurring corruption in this corpus is a second writer in disguise — a
  stale clone written back, an index updated by one path and not another. The
  rule was already stated as a principle and still cost rework, which is the
  signature of a rule worth stating louder and earlier rather than differently.
---

**Rule.** For each class of record, exactly one component may write it, and that
component writes it from one place. A change that appears to need a second
writer, a lock, or a compare-and-swap is the wrong shape: simplify until it
needs one writer.

**Why.** A single writer removes an entire category of bug — lost updates, torn
pairs, indexes that disagree with the records they index — at the cost of some
convenience. Locks and CAS do not remove the category, they move it somewhere
harder to test. Under a single writer, every state question has one answer and
one place to look for it.

**How to apply.** Name the writer in the module header. Every other component
reads through typed accessors and asks the writer to mutate. When you find
yourself cloning a record, doing work, and writing the clone back, stop: any
path that refreshed the record in between has just been overwritten. Re-read
after any call that may have written, or thread the mutation through the one
site that owns it.

**Does not apply when.** The record is genuinely per-actor and never read
across actors (a task's own scratch state), or the store itself provides the
serialization you need and you can prove no read-modify-write spans it.

## Where this comes from

Two independent defects in the source retrospective had the same root. In one,
a handler cloned a record, called a helper that recomputed and persisted a
derived value, then wrote the stale clone back — and because the record's new
state was terminal, nothing ever recomputed it. In the other, one code path
added edges to an index and no path removed them, so a cascading delete
terminated a record that no longer depended on the deleted one. Both are
single-writer violations written as ordinary code.

## Related

- [Deciders return effects; interpreters perform them](pure-decider-effects.md)
- [Re-read before you write back](read-modify-write-reads-again.md)
- [Terminal states are terminal, and nothing self-heals after them](terminal-means-terminal.md)
