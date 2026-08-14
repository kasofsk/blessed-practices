---
name: measure-on-a-clean-fixture
title: Measure on a fresh fixture, or the numbers lie
scope: testing
altitude: low
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/testing.md — measure on a fresh store directory with a raised stack size, or the numbers lie"
  - "job #385 — a suite writing a stray artifact into the checkout on every run, which would have dirtied the tree once the gate started running it"
rationale: >
  Performance and coverage numbers taken against a warm, dirty environment are
  the most confidently quoted wrong numbers in any project. Recording the
  measurement preconditions beside the figure is what makes them reproducible.
related: [date-the-measurement, counts-in-prose-are-liabilities, verification-is-reported-with-its-command]
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

## Derivation

This project's testing page records the preconditions in the same sentence as
the figures, for exactly this reason. Job #385 found the other half in a sibling
suite that had been writing a stray archive into the checkout on every run,
undetected because nothing had been running it.
