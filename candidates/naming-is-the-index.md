---
name: naming-is-the-index
title: Names are the index an agent navigates by
scope: code
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/style.md Tier 2 rule 4 — suffixes in descending significance, no abbreviations, helpers prefixed with their caller"
  - "job #250, #344 — reviews explicitly checking the suffix ordering and helper prefixes of new constants"
  - "job #384 cycle 2 — a constant renamed to match the ordering convention as a review outcome"
rationale: >
  A convention whose justification is specific to agent-driven development:
  agent-written code is navigated by grep, so predictable names are the index.
  Reviewers here check it by name, which is evidence it is operational rather
  than aspirational.
related: [no-duplication-threshold, one-decision-site, function-length-cap]
---

**Rule.** Units and qualifiers are suffixes in descending significance, so
related names sort together. No abbreviations in identifiers. A helper carries
its caller's name as a prefix, so the call tree is readable from the names alone.

**Why.** Both agents and humans find code by searching names. A consistent
ordering makes a prefix search enumerate a family; an inconsistent one makes
every name its own special case. Helper prefixes mean a grep for the caller
finds its whole implementation.

**How to apply.** Write the most significant term first and qualify rightward.
When adding a constant, look for its siblings and match their shape. Rename on
sight during review — this is cheap and compounding.

**Does not apply when.** The name is dictated by an external interface.

## Derivation

Reviews in this corpus check the convention explicitly and by rule number,
including approving a set of new constants for following it and requiring one
rename. The justification given in the rule is the agent-specific one: names are
the index.
