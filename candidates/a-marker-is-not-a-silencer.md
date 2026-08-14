---
name: a-marker-is-not-a-silencer
title: An exemption mechanism must be narrower than the thing it exempts
scope: documentation
altitude: mid
portability: universal
confidence: medium
status: candidate
evidence:
  - "docs/reference/style.md — markers cover the line that carries them, never the block"
  - "docs/reference/style.md — a duplication exception is a bracketed directive stating why, never a threshold change"
  - "The comment lint allows machine-read directives only on one line, so a wrapped justification is an ordinary comment and is rejected"
rationale: >
  Three independent exemption mechanisms in this repo were each deliberately
  scoped so they cannot be used broadly. That is a design pattern for gates, not
  an accident, and it is what keeps the gates from being disabled in practice.
related: [mark-unbuilt-intent, every-gate-has-a-test-suite, no-duplication-threshold]
---

**Rule.** Design every exemption to be narrower than the rule it escapes:
line-scoped rather than file-scoped, per-instance rather than per-threshold, and
requiring a written reason at the point of use.

**Why.** A broad exemption is used broadly. Once a file-level or threshold-level
escape exists, the cheapest response to any finding is to widen it, and the rule
stops meaning anything without anyone deciding to abandon it.

**How to apply.** Scope exemptions to the smallest unit the checker can see.
Require the justification inline where the checker can confirm it is present.
Prefer refusing a global knob outright — raising a threshold should not be an
available move.

**Does not apply when.** The rule is genuinely wrong for a whole category —
then change the rule, and say so.

## Derivation

The duplication gate's exception is a two-line bracket with the reason on the
directive line, and its documentation says explicitly "never a threshold
change". The comment lint's allowlist matches the text right after the opener,
which mechanically forces a directive to be one line.
