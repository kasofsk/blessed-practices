---
type: Blessed Practice
title: "Deciders return effects; interpreters perform them"
description: "Decision logic is a pure function from a read-only view and an event to a list of transitions and effects."
status: draft
tags:
  - bucket/general
  - scope/architecture
  - altitude/high
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  The largest successful refactor in this history is the extraction of pure
  decision functions from I/O-bound handlers. It is also what made the
  regressions in those refactors findable: a pure decider can be diffed against
  its predecessor line by line, and tested exhaustively at the cheapest tier.
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

## Where this comes from

Extracting pure decision functions out of I/O-bound handlers was the largest
successful refactor in the source project, and purity was what made its own
regressions findable: reviewers diffed the new pure expressions against the
imperative code they replaced, line by line. The one regression that landed
was an assignment made unconditional where the original was conditional —
visible precisely because both sides were expressions over the same inputs.

## Related

- [A refactor proves parity; it does not assert it](../process/behaviour-parity-is-proved-not-asserted.md)
- [New behaviour lands with a test at the lowest tier that can express it](../testing/lowest-tier-that-expresses-it.md)
- [One writer per record class](single-writer-per-record.md)
