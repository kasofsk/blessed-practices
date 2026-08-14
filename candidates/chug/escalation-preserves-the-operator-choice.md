---
type: Blessed Practice
title: "An escalation preserves the operator's distinct choices"
description: "Reusing existing machinery to implement an operator choice is fine; collapsing two distinct operator intents into one is not."
status: draft
tags:
  - bucket/chug
  - scope/process
  - altitude/mid
  - portability/project
  - confidence/medium
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
sources:
  - resource: https://github.com/kasofsk/chuggernaut
    title: "Chuggernaut — the platform this practice was derived from"
evidence:
  - "job #197 — a third next-step option dropped from an operator-facing control; the reviewer's finding was that reusing the machinery was authorised, removing the choice was not"
  - "Escalation reasons are distinct strings so the timeline distinguishes an intentional hold from a failure"
rationale: >
  Automation that reduces the operator's option set is a specific and common
  regression, and it is easy to justify internally as simplification. The
  distinction between reusing mechanism and removing intent is the useful part.
---

**Rule.** Reusing existing machinery to implement an operator choice is fine;
collapsing two distinct operator intents into one is not. Each intent keeps its
own name and its own record on the timeline.

**Why.** Operators reason from the timeline. "Held pending a configuration fix"
and "escalated because it failed" produce the same state but call for opposite
actions, and once they share a label nobody can reconstruct which happened.

**How to apply.** Keep the state machine small by reusing states, and keep the
vocabulary rich by giving each intent its own reason string and label. When a
brief authorises reuse of machinery, read it as permission about the mechanism,
not about the interface.

**Does not apply when.** The two intents genuinely lead to the same operator
action.

## Where this comes from

Job #197's reviewer separated the two readings precisely: the brief's latitude
clause "authorizes reusing the Escalated state machinery, NOT removing the
operator-facing choice", and named the distinct purpose the dropped option had —
fix the configuration, then let automation retry.

## Related

- [Prefer a loud refusal to a silent degradation](../general/architecture/refuse-loudly.md)
- [Record every deviation from the brief, with its reason](../general/process/deviation-is-recorded-not-silent.md)
- [Reserve human approval for what no gate and no reader can judge](human-approval-only-where-no-gate-can-judge.md)
