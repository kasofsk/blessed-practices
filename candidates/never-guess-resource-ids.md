---
name: never-guess-resource-ids
title: Thread identifiers from responses; never predict them
scope: operations
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "A guessed identifier once raced a concurrent create and released a different job than intended"
  - "The operating skill records the rule: never predict server-assigned ids, and re-verify a target's identity before a consequential mutation"
rationale: >
  A one-line rule with a recorded incident behind it, and one that agents
  violate naturally because the next number is usually right.
related: [destructive-actions-need-confirmation, refuse-loudly, a-commit-is-a-publication]
---

**Rule.** Take every server-assigned identifier from the response that created
the resource. Never compute or guess one. Before a consequential mutation,
re-read the target and confirm its identity.

**Why.** Sequential identifiers are predictable and usually correct, which is
what makes the failure rare and severe: under concurrency the guess names
someone else's resource, and the operation succeeds.

**How to apply.** Capture the identifier into a variable at creation and use the
variable. For destructive or state-changing calls, re-read the target's name and
state first if any time has passed — an agent's context is not a lock.

**Does not apply when.** The identifier is client-chosen and unique by
construction.

## Derivation

The incident is recorded in this project's operating instructions: a guessed
next-number raced a concurrent create and released a different job. The rule
that followed pairs the prohibition with a positive practice — re-verify title
and state before acting.
