---
name: ratchet-dont-sweep
title: Land a new rule as a ratchet, and make the debt greppable
scope: process
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/style.md — the panic-avoidance denies landed as a ratchet, with existing violations wearing a site-specific allow whose reason names the ticket that dissolves it"
  - "The two-sentence doc-comment cap judges only blocks a diff adds a line inside, because the tree carries pre-existing debt"
rationale: >
  How to introduce a rule into a large existing tree without either a
  thousand-file commit or an unenforced aspiration. The greppable-debt detail is
  what makes it converge rather than stall.
related: [whole-tree-not-just-the-diff, a-marker-is-not-a-silencer, boundaries-are-asserted-not-documented]
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

## Derivation

This project's panic-avoidance rule landed as "a ratchet, not a cleanup", with
each pre-existing violation carrying an allow whose reason names the ticket that
dissolves it, and with crate-level exemptions "rejected on sight". The comment
rule then completed the arc: one job cleared the debt, and the rule became
whole-tree.
