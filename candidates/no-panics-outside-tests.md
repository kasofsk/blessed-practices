---
name: no-panics-outside-tests
title: No unwrap or expect outside tests, especially in the core
scope: code
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/style.md Tier 1 — denied by the workspace lint table, tests exempted at scope"
  - "job #231 — seven production panics introduced into the pure core, in the crate the rule most targets"
  - "The 2026-07-23 outage — one revoked job's orphaned container panicked the single-threaded core and took down the platform"
rationale: >
  Ordinary advice with an extraordinary local justification: this system has a
  single-threaded writer, so one panic stalls every job in the graph. The corpus
  contains the outage that proves it.
related: [terminal-means-terminal, single-writer-per-record, refuse-loudly]
---

**Rule.** No panicking unwraps in production code. Where an invariant must be
asserted, use a debug assertion or a panic with a message naming the invariant —
and treat that as a last resort, not a shortcut around an error type.

**Why.** In a single-writer orchestrator a panic is not a crashed request, it is
a stalled graph. The majority of catastrophic distributed-system failures trace
to mishandled errors, and this system has already produced its own instance.

**How to apply.** Deny the lints workspace-wide with test scopes exempted at the
top of the scope. Land as a ratchet with per-site markers naming the ticket.
Where a decider needs an invariant guard, follow the established template rather
than inventing a second style.

**Does not apply when.** The code is a test, a fixture, or a startup path where
failing to start is the correct behaviour — and even there, prefer a message
that names the misconfiguration.

## Derivation

Job #231's reviewer found seven production panic sites added to the pure core in
a change that was otherwise exemplary, and named why it bites hardest there: "in
the single-writer dispatcher a panic stalls every job in the DAG". The template
crate beside it was already panic-free using debug assertions.
