---
type: Blessed Practice
title: "Report verification as commands and outputs, not as adjectives"
description: "State how you verified, not that you did: the command, its output or exit status, and what you did not exercise."
status: draft
tags:
  - bucket/general
  - scope/process
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  The reviews and summaries that hold up under scrutiny all report method. The
  ones that get overturned report conclusions. Stating the method also tells the
  next reader what was not checked, which is often the more useful half.
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

## Where this comes from

The strongest review in the source retrospective built both versions of a
change, served each against a mock backend with configurable latency and per-
endpoint failures, drove them in a headless browser at two viewports, and
labelled its findings exercised rather than read. Its findings were accepted
without argument, which is the practical payoff for reporting method.

## Related

- [A tool's outcome measures the tool, not your claim](../testing/a-tool-outcome-measures-the-tool.md)
- [Acceptance criteria name an observation, not an intention](acceptance-criteria-are-checkable.md)
- [Date every measurement, and name the host it was taken on](../documentation/date-the-measurement.md)
