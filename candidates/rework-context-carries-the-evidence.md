---
name: rework-context-carries-the-evidence
title: The rework brief carries the evidence, not just the verdict
scope: process
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "job #154 — the failing gate stage's compiler output never reached the fix brief; the brief rendered literally as 'no structured findings'"
  - "job #160 — the rework that threaded the captured output into the brief"
rationale: >
  An agent asked to fix a failure it cannot see will guess. The fix was
  mechanical and the effect large, which is the profile of a practice worth
  making explicit rather than leaving to the harness.
related: [branch-preserved-across-rework, scope-the-rework-explicitly, errors-name-the-actionable-thing]
---

**Rule.** Whatever produced the failure — compiler output, test output, the
reviewer's findings with file and line — is included verbatim in the brief the
next attempt receives. A brief that says only "the gate failed" is a defect.

**Why.** The fixer's whole job is to act on the evidence. Withholding it turns a
targeted fix into a re-derivation, which costs a full cycle and often produces a
different change than the reviewer asked for.

**How to apply.** Capture a bounded tail of the failing command's output at the
moment of failure and store it on the record. Render it into the brief under a
heading. For agent verdicts, pass the structured findings through untouched —
file, line, issue, suggestion.

**Does not apply when.** The output is enormous and unstructured — then bound it
and say it was bounded, rather than dropping it.

## Derivation

Job #154's reviewer found that the failing stage's structured field was empty
for command gates, so the brief rendered "(no structured findings)" while the
inline comment at the same site claimed the compiler output reached the agent.
Job #160 threaded the captured tail through and embedded it under its own
heading.
