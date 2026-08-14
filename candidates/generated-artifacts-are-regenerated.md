---
name: generated-artifacts-are-regenerated
title: Regenerate every committed derivative in the same commit
scope: code
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #298 — committed schema and wire-sample artifacts not re-emitted after a type gained three fields, so the workspace test fails and the gate goes red"
  - "job #441 — schemas rewritten while the source doc comments they derive from were reverted, guaranteeing the same failure"
  - "A workspace test asserts the committed artifacts match a fresh generation"
rationale: >
  Committed derivatives — schemas, typed clients, sample payloads — go stale in
  a way that is invisible in review and fatal in the gate. The pattern that
  works is a single regenerate command plus a test that compares.
related: [golden-artifacts-are-regenerated, additive-wire-evolution, docs-updated-in-the-same-commit]
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

## Derivation

Job #298 shipped a type with three new fields and left both the schema bundle
and the sample payloads unregenerated, which the reviewer identified as a
certain gate failure rather than a stylistic issue. The tree's answer includes a
formatting-ignore rule so the pre-commit formatter cannot rewrite a generated
file whose exact bytes a test asserts.
