---
name: lowest-tier-that-expresses-it
title: New behaviour lands with a test at the lowest tier that can express it
scope: testing
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/style.md Tier 2 rule 6"
  - "job #290 — half of a two-part fix untested because nothing observed the consumer afterwards; 'this is the half of the fix that cannot be verified by reading'"
  - "job #108 — a required property that was structurally untestable, so the reviewer asked for the code to be made injectable"
rationale: >
  Stated as a rule and enforced by reviewers in practice, with the sharper
  corollary that showed up repeatedly: if the property cannot be tested at any
  tier, that is a defect in the code's shape, not a licence to skip the test.
related: [pure-decider-effects, assertions-that-can-fail, no-vacuous-assertions]
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

## Derivation

Job #108's reviewer found that the one required test "cannot be written against
the code as shaped", because the value it depended on was a compile-time
constant that is absent in test builds, and asked for an injectable field. Job
#290's is the observation half: a cleanup call spelled so that failure is
indistinguishable from success needs an assertion on the consumer, not on the
call.
