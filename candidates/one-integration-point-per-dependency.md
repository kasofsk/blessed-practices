---
name: one-integration-point-per-dependency
title: One crate owns each external system
scope: architecture
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/crates.md — the store crate is the only crate that talks to the message broker"
  - "crates/test-utils/tests/boundary_guard.rs — the boundary is asserted over the dependency graph, not just documented"
  - "job #137 — a permission the transport required was missing, and there was exactly one place to fix it"
rationale: >
  A stated boundary that nothing checks decays. This project's version of the
  rule is notable for being executable: a test walks the dependency metadata and
  fails the build when a crate reaches past its integration point.
related: [pure-data-layer, boundaries-are-asserted-not-documented]
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

## Derivation

Job #137's failure is the argument: a worker's announce publish was denied in
production because the broker permission list did not include the subject. The
fix was one line in one file because only one crate composes those lists. Had
transport calls been spread across crates, the same fix would have been a
survey.
