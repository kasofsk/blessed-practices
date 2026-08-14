---
type: Blessed Practice
title: "Regenerate golden artifacts; never hand-patch them"
description: "When a change alters what a generator emits, re-run the generator and commit its output."
status: draft
tags:
  - bucket/general
  - scope/testing
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Generated artifacts are the most common cause of a mechanically red branch
  here, and hand-patching them is the most common wrong fix — it produces a
  green test asserting something the generator would not produce.
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

## Where this comes from

One change spans both sides. It was rejected when its golden fixtures went
stale — two code paths every scenario exercises had gained an event — and
accepted a cycle later because the fixtures were regenerated rather than hand-
patched, which let the reviewer verify that all seventeen added lines sat
exactly where the mechanism would place them and none where it would not.

## Related

- [A change updates the docs it makes stale, in the same commit](../documentation/docs-updated-in-the-same-commit.md)
- [Break it on purpose and watch the named case go red](assertions-that-can-fail.md)
- [Regenerate every committed derivative in the same commit](../code/generated-artifacts-are-regenerated.md)
