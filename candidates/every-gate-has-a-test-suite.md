---
name: every-gate-has-a-test-suite
title: A gate is code, so it has tests, and the tests are discovered
scope: process
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "The repo carries 28 shell suites for its own gates, discovered by glob so adding one needs no registration"
  - "job #385 — the discovery landed with a recursion guard the fixture suite asserts on itself, and found a sibling suite that had been red since an earlier job"
  - "job #433, #531 — gate changes rejected because the gate's own suite did not pin the new behaviour"
rationale: >
  The gates are the CI here, so an untested gate is untested CI. Discovery by
  glob rather than by list is the detail that makes this survive: nothing to
  register, and an empty match fails rather than passing quietly.
related: [gates-are-cheap-first, assertions-that-can-fail, a-check-that-cannot-run-exits-distinctly]
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

## Derivation

Job #385 added glob discovery with "the empty-match case failing rather than
passing quietly", handed each suite a recursion guard the fixture suite asserts
on itself, and in the process found a sibling suite that had been red since an
earlier job and was writing a stray artifact into the checkout on every run.
