---
type: Blessed Practice
title: "Suspect is not wrong — publish a reading list, block almost nowhere"
description: "Derive staleness from history rather than from declarations, report it as a reading list, and block only where the author is in a position to act."
status: draft
tags:
  - bucket/general
  - scope/documentation
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  A model for derived, zero-maintenance signals: nothing is declared, nothing is
  maintained, and the output is a reading list rather than a verdict. The
  restraint is the design — 'failing a build for history nobody in the commit
  caused is how a ledger gets disabled'.
---

**Rule.** Derive staleness from history rather than from declarations, report it
as a reading list, and block only where the author is in a position to act. A
document whose subject moved after it did is suspect, and suspect is not wrong.

**Why.** Declared freshness metadata is maintenance nobody performs. A derived
signal costs nothing to keep and is always current. But a derived signal is also
noisy, and a noisy blocking gate gets disabled — so almost all of it must be
advisory.

**How to apply.** Compute the signal from the same extractor the strict checks
use, so the two cannot disagree about what a document names. Print the whole
ledger; block only on documents this change edits, and only through non-document
movers. Exclude relations that can form cycles no commit can clear.

**Does not apply when.** The claim is checkable outright — then check it, and
block.

## Where this comes from

The restraint is the design, and it is recorded with its reason: the ledger
blocks almost nowhere on purpose, because failing a build for history nobody
in the commit caused is how a ledger gets disabled — and at that commit no
edit could clear it anyway. One relation was later excluded from the blocking
side entirely, being the only edge that can form a cycle no rework commit can
clear.

## Related

- [Clear an attention gate with an assertion of attention, not a timestamp](assertion-of-attention-over-timestamp.md)
- [Order gates cheapest-first and diff-aware](../process/gates-are-cheap-first.md)
- [Present-tense prose about the tree is a factual claim](present-tense-prose-is-a-claim.md)
