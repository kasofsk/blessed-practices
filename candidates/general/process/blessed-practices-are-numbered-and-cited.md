---
type: Blessed Practice
title: "Practices are numbered, tiered, injectable, and carry their why"
description: "Write practices so they can be cited and injected: numbered or named, tiered by how strictly they bind, short enough to include in a prompt, and each carrying its reasoning inline."
status: draft
tags:
  - bucket/general
  - scope/process
  - altitude/high
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  The meta-practice: how a practice corpus has to be shaped in order to actually
  condition agent behaviour. Every property here is functional, not editorial.
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

## Where this comes from

The source project's rule set states these constraints in its own preamble:
keep it short, because it is written to be injected into work and review
prompts, and give every rule its rationale inline, because the rationale is
what lets a reader generalise to a case the rule did not anticipate. That
rejections cite the rules by number is the evidence it works.

## Related

- [A rejection names the rule it rejects under](verdict-names-the-rule.md)
- [Land a new rule as a ratchet, and make the debt greppable](ratchet-dont-sweep.md)
- [Mechanise the checkable half; route the rest to judgement](mechanise-the-checkable-half.md)
