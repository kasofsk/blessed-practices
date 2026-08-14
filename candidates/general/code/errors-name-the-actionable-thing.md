---
type: Blessed Practice
title: "An error names one cause and one action, and only when it is that cause"
description: "An error message names the cause it actually detected and the action that follows from it."
status: draft
tags:
  - bucket/general
  - scope/code
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Misattributed error messages are worse than vague ones: they send the operator
  to a specific wrong action with confidence. Three jobs found this in three
  different subsystems.
---

**Rule.** An error message names the cause it actually detected and the action
that follows from it. Do not attach a specific diagnosis to a general failure
branch.

**Why.** Operators act on the message. A message that names a specific remedy
for a failure that had a different cause costs a wrong action plus the time to
discover it was wrong — and it does so most often during routine events like a
rolling deploy, where the general branch is busiest.

**How to apply.** Discriminate the causes before composing the message.
Where you cannot, say what you observed rather than what you infer. Reserve the
highest log level for messages that name a specific human action, and make sure
that level is only reachable on that cause.

**Does not apply when.** There genuinely is only one cause — prove it by
enumerating the error type's variants.

## Where this comes from

A transport error and an older peer's unknown-operation reply funnel into the
same error variant, and the message attached to that variant named one
specific remedy. So during a rolling update every task on the affected machine
logged a confidently wrong instruction, at the log level reserved for messages
naming a human action.

## Related

- [A dropped row reads like a negative result](../process/silent-filters-hide-rows.md)
- [An exit status is not an existence oracle](do-not-use-exit-status-as-an-oracle.md)
- [Prefer a loud refusal to a silent degradation](../architecture/refuse-loudly.md)
