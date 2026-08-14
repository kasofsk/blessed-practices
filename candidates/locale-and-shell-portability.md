---
name: locale-and-shell-portability
title: Pin the locale and know which shell binds your line
scope: code
altitude: low
portability: universal
confidence: high
status: candidate
evidence:
  - "job #366 — a character-class range whose membership depends on the locale's collation, silently passing names it was written to reject"
  - "job #501 — a quoted word inside a parameter expansion that binds different code under two shells while staying valid in both"
  - "The comment lint pins the locale so the verdict is the same on every host"
rationale: >
  Two distinct, silent, host-dependent defects found in gate scripts — the tools
  that decide whether everything else is correct. Both were invisible to syntax
  checking, which is what makes them worth a card.
related: [the-gate-container-is-the-authority, silent-filters-hide-rows, test-the-premise]
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

## Derivation

Job #501's case is the sharper of the two: the divergence moved a whole
pre-flight block into the branch above it, so the guard ran only when its own
check failed — valid in both shells, accepted by the syntax checker, and green
in the gate's shell while wrong in production's.
