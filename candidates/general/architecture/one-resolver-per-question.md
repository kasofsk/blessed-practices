---
type: Blessed Practice
title: "One resolver per lookup question"
description: "Each \"where does this live\" or \"which one applies\" question has one function."
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
  The lookup-drift bug — a listing that finds a thing and a read that cannot —
  appeared twice and both times the fix was to make one function own the
  question, not to fix the second copy.
---

**Rule.** Each "where does this live" or "which one applies" question has one
function. Listing, reading and validating all go through it, so a listing and a
read cannot disagree.

**Why.** Resolution logic is small and tempting to inline, so it gets written
twice with slightly different precedence. The result is a system that can see a
thing and not open it — a failure mode that reads as corruption.

**How to apply.** Return the resolved location, not just the result, so callers
can report what they resolved. Derive any ordering from the same candidate list
the read uses. Make the wrong-level accessor private so no call site can reach
it.

**Does not apply when.** The two lookups are genuinely different questions —
then name them differently, so the difference is visible.

## Where this comes from

The lookup-drift bug — a listing that finds an item and a read that cannot
open it — appeared twice, and both times the fix was to give the question one
owner rather than to correct the second copy. A later change applied the same
move to a resolution question and made the general accessor private, so no
call site could ask the wrong version of it.

## Related

- [One decision site per question](one-decision-site.md)
- [The shared types layer has no I/O and no runtime](pure-data-layer.md)
