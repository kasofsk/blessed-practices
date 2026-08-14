---
type: Blessed Practice
title: "A denial with no control identifies no mechanism"
description: "A single failed attempt does not identify why it failed."
status: draft
tags:
  - bucket/general
  - scope/testing
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  The complement to the previous rule and, in a security context, the more
  dangerous half: a refusal feels like proof of a boundary, and one refusal
  proves only that this attempt failed.
---

**Rule.** A single failed attempt does not identify why it failed. Run the
control — the same operation in a case you expect to succeed — or state plainly
that the mechanism is documented behaviour rather than your result.

**Why.** Denials have many causes: policy, ownership, provenance, a typo, an
unrelated misconfiguration. Without a control, all of them produce identical
evidence, and the one you happen to believe becomes the recorded finding.

**How to apply.** Pair every negative result with a positive control that
isolates one variable. Where no control is possible, say so and downgrade the
claim from "we measured" to "the documentation says". Record both results, not
just the interesting one.

**Does not apply when.** The mechanism is already established and you are
regression-testing it.

## Where this comes from

A load-bearing security premise rested on a single refusal, which was equally
consistent with two different mechanisms — denied by policy, or denied by the
caller's provenance. The reviewer named both hypotheses and prescribed the
control that separates them: the same operation against a subject the caller
created itself.

## Related

- [A tool's outcome measures the tool, not your claim](a-tool-outcome-measures-the-tool.md)
- [An unenforced intention gets read as a statement of fact](../architecture/unenforced-intentions-become-believed-facts.md)
- [Report verification as commands and outputs, not as adjectives](../process/verification-is-reported-with-its-command.md)
