---
type: Blessed Practice
title: "An exemption mechanism must be narrower than the thing it exempts"
description: "Design every exemption to be narrower than the rule it escapes: line-scoped rather than file-scoped, per-instance rather than per-threshold, and requiring a written reason at the point of use."
status: draft
tags:
  - bucket/general
  - scope/documentation
  - altitude/mid
  - portability/universal
  - confidence/medium
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Three independent exemption mechanisms in this repo were each deliberately
  scoped so they cannot be used broadly. That is a design pattern for gates, not
  an accident, and it is what keeps the gates from being disabled in practice.
---

**Rule.** Design every exemption to be narrower than the rule it escapes:
line-scoped rather than file-scoped, per-instance rather than per-threshold, and
requiring a written reason at the point of use.

**Why.** A broad exemption is used broadly. Once a file-level or threshold-level
escape exists, the cheapest response to any finding is to widen it, and the rule
stops meaning anything without anyone deciding to abandon it.

**How to apply.** Scope exemptions to the smallest unit the checker can see.
Require the justification inline where the checker can confirm it is present.
Prefer refusing a global knob outright — raising a threshold should not be an
available move.

**Does not apply when.** The rule is genuinely wrong for a whole category —
then change the rule, and say so.

## Where this comes from

Three independent exemption mechanisms in the source project were each
deliberately scoped so they cannot be used broadly — line-scoped rather than
file-scoped, per-instance rather than per-threshold, and requiring the
justification inline where the checker can see it. One lint enforces the one-
line constraint mechanically by matching only the text immediately after the
comment opener.

## Related

- [A gate is code, so it has tests, and the tests are discovered](../process/every-gate-has-a-test-suite.md)
- [Marking is a syntax, and the markers are not interchangeable](mark-unbuilt-intent.md)
- [Zero duplication, because agent-written code clones readily](../code/no-duplication-threshold.md)
