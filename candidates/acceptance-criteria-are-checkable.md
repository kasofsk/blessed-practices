---
name: acceptance-criteria-are-checkable
title: Acceptance criteria name an observation, not an intention
scope: process
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "jobs #449, #453, #469, #495 — rejections where the acceptance criterion was 'CI green' and CI was never run on the branch until the final cycle"
  - "job #395 — a summary that contradicted itself on every failing run, rejected against a criterion about the summary"
rationale: >
  Criteria phrased as intentions are unfalsifiable and are routinely reported as
  met. Criteria phrased as observations force the implementer to produce the
  observation, which is most of the value.
related: [the-ticket-is-the-contract, verification-is-reported-with-its-command, assertions-that-can-fail]
---

**Rule.** Every acceptance criterion is a specific observation someone can make:
a command and its expected output, a file that must not exist, a string that
must not appear in the tree. "Works correctly" and "is documented" are not
criteria.

**Why.** An unobservable criterion is satisfied by assertion. The implementer
writes "done", the reviewer cannot cheaply refute it, and the failure surfaces
later at much higher cost.

**How to apply.** Prefer criteria you can express as a grep or a command exit.
Where the criterion is a negative ("nothing in the tree still says X"), give the
search. Where it is a measurement, give the command that produces the number.

**Does not apply when.** The judgement is genuinely human (is this argument
honest, is this doc readable) — then say that a human decides it, and route it
to one.

## Derivation

Several late jobs carried "CI green" as a criterion and failed on it repeatedly
because the branch's earlier cycles never reached the stage that runs CI. The
lesson the reviewers drew is in the criterion's phrasing: name the stage and the
command, so the implementer knows the observation has to be produced, not
predicted.
