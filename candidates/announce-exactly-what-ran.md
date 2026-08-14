---
name: announce-exactly-what-ran
title: Announce exactly what ran — never a tier you did not execute
scope: process
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #375 — an announcement claiming a whole test tier executed when it self-skipped"
  - "job #378 — the same defect at smaller scale: a new path announced 26 files when several could not run, and the fix was a few lines because a sibling script already printed the correct caveat"
  - "job #405 — a header count re-measured and dated, with a re-measure instruction beside it"
rationale: >
  Two jobs in the same week shipped announcements broader than the work they
  described. The rule that emerged is unusually crisp: the announcement is a
  claim, and it is checked like one.
related: [a-check-that-cannot-run-exits-distinctly, present-tense-prose-is-a-claim, silent-filters-hide-rows]
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

## Derivation

Job #378's reviewer rejected a change that fixed this defect while re-creating
it: the new dependency-less path "announces a tier it does not fully run", and
the sibling script using the identical mechanism already printed the correct
caveat. Job #405 landed the durable form — the count, its command, its date.
