---
name: validate-before-you-mutate
title: Validate everything first, then mutate
scope: architecture
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #183 — the worker self-refresh was made validate-first so a failed refresh could no longer strand a node with no images"
  - "job #250 — a disk pre-flight was placed inside the validate-first block, before the fetch and before any container call"
  - "job #476 — node facts probed and refused before the first image build"
rationale: >
  Half-applied changes to a running node were the most expensive operational
  failures in this history. The fix was structural and repeatable: everything
  that can refuse, refuses before anything that can break.
related: [stage-then-swap, refuse-loudly, deploy-legs-report-skipped]
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

## Derivation

Job #183 rewrote the node refresh so the git URL and key file were required
before any container mutation, and job #250 added a disk pre-flight "inside the
validate-first block (before the fetch and before any docker call)". The
reviewer treated placement relative to that block as the acceptance criterion,
not the check itself.
