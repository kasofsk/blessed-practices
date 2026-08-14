---
name: merge-conflicts-keep-both-records
title: Resolve record conflicts by keeping both, in landing order
scope: process
altitude: mid
portability: project
confidence: high
status: candidate
evidence:
  - "jobs #550, #551, #554, #555, #556, #560, #563, #565, #566 — near-identical conflict resolutions, all keeping both sides"
  - "job #565 — 'both append-only corrections kept, #567's first because it merged first'"
rationale: >
  Nine consecutive jobs resolved the same class of conflict the same way, and
  each commit message re-derived the reasoning from scratch. That is a practice
  waiting to be written down.
related: [mutable-head-append-only-body, corrections-are-appended-and-dated, stale-base-is-not-an-authoring-failure]
---

**Rule.** When two branches append independent records to the same file, the
resolution is the union in landing order — never a choice between them. When
they both rewrite a summary, merge the summary so it is true of both landings,
rather than taking one side's list.

**Why.** Appended records are statements about different events; neither
invalidates the other, so choosing loses history. Summaries are the opposite:
each side wrote a sentence true of its own landing only, so keeping either one
leaves the file asserting a falsehood about the other.

**How to apply.** Body: concatenate, ordered by merge order, separated as the
file's own convention separates them. Head: rewrite to current truth naming both
landings. Scratch files whose semantics are "lines this diff adds" have no
precedence question at all — take the union and say why.

**Does not apply when.** The two changes genuinely contradict — then it is a
decision, and it belongs to a human, not to the merge.

## Derivation

The pattern is stated most compactly in job #556: the gate "reads the lines a
diff adds against its base, never the file's contents, so there was nothing to
reconcile between the sides — only to keep". The head half is stated in #551:
each side claimed the other slices remained, so the merged line names both.
