---
type: Blessed Practice
title: "The change that implements a planned unit writes its status row"
description: "The commit that implements a planned unit of work flips that unit's status row and adjusts the document's status line, in the same commit."
status: draft
tags:
  - bucket/general
  - scope/documentation
  - altitude/mid
  - portability/project
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Assigning the doc update to the landing job is what makes status checkable at
  all: a row claiming a merged job can be resolved against history, and the
  landing job is the only actor that knows the row is now true.
---

**Rule.** The commit that implements a planned unit of work flips that unit's status
row and adjusts the document's status line, in the same commit. Nobody else owns
that update.

**Why.** Any later owner has to re-derive what landed from a diff. And a status
row that names a merged change is machine-checkable — but only if the convention is
that the implementing change writes it, since at the moment of writing the merge does
not exist yet.

**How to apply.** Flip the row, state what landed and what did not, and adjust
the status word — a document with some slices shipped is not the same as one
with none. Write the row in the exact shape the checker parses; a paraphrase is
skipped, which buys silence rather than approval.

**Does not apply when.** The change deliberately lands nothing (a measurement)
— then record that, which is also a status.

## Where this comes from

Two instances. One change implemented the first slice of a plan while leaving
that plan's head reading "nothing below is built" — and the automated checker
cannot catch it, because it exempts the change doing the landing by
construction. A subtler variant flipped the status row and left the summary
word unchanged, so the document said both things at once.

## Related

- [A change updates the docs it makes stale, in the same commit](docs-updated-in-the-same-commit.md)
- [A doc asserting another doc's status is the most fragile sentence you can write](cross-doc-state-claims.md)
- [Mechanise the checkable half; route the rest to judgement](../process/mechanise-the-checkable-half.md)
