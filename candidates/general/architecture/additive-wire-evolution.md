---
type: Blessed Practice
title: "Wire changes are additive, epoch-gated, and tolerated by N-1"
description: "New wire and config fields are optional and additive."
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
  A self-deploying system is permanently in a mixed-version window. The pattern
  that survived here is specific: tolerate unknown fields, declare a minimum
  version, and make the old side fail by name rather than drop meaning.
---

**Rule.** New wire and config fields are optional and additive. A field whose
absence changes meaning carries a declared minimum version, and the old side
refuses by name rather than ignoring it.

**Why.** The dangerous case is not an unknown field — it is a known-shaped
message whose new field silently means "do the opposite". Tolerance keeps
rollouts alive; the version declaration is what stops tolerance from becoming
semantic loss.

**How to apply.** Default-and-skip-serializing new fields so an old payload
round-trips byte-identically, and pin that with a test. Bump a per-feature
frozen constant beside the shared epoch in the same commit. Make the gate key on
the *presence of the block*, not on one of its sub-fields.

**Does not apply when.** Both sides deploy atomically and you can prove it.

## Where this comes from

A version-skew gate keyed on a nested field rather than on the presence of the
block containing it, so a declaration carrying the block but not that field
slipped every defence — and a unit of work meaning run-natively silently ran
in a container instead. The corrected shape appears in a later change: an
additive field plus a guard that converts the older side's silent drop into a
named failure.

## Related

- [Design for the mixed-version window, because you are always in one](../operations/mixed-version-windows-are-designed-for.md)
- [Prefer a loud refusal to a silent degradation](refuse-loudly.md)
- [Regenerate every committed derivative in the same commit](../code/generated-artifacts-are-regenerated.md)
