---
type: Blessed Practice
title: "Measure on a fresh fixture, or the numbers lie"
description: "Take timing and coverage measurements against a freshly created fixture, with the environment stated."
status: draft
tags:
  - bucket/general
  - scope/testing
  - altitude/low
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Performance and coverage numbers taken against a warm, dirty environment are
  the most confidently quoted wrong numbers in any project. Recording the
  measurement preconditions beside the figure is what makes them reproducible.
---

**Rule.** Take timing and coverage measurements against a freshly created
fixture, with the environment stated. Suites leave nothing behind in the
checkout.

**Why.** A warm cache, a populated store or a leftover artifact from a previous
run changes the number by an order of magnitude and changes it in the flattering
direction. And a suite that writes into the working tree will eventually dirty a
gate run.

**How to apply.** Create the fixture in a throwaway directory and remove it.
State the preconditions with the figure — fresh store, this stack size, this
container. Assert in the suite that the working tree is unchanged when it
finishes.

**Does not apply when.** The warm case is the case you are measuring — then say
so.

## Where this comes from

The source project records measurement preconditions in the same sentence as
its figures, because a warm cache or a populated store moves the number by an
order of magnitude and always in the flattering direction. The other half came
from a suite found to be writing a stray archive into the working tree on
every run — undetected because nothing had been executing it.

## Related

- [A count in prose is a liability; give the command instead](../documentation/counts-in-prose-are-liabilities.md)
- [Date every measurement, and name the host it was taken on](../documentation/date-the-measurement.md)
- [Report verification as commands and outputs, not as adjectives](../process/verification-is-reported-with-its-command.md)
