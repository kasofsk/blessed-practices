---
name: capture-before-disposal
title: Harvest before you reclaim, and never fail a job on cleanup
scope: architecture
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #10 — container removal wired into every exit path strictly after artifact collection, with a startup sweep for orphans"
  - "crates/platform-ops/src/harvest.rs — a failed removal leaks disk but must never fail a job, so it only warns"
  - "job #381 — an error message asserting the over-band cause for every failure, including a routine version-skew transport miss"
rationale: >
  A small ordering rule with two independent halves, both of which were violated
  once and caught in review. The second half — cleanup never fails the work — is
  what keeps a disk problem from looking like a code problem.
related: [refuse-loudly, errors-name-the-actionable-thing, restart-reconciliation-is-first-class]
---

**Rule.** Collect every artifact before disposing of the thing that holds it.
Disposal is best-effort: it warns, it never fails the job. A sweep at startup
reclaims what a crash left behind.

**Why.** Capture-happens-before-removal is the only ordering that survives a
crash between the two. Making disposal fatal converts a housekeeping problem
into a work failure and hides the real result.

**How to apply.** Put disposal after collection on every exit path — success,
failure, timeout, kill — and assert the ordering in a test. Add a startup sweep
that removes only artifacts bound to no live record, and skip the whole sweep
rather than risk removing a live one when the record listing errors.

**Does not apply when.** The artifact is the failure signal itself and losing it
must be loud — then it is not cleanup, it is a harvest step, and it belongs
above the line.

## Derivation

Job #10 established the ordering across every path and added the startup sweep,
with the fail-safe noted by the reviewer: on a listing error it "skips the whole
sweep rather than risk removing a live container". Job #381 shows the
error-message half — a warn that named one cause for every failure sent
operators to the wrong action during a routine deploy window.
