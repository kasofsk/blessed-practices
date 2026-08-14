---
name: existence-identity-provenance
title: Existence, identity and provenance are three separate questions
scope: architecture
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #384 — three failures in one job: mounted nowhere (existence), symlink resolved away (identity), fixed by asserting the canonicalized target lands under the expected root (provenance)"
  - "docs/reference/style.md Tier 2 rule 7"
rationale: >
  A refinement of the namespace rule that earns its own card because the three
  checks look interchangeable and are not — passing one is routinely reported as
  passing all three.
related: [re-derive-facts-in-the-executing-namespace, reachability-by-uid, assertions-that-can-fail]
---

**Rule.** For any external artifact, ask three questions and write three checks:
is it there, is it the thing it claims to be, and did it arrive by a route that
survives the next rebuild.

**Why.** `exists()` answers the first and is routinely cited as answering all
three. A path can exist and be the wrong artifact; it can be the right artifact
and be there by an accident that the next deploy removes.

**How to apply.** Existence: stat it from the right namespace. Identity:
canonicalize and assert the resolved target has the property you need — under
the expected root, of the expected architecture, matching the expected hash
class. Provenance: assert it was placed by the mechanism you rely on, not merely
found.

**Does not apply when.** The artifact is created and consumed within one
process's lifetime.

## Derivation

Job #384 is the worked example and the three-way split is taken from its
review; job #480 later added the architecture case — a binary staged on one
machine and executed on another passes existence and identity and still fails,
which is why which-kernel-execs-it exists as a separate card.
