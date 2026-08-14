---
type: Blessed Practice
title: "An exit status is not an existence oracle"
description: "Do not infer existence, absence or identity from a command's exit status unless the command documents that mapping."
status: draft
tags:
  - bucket/general
  - scope/code
  - altitude/low
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  A small, sharp instance of a general problem: inferring a fact from a tool's
  exit code without checking what that tool's exit code means. The stub-testing
  half is the more interesting lesson.
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

## Where this comes from

A forced removal exits zero whether or not the target existed, and also when
the daemon it talks to is unreachable, so one status was read as three
distinct facts — including the dangerous one, where the removal silently did
nothing and the caller announced success. The suite could not catch it,
because the stub's exit statuses encoded the author's assumption rather than
the real tool's behaviour.

## Related

- [A tool's outcome measures the tool, not your claim](../testing/a-tool-outcome-measures-the-tool.md)
- [An error names one cause and one action, and only when it is that cause](errors-name-the-actionable-thing.md)
- [Test the premise, not only the behaviour](../testing/test-the-premise.md)
