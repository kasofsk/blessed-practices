---
name: counts-in-prose-are-liabilities
title: A count in prose is a liability; give the command instead
scope: documentation
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "jobs #449, #450 — three cycles spent on which of three defensible denominators a suite's case count is"
  - "job #405 — counts kept, but dated and given with the command that produces them"
  - "job #450 — the resolution: delete the count, state the command, and let the reader run it"
rationale: >
  Three consecutive jobs and roughly seven rework cycles were spent on numbers
  in prose. The eventual answer — prefer the command to the number — is the
  cheapest durable fix in the entire corpus.
related: [date-the-measurement, verification-is-reported-with-its-command, present-tense-prose-is-a-claim]
---

**Rule.** Prefer naming the command that produces a count over stating the
count. When a number is genuinely needed, give the command beside it and the
date it was measured, and expect to re-measure rather than to trust it.

**Why.** Counts go stale on the next commit, and they go stale invisibly. Worse,
most countable things have several defensible denominators, so two honest
authors produce two different true numbers and the discrepancy reads as an
error in one of them.

**How to apply.** Write "the count is `<command>`" rather than "there are N".
Where the number carries the argument, state which denominator you counted and
why. In an append-only body, the cheapest honest fix for a stale number is the
tense.

**Does not apply when.** The number is the finding — a measurement whose value
is the point. Date it.

## Derivation

Jobs #449 and #450 spent three cycles between them on a suite's case count,
because call sites, numbered comment markers and executed assertions are three
different numbers and the file supported all three. The resolution deleted every
total and left the commands.
