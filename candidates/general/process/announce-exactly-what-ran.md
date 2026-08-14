---
type: Blessed Practice
title: "Announce exactly what ran — never a tier you did not execute"
description: "Any line a gate prints about what it covered is a factual claim."
status: draft
tags:
  - bucket/general
  - scope/process
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Two jobs in the same week shipped announcements broader than the work they
  described. The rule that emerged is unusually crisp: the announcement is a
  claim, and it is checked like one.
---

**Rule.** Any line a gate prints about what it covered is a factual claim.
Enumerate what actually executed on this path, on this host, and name what did
not — with the reason.

**Why.** Coverage announcements are read as receipts. An announcement that
over-claims converts a partial run into a believed full run, and the belief
persists in every doc that cites the number.

**How to apply.** Derive the announcement from the same data the run used, not
from a constant. Where the set differs per path (with and without a dependency),
print per path. When you must state a count, print the command that produces it
beside it, and date it.

**Does not apply when.** The announcement is a fixed label with no quantity in it.

## Where this comes from

One change fixed an over-broad coverage announcement while re-creating it at
smaller scale: the new code path announced a whole tier when several of its
files could not execute there, and a sibling script using the identical
mechanism already printed the correct caveat. The durable form landed later —
the count, the command that produces it, and the date it was taken.

## Related

- [A dropped row reads like a negative result](silent-filters-hide-rows.md)
- [Cannot-run and passed must not print the same](a-check-that-cannot-run-exits-distinctly.md)
- [Present-tense prose about the tree is a factual claim](../documentation/present-tense-prose-is-a-claim.md)
