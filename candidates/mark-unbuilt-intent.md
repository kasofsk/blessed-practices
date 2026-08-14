---
name: mark-unbuilt-intent
title: Marking is a syntax, and the markers are not interchangeable
scope: documentation
altitude: mid
portability: project
confidence: high
status: candidate
evidence:
  - "docs/reference/style.md — three markers, ordered by tense: designed-not-built, correctly-absent-from-version-control, named-because-it-does-not-exist"
  - "job #436 — the marker's bright-line definition violated three times in the commit that introduced it"
rationale: >
  A doc corpus needs a way to name things that do not exist without lying about
  them. Three markers rather than one is the interesting choice: each has a
  different tense, and collapsing them would turn the mechanism into a general
  silencer.
related: [present-tense-prose-is-a-claim, a-marker-is-not-a-silencer, mechanise-the-checkable-half]
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

## Derivation

Job #436's review is the case that fixed the definition: the change introduced
the narrowest marker with a bright-line rule and used it three times in ways its
own rule forbids. The resulting definition — honest only when deleting the
marker would leave the line still asserting absence — is what keeps it from
becoming a silencer.
