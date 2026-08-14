---
type: Blessed Practice
title: "A count in prose is a liability; give the command instead"
description: "Prefer naming the command that produces a count over stating the count."
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
  Three consecutive jobs and roughly seven rework cycles were spent on numbers
  in prose. The eventual answer — prefer the command to the number — is the
  cheapest durable fix in the entire corpus.
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

## Where this comes from

Two consecutive changes and roughly seven review cycles were spent arguing
about a test suite's case count, because call sites, numbered comment markers
and executed assertions are three different numbers and the file supported all
three. The resolution deleted every total and left the commands that produce
them.

## Related

- [Date every measurement, and name the host it was taken on](date-the-measurement.md)
- [Present-tense prose about the tree is a factual claim](present-tense-prose-is-a-claim.md)
- [Report verification as commands and outputs, not as adjectives](../process/verification-is-reported-with-its-command.md)
