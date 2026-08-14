---
name: one-decision-site
title: One decision site per question
scope: architecture
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #522 — admits() is the single decision site for a grant"
  - "job #298 — a helper deduped a three-case resolution so the launch path and the reported snapshot could not disagree"
  - "job #137 — a config snapshot refreshed two fields of three, so the UI and the scheduler disagreed about a node"
rationale: >
  Divergence between a decision and its report is a distinct bug class here: the
  system does the right thing and tells the operator something else. One
  decision site, consumed by both, removes it structurally.
related: [single-writer-per-record, one-resolver-per-question, pure-decider-effects]
---

**Rule.** Each policy question is answered by exactly one function. Everything
that acts on the answer, and everything that displays the answer, calls it.

**Why.** When the actor and the reporter compute the same thing separately, they
drift, and the drift is invisible until an operator debugs against the report.
The report then actively misleads, which is worse than having no report.

**How to apply.** Extract the predicate before you have two callers, not after.
When adding a display of an existing behaviour, wire the display to the
behaviour's own function rather than reconstructing it from inputs.

**Does not apply when.** The display is deliberately a different question (an
intent versus an observation) — in which case label both, per
separate-intent-from-observation.

## Derivation

Job #137's finding: a config snapshot refreshed availability and version from
live state but not slot count, so the fleet status and the settings page
disagreed about a node until the next restart. Job #298 fixed the same shape
prospectively by deduplicating the resolution so "place() and the snapshot
cannot disagree".
