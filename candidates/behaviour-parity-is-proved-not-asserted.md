---
name: behaviour-parity-is-proved-not-asserted
title: A refactor proves parity; it does not assert it
scope: process
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "job #231 — traces extended in a separate groundwork commit and left untouched by the extraction, so the unchanged traces are the parity proof"
  - "job #236 — a thirteen-module split reviewed line by line against the original, with the reviewer stating no behavioural change was found"
  - "job #235 — a parity claim that was false: a result field overwritten where the old code left it alone"
rationale: >
  The refactors that landed cleanly here all carried a mechanical parity
  argument, not a promise. The one that did not carried a real regression, found
  by a reviewer diffing expressions by hand.
related: [pure-decider-effects, golden-artifacts-are-regenerated, assertions-that-can-fail]
---

**Rule.** A change that claims to preserve behaviour ships the evidence: a
characterisation test or trace landed *before* the refactor and unchanged by it,
or a line-by-line correspondence the reviewer can check.

**Why.** "No behaviour change" is the most common false claim in a refactor,
because the author has just spent hours convincing themselves the shapes are
equivalent. A pre-existing artifact that the refactor does not touch is the only
cheap proof.

**How to apply.** Land the characterisation artifact in its own commit first, so
its content cannot be tuned to the new code. Keep the refactor commit free of
changes to it. Where no such artifact exists, structure the diff so
correspondence is checkable — same ordering, same names, one concern per commit.

**Does not apply when.** The change deliberately alters behaviour — then say so
and test the new behaviour.

## Derivation

Job #231's review names the technique as the reason it passes: "traces extended
in a separate groundwork commit and left untouched by the extraction = behavior
parity proof". Job #235, structurally similar, was rejected for a single
unconditional assignment that the old code performed conditionally.
