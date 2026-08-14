---
name: reserved-namespace-prefixes
title: Reserve a prefix for platform-owned names
scope: architecture
altitude: low
portability: universal
confidence: high
status: candidate
evidence:
  - "job #269 — a job type declaring a reserved-prefix secret could never be released; the platform's deploy path would have been dead, not merely gated"
  - "job #518 — a second prefix reserved, with release validation and injection updated together"
rationale: >
  Cheap to state, expensive to retrofit. The corpus contains both the good case
  (a reservation that caught a real collision at validation) and the bad one (a
  change that used the reserved prefix and would have bricked a job type).
related: [fail-closed-allow-lists, additive-wire-evolution, refuse-loudly]
---

**Rule.** Platform-injected names live under a reserved prefix. User
configuration may not declare a name under it, and the refusal happens at
validation with the offending name in the message.

**Why.** Without a reservation, a user variable can shadow a platform one and
the failure appears somewhere unrelated. With one, the collision is a validation
error at the moment of authoring.

**How to apply.** Reserve at declaration validation *and* at injection, so a
name that slips one is caught by the other. When you add a second reserved
prefix, grep for prose that enumerates the first — it will exist, and it will
now be wrong.

**Does not apply when.** The namespace is genuinely shared and collisions are
resolved by documented precedence — say which side wins and test it.

## Derivation

Job #269's blocker: a proposed wiring used the reserved prefix for its own
token, and release validation refuses any declared secret under it — so with
that merged, no job of that type could ever be released. Job #518 added a second
prefix and its reviewers immediately found the enumerating prose in two other
files.
