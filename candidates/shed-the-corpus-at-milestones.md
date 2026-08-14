---
name: shed-the-corpus-at-milestones
title: A knowledge corpus needs a shedding process, not only an appending one
scope: documentation
altitude: high
portability: universal
confidence: medium
status: candidate
evidence:
  - "design #533 — one job type whose product is removing true sentences at a milestone"
  - "job #576 — the first shed, seven rework cycles, four wrongly-shed sentences restored"
  - "The doc corpus reached roughly 30,000 lines across 70 tracked files before the first shed"
rationale: >
  Every other practice here adds text. Without a counterweight the corpus grows
  until nobody reads it, at which point its accuracy stops mattering. This is
  the only mechanism in the corpus designed to remove knowledge deliberately.
related: [mutable-head-append-only-body, deletion-needs-accounting, growth-is-measured-not-felt]
---

**Rule.** Periodically and deliberately remove knowledge that has stopped
earning its place: heads compacted, fully-implemented designs deleted outright,
every referrer repointed or stubbed. Shedding is a distinct kind of work with
its own review, not a side effect of other jobs.

**Why.** An append-only corpus grows without bound, and the practical failure is
not wrongness but unreadability — the reader stops reading, so the accuracy
nobody is checking stops mattering. Removal must be a first-class operation or
it never happens.

**How to apply.** Trigger on a milestone, not a threshold. Licence deletion
narrowly: only artefacts whose status says they are fully implemented, so the
knowledge is in the code. Repoint or stub every reference. Keep the rejected
alternatives — they are the part that cannot be re-derived.

**Does not apply when.** The corpus is small enough that nobody skips it.

## Derivation

The first shed took seven rework cycles, and its most instructive cycle restored
four sentences that earlier passes had removed: provenance and authorship
statements that "named no mechanism and described no behaviour", so every
mechanical gate was green while they were missing. That is the failure mode the
design predicted, observed on the first run.
