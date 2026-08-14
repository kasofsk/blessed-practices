---
type: Blessed Practice
title: "Regenerate every committed derivative in the same commit"
description: "Any artifact generated from the source and committed to the repository is regenerated and committed in the same change that alters its source."
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
  Committed derivatives — schemas, typed clients, sample payloads — go stale in
  a way that is invisible in review and fatal in the gate. The pattern that
  works is a single regenerate command plus a test that compares.
---

**Rule.** Any artifact generated from the source and committed to the repository
is regenerated and committed in the same change that alters its source. A test
asserts the committed copy matches a fresh generation.

**Why.** A derivative is invisible while reviewing the source, and its
correctness is not a matter of judgement — it is a matter of having run the
command. Making the gate assert it turns a class of avoidable red builds into a
one-command step.

**How to apply.** Expose one command that regenerates everything derived and
name it in the contributor docs. Add the compare test to the default test run,
so drift fails locally. Keep formatting tools away from generated files whose
bytes a test asserts.

**Does not apply when.** The artifact is generated at build time and not
committed.

## Where this comes from

One change added three fields to a type and left both the generated schema
bundle and the sample payloads unregenerated, which a reviewer identified as a
certain build failure rather than a stylistic point. Another rewrote the
generated files while reverting the source comments they derive from,
guaranteeing the same failure from the opposite direction.

## Related

- [A change updates the docs it makes stale, in the same commit](../documentation/docs-updated-in-the-same-commit.md)
- [Regenerate golden artifacts; never hand-patch them](../testing/golden-artifacts-are-regenerated.md)
- [Wire changes are additive, epoch-gated, and tolerated by N-1](../architecture/additive-wire-evolution.md)
