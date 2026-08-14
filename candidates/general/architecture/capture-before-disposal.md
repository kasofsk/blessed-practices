---
type: Blessed Practice
title: "Harvest before you reclaim, and never fail a job on cleanup"
description: "Collect every artifact before disposing of the thing that holds it."
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
  A small ordering rule with two independent halves, both of which were violated
  once and caught in review. The second half — cleanup never fails the work — is
  what keeps a disk problem from looking like a code problem.
---

**Rule.** Collect every artifact before disposing of the thing that holds it.
Disposal is best-effort: it warns, it never fails the work. A sweep at startup
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

## Where this comes from

Reclamation was wired into every exit path strictly after collection, with a
startup sweep for what a crash left behind, and a deliberate fail-safe: on an
error listing live records the sweep is skipped entirely rather than risking
the removal of a live artifact. The message half came from a separate finding,
where a warning named one specific cause for every failure and sent operators
to the wrong action during a routine rolling update.

## Related

- [An error names one cause and one action, and only when it is that cause](../code/errors-name-the-actionable-thing.md)
- [Every in-flight state has a restart arm](restart-reconciliation-is-first-class.md)
- [Prefer a loud refusal to a silent degradation](refuse-loudly.md)
