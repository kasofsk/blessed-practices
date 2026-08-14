---
type: Blessed Practice
title: "Ask each artifact the question its own executor asks"
description: "Every staged artifact is proved runnable on the machine that will exec it, before the first install — not on the machine that built it."
status: draft
tags:
  - bucket/general
  - scope/architecture
  - altitude/mid
  - portability/universal
  - confidence/medium
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  A late-arriving member of the namespace family, and the least intuitive: the
  premise that failed was never expressed as a flag, so no audit of the launch
  configuration could have seen it.
---

**Rule.** Every staged artifact is proved runnable on the machine that will
exec it, before the first install — not on the machine that built it.

**Why.** A property true by construction inside a build context stops being
guaranteed the moment the artifact leaves it. Architecture, libc, code signing
and interpreter paths are all invisible to a review of the staging code, because
none of them is a parameter of the staging code.

**How to apply.** Add an exec probe to the install path: run the artifact with a
harmless argument on the target and require a specific exit or output. Where a
probe is impossible, inspect the artifact's own header for the target's
architecture and refuse a mismatch by name.

**Does not apply when.** The build and the execution genuinely happen in the
same image on the same host.

## Where this comes from

A binary extracted from an image built for one architecture was staged onto a
machine of another. The staging code was correct and reviewable; the premise
that failed — which kernel would exec the artifact — was never expressed as a
parameter, so no audit of the launch configuration could have seen it. The fix
was both a header check and an exec probe before the first install.

## Related

- [Existence, identity and provenance are three separate questions](existence-identity-provenance.md)
- [Re-derive every host fact inside the namespace that will use it](re-derive-facts-in-the-executing-namespace.md)
