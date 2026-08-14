---
name: a-check-that-cannot-run-exits-distinctly
title: Cannot-run and passed must not print the same
scope: process
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - ".chug/tasks/check-doc-facts.sh — a check that cannot run exits 2 as a linter error, never as a clean tree"
  - ".chug/tasks/check-molt.sh — an unresolvable base exits 2, because 'nothing lost' and 'never looked' must not print the same"
  - "job #531 — two new passes opened files without the existence guard the rest of the script uses, so an input the script previously skipped aborted the whole run"
rationale: >
  The most quietly dangerous state a gate can be in. This project gives it a
  dedicated exit code and a distinct label, which is a small convention with an
  outsized effect on trust.
related: [every-gate-has-a-test-suite, refuse-loudly, announce-exactly-what-ran]
---

**Rule.** A check has three outcomes, not two: passed, failed, and could not
run. Could-not-run has its own exit code and its own label, and it is never
reported as a pass.

**Why.** Missing tooling, an unreadable input, an unresolvable base — each makes
a check vacuous. If vacuous prints green, the gate silently stops gating and
nobody notices, because green is what it always printed.

**How to apply.** Reserve an exit code for the linter-error case and check for
it explicitly at the call site. Degrade to a loud skip only where the check is
advisory, and say what was skipped. Guard every file open in a scanner the same
way the main loop does — a deleted path appears in a diff and has no content.

**Does not apply when.** The check is optional by design; even then, print the
skip.

## Derivation

Both of this project's whole-tree doc gates reserve exit 2 for unrunnable, and
the molt accounting gate states the reason directly: "nothing lost" and "never
looked" must not print the same. Job #531 found the failure mode from the other
side — an unguarded open under `set -eu` aborted the script with no finding line
at all.
