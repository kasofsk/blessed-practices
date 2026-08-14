---
type: Blessed Practice
title: "Credential teardown runs after every consumer, not before"
description: "Scope credential material to its own directory, never one shared with artifacts you need afterwards, and order teardown after every consumer — including harvest."
status: draft
tags:
  - bucket/general
  - scope/architecture
  - altitude/mid
  - portability/universal
  - confidence/medium
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Two independent lessons about credential handling that both come down to
  ordering and scope: what is torn down, when, and what else happened to live
  inside the thing being deleted.
---

**Rule.** Scope credential material to its own directory, never one shared with
artifacts you need afterwards, and order teardown after every consumer —
including harvest. Prefer a withdrawable delivery over an inherited environment
variable.

**Why.** Teardown that deletes a shared parent silently destroys anything else
under it, and the loss looks like a feature that never worked rather than a
cleanup bug. And a credential in the environment has a lifetime; a credential
delivered on a descriptor that is then closed has a window.

**How to apply.** Give credentials their own path and delete exactly that path.
Put teardown after the harvest step in the same wrapper, and test that an
artifact written beside the credentials survives. When choosing a delivery
mechanism, prefer the one whose exposure ends at a point you control, and state
what a determined task could still read.

**Does not apply when.** Nothing else is written under the credential path and
nothing needs to outlive the task.

## Where this comes from

A task wrapper deleted its whole credential tree at exit, and the agent's
configuration directory — including the transcript the harvest collects
afterwards — resolved underneath it. So that class of task could never produce
a transcript, while three sentences the same change added claimed it could.
The delivery half comes from a separate design: a credential inherited through
the environment has a lifetime, one delivered on a descriptor that is then
closed has a window.

## Related

- [Every in-flight state has a restart arm](restart-reconciliation-is-first-class.md)
- [Harvest before you reclaim, and never fail a job on cleanup](capture-before-disposal.md)
- [What a process is told is not what its uid may open](reachability-by-uid.md)
