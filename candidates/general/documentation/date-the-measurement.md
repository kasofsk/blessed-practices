---
type: Blessed Practice
title: "Date every measurement, and name the host it was taken on"
description: "Every measured figure carries its date, the command that produced it, and — where it depends on the machine — the host and its relevant state."
status: draft
tags:
  - bucket/general
  - scope/documentation
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  A dated measurement stops being a claim about today and becomes a record,
  which is both more honest and more durable. It also tells the next reader
  exactly how much to trust it.
---

**Rule.** Every measured figure carries its date, the command that produced it,
and — where it depends on the machine — the host and its relevant state.

**Why.** Undated numbers are read as current forever. Dated ones age gracefully:
a reader can see the measurement is two months old and decide whether to re-run
it, which is exactly the decision you want them making.

**How to apply.** Put the date in the sentence, not in the file's metadata. Name
the host when the number could differ per machine, and the tree state when it
could differ per commit. Include a re-measure instruction where the number is
one somebody will want fresh.

**Does not apply when.** The figure is a defined constant rather than a
measurement — then cite the definition.

## Where this comes from

One change defended a count in a script header on the ground that dating
protects a claim that was true when written — converting an assertion into a
record. A later one extended it to proofs, so each recorded proof carries
host, operating system, tree state and command, letting a reader judge whether
it still applies to their machine.

## Related

- [A count in prose is a liability; give the command instead](counts-in-prose-are-liabilities.md)
- [Corrections are appended, dated, and name their job](corrections-are-appended-and-dated.md)
- [Report verification as commands and outputs, not as adjectives](../process/verification-is-reported-with-its-command.md)
