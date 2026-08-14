---
type: Blessed Practice
title: "Cannot-run and passed must not print the same"
description: "A check has three outcomes, not two: passed, failed, and could not run."
status: draft
tags:
  - bucket/general
  - scope/process
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  The most quietly dangerous state a gate can be in. This project gives it a
  dedicated exit code and a distinct label, which is a small convention with an
  outsized effect on trust.
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

## Where this comes from

Both whole-tree checkers in the source project reserve a distinct exit code
for "could not run", and the accounting checker states the reason directly:
nothing lost and never looked must not print the same. The complementary
failure came from a change whose new scanning passes opened files without the
existence guard the rest of the script used, aborting the whole run with no
finding line at all.

## Related

- [A gate is code, so it has tests, and the tests are discovered](every-gate-has-a-test-suite.md)
- [Announce exactly what ran — never a tier you did not execute](announce-exactly-what-ran.md)
- [Prefer a loud refusal to a silent degradation](../architecture/refuse-loudly.md)
