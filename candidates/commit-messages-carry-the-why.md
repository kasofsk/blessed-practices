---
name: commit-messages-carry-the-why
title: The commit message carries the why
scope: documentation
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/style.md Tier 2 rule 5"
  - "jobs #330, #296 — deviations accepted because the commit message argued them"
  - "The commit corpus here averages several hundred words of rationale per merge, structured as what changed, why, and how verified"
rationale: >
  In this project the commit message is the primary durable record of reasoning,
  and it visibly works: reviewers cite commit bodies as evidence, and deviations
  argued there are accepted rather than reworked.
related: [deviation-is-recorded-not-silent, docs-are-the-knowledge-store, verification-is-reported-with-its-command]
---

**Rule.** The commit message explains why the change is shaped the way it is:
what changed, why this shape, what was deliberately not done, and how it was
verified. The diff shows what; only the message can show why.

**Why.** Pull-request threads and chat transcripts do not persist and are not
searchable from the code. The commit is attached to the change forever and is
what a future reader reaches through blame.

**How to apply.** Structure it: a one-line subject naming the outcome, then what
changed by file or subsystem, then the reasoning for any non-obvious choice,
then verification with commands. Name the alternatives you rejected. Never
leave a work-in-progress message on a merged commit — amend it into a real one.

**Does not apply when.** The change is genuinely mechanical and its subject line
says everything.

## Derivation

Job #550 amended a conflict-resolution commit "into a real message carrying the
rationale rather than leaving a WIP commit on the branch", citing the rule by
number — an instance of the practice being enforced on its own record-keeping.
