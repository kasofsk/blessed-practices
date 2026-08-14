---
type: Blessed Practice
title: "Zero duplication, because agent-written code clones readily"
description: "Zero tolerated clones."
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
  The argument is specific to agent-written code and is the strongest reason in
  the corpus for a rule that would be excessive in a human-only codebase: an
  agent that cannot find the existing helper writes a second one.
---

**Rule.** Zero tolerated clones. Extract the shared body into a helper named
after its caller. A deliberate exception is a bracketed directive stating why —
never a threshold change.

**Why.** Duplicated logic drifts apart, and the copy that did not get the fix is
where the next bug lives. Agents duplicate far more readily than humans, because
finding the existing helper costs a search and writing a new one does not — so
any threshold above zero ratchets the wrong way.

**How to apply.** Run the detector whole-tree and unconditionally if it is fast
enough. Pin its version exactly, since detection behaviour changes between
releases. Exclude generated and vendored trees by path, not by raising the bar.

**Does not apply when.** The two copies are genuinely coincidental structure
with no shared meaning — that is what the per-instance exception is for.

## Where this comes from

The justification is recorded with the rule: a threshold set anywhere above
zero ratchets the wrong way for code written by agents, because an agent that
cannot find the existing helper writes a second one. The gate found a real
clone in the very change that introduced it, and a later change was blocked by
a twelve-line verbatim clone in an otherwise-accepted diff.

## Related

- [An exemption mechanism must be narrower than the thing it exempts](../documentation/a-marker-is-not-a-silencer.md)
- [Names are the index an agent navigates by](naming-is-the-index.md)
- [One decision site per question](../architecture/one-decision-site.md)
