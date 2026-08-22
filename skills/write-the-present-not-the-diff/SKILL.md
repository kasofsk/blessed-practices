---
name: write-the-present-not-the-diff
description: Write prose that states what is true now, without narrating the correction, the superseded claim, or the path that got there. Use when updating documentation whose claims turned out to be wrong, writing a README, comment, or PR description, reporting results back to the operator, or when tempted to write "previously", "used to", "now correctly", or "as it turns out".
---

# Write the Present, Not the Diff

## Core principle

Prose — documentation, comments, PR descriptions, notes back to the operator —
should say **what is true**. It should not narrate the claim it replaced, the
measurement that disproved it, or the awkwardness of having been wrong. Write
as though the system was always meant to be the way it now is.

## How we get there

### 1. Correct the claim; don't report the correction

A document said a tool saved 20–50× tokens. Measurement put it at 3×. The
correct edit is:

> Saves roughly 3× tokens. *(link to the measurement)*

Not:

> These numbers claimed 20–50× for months, but once actually measured the
> saving turned out to be only about 3×.

The second version spends its words on the history of the document rather than
on the subject of the document. A reader who arrives tomorrow does not care
what the page used to say; they care what is true and how it was established.
Replacing a wrong number with a right one *is* the correction — it does not
also need to be announced.

### 2. Apply the drop test

If the preceding context can be removed without hurting the quality of the
sentence, remove it. Run it on every clause that points backward — "previously",
"used to", "as it turns out", "now correctly", "this was changed because",
"unlike the old behaviour". Delete the clause and reread. If the sentence still
tells the reader everything they need, the clause was residue and belongs in the
commit message, where the history is already kept better.

### 3. Drop the sheepish register

Being wrong earlier is not something the prose needs to atone for. Hedges,
apologies, and self-conscious framing — "the earlier claim was unsubstantiated",
"to be fair, this was never verified" — cost the reader attention and cost the
document authority. A document that keeps apologizing for its past reads as
though it might be wrong right now too. Confident, plain statements of the
current truth are what earn trust; the evidence link, not the confession, is
what makes them credible.

### 4. Keep history only when the reader needs it to act

Some history is content, not residue: migration guides, deprecation notices,
changelogs, incident write-ups, architecture decision records, and the comment
that explains why an obvious-looking approach does not work here. The test is
whether a reader needs the past in order to do the right thing **right now** —
to migrate off the old call, to avoid re-introducing a fix, to understand a
constraint they would otherwise trip over. If yes, state it as fact, in the
same plain register as everything else. If no, it is the diff, and the diff is
already recorded elsewhere.

### 5. The same applies to talking to the operator

Report the state of the work, not a tour of the route. "The parser handles
nested groups; the three cases in `test_groups.py` cover it" beats "I initially
tried a regex, which broke on nesting, so I rewrote it as a recursive
descent parser." This is not permission to hide bad news — current state
includes failures, gaps, and things left undone, and those must be said plainly.
The distinction is between *what is true now*, which the operator needs, and
*how it came to be true*, which they generally do not.

## Why this matters

Every backward-looking clause is a fossil in the making. "Now correctly handles
Unicode" is stale the moment the next change lands, and a document accreting
these becomes a stratigraphy of past states that a reader has to excavate to
find the present one. Version control, PRs, and issue trackers already record
the past, with timestamps and authorship that prose cannot match — duplicating
that record in the documentation makes it worse in both places. Writing only
the present keeps every document a description of the system rather than a
description of its own editing, and the habit generalizes: it is the same rule
the **comments-describe-the-code** practice
(`comments-describe-the-code@blessed-practices`) applies to comments, extended
to everything else we write.
