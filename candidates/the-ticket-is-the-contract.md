---
name: the-ticket-is-the-contract
title: The ticket is the contract, and both sides read it verbatim
scope: process
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "The job description is injected verbatim into both the work prompt and the evaluation prompt"
  - "jobs #135, #197, #207 — rejections whose entire content is 'requirement N of the brief is unimplemented'"
  - "job #106 — a job typed for the front end that structurally required backend changes; the reviewer escalated rather than reworked"
rationale: >
  Roughly a third of all rejections in this corpus are 'the brief said X and X
  is missing'. That is not an agent-quality problem; it is a contract problem
  that the ticket format can largely solve.
related: [acceptance-criteria-are-checkable, deviation-is-recorded-not-silent, escalate-when-the-brief-is-unsatisfiable]
---

**Rule.** Write the ticket as the contract both the implementer and the
reviewer are held to. Enumerate deliverables so they can be checked off
individually, state what is out of scope, and give the acceptance criteria in
the form the reviewer will verify them.

**Why.** When the same text drives the work and the review, ambiguity costs a
whole rework cycle: the implementer reads latitude where the reviewer reads a
requirement. Numbered deliverables convert that argument into a checklist.

**How to apply.** One numbered list of required changes; one list of what not to
build; acceptance criteria phrased as observable facts ("the suite passes with
Docker absent", "no doc still asserts X"). Name the files you expect to change
when you know them, and say when the list is not exhaustive.

**Does not apply when.** The job is genuinely exploratory — then say so, and make
the deliverable a document, not a change.

## Derivation

Job #197's rejection is representative: the brief required three next-step
values, the implementation shipped two, and the reviewer rejected on the ground
that the brief's latitude clause "authorizes reusing the machinery, NOT removing
the operator-facing choice". The disagreement is entirely about what the ticket
licensed.
