---
type: Blessed Practice
title: "Measure corpus growth; do not set a threshold for it"
description: "Build the measurement that informs a judgement, and do not encode the judgement as a threshold."
status: draft
tags:
  - bucket/general
  - scope/documentation
  - altitude/low
  - portability/universal
  - confidence/medium
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  A tool that answers 'is it time' without pretending to decide. The deliberate
  absence of a threshold, and the two git traps recorded with it, make this a
  good template for measurement tooling generally.
---

**Rule.** Build the measurement that informs a judgement, and do not encode the
judgement as a threshold. Report the ranking and let a human decide when it is
time.

**Why.** "The corpus has re-grown" is a judgement about a milestone, not a
defect in any commit, so wiring it to a gate would fail builds for something
nobody in the commit caused. Reported and unwired, it stays useful.

**How to apply.** Make the measurement reproducible and state its method
precisely, including its traps. Report "never measured" distinctly from "zero".
Rank rather than score. Leave it out of the gate.

**Does not apply when.** The threshold is a genuine hard limit (a payload size,
a timeout) rather than a matter of taste.

## Where this comes from

The measurement tool carries two traps that are easy to get wrong and were: a
pathspec suppresses rename detection, so a moved document reports as a total
rewrite, and summing per-commit line counts double-counts a line touched more
than once, so the sum is never the end-to-end figure. A published figure that
had fallen into the second was corrected later.

## Related

- [A count in prose is a liability; give the command instead](counts-in-prose-are-liabilities.md)
- [A knowledge corpus needs a shedding process, not only an appending one](shed-the-corpus-at-milestones.md)
- [Date every measurement, and name the host it was taken on](date-the-measurement.md)
