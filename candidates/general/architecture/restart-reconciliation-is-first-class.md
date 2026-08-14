---
type: Blessed Practice
title: "Every in-flight state has a restart arm"
description: "Adding a state a task can be in while a process is alive obliges you to add its recovery arm in the same change: what the process does with a record found in that state at startup, and a test that restarts mid-state."
status: draft
tags:
  - bucket/general
  - scope/architecture
  - altitude/high
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Restart is not an edge case in a long-running orchestrator that redeploys
  itself; it is a routine event. Three separate jobs shipped a new in-flight
  state and forgot its recovery arm, each time reintroducing the bug the feature
  existed to prevent.
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

## Where this comes from

Three separate changes added a new in-flight state and omitted its recovery
arm, each time reintroducing the bug the feature existed to prevent. In the
clearest, a restart during a post-completion step skipped that step entirely
and finished the work as successful, while the orphaned record stayed in a
running state forever — which then poisoned every sweep that treats running as
live.

## Related

- [A re-queued item keeps its original clock](a-queue-entry-keeps-its-clock.md)
- [Everything is bounded, and the bound is loud](bounded-and-loud.md)
- [One writer per record class](single-writer-per-record.md)
