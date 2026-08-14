---
type: Blessed Practice
title: "The shared types layer has no I/O and no runtime"
description: "The crate that defines the shared data types also defines their validation rules, and depends on no async runtime, no I/O, and no transport."
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
  Validation duplicated between a server and its clients is the most common
  drift this corpus records. Putting the rules in a layer both sides depend on
  turns a class of bug into a compile-time impossibility.
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

## Where this comes from

Validation duplicated between a server and its clients was the most common
drift in the source retrospective. Where the rules lived in a layer both sides
depended on, reviews credited changes for delegating to the existing checks
rather than writing a second copy — and the reviewers checked for exactly
that, because a second copy is the default outcome under time pressure.

## Related

- [New behaviour lands with a test at the lowest tier that can express it](../testing/lowest-tier-that-expresses-it.md)
- [One crate owns each external system](one-integration-point-per-dependency.md)
- [One resolver per lookup question](one-resolver-per-question.md)
