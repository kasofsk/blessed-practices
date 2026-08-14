---
type: Blessed Practice
title: "An unenforced intention gets read as a statement of fact"
description: "Do not write a constraint you are not enforcing."
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
  This is the strongest single argument in the corpus for the difference between
  a rule and a check, and it is stated with a date and a duration. It deserves
  its own card because the failure is epistemic, not mechanical: the sentence
  never carried a check, and every subsequent design reasoned from it.
---

**Rule.** Do not write a constraint you are not enforcing. If you must record an
intention, mark it as intent in the same sentence, so nobody reasons from it as
a fact.

**Why.** Downstream designs cite constraints. A constraint that is merely
intended is cited identically to one that is enforced, and the citation chain
grows faster than anyone re-checks the root. By the time it is measured, several
decisions rest on it.

**How to apply.** When you state a security or isolation property, ship the
check with it or write "not enforced" beside it. When you inherit such a
property from another document, measure it before you build on it — and record
the measurement with its date and command.

**Does not apply when.** The property is enforced by something outside your
system that you can name and cite.

## Where this comes from

A security property was written down, was never checked, and was cited by
several later designs as an established constraint. When it was finally
measured it had been false from the day it was written, on the one machine
where it mattered. The recorded lesson is the rule: the sentence never carried
a check, and the citation chain grew faster than anyone re-verified its root.

## Related

- [An architectural boundary that nothing checks is a comment](boundaries-are-asserted-not-documented.md)
- [Prefer a loud refusal to a silent degradation](refuse-loudly.md)
- [Present-tense prose about the tree is a factual claim](../documentation/present-tense-prose-is-a-claim.md)
