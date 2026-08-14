---
type: Retrospective
title: Where these practices came from
description: A retrospective over one project's full agent-driven development run, and the defect classes it exposed.
status: draft
tags:
  - bucket/general
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
sources:
  - resource: https://github.com/kasofsk/chuggernaut
    title: "Chuggernaut — the platform whose run this retrospective covers"
---

# Where these practices came from

Every concept in this bundle was derived from one project's own development
history rather than from general engineering advice. That project is an
agent-orchestration platform that develops itself: work is filed as units, each
one is implemented by an agent on its own branch, reviewed by other agents under
a read-only profile, gated by scripts, and merged automatically. The corpus
covers its first 577 units of work, to 2026-08-14.

## Method

| Quantity | Value |
| --- | --- |
| Units of work filed | 577 |
| Merged | 411 (261 code, 62 web, 45 docs, 33 design, 8 manual, 1 corpus-shedding) |
| Task records | 2,940 |
| Review rejections | 355 |
| Merged with no rework | 284 of 497 |
| Needing three or more cycles | 86 |
| Tasks lost to infrastructure | 38 |

The 355 rejections are the primary source. Most carry file, line, mechanism and
a suggested fix, which is what lets a defect class be **counted** rather than
recalled — the difference between these findings and a list of opinions. Commit
bodies, the design corpus and the gate scripts are secondary. Figures were taken
on 2026-08-14; re-derive rather than trust them.

## What the history says

**1. Stale present-tense prose is the dominant defect, by a wide margin.** 98 of
the 355 rejections came from the two documentation reviewers, and nearly all say
the same thing: a sentence describes, in the present tense, behaviour the change
just altered. Nothing else is close.
→ [present-tense-prose-is-a-claim](general/documentation/present-tense-prose-is-a-claim.md),
[docs-updated-in-the-same-commit](general/documentation/docs-updated-in-the-same-commit.md),
[cross-doc-state-claims](general/documentation/cross-doc-state-claims.md),
[sweep-the-class-not-the-instance](general/process/sweep-the-class-not-the-instance.md)

**2. The second-largest class is the check that cannot fail.** Guards that could
not fire, tests green against the unfixed code, assertions on values the
function never reads, and a coverage announcement for a tier that self-skipped.
→ [assertions-that-can-fail](general/testing/assertions-that-can-fail.md),
[no-vacuous-assertions](general/testing/no-vacuous-assertions.md),
[announce-exactly-what-ran](general/process/announce-exactly-what-ran.md),
[a-check-that-cannot-run-exits-distinctly](general/process/a-check-that-cannot-run-exits-distinctly.md)

**3. The most expensive architectural defect is the namespace question.** A
machine fact established from the wrong view — a container's instead of the
host's, the staging machine's instead of the executor's, an operator's uid
instead of the task's. It caused rework across at least six changes and survived
a complete repackaging of the component involved.
→ [re-derive-facts-in-the-executing-namespace](general/architecture/re-derive-facts-in-the-executing-namespace.md)
and its four refinements

**4. Silent success costs most per incident.** A launch error that left a record
running forever; a missing transport permission that made a whole feature a
no-op in production; a security rule believed for eleven days that was false the
entire time on the one machine that mattered.
→ [refuse-loudly](general/architecture/refuse-loudly.md),
[unenforced-intentions-become-believed-facts](general/architecture/unenforced-intentions-become-believed-facts.md),
[silent-filters-hide-rows](general/process/silent-filters-hide-rows.md)

**5. Rework is the normal path, so its economics dominate.** 43% of units needed
at least one rework cycle. The practices that shorten cycles are worth more than
any individual code rule.
→ [branch-preserved-across-rework](chug/branch-preserved-across-rework.md),
[rework-context-carries-the-evidence](chug/rework-context-carries-the-evidence.md),
[scope-the-rework-explicitly](chug/scope-the-rework-explicitly.md)

**6. Several late cycles were lost to mechanical gate traps rather than bad
work.** Commit ordering against a staleness ledger accounts for at least six.
→ [one-commit-when-ordering-matters](chug/one-commit-when-ordering-matters.md),
[assertion-of-attention-over-timestamp](general/documentation/assertion-of-attention-over-timestamp.md),
[staleness-is-suspect-not-wrong](general/documentation/staleness-is-suspect-not-wrong.md)

## The six architectural decisions

Six choices shaped everything downstream, and each is proposed as a rule rather
than as a description: a single writer per record class; pure deciders returning
effects for one interpreter; one component per external system; project-owned,
version-controlled configuration; reading reviewers separated from executing
gates; and a mutable head over an append-only body for every decision document.

## How to read a concept

Each file states the rule imperatively and portably, so it can be injected into
a work or review prompt verbatim, then gives the why, how to apply it, and when
it does not apply — followed by `## Where this comes from`, which is evidence
rather than instruction.

`confidence` in the tags reflects how well the evidence supports the rule, **not**
how strongly it is recommended. `portability/universal` means the rule as written
should transfer to another agent-directed repository; `portability/project` means
it encodes something about a particular platform's shape.

## Suggested review order

1. The six architectural decisions above — they constrain the rest.
2. The four documentation practices in finding 1: a third of all rejections, and
   the cheapest to adopt.
3. The rework-economics group in finding 5.
4. Everything else, by section.

Reject freely. 110 is the widest honest net over the evidence, not a target. The
useful output of this review is a much smaller set that actually gets enforced.
