---
type: Blessed Practice
title: "Reviewers read; gates run"
description: "Separate judgement from execution."
status: draft
tags:
  - bucket/chug
  - scope/process
  - altitude/high
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
sources:
  - resource: https://github.com/kasofsk/chuggernaut
    title: "Chuggernaut — the platform this practice was derived from"
evidence:
  - "docs/spec.md §4.3 — agent evaluators launch under a read-only permission profile"
  - "job #273 — the read-only profile omitted the git plumbing every review prompt's first command depends on"
  - "355 evaluator rejections, of which 35 came from the executing gate and 320 from reading reviewers"
rationale: >
  The split is this platform's central process decision and it is load-bearing:
  the expensive executing gate runs only on changes a reader already accepted.
  The corpus also shows the failure mode — a reader denied the tools reading
  requires.
---

**Rule.** Separate judgement from execution. Reviewing agents read the diff, the
tree and the docs under a read-only profile and produce a verdict with findings.
Building, testing and linting belong to a command gate that runs afterwards.

**Why.** A reviewer that can build will spend its budget building, and its
verdict becomes a slower, less reliable copy of the gate. A reviewer that reads
catches the things a gate cannot: unimplemented requirements, wrong
abstractions, claims that contradict the tree.

**How to apply.** Never add "build it and check" to a review prompt; add it to
the gate script. Give the reviewer exactly the read tools its prompts need —
including the fetch its diff command depends on — and log denials so a missing
tool is visible rather than silently degrading the review.

**Does not apply when.** The only way to judge is to run it — then the check is
a gate, and it should be written as one.

## Where this comes from

Job #273 tightened the review profile and removed the fetch that makes the
reviewer's own first command work; the reviewer caught it and named the
consequence — "a WARN denial on effectively every review run, which is exactly
the noise that makes the new denial log stop meaning anything".

## Related

- [A gate is code, so it has tests, and the tests are discovered](../general/process/every-gate-has-a-test-suite.md)
- [Order gates cheapest-first and diff-aware](../general/process/gates-are-cheap-first.md)
- [The gate's environment is the authority; local runs produce false reds](../general/testing/the-gate-container-is-the-authority.md)
