---
name: a-commit-is-a-publication
title: Treat a merge as publication, and know your disclosure boundary
scope: operations
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "This repo mirrors to a public host every five minutes with no review step between merge and publication"
  - "The ignore rules for the infrastructure tree are documented as a disclosure boundary rather than tidiness"
  - "job #50 — a binary core dump accidentally committed and caught only by a reading reviewer"
rationale: >
  When agents merge autonomously and a mirror publishes minutes later, the
  disclosure boundary has to be a property of the repository, not of a human's
  attention at review time.
related: [never-guess-resource-ids, destructive-actions-need-confirmation, refuse-loudly]
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

## Derivation

Job #50 found a 1.8 MB binary core dump committed alongside two legitimate test
fixes. The reviewer's remedy was both halves: remove the file, and add the
ignore rule "so it can't recur" — the exclusion arriving with the incident
rather than before it.
