---
name: verification-is-reported-with-its-command
title: Report verification as commands and outputs, not as adjectives
scope: process
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #256 — a review that built both branches, served them against a mock API and drove them in a headless browser, reporting per-request timings"
  - "job #250 — 'I ran the suite — ALL PASS (16 cases, incl. the 4 new ones)'"
  - "job #449 — 'verified by reading; nothing built, tested or linted' stated up front"
rationale: >
  The reviews and summaries that hold up under scrutiny all report method. The
  ones that get overturned report conclusions. Stating the method also tells the
  next reader what was not checked, which is often the more useful half.
related: [acceptance-criteria-are-checkable, date-the-measurement, a-tool-outcome-measures-the-tool]
---

**Rule.** State how you verified, not that you did: the command, its output or
exit status, and what you did not exercise. If you verified by reading, say so
explicitly.

**Why.** "Verified" is unfalsifiable and is routinely written about things that
were only read. Naming the method lets a reader weigh the claim and lets the
next person reproduce it, and it makes the gaps visible without anyone having to
admit to them.

**How to apply.** Quote the command and the salient output. Separate "I ran it"
from "I read it" from "I reasoned about it". Name the tier or environment —
results on a developer machine and results in the gate's container are different
claims.

**Does not apply when.** The verification is the gate's own, already recorded —
cite it rather than restating it.

## Derivation

Job #256's review is the high-water mark: two builds, a mock API with
configurable latency and per-endpoint failures, a headless browser at two
viewports, and findings labelled "exercised, not read-through". Its findings
were accepted without argument, which is the practical payoff.
