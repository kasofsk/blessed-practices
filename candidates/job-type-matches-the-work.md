---
name: job-type-matches-the-work
title: The unit of work carries the type its change actually needs
scope: process
altitude: mid
portability: project
confidence: medium
status: candidate
evidence:
  - "job #106 — a front-end-typed job whose feature structurally required backend fields; escalated rather than reworked"
  - "job #289 — a front-end job whose correct implementation needed data the list payload does not carry"
  - "Job types differ in their reviewers, their gates, their permission profile and their prompts"
rationale: >
  Typing determines which reviewers, gates and prompts a change meets. A
  mistyped job is not a labelling problem — it is a change reviewed by the wrong
  criteria, or one that cannot be completed within its own scope rules.
related: [the-ticket-is-the-contract, escalate-when-the-brief-is-unsatisfiable, mechanise-the-checkable-half]
---

**Rule.** Type the unit of work by what the change actually requires, not by
where the visible symptom is. If the required change crosses the type's scope
boundary, re-type or split before starting.

**Why.** Each type carries its own reviewers and gates; a change reviewed under
the wrong ones is either under-checked or blocked by rules that do not fit it.
And a scoped type whose deliverable needs out-of-scope changes cannot be
satisfied at all.

**How to apply.** Before releasing, ask what data or capability the deliverable
needs and where it lives. When a reviewer finds the mismatch, escalate rather
than rework — the fix is a new ticket, not a new attempt.

**Does not apply when.** The types are cosmetic and carry the same criteria.

## Derivation

Job #106's reviewer established that no front-end-only path existed, because the
payload the page receives carries no such field, and escalated on that ground.
Job #289 shows the near-miss version: a front-end-only implementation was
possible, and it cost two hundred extra requests per view to get the data.
