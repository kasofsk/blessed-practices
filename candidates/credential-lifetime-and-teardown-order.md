---
name: credential-lifetime-and-teardown-order
title: Credential teardown runs after every consumer, not before
scope: architecture
altitude: mid
portability: universal
confidence: medium
status: candidate
evidence:
  - "job #497 — a task wrapper deleted the whole credential tree at exit, and the agent's transcript lived inside it, so no host agent task could ever yield one"
  - "design #529 — a withdrawable credential source gives a window where an environment variable gives a lifetime"
rationale: >
  Two independent lessons about credential handling that both come down to
  ordering and scope: what is torn down, when, and what else happened to live
  inside the thing being deleted.
related: [capture-before-disposal, reachability-by-uid, restart-reconciliation-is-first-class]
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

## Derivation

Job #497's reviewer traced the whole chain: the agent's configuration directory
resolved under the credentials root, the wrapper removed that root before
writing the exit code, and the harvest runs strictly afterwards — so the
transcript "can never" be collected, while three sentences the same change added
claimed it could.
