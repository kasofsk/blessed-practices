---
name: silent-filters-hide-rows
title: A dropped row reads like a negative result
scope: process
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #493 — an operator instruction naming a log target that matches nothing; the filter accepts unknown targets silently, so following the instruction raises no level at all"
  - "job #366 — a locale-dependent character class silently passed names it was written to reject"
rationale: >
  A recurring shape across tooling, docs and UI: something filters, finds
  nothing, and reports the empty set as an answer. The reader concludes the
  thing is absent rather than that the query was wrong.
related: [announce-exactly-what-ran, a-check-that-cannot-run-exits-distinctly, verification-is-reported-with-its-command]
---

**Rule.** Any filter, selector or query that can silently match nothing must say
so. Print the selector, the population, and the count — and treat "zero matches"
as a distinct outcome from "zero findings".

**Why.** A filter that quietly matches nothing produces a confident negative
result. Both the machine and the reader then act on it: the gate passes, the
operator concludes the setting had no effect, the author concludes the tree is
clean.

**How to apply.** Give the command beside any measured figure so it can be
re-run. When a selector is user-supplied, validate it against the known set and
refuse an unknown value. When a scan finds nothing, print how many inputs it
examined.

**Does not apply when.** The empty set is the normal, expected outcome and the
population is obvious — even then, printing the population costs one line.

## Derivation

Job #493 is the cleanest instance: the documented log directive named a crate
that does not exist under that name, the filter library accepts unknown targets
without complaint, and "an operator who follows this raises no level at all —
the instruction fails without saying so".
