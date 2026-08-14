---
type: Blessed Practice
title: "Match exhaustively; a new variant should break the build"
description: "Match every variant explicitly."
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
  A small rule that converts a whole class of runtime surprise into a compile
  error. Worth stating because the tempting fix when a match fails to compile is
  to add a wildcard.
---

**Rule.** Match every variant explicitly. Do not add a catch-all arm to a match
over a domain enum — when a new variant is added, every place that must consider
it should fail to compile.

**Why.** The compile error is a free, exhaustive audit of everywhere a new state
matters. A wildcard converts that audit into a silent default, and the default
is wrong somewhere.

**How to apply.** When a match fails to compile after adding a variant, handle
the variant — do not widen the arm. Where a genuine default exists, write it as
explicit arms grouped together, so the next addition still fails.

**Does not apply when.** The enum is external and non-exhaustive by declaration.

## Where this comes from

A change added a new state variant and a match elsewhere failed to compile,
blocking the whole change — the rule doing its job rather than failing. The
reviewer's instruction was the durable part: add the arm, and keep the match
free of catch-alls so the next addition is caught the same way.

## Related

- [Every in-flight state has a restart arm](../architecture/restart-reconciliation-is-first-class.md)
- [Prefer a loud refusal to a silent degradation](../architecture/refuse-loudly.md)
- [Terminal states are terminal, and nothing self-heals after them](../architecture/terminal-means-terminal.md)
