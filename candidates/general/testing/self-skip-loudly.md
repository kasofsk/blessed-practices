---
type: Blessed Practice
title: "A test that cannot run says so; it never passes vacuously"
description: "A test that cannot run in this environment prints that it did not run, naming what was missing."
status: draft
tags:
  - bucket/general
  - scope/testing
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Environment-dependent tests are unavoidable in an orchestrator that touches
  containers, systemd and clouds. The discipline that makes them survivable is
  that a skip is visible, cheap, and distinguishable from a pass in the output.
---

**Rule.** A test that cannot run in this environment prints that it did not run,
naming what was missing. It never returns green silently, and it never costs
more than a fast probe to decide.

**Why.** A silent skip makes a green run indistinguishable from a covered run,
so coverage claims drift upward with no change in reality. And an expensive skip
— retrying an unreachable dependency per test — can dominate suite time without
providing anything.

**How to apply.** Route every environment gate through one named helper that
prints. Answer the availability question once, process-wide, and cache the
verdict. Make the summary line count skips separately from passes, so a run that
skipped half its cases cannot report as a full run.

**Does not apply when.** The dependency is universally available in every
environment the suite runs in.

## Where this comes from

An unreachable dependency once accounted for 55% of a test suite's wall time,
through per-call retry backoff on a question whose answer could not change;
the verdict is now a permanent, process-wide answer given instantly. The
printing half came from a helper that states "is not covered by this run"
rather than returning green in silence.

## Related

- [A test must be able to observe what its name claims](no-vacuous-assertions.md)
- [Announce exactly what ran — never a tier you did not execute](../process/announce-exactly-what-ran.md)
- [Cannot-run and passed must not print the same](../process/a-check-that-cannot-run-exits-distinctly.md)
