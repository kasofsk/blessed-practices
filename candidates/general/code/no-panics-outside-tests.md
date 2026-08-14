---
type: Blessed Practice
title: "No unwrap or expect outside tests, especially in the core"
description: "No panicking unwraps in production code."
status: draft
tags:
  - bucket/general
  - scope/code
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Ordinary advice with an extraordinary local justification: this system has a
  single-threaded writer, so one panic stalls every job in the graph. The corpus
  contains the outage that proves it.
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

## Where this comes from

One review found seven new panic sites added to a pure core in a change that
was otherwise exemplary, and named why they bite hardest there: with a single
writer, a panic stalls every unit of work in the graph rather than failing one
request. The corpus contains the matching outage — one terminated unit's
orphaned container drove a path expecting live state and took the platform
down.

## Related

- [One writer per record class](../architecture/single-writer-per-record.md)
- [Prefer a loud refusal to a silent degradation](../architecture/refuse-loudly.md)
- [Terminal states are terminal, and nothing self-heals after them](../architecture/terminal-means-terminal.md)
