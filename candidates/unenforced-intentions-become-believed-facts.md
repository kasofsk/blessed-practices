---
name: unenforced-intentions-become-believed-facts
title: An unenforced intention gets read as a statement of fact
scope: architecture
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "design #517 — a rule saying host tasks do not get the docker socket entered the tree, was believed from that day, and was false the whole time on the node that had one"
  - "job #516 — the read-only probe that measured it, eleven days later"
rationale: >
  This is the strongest single argument in the corpus for the difference between
  a rule and a check, and it is stated with a date and a duration. It deserves
  its own card because the failure is epistemic, not mechanical: the sentence
  never carried a check, and every subsequent design reasoned from it.
related: [refuse-loudly, boundaries-are-asserted-not-documented, present-tense-prose-is-a-claim]
---

**Rule.** Do not write a constraint you are not enforcing. If you must record an
intention, mark it as intent in the same sentence, so nobody reasons from it as
a fact.

**Why.** Downstream designs cite constraints. A constraint that is merely
intended is cited identically to one that is enforced, and the citation chain
grows faster than anyone re-checks the root. By the time it is measured, several
decisions rest on it.

**How to apply.** When you state a security or isolation property, ship the
check with it or write "not enforced" beside it. When you inherit such a
property from another document, measure it before you build on it — and record
the measurement with its date and command.

**Does not apply when.** The property is enforced by something outside your
system that you can name and cite.

## Derivation

Design #517's amendment records the sequence exactly: the rule entered on one
date, was believed from that day, and was false the whole time on the one node
that had a socket, until a read-only probe measured it eleven days later. The
lesson recorded there — "the sentence never carried a check" — is the rule.
