---
type: Blessed Practice
title: "A multi-leg operation reports every leg, including the ones it skipped"
description: "A multi-step operation emits a record for every step, always, including on failure: which succeeded, which failed with what error, and which were skipped because an earlier one failed."
status: draft
tags:
  - bucket/general
  - scope/operations
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Deploy reports here are unusually good, and they became good through two
  rework cycles that both concerned the failure path — the path where the report
  matters most and is most often dropped.
---

**Rule.** A multi-step operation emits a record for every step, always,
including on failure: which succeeded, which failed with what error, and which
were skipped because an earlier one failed. The failure path emits the report
first, not last.

**Why.** The report exists for the failure case. A structure that attaches the
report only to the success path produces nothing exactly when someone needs it,
and a reader cannot distinguish "did not run" from "ran and was not recorded".

**How to apply.** Pre-register the leg list so a failure in any leg still knows
what follows it. Attach the structured record on both the success and failure
branches of the exit handler. Test the case where the first leg fails and the
case where the reporting leg itself fails.

**Does not apply when.** The operation is a single step.

## Where this comes from

One change dropped the structured report on the non-zero-exit branch,
attaching it only on success — for an operation whose entire purpose was
capturing what happened. The follow-up found the residual: the skipped-step
loop was suppressed on exactly the path where the step that names the
remaining steps was itself the one that failed.

## Related

- [A dropped row reads like a negative result](../process/silent-filters-hide-rows.md)
- [Announce exactly what ran — never a tier you did not execute](../process/announce-exactly-what-ran.md)
- [Prefer a loud refusal to a silent degradation](../architecture/refuse-loudly.md)
