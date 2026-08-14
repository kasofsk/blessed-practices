---
type: Blessed Practice
title: "Validate everything first, then mutate"
description: "A procedure that mutates external state does all of its checking first, in one block, before the first mutation."
status: draft
tags:
  - bucket/general
  - scope/architecture
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Half-applied changes to a running node were the most expensive operational
  failures in this history. The fix was structural and repeatable: everything
  that can refuse, refuses before anything that can break.
---

**Rule.** A procedure that mutates external state does all of its checking
first, in one block, before the first mutation. Every refusal names the value
it refused and exits non-zero.

**Why.** A procedure that interleaves checks and mutations has as many partial
states as it has steps, and each one is a distinct recovery problem for whoever
finds the machine that way. Validate-first collapses them to two: untouched, or
completed.

**How to apply.** Hoist every existence check, every parse, every credential
check and every capacity check above the first destructive call. Where a check
needs a value only the mutation produces, that is a signal to split the
procedure, not to interleave. State in the header that the block is
validate-first so a later author does not append a check below the line.

**Does not apply when.** A check is genuinely only answerable mid-flight — then
make the mid-flight failure explicitly recoverable and say what state it leaves.

## Where this comes from

Half-applied changes to live machines were the most expensive operational
failures in the source retrospective, and the fix was structural rather than
per-incident: every check that can refuse was hoisted above the first
destructive call. Reviewers afterwards treated placement relative to that
block as the acceptance criterion — not whether the check existed, but whether
it ran before anything could break.

## Related

- [A multi-leg operation reports every leg, including the ones it skipped](../operations/deploy-legs-report-skipped.md)
- [Build aside, then swap atomically](stage-then-swap.md)
- [Prefer a loud refusal to a silent degradation](refuse-loudly.md)
