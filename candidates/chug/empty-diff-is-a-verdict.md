---
type: Blessed Practice
title: "An empty diff is a first-class finding, verified not assumed"
description: "A review's first step is to establish the diff and confirm it is non-empty."
status: draft
tags:
  - bucket/chug
  - scope/process
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
sources:
  - resource: https://github.com/kasofsk/chuggernaut
    title: "Chuggernaut — the platform this practice was derived from"
evidence:
  - "jobs #54, #79, #106, #289, #464 — branches byte-identical to their base, each caught by a reviewer that checked rather than assumed"
  - "job #79 — the reviewer verified via diff, stash list, reflog, fsck and all refs before concluding"
rationale: >
  Five jobs produced no change at all. Every one was caught, and caught the same
  way: the reviewer's first act was to establish what the diff actually is,
  exhaustively, before reading anything.
---

**Rule.** A review's first step is to establish the diff and confirm it is
non-empty. "No change was made" is a complete, reportable verdict, and it is
established by evidence, not by absence of evidence.

**Why.** An implementer that produced nothing will still write a summary
describing what it intended. A reviewer that reads the summary and then looks
for the code will find the pre-existing code and may accept it.

**How to apply.** Compare against the merge base, then confirm with the working
tree state, the stash, the reflog and the ref set — an agent can leave work
uncommitted, on a detached head, or on the wrong branch. Report which checks you
ran. Then point at the exact code that still needs to change.

**Does not apply when.** The job's product is genuinely not a diff (a
measurement, an approval) — then say what the product is and check for that.

## Where this comes from

Job #79's verdict enumerates the checks by name and then states the current code
still lacks each deliverable, with file and field. That combination — the diff
is empty, and here is the unchanged code — is what makes the verdict actionable
rather than accusatory.

## Related

- [Distinguish a stale base from a bad attempt](stale-base-is-not-an-authoring-failure.md)
- [Report verification as commands and outputs, not as adjectives](../general/process/verification-is-reported-with-its-command.md)
- [Reviewers read; gates run](reviewers-read-they-do-not-run.md)
