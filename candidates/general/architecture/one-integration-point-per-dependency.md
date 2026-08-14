---
type: Blessed Practice
title: "One crate owns each external system"
description: "Each external system — broker, container runtime, VCS, cloud API — has exactly one module or crate that speaks to it."
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
  A stated boundary that nothing checks decays. This project's version of the
  rule is notable for being executable: a test walks the dependency metadata and
  fails the build when a crate reaches past its integration point.
---

**Rule.** Each external system — broker, container runtime, VCS, cloud API —
has exactly one module or crate that speaks to it. Everything else uses that
module's typed accessors.

**Why.** One integration point means one place to add a permission, one place
to change a timeout, one place to pin a client version, and one place to look
when the external system misbehaves. It also makes the dependency graph a
meaningful artifact rather than an accident.

**How to apply.** Put the client library dependency in exactly one crate's
manifest, and add a test that reads the dependency graph and fails if any other
crate resolves it. Expose the capability, not the client: return domain types,
not the vendor's.

**Does not apply when.** Two consumers need genuinely different subsets of a
large API and sharing one facade would produce a worse abstraction than two —
in which case say so, and keep the count at two, not many.

## Where this comes from

A permission required by an external transport was missing, and the whole
feature silently did nothing in production. The fix was one line in one file
because a single component composed those permission lists; had transport
calls been spread across the codebase, the same fix would have been a survey.
The boundary was also asserted as a test over the dependency graph rather than
stated in prose, which is what kept it true.

## Related

- [An architectural boundary that nothing checks is a comment](boundaries-are-asserted-not-documented.md)
- [The shared types layer has no I/O and no runtime](pure-data-layer.md)
