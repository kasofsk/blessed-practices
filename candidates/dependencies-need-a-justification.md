---
name: dependencies-need-a-justification
title: Every new dependency states its justification in the commit
scope: code
altitude: low
portability: universal
confidence: medium
status: candidate
evidence:
  - "docs/reference/style.md Tier 3 — not zero-deps absolutism, but every new package says why in its commit message"
  - "job #314 — a new crate added with the justification recorded in both the manifest and the commit"
  - "job #207 — a version pin decision documented rather than silently taken"
rationale: >
  A lightweight rule with a real effect: the justification is what a later
  reader needs when deciding whether the dependency can be removed, and it costs
  one paragraph at the moment it is cheapest to write.
related: [commit-messages-carry-the-why, deviation-is-recorded-not-silent]
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

## Derivation

The rule is stated in this project's principles tier and observed in practice;
reviews check for it on new crates, and at least one pinned version carries its
decision record in the commit rather than in a comment.
