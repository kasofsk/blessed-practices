---
type: Blessed Practice
title: "Land a new rule as a ratchet, and make the debt greppable"
description: "A new rule lands enforcing on new code immediately, with existing violations individually marked and the marker naming the work that removes them."
status: draft
tags:
  - bucket/general
  - scope/process
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  How to introduce a rule into a large existing tree without either a
  thousand-file commit or an unenforced aspiration. The greppable-debt detail is
  what makes it converge rather than stall.
---

**Rule.** A new rule lands enforcing on new code immediately, with existing
violations individually marked and the marker naming the work that removes them.
Blanket file-level or crate-level exemptions are rejected on sight.

**Why.** A rule that requires cleaning the whole tree first never lands. A rule
that exempts existing code broadly never converges, because the exemption is
where new violations go. Per-site markers give both: no new debt, and a
countable backlog.

**How to apply.** Mark each violation at its site, with a reason naming the
ticket. Make the debt a one-line grep. Refuse the wide exemption explicitly in
the rule's own text, since that is the shortcut a later author will reach for.
Convert to whole-tree enforcement when the count hits zero.

**Does not apply when.** The tree is small enough to fix in one change — then
fix it and enforce whole-tree from the start.

## Where this comes from

A rule banning a panicking idiom landed as a ratchet rather than a cleanup:
each pre-existing violation carries a site-local exemption whose reason names
the work that dissolves it, the remaining debt is a one-line search, and
blanket file- or module-level exemptions are rejected on sight. A second rule
completed the arc — one change cleared its debt, and enforcement moved to the
whole tree.

## Related

- [An architectural boundary that nothing checks is a comment](../architecture/boundaries-are-asserted-not-documented.md)
- [An exemption mechanism must be narrower than the thing it exempts](../documentation/a-marker-is-not-a-silencer.md)
- [Cheap checks run whole-tree, not only over the diff](whole-tree-not-just-the-diff.md)
