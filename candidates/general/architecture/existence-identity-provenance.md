---
type: Blessed Practice
title: "Existence, identity and provenance are three separate questions"
description: "For any external artifact, ask three questions and write three checks: is it there, is it the thing it claims to be, and did it arrive by a route that survives the next rebuild."
status: draft
tags:
  - bucket/general
  - scope/architecture
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  A refinement of the namespace rule that earns its own card because the three
  checks look interchangeable and are not — passing one is routinely reported as
  passing all three.
---

**Rule.** For any external artifact, ask three questions and write three checks:
is it there, is it the thing it claims to be, and did it arrive by a route that
survives the next rebuild.

**Why.** `exists()` answers the first and is routinely cited as answering all
three. A path can exist and be the wrong artifact; it can be the right artifact
and be there by an accident that the next deploy removes.

**How to apply.** Existence: stat it from the right namespace. Identity:
canonicalize and assert the resolved target has the property you need — under
the expected root, of the expected architecture, matching the expected hash
class. Provenance: assert it was placed by the mechanism you rely on, not merely
found.

**Does not apply when.** The artifact is created and consumed within one
process's lifetime.

## Where this comes from

One change produced all three failures in sequence: an artifact mounted
nowhere, then a bind that resolved a symlink away so the path existed but was
the wrong thing, then a fix that asserted the canonicalized target landed
under the expected root. A later change added the fourth case from a different
angle — an artifact staged on one machine and executed on another passes
existence and identity and still cannot run.

## Related

- [Break it on purpose and watch the named case go red](../testing/assertions-that-can-fail.md)
- [Re-derive every host fact inside the namespace that will use it](re-derive-facts-in-the-executing-namespace.md)
- [What a process is told is not what its uid may open](reachability-by-uid.md)
