---
name: restart-reconciliation-is-first-class
title: Every in-flight state has a restart arm
scope: architecture
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "job #44 cycle 3 — a restart during the post-merge command silently skipped it and completed the job"
  - "job #150 cycle 4 — restart discarded launch priority"
  - "job #298 cycle 2 — an on-announce reconcile ran before the roster it consults was updated"
rationale: >
  Restart is not an edge case in a long-running orchestrator that redeploys
  itself; it is a routine event. Three separate jobs shipped a new in-flight
  state and forgot its recovery arm, each time reintroducing the bug the feature
  existed to prevent.
related: [bounded-and-loud, a-queue-entry-keeps-its-clock, single-writer-per-record]
---

**Rule.** Adding a state a task can be in while a process is alive obliges you to
add its recovery arm in the same change: what the process does with a record
found in that state at startup, and a test that restarts mid-state.

**Why.** Anything in flight at restart is either resumed, re-run, or lost. If
nobody decided which, the answer is "lost, silently, and the record stays
Running forever" — which then poisons every sweep that treats Running as live.

**How to apply.** Enumerate the non-terminal states in the recovery routine and
require a match arm per state, with no wildcard, so a new state fails to
compile. Order reconciliation so state is rebuilt before anything reads it.
Write the restart test at the tier that can actually restart the component.

**Does not apply when.** The state is durable by construction and its resumption
is the storage layer's problem, not yours — say so explicitly rather than
leaving it unstated.

## Derivation

Job #44's reviewer: the recovery routine failed one kind of running task and
left the sibling untouched, so on any restart mid-hook the hook "never re-runs
and the job goes straight to Done", with an orphaned Running task preserved
forever by the sweep that treats Running containers as live.
