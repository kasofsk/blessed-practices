---
type: Blessed Practice
title: "The rework brief carries the evidence, not just the verdict"
description: "Whatever produced the failure — compiler output, test output, the reviewer's findings with file and line — is included verbatim in the brief the next attempt receives."
status: draft
tags:
  - bucket/chug
  - scope/process
  - altitude/high
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
sources:
  - resource: https://github.com/kasofsk/chuggernaut
    title: "Chuggernaut — the platform this practice was derived from"
evidence:
  - "job #154 — the failing gate stage's compiler output never reached the fix brief; the brief rendered literally as 'no structured findings'"
  - "job #160 — the rework that threaded the captured output into the brief"
rationale: >
  An agent asked to fix a failure it cannot see will guess. The fix was
  mechanical and the effect large, which is the profile of a practice worth
  making explicit rather than leaving to the harness.
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

## Where this comes from

Job #154's reviewer found that the failing stage's structured field was empty
for command gates, so the brief rendered "(no structured findings)" while the
inline comment at the same site claimed the compiler output reached the agent.
Job #160 threaded the captured tail through and embedded it under its own
heading.

## Related

- [A verdict says what to change and what not to touch](scope-the-rework-explicitly.md)
- [An error names one cause and one action, and only when it is that cause](../general/code/errors-name-the-actionable-thing.md)
- [Rework builds on the previous attempt; it does not restart it](branch-preserved-across-rework.md)
