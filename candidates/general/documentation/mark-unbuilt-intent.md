---
type: Blessed Practice
title: "Marking is a syntax, and the markers are not interchangeable"
description: "When a document names something that does not resolve, mark why on the same line, with a marker whose meaning matches the tense: it will exist later, it exists on a machine but not in version control, or it exists nowhere and that is the sentence's point."
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
  A doc corpus needs a way to name things that do not exist without lying about
  them. Three markers rather than one is the interesting choice: each has a
  different tense, and collapsing them would turn the mechanism into a general
  silencer.
---

**Rule.** When a document names something that does not resolve, mark why on the
same line, with a marker whose meaning matches the tense: it will exist later, it
exists on a machine but not in version control, or it exists nowhere and that is
the sentence's point.

**Why.** Without markers, a checker forces you to choose between deleting honest
prose and disabling the check. With one undifferentiated marker, the mechanism
degrades into a way to silence anything.

**How to apply.** Pick by tense. Test the narrowest marker by deleting it
mentally: if a reader would still read the line as asserting the thing is gone,
the marker is honest. A path that resolves in another repository takes no marker
— qualify it instead, which fixes the prose for humans too.

**Does not apply when.** The claim is simply stale — that is an edit, not a
marker.

## Where this comes from

The definition was fixed by a review of the change that introduced it: it
proposed the narrowest marker with a bright-line rule and then used it three
times in ways its own rule forbids. The resulting test — the marker is honest
only if a reader who deleted it would still read the line as asserting absence
— is what keeps the mechanism from degrading into a general silencer.

## Related

- [An exemption mechanism must be narrower than the thing it exempts](a-marker-is-not-a-silencer.md)
- [Mechanise the checkable half; route the rest to judgement](../process/mechanise-the-checkable-half.md)
- [Present-tense prose about the tree is a factual claim](present-tense-prose-is-a-claim.md)
