---
name: additive-wire-evolution
title: Wire changes are additive, epoch-gated, and tolerated by N-1
scope: architecture
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/spec.md §14.2/§14.3 — unknown fields tolerated with a warning; a config declaring a newer epoch parks the job"
  - "job #403 — an additive RPC field plus a dispatcher-built guard turning an N-1 semantic drop into a named task failure"
  - "job #401 — a skew gate keyed on the wrong sub-field, so a whole declaration slipped every defense"
rationale: >
  A self-deploying system is permanently in a mixed-version window. The pattern
  that survived here is specific: tolerate unknown fields, declare a minimum
  version, and make the old side fail by name rather than drop meaning.
related: [refuse-loudly, mixed-version-windows-are-designed-for, generated-artifacts-are-regenerated]
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

## Derivation

Job #401's reviewer walked the N-1 path field by field and found the gate keyed
on a nested field, so a declaration carrying the outer block but not that field
"slips every defense" and a job meaning run-natively silently ran in a
container. Job #403 shows the corrected shape: additive field plus a guard that
converts the old side's silent drop into a named task failure.
