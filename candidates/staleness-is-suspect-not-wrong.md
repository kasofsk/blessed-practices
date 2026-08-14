---
name: staleness-is-suspect-not-wrong
title: Suspect is not wrong — publish a reading list, block almost nowhere
scope: documentation
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "design #415 D7 — a git-derived ledger: for each doc, the files it names and whether any has a newer commit"
  - "The ledger is advisory whole-tree and blocks in exactly one case: a doc this diff edits that is still suspect through a non-doc file"
  - "job #454 — markdown movers excluded from the blocking side, because doc-names-doc is a cycle no rework can clear"
rationale: >
  A model for derived, zero-maintenance signals: nothing is declared, nothing is
  maintained, and the output is a reading list rather than a verdict. The
  restraint is the design — 'failing a build for history nobody in the commit
  caused is how a ledger gets disabled'.
related: [assertion-of-attention-over-timestamp, present-tense-prose-is-a-claim, gates-are-cheap-first]
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

## Derivation

Design #415 D7 states the restraint directly: the ledger blocks nowhere else on
purpose, because "failing a build for history nobody in the commit caused is how
a ledger gets disabled, and at the commit no edit could clear it anyway".
