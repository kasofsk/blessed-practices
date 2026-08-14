---
type: Blessed Practice
title: "Thread identifiers from responses; never predict them"
description: "Take every server-assigned identifier from the response that created the resource."
status: draft
tags:
  - bucket/general
  - scope/operations
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  A one-line rule with a recorded incident behind it, and one that agents
  violate naturally because the next number is usually right.
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

## Where this comes from

A guessed next identifier raced a concurrent creation and acted on a different
resource than intended. The rule that followed pairs the prohibition with a
positive practice — take the identifier from the creating response, and re-
verify the target's name and state before a consequential mutation, because an
agent's context is not a lock.

## Related

- [Destructive and outward-facing actions are confirmed, every time](destructive-actions-need-confirmation.md)
- [Prefer a loud refusal to a silent degradation](../architecture/refuse-loudly.md)
- [Treat a merge as publication, and know your disclosure boundary](a-commit-is-a-publication.md)
