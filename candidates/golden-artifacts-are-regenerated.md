---
name: golden-artifacts-are-regenerated
title: Regenerate golden artifacts; never hand-patch them
scope: testing
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #414 cycle 2 — golden traces stale because two paths every scenario exercises gained an event; the gate would have gone red"
  - "job #414 cycle 3 — accepted because the traces were regenerated, not hand-patched, and the reviewer verified every added line sat where the mechanism would put it"
  - "job #298 — committed schema and sample artifacts not re-emitted after a type gained three fields, failing the workspace test"
rationale: >
  Generated artifacts are the most common cause of a mechanically red branch
  here, and hand-patching them is the most common wrong fix — it produces a
  green test asserting something the generator would not produce.
related: [generated-artifacts-are-regenerated, assertions-that-can-fail, docs-updated-in-the-same-commit]
---

**Rule.** When a change alters what a generator emits, re-run the generator and
commit its output. Never edit a golden file by hand to make a test pass.

**Why.** A hand-patched golden asserts what the author believed the generator
would produce. If they were wrong, the test is now wrong in the same direction
as the bug, and it will stay green through the bug's whole life.

**How to apply.** Make regeneration a single documented command and run it as
part of the change. Have a test assert that the committed artifacts match a
fresh generation, so drift is caught rather than reported. When reviewing,
verify the shape of the added lines against the mechanism, not just their
presence.

**Does not apply when.** The golden is a hand-authored fixture by design — then
say so, and keep it out of the regenerate-and-compare set.

## Derivation

Job #414 spans both sides: cycle 2 rejected because the goldens were stale and
the gate was certain to fail; cycle 3 accepted because they were regenerated and
the reviewer could check that all seventeen added lines sat exactly where the
mechanism would place them, and none where it would not.
