---
name: cross-doc-state-claims
title: A doc asserting another doc's status is the most fragile sentence you can write
scope: documentation
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "job #483 — three sibling design heads made the same status claim; two were corrected and the third was missed"
  - "job #522 — a head calling a slice 'still proposed' thirty lines above the table row saying it landed"
  - ".chug/tasks/review-docs-updated.md class 1 — cross-doc state claims are its first blocking class"
rationale: >
  A distinct sub-class of stale prose worth its own card because the falsifying
  change is usually in a different document than the false sentence, so the
  author never sees it.
related: [present-tense-prose-is-a-claim, the-landing-job-owns-the-doc-update, mutable-head-append-only-body]
---

**Rule.** Avoid asserting another document's implementation status. When you
must, link to the row that owns the answer rather than restating it — and when
you land something, sweep every doc that names it.

**Why.** Status claims propagate: a design cites a sibling's phase as
unimplemented to justify its own scope, and three documents later the citation
is load-bearing. The landing that falsifies them all happens in a fourth place.

**How to apply.** Keep status in exactly one place per subject — the design's own
slice table — and link to it. When landing, grep for the design number and for
the subject's name, and read every head that names it. Expect three hits when
you predicted one.

**Does not apply when.** The claim is dated and framed as history.

## Derivation

Job #483's finding is the shape: a phase row said "no such record exists yet",
while the same diff added the record, and the reviewer notes that the two
sibling heads making the identical claim were both corrected by the same diff —
"this is the third, and it was missed".
