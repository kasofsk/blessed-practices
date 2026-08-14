---
type: Blessed Practice
title: "Every new dependency states its justification in the commit"
description: "Adding a dependency requires a sentence in the commit message: what it does, why the standard library or an existing dependency does not, and what would let it be removed."
status: draft
tags:
  - bucket/general
  - scope/code
  - altitude/low
  - portability/universal
  - confidence/medium
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  A lightweight rule with a real effect: the justification is what a later
  reader needs when deciding whether the dependency can be removed, and it costs
  one paragraph at the moment it is cheapest to write.
---

**Rule.** Adding a dependency requires a sentence in the commit message: what it
does, why the standard library or an existing dependency does not, and what
would let it be removed.

**Why.** Dependencies are added under time pressure and removed under audit, and
the audit has no record of why the choice was made. The justification is also a
useful filter at the moment of adding — several turn out to be unnecessary while
writing it.

**How to apply.** Pin exactly where behaviour matters. Record the pin's reason
beside it. When a dependency is added for one function, say so — that is the
strongest signal that it can be dropped later.

**Does not apply when.** The dependency is already a transitive requirement and
you are only making it direct.

## Where this comes from

Stated in the source project's principles and observed in review: new packages
are checked for the justification, and at least one exact version pin carries
its decision record in the commit message rather than in a comment beside it.
Writing the justification also filters — several proposed dependencies turn
out to be unnecessary while the sentence is being composed.

## Related

- [Record every deviation from the brief, with its reason](../process/deviation-is-recorded-not-silent.md)
- [The commit message carries the why](../documentation/commit-messages-carry-the-why.md)
