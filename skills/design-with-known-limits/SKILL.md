---
name: design-with-known-limits
description: Design systems with explicit correctness limits, failure modes, and operational assumptions instead of automatically engineering every weakness away. Use when reviewing reliability gaps, edge cases, retry windows, capacity bounds, SLAs, hardening proposals, or whether a risk deserves code, operations, documentation, or acceptance.
---

# Design With Known Limits

## Core principle

A sound system does not have to be perfect. It has to be honest about where its
correctness ends, what happens beyond that boundary, and who has accepted the
risk.

Do not automatically turn every discovered weakness into code. A fix consumes
design time, implementation effort, complexity, runtime cost, and future
maintenance. Those costs may exceed the expected harm, especially early in a
project or where an operational control already makes the risk acceptable.

## State the correctness envelope

Describe guarantees together with the conditions that make them true: retry
windows, retention periods, traffic bounds, singleton ownership, recovery time,
trusted inputs, or operator procedures. Name what the system does outside those
conditions. A documented limit is part of the design; a silent limit is a bug
waiting to be misclassified.

Distinguish among:

- an invariant the system must preserve;
- a guarantee conditional on an SLA or operational assumption;
- a detected failure that stops safely;
- an accepted risk that may produce a known degraded outcome.

Do not describe a conditional guarantee as absolute, and do not call an
unmeasured hope an operational assumption.

## Price the fix and the risk

For each weakness, compare the credible impact and likelihood with the full
lifecycle cost of fixing it. Include the complexity the fix adds to the
correctness argument itself. A mechanism that closes one rare edge case while
creating more state, coordination, and recovery paths can make the overall
system less dependable.

Prefer the least expensive control that brings risk inside the operator's
tolerance. Depending on the system, that may be code, configuration, monitoring,
an alert, a runbook, a capacity limit, an SLA, or explicit acceptance. Revisit
the choice when scale, exposure, reversibility, or business impact changes.

## Trust operator judgment

Present operators with the limit, consequence, observability, mitigation, and
cost of stronger protection. Let them decide which risks justify investment.
Do not silently spend complexity to pursue theoretical completeness, and do not
silently accept a risk whose consequence the operator has not been given a fair
chance to evaluate.

Operator acceptance is not a waiver for hidden data loss, security boundaries,
or irreversible harm. The higher the impact and the harder the failure is to
detect or recover from, the stronger the evidence and explicit agreement should
be.

## Why this matters

Engineering is allocation under uncertainty. Treating every imperfection as a
mandatory fix produces expensive systems whose complexity outruns their needs.
Treating every limit as harmless produces fragile systems nobody understands.
Known limits, explicit risks, and deliberate operator choices keep correctness
claims honest while preserving room to invest where it matters most.
