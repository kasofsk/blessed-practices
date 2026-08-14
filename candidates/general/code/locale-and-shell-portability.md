---
type: Blessed Practice
title: "Pin the locale and know which shell binds your line"
description: "Any script that classifies text pins its locale explicitly."
status: draft
tags:
  - bucket/general
  - scope/code
  - altitude/low
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Two distinct, silent, host-dependent defects found in gate scripts — the tools
  that decide whether everything else is correct. Both were invisible to syntax
  checking, which is what makes them worth a card.
---

**Rule.** Any script that classifies text pins its locale explicitly. Any script
that may run under more than one shell avoids constructs the shells disagree
about — notably quotes inside the word of a parameter expansion.

**Why.** Both defects are silent and both are invisible to a syntax check: the
script parses, runs, and produces a different verdict depending on where it ran.
For a gate, that means the answer to "is this change acceptable" is
environment-dependent.

**How to apply.** Set the locale at the top of any script using character
classes, ranges or sorting, with the reason on the line. Rewrite prose rather
than escaping quotes inside expansions. Where a divergence is silent in both
shells, write a lexical gate for the class of construct, not for the one
spelling that failed.

**Does not apply when.** The script runs under exactly one pinned interpreter in
exactly one image — which is worth verifying rather than assuming.

## Where this comes from

Two silent, host-dependent defects were found in the scripts that decide
whether everything else is correct. A character-class range whose membership
follows the locale's collation accepted names it was written to reject. And a
quoted word inside a parameter expansion bound different code under two shells
while staying valid in both — it moved an entire pre-flight block into the
branch above it, so the guard ran only when its own check failed, and the
syntax checker was happy.

## Related

- [A dropped row reads like a negative result](../process/silent-filters-hide-rows.md)
- [Test the premise, not only the behaviour](../testing/test-the-premise.md)
- [The gate's environment is the authority; local runs produce false reds](../testing/the-gate-container-is-the-authority.md)
