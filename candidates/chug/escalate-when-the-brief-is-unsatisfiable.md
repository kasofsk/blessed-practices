---
type: Blessed Practice
title: "Escalate an unsatisfiable brief instead of reworking it"
description: "If the brief cannot be satisfied on this base — its premise is false, its scope excludes the change it requires, its target does not exist — say so and escalate."
status: draft
tags:
  - bucket/chug
  - scope/process
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
sources:
  - resource: https://github.com/kasofsk/chuggernaut
    title: "Chuggernaut — the platform this practice was derived from"
evidence:
  - "job #106 — a front-end-typed job that structurally required backend changes; the reviewer escalated rather than sending it back"
  - "job #419 — a brief whose premise did not hold against the branch's base; 'no rework on this base can fix this'"
  - "job #464 — the same shape: the text the brief asks to correct does not exist in this checkout"
rationale: >
  Rework loops on an unsatisfiable brief are the most wasteful failure in the
  corpus, and they are recognisable early. Three reviewers named the condition
  precisely and refused to loop; that judgement should be a stated licence, not
  an act of courage.
---

**Rule.** If the brief cannot be satisfied on this base — its premise is false,
its scope excludes the change it requires, its target does not exist — say so
and escalate. Do not send it back for a rework that cannot succeed.

**Why.** Every rework cycle on an unsatisfiable brief costs a full agent run and
ends in the same verdict. The only thing that changes it is a human editing the
ticket or a dependency landing.

**How to apply.** State the test you ran that shows unsatisfiability — the
missing symbol, the empty grep, the line numbers that do not exist — and say
what would have to change for the job to be workable. Distinguish "wrong base"
from "wrong ticket", because the remedies differ.

**Does not apply when.** The brief is merely hard, ambiguous or partly wrong —
then implement the satisfiable part under a stated assumption and report the
rest.

## Where this comes from

Job #419's verdict: "The brief's premise does not hold against this base ... The
change therefore appends a dated correction to prose that is not in the document,
citing symbols that are not in the repo — and no rework on this base can fix
that." The job was revoked rather than looped.

## Related

- [A rejection names the rule it rejects under](../general/process/verdict-names-the-rule.md)
- [Distinguish a stale base from a bad attempt](stale-base-is-not-an-authoring-failure.md)
- [The ticket is the contract, and both sides read it verbatim](the-ticket-is-the-contract.md)
