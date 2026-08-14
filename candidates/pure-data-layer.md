---
name: pure-data-layer
title: The shared types layer has no I/O and no runtime
scope: architecture
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/crates.md — the types crate is pure data; validation lives there so every consumer shares one implementation"
  - "jobs #314, #359, #376 — field rules, cron parsing and input validation all landed in the pure layer with tier-1 tests"
rationale: >
  Validation duplicated between a server and its clients is the most common
  drift this corpus records. Putting the rules in a layer both sides depend on
  turns a class of bug into a compile-time impossibility.
related: [one-integration-point-per-dependency, one-resolver-per-question, lowest-tier-that-expresses-it]
---

**Rule.** The crate that defines the shared data types also defines their
validation rules, and depends on no async runtime, no I/O, and no transport.

**Why.** Every consumer then validates identically by construction, and the
rules are testable without standing anything up. A validation rule that lives
in the server is a rule the CLI, the scheduler and the config linter each
reimplement slightly differently.

**How to apply.** Field rules, parsers, name shapes, bounds and defaults go in
the pure layer next to the type. Consumers call them; they never restate them.
Assert the absence of runtime dependencies in the dependency-graph test.

**Does not apply when.** A rule genuinely needs the world (does this path exist,
is this node reachable) — that is a runtime check and belongs with the component
that has the view, per re-derive-facts-in-the-executing-namespace.

## Derivation

Job #376 is the clean case: a scheduler gained user-supplied inputs and the
review explicitly credited it for delegating to the existing shared checks
rather than writing a second copy — "no second validation copy" was the
reviewer's phrasing. Job #314 landed the original rules in the same layer with
each rule individually tested.
