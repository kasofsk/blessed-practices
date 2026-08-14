---
name: pure-decider-effects
title: Deciders return effects; interpreters perform them
scope: architecture
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "jobs #230, #231, #235, #236 — the decide/effects carve-out of the dispatcher's lifecycle logic"
  - "job #235 — a behaviour regression (a result unconditionally overwritten with None) was caught precisely because the decider was pure and diffable against the code it replaced"
  - "docs/reference/style.md Tier 2 rule 1"
rationale: >
  The largest successful refactor in this history is the extraction of pure
  decision functions from I/O-bound handlers. It is also what made the
  regressions in those refactors findable: a pure decider can be diffed against
  its predecessor line by line, and tested exhaustively at the cheapest tier.
related: [single-writer-per-record, lowest-tier-that-expresses-it, behaviour-parity-is-proved-not-asserted]
---

**Rule.** Decision logic is a pure function from a read-only view and an event
to a list of transitions and effects. It performs no I/O, holds no clock, and
awaits nothing. One interpreter executes the effects.

**Why.** Pure deciders are exhaustively testable at the lowest tier, so their
branch coverage is affordable rather than aspirational. They can be reviewed as
a unit, diffed against the imperative code they replace, and reasoned about
without a broker, a container runtime, or a scheduler. The effect list is also
the natural place to assert what a decision is allowed to do.

**How to apply.** Build the view, call `decide`, apply the transitions, then
interpret the effects — in that order, at every call site, so the ordering
cannot differ per path. Give the decider a contract header naming its
preconditions, postconditions and the effect variants it owns. Keep the clock
and the randomness in the view, passed in.

**Does not apply when.** The logic is genuinely a thin pass-through to a
transport, where a decider would be an empty ceremony around one call.

## Derivation

The carve-out ran across jobs #230–#236 and shrank the largest handler file
substantially. Its reviewers repeatedly used purity as the review technique:
job #235's blocking finding was that the new decider assigned a freshly
computed result unconditionally where the old code assigned it only when
present — visible because both were pure expressions over the same inputs.
