---
name: growth-is-measured-not-felt
title: Measure corpus growth; do not set a threshold for it
scope: documentation
altitude: low
portability: universal
confidence: medium
status: candidate
evidence:
  - ".chug/tasks/molt-debt.sh — ranks docs by growth since the last shed, carries no threshold on purpose, and is wired to nothing"
  - "job #544 — a measurement correction: a summed history figure is a different quantity from an end-to-end diff, and a pathspec suppresses rename detection"
rationale: >
  A tool that answers 'is it time' without pretending to decide. The deliberate
  absence of a threshold, and the two git traps recorded with it, make this a
  good template for measurement tooling generally.
related: [shed-the-corpus-at-milestones, counts-in-prose-are-liabilities, date-the-measurement]
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

## Derivation

The debt tool carries two documented git traps that are easy to get wrong and
were: a pathspec suppresses rename detection, so a moved document reports as a
total rewrite; and summing per-commit line counts double-counts a line touched
twice, so it is never the end-to-end figure. Job #544 corrected a published
figure that had fallen into the second.
