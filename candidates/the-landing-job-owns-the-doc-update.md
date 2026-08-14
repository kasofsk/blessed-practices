---
name: the-landing-job-owns-the-doc-update
title: The job that lands a slice writes its status row
scope: documentation
altitude: mid
portability: project
confidence: high
status: candidate
evidence:
  - "design #415 D10 — the implementing job owns the update, in the same commit its merge creates"
  - "job #535 — a slice landed with its design head still saying 'nothing below is built'"
  - "job #491 — a head left at the status word meaning nothing was built, in the commit that built it"
rationale: >
  Assigning the doc update to the landing job is what makes status checkable at
  all: a row claiming a merged job can be resolved against history, and the
  landing job is the only actor that knows the row is now true.
related: [docs-updated-in-the-same-commit, cross-doc-state-claims, mechanise-the-checkable-half]
---

**Rule.** The commit that implements a planned slice flips that slice's status
row and adjusts the document's status line, in the same commit. Nobody else owns
that update.

**Why.** Any later owner has to re-derive what landed from a diff. And a status
row that names a merged job is machine-checkable — but only if the convention is
that the landing job writes it, since at the moment of writing the merge does
not exist yet.

**How to apply.** Flip the row, state what landed and what did not, and adjust
the status word — a document with some slices shipped is not the same as one
with none. Write the row in the exact shape the checker parses; a paraphrase is
skipped, which buys silence rather than approval.

**Does not apply when.** The job deliberately lands nothing (a measurement job)
— then record that, which is also a status.

## Derivation

Job #535's reviewers both blocked on the same thing: the design head still said
"nothing below is built" in the commit that built the first slice, and the
checker cannot catch it because it exempts the landing job by construction. Job
#491's variant is subtler — the row flipped, the status word did not.
