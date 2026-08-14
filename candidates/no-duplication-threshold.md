---
name: no-duplication-threshold
title: Zero duplication, because agent-written code clones readily
scope: code
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/style.md Tier 1 — a pinned detector at zero threshold over the whole repo, about 30ms"
  - "job #258 — the gate landed and immediately caught a real clone in the same change"
  - "job #476 — a twelve-line verbatim comment clone blocking an otherwise-accepted change"
rationale: >
  The argument is specific to agent-written code and is the strongest reason in
  the corpus for a rule that would be excessive in a human-only codebase: an
  agent that cannot find the existing helper writes a second one.
related: [one-decision-site, a-marker-is-not-a-silencer, naming-is-the-index]
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

## Derivation

The rule's justification is recorded with it: a threshold set anywhere above
zero would ratchet the wrong way for agent-written code. Job #258's experience
supports it — the gate found a real clone in the very change that introduced it.
