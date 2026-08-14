---
name: blessed-practices-are-numbered-and-cited
title: Practices are numbered, tiered, injectable, and carry their why
scope: process
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/style.md — three tiers, numbered rules, each carrying its rationale inline, written to be injected into work and review prompts"
  - "Rejections throughout this corpus cite rules by tier and number"
rationale: >
  The meta-practice: how a practice corpus has to be shaped in order to actually
  condition agent behaviour. Every property here is functional, not editorial.
related: [verdict-names-the-rule, mechanise-the-checkable-half, ratchet-dont-sweep]
---

**Rule.** Write practices so they can be cited and injected: numbered or named,
tiered by how strictly they bind, short enough to include in a prompt, and each
carrying its reasoning inline.

**Why.** The rationale is what lets a worker or reviewer generalise correctly to
a case the rule did not anticipate — a rule without its why is applied
literally or ignored. The tiering is what lets a reviewer know whether to block.
And the length constraint is real: a practice document that does not fit in a
prompt does not reach the agent doing the work.

**How to apply.** State the rule in one imperative sentence, then the why, then
how to apply it, then when it does not apply. Tag each with how it is enforced —
machine-checked, reviewer-checked, or principle — so its weight is unambiguous.
Keep the whole tier short, and prefer deleting a weak rule to adding a caveat.

**Does not apply when.** The corpus is for human reference only and nobody is
injecting it.

## Derivation

This project's rule set states the constraint in its own preamble: keep it
short, because it is written to be injectable into work and evaluation prompts,
and each rule carries its why because the why is what lets a reader generalise.
The citation pattern in rejections is the evidence that it works.
