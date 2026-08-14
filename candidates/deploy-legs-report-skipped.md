---
name: deploy-legs-report-skipped
title: A multi-leg operation reports every leg, including the ones it skipped
scope: operations
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #187 — a failed deploy discarded its structured leg report, which is the case the ticket existed to capture"
  - "job #207 — the skipped-leg completeness gap: when the reporting leg itself failed, the tail legs were never emitted"
  - "The deploy records in this history show per-leg status including 'skipped' for every leg after a failure"
rationale: >
  Deploy reports here are unusually good, and they became good through two
  rework cycles that both concerned the failure path — the path where the report
  matters most and is most often dropped.
related: [announce-exactly-what-ran, refuse-loudly, silent-filters-hide-rows]
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

## Derivation

Job #187's finding: on the non-zero-exit branch the harvested report was
dropped, "only the success branch attaches it" — for a job type whose whole
purpose is capturing what happened. Job #207 then found the residual: the
skipped-leg loop was suppressed on exactly the path where the failing leg was
the one that names itself.
