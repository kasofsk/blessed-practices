---
type: Blessed Practice
title: "An architectural boundary that nothing checks is a comment"
description: "State every architectural boundary as an executable assertion, and prove the assertion can fail by making it fail on purpose before you ship it."
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
  This corpus contains a guard that could not fire, shipped and believed. The
  practice is not 'add guards' but 'prove the guard fires', which is a different
  and much rarer discipline.
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

## Where this comes from

A guard intended to prove that one subsystem never consults another's state
was shipped and believed. A reviewer's finding was that as written it could
not fire for any realistic violating change. The replacement was a scoped
window that panics at the offending access, with tests proving it fires — the
difference between a check and a decoration.

## Related

- [An unenforced intention gets read as a statement of fact](unenforced-intentions-become-believed-facts.md)
- [Break it on purpose and watch the named case go red](../testing/assertions-that-can-fail.md)
- [One crate owns each external system](one-integration-point-per-dependency.md)
