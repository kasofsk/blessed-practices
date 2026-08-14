---
name: a-denial-with-no-control
title: A denial with no control identifies no mechanism
scope: testing
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/style.md Tier 2 rule 8, second half"
  - "design #529 — a single refusal equally consistent with 'denied by policy' and 'denied by the caller's provenance'"
rationale: >
  The complement to the previous rule and, in a security context, the more
  dangerous half: a refusal feels like proof of a boundary, and one refusal
  proves only that this attempt failed.
related: [a-tool-outcome-measures-the-tool, unenforced-intentions-become-believed-facts, verification-is-reported-with-its-command]
---

**Rule.** A single failed attempt does not identify why it failed. Run the
control — the same operation in a case you expect to succeed — or state plainly
that the mechanism is documented behaviour rather than your result.

**Why.** Denials have many causes: policy, ownership, provenance, a typo, an
unrelated misconfiguration. Without a control, all of them produce identical
evidence, and the one you happen to believe becomes the recorded finding.

**How to apply.** Pair every negative result with a positive control that
isolates one variable. Where no control is possible, say so and downgrade the
claim from "we measured" to "the documentation says". Record both results, not
just the interesting one.

**Does not apply when.** The mechanism is already established and you are
regression-testing it.

## Derivation

Design #529's reviewer named the two hypotheses the single denial could not
distinguish, and prescribed the control: the same read against a process the
reader forked itself. Without it, the document's central premise rested on an
ambiguous refusal.
