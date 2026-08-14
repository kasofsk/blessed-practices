---
name: single-writer-per-record
title: One writer per record class
scope: architecture
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/spec.md — the dispatcher is the sole writer of job records, single-threaded by design"
  - "job #291 — revoke_job wrote a pre-refresh clone back over a total another path had just recomputed; Revoked is terminal, so nothing self-healed it"
  - "job #72 — a second mutation path left stale reverse-dependency edges that terminated the wrong job"
rationale: >
  Every recurring corruption in this corpus is a second writer in disguise — a
  stale clone written back, an index updated by one path and not another. The
  rule was already stated as a principle and still cost rework, which is the
  signature of a rule worth stating louder and earlier rather than differently.
related: [pure-decider-effects, read-modify-write-reads-again, terminal-means-terminal]
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

## Derivation

Job #291's reviewer traced the exact shape: `revoke_job` cloned the job, called
a helper that recomputed and persisted a derived total, then wrote the stale
clone back over it. Job #72 found the mirror image on an index — one path added
reverse-dependency edges, none removed them, and a revoke cascade then killed a
job that no longer depended on the revoked one. Both are single-writer
violations expressed as ordinary Rust.
