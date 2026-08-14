---
name: assert-negative-space
title: Assert what must never happen
scope: code
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/style.md Tier 2 rule 2 — pair assertions across the persistence boundary, and assert negative space"
  - "job #298 — an assertion window that panics at an illegal read, with tests proving it fires"
  - "job #414 — an empty-declaration assertion narrowed so it cannot kill the single writer on legitimate configuration"
rationale: >
  The positive assertions get written; the negative ones are what catch the
  transitions nobody meant to add. This corpus also shows the counter-discipline:
  a negative assertion that is too broad becomes an outage of its own.
related: [boundaries-are-asserted-not-documented, no-panics-outside-tests, single-writer-per-record]
---

**Rule.** Alongside asserting what should hold, assert what must never happen —
no transition out of a terminal state, no second writer, no read of this value
from that path. Pair assertions across a persistence boundary: check before the
write and again on read-back.

**Why.** Positive assertions verify the path you thought about. Negative ones
catch the path you did not, which is where the bugs are. The persistence pairing
catches serialization and schema drift at the moment of corruption rather than
three subsystems later.

**How to apply.** Write the negative assertion narrowly enough that legitimate
configuration cannot trip it, and add a test that proves it fires on the
violation. In a single-writer system, prefer a scoped, testable panic window
over a broad assertion that any surprising input can trigger.

**Does not apply when.** The negative condition is unreachable by construction —
then the type system already asserted it.

## Derivation

Job #414 shows both edges in one job: the empty-declaration assertion was
required by the brief, and cycle 3 narrowed it so that a project legitimately
setting its own credential path "survives instead of killing the single writer".
The assertion stayed; its predicate got precise.
