---
name: do-not-use-exit-status-as-an-oracle
title: An exit status is not an existence oracle
scope: code
altitude: low
portability: universal
confidence: high
status: candidate
evidence:
  - "job #475 cycle 2 — a forced removal exits zero whether or not the target existed, and also when the daemon is unreachable, so one status was treated as three facts"
  - "job #475 cycle 2 — the suite could not catch it because its stub's exit statuses were the assumption rather than the real tool's behaviour"
rationale: >
  A small, sharp instance of a general problem: inferring a fact from a tool's
  exit code without checking what that tool's exit code means. The stub-testing
  half is the more interesting lesson.
related: [errors-name-the-actionable-thing, test-the-premise, a-tool-outcome-measures-the-tool]
---

**Rule.** Do not infer existence, absence or identity from a command's exit
status unless the command documents that mapping. Query the state explicitly,
and treat "could not determine" as its own outcome.

**Why.** Tools collapse many outcomes into zero, especially under force flags.
The dangerous case is not the false positive but the unreachable-dependency
case, where the operation silently did nothing and the caller announces success.

**How to apply.** Query, then act, then verify. Where a tool offers a distinct
query, use it. When testing against a stub, make the stub reproduce the real
tool's status mapping — otherwise the suite pins your assumption, not the
behaviour.

**Does not apply when.** The tool's contract explicitly gives the mapping.

## Derivation

Job #475's reviewer names all three conflated facts and the reason the suite was
blind: "its stub's exit statuses are the assumption rather than docker's
behaviour", so the test proved the code consistent with itself.
