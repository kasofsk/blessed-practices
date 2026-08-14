---
type: Blessed Practice
title: "Break it on purpose and watch the named case go red"
description: "Before you rely on a test or a guard, make it fail."
status: draft
tags:
  - bucket/general
  - scope/testing
  - altitude/high
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  The most consistently valuable review technique in this corpus, and the one
  most often missing from the work it reviews. A test nobody has seen fail is
  not evidence.
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

## Where this comes from

A regression test was written for a fix and was green against the unfixed
code, because the input it used did not actually contain the pattern the old
code searched for — so the surface the change was named after ended up covered
by nothing. Two other instances in the same corpus: a guard that could not
fire for any realistic violating change, and a test asserting a contract the
function under test never reads.

## Related

- [A test must be able to observe what its name claims](no-vacuous-assertions.md)
- [An architectural boundary that nothing checks is a comment](../architecture/boundaries-are-asserted-not-documented.md)
- [New behaviour lands with a test at the lowest tier that can express it](lowest-tier-that-expresses-it.md)
