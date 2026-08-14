---
type: Blessed Practice
title: "Names are the index an agent navigates by"
description: "Units and qualifiers are suffixes in descending significance, so related names sort together."
status: draft
tags:
  - bucket/general
  - scope/code
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  A convention whose justification is specific to agent-driven development:
  agent-written code is navigated by grep, so predictable names are the index.
  Reviewers here check it by name, which is evidence it is operational rather
  than aspirational.
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

## Where this comes from

Reviews in the source corpus check this convention explicitly and by rule
number, including approving a set of new constants for following it and
requiring one rename to match. The justification given is the agent-specific
one: code written by agents is navigated by search, so predictable names are
the index.

## Related

- [A numeric function-length cap, enforced](function-length-cap.md)
- [One decision site per question](../architecture/one-decision-site.md)
- [Zero duplication, because agent-written code clones readily](no-duplication-threshold.md)
