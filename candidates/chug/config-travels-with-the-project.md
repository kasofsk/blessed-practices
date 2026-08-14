---
type: Blessed Practice
title: "Configuration is project-owned and repo-versioned"
description: "Everything that defines how the platform treats a project — job definitions, prompts, gate scripts, schedules — lives in that project's repository, under one configuration root, and is versioned with the code."
status: draft
tags:
  - bucket/chug
  - scope/architecture
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
  - "Job types, prompts, tasks, tags and schedules all live under a single configuration root in the project repository"
  - "job #306 — the move to that root, with one resolver owning the lookup and a fallback for the older layout"
rationale: >
  A structural decision that shapes everything else: the platform reads its
  behaviour from the repository it is operating on, so a change to how work is
  done is reviewed by the same process as a change to the code.
---

**Rule.** Everything that defines how the platform treats a project — job
definitions, prompts, gate scripts, schedules — lives in that project's
repository, under one configuration root, and is versioned with the code.

**Why.** Config in the platform is invisible to the people changing the code and
cannot be reviewed alongside it. Config in the repository means a change to the
review criteria goes through review, a change to a gate is tested by the gate,
and rolling back the code rolls back its process.

**How to apply.** Pick one root directory and put everything under it. Write one
resolver for the lookup, with the compatibility fallback in that one place.
Never write outside the new root, even when reading tolerates the old one.

**Does not apply when.** The setting is genuinely about the platform's own
deployment rather than about the project.

## Where this comes from

Job #306 moved five directories under one root, with a single resolver owning
the two-layout lookup and tests pinning both plus the shadowing order. Its
review found the predictable residue: the front end hard-coded the new path
while the backend deliberately resolved both.

## Related

- [One resolver per lookup question](../general/architecture/one-resolver-per-question.md)
- [Order gates cheapest-first and diff-aware](../general/process/gates-are-cheap-first.md)
- [Wire changes are additive, epoch-gated, and tolerated by N-1](../general/architecture/additive-wire-evolution.md)
