---
name: destructive-actions-need-confirmation
title: Destructive and outward-facing actions are confirmed, every time
scope: operations
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "Project instructions: do not run destructive commands — deploys, restarts, data resets — without asking first"
  - "The operating skill: revoking kills running containers; confirm first"
  - "Releasing a deploy job restarts the supervisor that supervises it, by design"
rationale: >
  Standing policy in this project, and worth stating as a practice because the
  boundary is not obvious in a self-hosting system: the deploy restarts the
  thing running the deploy.
related: [never-guess-resource-ids, a-commit-is-a-publication, validate-before-you-mutate]
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

## Derivation

The non-obvious cases here are instructive: revoking a job kills its running
containers, and releasing a deploy job restarts the dispatcher supervising that
very job. Both are documented as confirm-first for that reason.
