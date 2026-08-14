---
type: Blessed Practice
title: "A dropped row reads like a negative result"
description: "Any filter, selector or query that can silently match nothing must say so."
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
  A recurring shape across tooling, docs and UI: something filters, finds
  nothing, and reports the empty set as an answer. The reader concludes the
  thing is absent rather than that the query was wrong.
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

## Where this comes from

The cleanest instance is an operator instruction naming a log target that
matches nothing: the filtering library accepts unknown targets without
complaint, so anyone following the instruction raises no level at all and the
instruction fails without saying so. A second: a locale-dependent character
class silently accepting the names it was written to reject.

## Related

- [Announce exactly what ran — never a tier you did not execute](announce-exactly-what-ran.md)
- [Cannot-run and passed must not print the same](a-check-that-cannot-run-exits-distinctly.md)
- [Report verification as commands and outputs, not as adjectives](verification-is-reported-with-its-command.md)
