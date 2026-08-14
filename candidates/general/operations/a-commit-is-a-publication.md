---
type: Blessed Practice
title: "Treat a merge as publication, and know your disclosure boundary"
description: "Know how long it takes for a merge to become public, and treat the ignore rules that keep secrets out as a security control with its own review — not as housekeeping."
status: draft
tags:
  - bucket/general
  - scope/operations
  - altitude/high
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  When agents merge autonomously and a mirror publishes minutes later, the
  disclosure boundary has to be a property of the repository, not of a human's
  attention at review time.
---

**Rule.** Know how long it takes for a merge to become public, and treat the
ignore rules that keep secrets out as a security control with its own review —
not as housekeeping. A new tree containing anything sensitive adds its exclusion
before its first commit.

**Why.** With autonomous merges and an automated mirror there is no human step
between a mistake and its publication, and published content is cached and
indexed regardless of later deletion. The exclusion has to exist before the file
does.

**How to apply.** Write down which paths are excluded and why, next to the tree
they protect. Prefer excluding the secret and derived half of a directory over
excluding the directory — a blanket exclusion silently swallows every attempt to
add the legitimate half. Have reviewers check for artifacts that should never be
committed at all.

**Does not apply when.** The repository is genuinely private and stays that way
— which is a fact to verify with a date.

## Where this comes from

The source project mirrors to a public host every few minutes with no human
step between a merge and its publication, which turns the ignore rules into a
security control rather than housekeeping. One review caught a 1.8 MB binary
core dump committed alongside two legitimate fixes; the remedy was both halves
— remove the file, and add the exclusion so it cannot recur.

## Related

- [Destructive and outward-facing actions are confirmed, every time](destructive-actions-need-confirmation.md)
- [Prefer a loud refusal to a silent degradation](../architecture/refuse-loudly.md)
- [Thread identifiers from responses; never predict them](never-guess-resource-ids.md)
