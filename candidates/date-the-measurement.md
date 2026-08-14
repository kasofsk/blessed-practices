---
name: date-the-measurement
title: Date every measurement, and name the host it was taken on
scope: documentation
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #405 — 'dating protects a claim that was true when written'"
  - "job #457 — proofs recorded with host, OS, tree sha and command"
  - "docs/design/577 — surveyed hardware recorded with the date and the command named beside each class of figure"
rationale: >
  A dated measurement stops being a claim about today and becomes a record,
  which is both more honest and more durable. It also tells the next reader
  exactly how much to trust it.
related: [counts-in-prose-are-liabilities, verification-is-reported-with-its-command, corrections-are-appended-and-dated]
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

## Derivation

Job #405 stated the principle while defending a count in a script header:
dating is what converts an assertion into a record. Job #457 extended it to
proofs — each proof line carries host, OS, tree sha and command, so a later
reader can tell whether it still applies to their machine.
