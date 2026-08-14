---
name: errors-name-the-actionable-thing
title: An error names one cause and one action, and only when it is that cause
scope: code
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #381 — an error message asserting the over-band cause for every failure, including a routine version-skew transport miss"
  - "job #493 — an operator instruction naming a target that matches nothing"
  - "job #475 cycle 2 — an exit status used as an existence oracle, so one status was reported as three distinct facts"
rationale: >
  Misattributed error messages are worse than vague ones: they send the operator
  to a specific wrong action with confidence. Three jobs found this in three
  different subsystems.
related: [refuse-loudly, silent-filters-hide-rows, do-not-use-exit-status-as-an-oracle]
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

## Derivation

Job #381's reviewer traced how a transport error and an unknown-operation reply
from an older node both funnel into the same variant, so during "the
mixed-version deploy window your own commit message anticipates", every task on
that node logged an instruction to move the output to a bucket.
