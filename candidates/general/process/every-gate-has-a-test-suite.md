---
type: Blessed Practice
title: "A gate is code, so it has tests, and the tests are discovered"
description: "Every gate script has a test suite that drives the real script against fixtures, including at least one case that must fail."
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
  The gates are the CI here, so an untested gate is untested CI. Discovery by
  glob rather than by list is the detail that makes this survive: nothing to
  register, and an empty match fails rather than passing quietly.
---

**Rule.** Every gate script has a test suite that drives the real script against
fixtures, including at least one case that must fail. Suites are discovered by
pattern, not by a list, and a pattern matching nothing fails the stage.

**Why.** A gate that cannot fail is the most expensive artifact in the system —
it consumes time on every change and provides false assurance. Fixtures are the
only way to prove it can, since by construction the tree is supposed to be
clean.

**How to apply.** Build fixtures in a throwaway working directory so the suite
never depends on the tree's current state. Include the negative case, the
cannot-run case, and the case that regressed once. Cap each suite and the total,
and name what was not run when a cap is hit.

**Does not apply when.** The gate is a thin invocation of a third-party tool
whose behaviour you are not asserting — then test the wiring, not the tool.

## Where this comes from

Discovery by pattern rather than by a maintained list landed with a recursion
guard that the fixture suite asserts on itself, so every green run re-proves
it. The change also surfaced a sibling suite that had been failing since an
earlier change and was writing a stray archive into the working tree on every
run — undetected because nothing had been executing it.

## Related

- [Break it on purpose and watch the named case go red](../testing/assertions-that-can-fail.md)
- [Cannot-run and passed must not print the same](a-check-that-cannot-run-exits-distinctly.md)
- [Order gates cheapest-first and diff-aware](gates-are-cheap-first.md)
