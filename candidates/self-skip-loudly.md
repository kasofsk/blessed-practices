---
name: self-skip-loudly
title: A test that cannot run says so; it never passes vacuously
scope: testing
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #447 — two assertions self-skip through a helper that prints 'is NOT covered by this run' rather than passing silently"
  - "job #395 — a proof ladder whose summary contradicted itself on every failing run"
  - "docs/reference/testing.md — the skip guards are named macros, and a skip is free by construction"
rationale: >
  Environment-dependent tests are unavoidable in an orchestrator that touches
  containers, systemd and clouds. The discipline that makes them survivable is
  that a skip is visible, cheap, and distinguishable from a pass in the output.
related: [a-check-that-cannot-run-exits-distinctly, announce-exactly-what-ran, no-vacuous-assertions]
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

## Derivation

An unreachable container daemon once accounted for 55% of this suite's wall time
through per-call retry backoff, which is why the availability verdict is now a
permanent, process-wide answer given instantly. Job #447's helper is the shape
for the printing half.
