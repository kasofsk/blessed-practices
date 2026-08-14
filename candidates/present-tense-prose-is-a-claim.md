---
name: present-tense-prose-is-a-claim
title: Present-tense prose about the tree is a factual claim
scope: documentation
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "61 rejections from the docs-updated evaluator and 37 from the docs reviewer — the largest single failure class in this corpus"
  - "jobs #478, #484, #495, #497, #502, #513, #519, #522, #524, #525 — each rejected for a sentence describing pre-change behaviour in the present tense"
  - "docs/reference/style.md Tier 2 rule 5"
rationale: >
  This is the dominant defect class in the entire history — nearly a third of
  all rejections. Nothing else comes close, and it is not a code problem: it is
  prose making unchecked assertions about machinery.
related: [docs-updated-in-the-same-commit, mark-unbuilt-intent, cross-doc-state-claims, unenforced-intentions-become-believed-facts]
---

**Rule.** A sentence in the present tense about what the system does, what a
gate checks, what a path holds or what a constant equals is a factual claim
about the tree. Check it or mark it. Do not write one you have not verified.

**Why.** Present-tense prose about machinery is trusted and acted on. A stale
claim is worse than silence: it sends the next author to build against something
that is not there, and it lets a reviewer accept it as an answer. In this
history it also compounds — one stale sentence is copied into three
operator-facing files before anyone re-checks the original.

**How to apply.** When you change behaviour, grep for prose describing the old
behaviour before you write the new prose. Write what the tree does, date any
measurement, and mark anything unbuilt in the sentence rather than describing it
as if it ran. Prefer naming the mechanism over restating its output.

**Does not apply when.** The sentence is explicitly historical or dated — past
tense is not a claim about today.

## Derivation

The class dominates the late corpus. Job #497's instance is representative: a
runbook said "nothing reads it yet — slice 3 only puts the file there", and the
same commit made both halves false while correcting the identical sentence in a
sibling file. The reviewer's phrasing recurs almost verbatim across ten jobs.
