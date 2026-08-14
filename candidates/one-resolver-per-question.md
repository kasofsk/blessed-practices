---
name: one-resolver-per-question
title: One resolver per lookup question
scope: architecture
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #306 — the configuration-path resolver, with the listing order derived from the same candidate list the read uses"
  - "job #306 cycle 2 — a listing and a read that could otherwise drift, made to share one owner"
  - "job #507 — level resolution moved into the shared types layer and made private so no launch site can ask the wrong question"
rationale: >
  The lookup-drift bug — a listing that finds a thing and a read that cannot —
  appeared twice and both times the fix was to make one function own the
  question, not to fix the second copy.
related: [config-travels-with-the-project, one-decision-site, pure-data-layer]
---

**Rule.** Each "where does this live" or "which one applies" question has one
function. Listing, reading and validating all go through it, so a listing and a
read cannot disagree.

**Why.** Resolution logic is small and tempting to inline, so it gets written
twice with slightly different precedence. The result is a system that can see a
thing and not open it — a failure mode that reads as corruption.

**How to apply.** Return the resolved location, not just the result, so callers
can report what they resolved. Derive any ordering from the same candidate list
the read uses. Make the wrong-level accessor private so no call site can reach
it.

**Does not apply when.** The two lookups are genuinely different questions —
then name them differently, so the difference is visible.

## Derivation

Job #306's cycle-2 review credits the fix in exactly these terms: one type keeps
one owner for the layout question, and the listing order is derived from the
same candidate list "so a listing and a read cannot drift". Job #507 applied the
same move to level resolution and made the general accessor private.
