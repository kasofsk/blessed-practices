---
type: Blessed Practice
title: "Reserve a prefix for platform-owned names"
description: "Platform-injected names live under a reserved prefix."
status: draft
tags:
  - bucket/general
  - scope/architecture
  - altitude/low
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Cheap to state, expensive to retrofit. The evidence contains both the good case
  — a reservation that caught a real collision at validation — and the bad one, a
  change that used the reserved prefix and would have made a whole configuration
  type unusable.
---

**Rule.** Platform-injected names live under a reserved prefix. User
configuration may not declare a name under it, and the refusal happens at
validation with the offending name in the message.

**Why.** Without a reservation, a user variable can shadow a platform one and
the failure appears somewhere unrelated. With one, the collision is a validation
error at the moment of authoring.

**How to apply.** Reserve at declaration validation *and* at injection, so a
name that slips one is caught by the other. When you add a second reserved
prefix, grep for prose that enumerates the first — it will exist, and it will
now be wrong.

**Does not apply when.** The namespace is genuinely shared and collisions are
resolved by documented precedence — say which side wins and test it.

## Where this comes from

One proposed configuration used the platform's reserved prefix for its own
credential, and validation refuses any declared name under it — so had it
merged, no unit of that type could ever have been started. A later change
added a second reserved prefix, and reviewers immediately found prose in two
other files enumerating the first as if it were the only one.

## Related

- [Grants are allow-lists, fail-closed, refused at three layers](fail-closed-allow-lists.md)
- [Prefer a loud refusal to a silent degradation](refuse-loudly.md)
- [Wire changes are additive, epoch-gated, and tolerated by N-1](additive-wire-evolution.md)
