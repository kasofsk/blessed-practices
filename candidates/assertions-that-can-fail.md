---
name: assertions-that-can-fail
title: Break it on purpose and watch the named case go red
scope: testing
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "job #505 — a regression test that was green against the pre-fix code, so it covered nothing the job fixed"
  - "job #276 — a test whose name and doc comment claimed a contract the code structurally cannot observe; it passes identically with the opposite input"
  - "job #298 — a guard rewritten because as written it could not fire"
rationale: >
  The most consistently valuable review technique in this corpus, and the one
  most often missing from the work it reviews. A test nobody has seen fail is
  not evidence.
related: [no-vacuous-assertions, boundaries-are-asserted-not-documented, lowest-tier-that-expresses-it]
---

**Rule.** Before you rely on a test or a guard, make it fail. Run it against the
code without the fix, or against a fixture that violates the property, and
confirm the named case goes red for the stated reason.

**Why.** Tests that cannot fail are written constantly and are indistinguishable
from working tests by every other means. They are worse than no test, because
they represent the property as covered.

**How to apply.** For a regression test, run it at the parent commit and record
that it fails. For a guard, construct the violating change. For a fixture suite,
include the negative case permanently, so a future refactor that defeats the
check is caught. State in the commit message that you did this.

**Does not apply when.** The assertion is a type-level guarantee the compiler
already enforces.

## Derivation

Job #505's finding is exact: the test's lookalike input did not contain the
substring the old code searched for, "so the old code already answered no before
this change" — the test was green before and after, and the surface it was
written for was covered by nothing.
