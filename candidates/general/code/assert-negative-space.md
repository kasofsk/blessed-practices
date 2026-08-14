---
type: Blessed Practice
title: "Assert what must never happen"
description: "Alongside asserting what should hold, assert what must never happen — no transition out of a terminal state, no second writer, no read of this value from that path."
status: draft
tags:
  - bucket/general
  - scope/code
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  The positive assertions get written; the negative ones are what catch the
  transitions nobody meant to add. This corpus also shows the counter-discipline:
  a negative assertion that is too broad becomes an outage of its own.
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

## Where this comes from

One change shows both edges at once. A negative assertion was required — that
a particular launch never carries a credential it did not declare — and the
first implementation was broad enough that legitimate configuration could trip
it, which in a single-writer system means an outage. The final version
narrowed the predicate until only the real violation fires, and kept tests
proving it does.

## Related

- [An architectural boundary that nothing checks is a comment](../architecture/boundaries-are-asserted-not-documented.md)
- [No unwrap or expect outside tests, especially in the core](no-panics-outside-tests.md)
- [One writer per record class](../architecture/single-writer-per-record.md)
