---
name: boundaries-are-asserted-not-documented
title: An architectural boundary that nothing checks is a comment
scope: architecture
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "crates/test-utils/tests/boundary_guard.rs — dependency-graph invariants executed as a test"
  - "job #298 — a guard asserting 'placement never reads intent' was rewritten from a vacuous read-counter into a window that actually panics at the offending read"
  - "docs/reference/style.md Tier 3 — a control that reports success and does nothing is worse than no control"
rationale: >
  This corpus contains a guard that could not fire, shipped and believed. The
  practice is not 'add guards' but 'prove the guard fires', which is a different
  and much rarer discipline.
related: [assertions-that-can-fail, one-integration-point-per-dependency, unenforced-intentions-become-believed-facts]
---

**Rule.** State every architectural boundary as an executable assertion, and
prove the assertion can fail by making it fail on purpose before you ship it.

**Why.** A boundary in prose is advice; a boundary in a test is a constraint. But
a guard nobody has seen go red is indistinguishable from a guard that cannot go
red, and the second is worse than nothing — it converts an unenforced intention
into a believed fact.

**How to apply.** Write the guard, then write the violating change and watch the
named case fail. Prefer guards that fire at the offending operation (a panicking
read window, a dependency-graph walk) over guards that count or sample. Keep the
guard inert in production if it costs anything.

**Does not apply when.** The boundary is already enforced by the type system or
the module system — do not add a runtime check for something the compiler
refuses.

## Derivation

Job #298 shipped a guard intended to prove that placement never consults
declared capacity intent. The reviewer's finding was that as written it "cannot
fire for any realistic violating change". Cycle 2 replaced it with a scoped
window spanning the whole launch decision that panics at the offending read,
with should-panic tests proving it fires.
