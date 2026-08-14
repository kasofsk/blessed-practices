---
name: exhaustive-matches-no-wildcard
title: Match exhaustively; a new variant should break the build
scope: code
altitude: low
portability: universal
confidence: high
status: candidate
evidence:
  - "job #138 — a non-exhaustive match on a state enum failed to compile after a new variant landed, which is the rule working"
  - "job #138 — the reviewer's instruction: the match is deliberately exhaustive so future additions are caught; keep it that way"
rationale: >
  A small rule that converts a whole class of runtime surprise into a compile
  error. Worth stating because the tempting fix when a match fails to compile is
  to add a wildcard.
related: [restart-reconciliation-is-first-class, terminal-means-terminal, refuse-loudly]
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

## Derivation

Job #138 shipped a match missing a state variant and the crate failed to
compile, blocking the whole change — the rule doing its job. The reviewer's
suggestion was to add the arm and keep the match wildcard-free for exactly this
reason.
