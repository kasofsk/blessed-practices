---
type: Blessed Practice
title: "Destructive and outward-facing actions are confirmed, every time"
description: "Ask before anything destructive or outward-facing: deploys, restarts, revocations, data resets, anything that sends content off the machine."
status: draft
tags:
  - bucket/general
  - scope/operations
  - altitude/high
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Standing policy in this project, and worth stating as a practice because the
  boundary is not obvious in a self-hosting system: the deploy restarts the
  thing running the deploy.
---

**Rule.** Ask before anything destructive or outward-facing: deploys, restarts,
revocations, data resets, anything that sends content off the machine. Approval
for one action does not extend to the next.

**Why.** Automation's value comes from acting without asking; its risk is
concentrated in a small set of actions that are hard to reverse. Separating them
explicitly keeps the rest of the loop fast.

**How to apply.** Enumerate the destructive verbs for your system, including the
non-obvious ones, and require confirmation at those call sites. State the
blast radius in the confirmation — what will be killed, what will restart, who
will see it. Prefer a reversible variant where one exists.

**Does not apply when.** The user has given durable, explicit authorisation for
the specific class of action.

## Where this comes from

The non-obvious cases are the instructive ones. In the source system,
terminating a unit of work kills its running containers, and triggering a
deploy restarts the very supervisor that is running the deploy. Both are
documented as confirm-first for that reason, which is the general lesson: the
destructive verbs are not always the ones that sound destructive.

## Related

- [Thread identifiers from responses; never predict them](never-guess-resource-ids.md)
- [Treat a merge as publication, and know your disclosure boundary](a-commit-is-a-publication.md)
- [Validate everything first, then mutate](../architecture/validate-before-you-mutate.md)
