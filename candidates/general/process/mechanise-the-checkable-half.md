---
type: Blessed Practice
title: "Mechanise the checkable half; route the rest to judgement"
description: "For each rule you care about, separate the part that resolves against the tree from the part that needs judgement."
status: draft
tags:
  - bucket/general
  - scope/process
  - altitude/high
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  The clearest organising principle behind this project's quality system: every
  rule is split into the part a script can resolve and the part it cannot, and
  the two are enforced by different machinery at different costs.
---

**Rule.** For each rule you care about, separate the part that resolves against
the tree from the part that needs judgement. Script the first. Give the second
to a reader, with the class named so their attention is directed.

**Why.** Scripts are cheap, deterministic and never tired, but they can only
resolve. Readers are expensive and variable, but they can judge. Mixing the two
wastes the reader on resolvable questions and leaves the judgement to whoever
happens to look.

**How to apply.** Ask what evidence would settle the question. Anything that
grounds out in a path, a constant, a commit, a row or a link is scriptable.
Anything requiring "is this argument honest" or "does this claim still hold
about behaviour" is a reading class — name the classes explicitly so the reader
knows what they own.

**Does not apply when.** The scriptable half is so narrow that the script
provides false assurance — then say so and keep it with the reader.

## Where this comes from

The split is visible in a pair of checks: a shell script resolves six
mechanical claim classes over the whole tree in under a second, while a
reading reviewer owns exactly three classes no script can decide. Neither
duplicates the other, and every rejection says which side it came from.

## Related

- [A gate is code, so it has tests, and the tests are discovered](every-gate-has-a-test-suite.md)
