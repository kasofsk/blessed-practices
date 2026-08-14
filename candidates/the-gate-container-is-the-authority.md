---
name: the-gate-container-is-the-authority
title: The gate's environment is the authority; local runs produce false reds
scope: testing
altitude: mid
portability: project
confidence: high
status: candidate
evidence:
  - "docs/reference/testing.md — the shell suites assume the gate container's tooling, so hand-running them elsewhere produces false reds"
  - "job #366 — a locale-dependent character class whose verdict differed by host and shell"
  - "job #501 — a shell divergence where the gate's shell and production's shell bind different code from the same line"
rationale: >
  Environment-dependent verdicts are a recurring trap in a fleet with two
  operating systems and two shells. The rule has two halves: name the
  authoritative environment, and pin the environment-sensitive things so the
  answer is the same everywhere.
related: [self-skip-loudly, locale-and-shell-portability, which-kernel-execs-it]
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

## Derivation

Job #366 found a character-class check whose membership depends on the locale's
collation, so an uppercase name silently passed a gate written to reject it — on
exactly the configuration the commit hook runs in. The tree's answer was to pin
the locale, with the reason recorded on the line.
