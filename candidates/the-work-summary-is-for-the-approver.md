---
name: the-work-summary-is-for-the-approver
title: Write the summary for whoever has to judge it, close calls first
scope: process
altitude: mid
portability: universal
confidence: medium
status: candidate
evidence:
  - "design #533 — the work agent's summary is written for the human approver, close calls first"
  - "job #576 — a summary that opens with 'The close calls' and takes each restoration one at a time"
  - "The work summary becomes the squash-merge commit body"
rationale: >
  A small framing decision with a large effect on review cost: the summary is
  not a record of effort, it is the input to someone else's decision, and
  ordering it by their risk rather than by your chronology is most of the value.
related: [human-approval-only-where-no-gate-can-judge, commit-messages-carry-the-why, verification-is-reported-with-its-command]
---

**Rule.** Write the work summary for the person or agent who must approve it.
Lead with the judgement calls and the things you are least sure about, then what
changed, then how you verified. Never lead with a chronology.

**Why.** The approver's scarce resource is attention on the risky parts. A
summary ordered by what the author did forces them to find the risk themselves,
and the risk is exactly what the author is best placed to point at.

**How to apply.** Open with the close calls: what you decided that could
reasonably have gone the other way, and why you chose as you did. Then
deviations, then the change, then verification. Where the summary becomes the
permanent commit body, write it to be readable in six months.

**Does not apply when.** There were no judgement calls — say that, briefly.

## Derivation

The shedding job type makes this explicit because its approver is a human
judging removals; the first shed's summary opens with "The close calls" and
takes each contested restoration individually, with the reason it was originally
removed and the reason it came back.
