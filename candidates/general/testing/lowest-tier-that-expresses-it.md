---
type: Blessed Practice
title: "New behaviour lands with a test at the lowest tier that can express it"
description: "Every behaviour change lands with a regression test at the cheapest tier that can express it."
status: draft
tags:
  - bucket/general
  - scope/testing
  - altitude/high
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Stated as a rule and enforced by reviewers in practice, with the sharper
  corollary that showed up repeatedly: if the property cannot be tested at any
  tier, that is a defect in the code's shape, not a licence to skip the test.
---

**Rule.** Every behaviour change lands with a regression test at the cheapest
tier that can express it. If no tier can express it, change the code's shape
until one can.

**Why.** The lower the tier, the more often the test actually runs, and the
faster it fails. A property that is only expressible at the most expensive tier
is a property that will be checked rarely, if at all.

**How to apply.** Push the logic down to a pure function so its branches are
tier-one testable, and reserve the expensive tiers for the wiring. When a
required property is unreachable — because a value is a compile-time constant, or
an effect has no observer — make it injectable or observable, and say so in the
commit.

**Does not apply when.** The behaviour is genuinely an integration property
(does this actually reach the broker) — then test it there and say why.

## Where this comes from

One review found that a required test could not be written against the code as
shaped, because the value it depended on was a compile-time constant absent in
test builds, and asked for it to be made injectable rather than waiving the
test. Another found the observation half: a cleanup call spelled so that
failure is indistinguishable from success needs an assertion on the consumer,
not on the call.

## Related

- [A test must be able to observe what its name claims](no-vacuous-assertions.md)
- [Break it on purpose and watch the named case go red](assertions-that-can-fail.md)
- [Deciders return effects; interpreters perform them](../architecture/pure-decider-effects.md)
