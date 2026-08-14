---
type: Blessed Practice
title: "The gate's environment is the authority; local runs produce false reds"
description: "Name one environment as authoritative for gate results, and say so where people will run the gates."
status: draft
tags:
  - bucket/general
  - scope/testing
  - altitude/mid
  - portability/project
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Environment-dependent verdicts are a recurring trap wherever checks run on more
  than one operating system or shell. The rule has two halves: name the
  authoritative environment, and pin the environment-sensitive things so the
  answer does not differ in the first place.
---

**Rule.** Name one environment as authoritative for gate results, and say so
where people will run the gates. Independently, pin everything that makes a
check's verdict environment-dependent — locale, shell, tool versions — so the
answer does not differ in the first place.

**Why.** Contributors run checks locally and act on the result. If the local
answer differs, they either chase a phantom failure or ship a real one. And a
check whose verdict depends on the host is not a check, it is a sample.

**How to apply.** Set the locale explicitly in any script that classifies text.
Pin tool versions exactly. Where a divergence cannot be removed, write a gate
for the divergence itself and explain that the local shell hides it. Document
which environment is authoritative and what differs locally.

**Does not apply when.** The check is genuinely about the local environment.

## Where this comes from

A character-class check whose verdict depends on the locale's collation
silently passed input it was written to reject — on exactly the configuration
the pre-commit hook runs in. The answer had two halves: pin the locale with
the reason recorded on the line, and name which environment is authoritative
so contributors know when a local red is a phantom.

## Related

- [A test that cannot run says so; it never passes vacuously](self-skip-loudly.md)
- [Ask each artifact the question its own executor asks](../architecture/which-kernel-execs-it.md)
- [Pin the locale and know which shell binds your line](../code/locale-and-shell-portability.md)
