---
name: no-content-hash-in-config
title: A content hash never enters operator-typed config
scope: architecture
altitude: low
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/style.md Tier 2 rule 9"
  - "design #367 — a content-addressed toolchain path in node configuration"
  - "crates/worker/src/config.rs — parsers refuse a store hash by name in several settings"
rationale: >
  A narrow rule with a distinctive failure signature: it keeps working against
  the previous artifact until a garbage collection, then fails with a not-found
  on a path nobody typed recently.
related: [re-derive-facts-in-the-executing-namespace, refuse-loudly]
---

**Rule.** Configuration a human types names stable paths. Content-addressed
paths are resolved at the moment of use by whatever already resolves host paths.

**Why.** A content-addressed path changes with every rebuild of what it names.
Config holding one silently keeps pointing at the stale artifact, so the change
appears to have no effect — and then, at an unrelated garbage collection, fails
with an unattributable not-found.

**How to apply.** Refuse a hash-shaped path at parse time, naming the setting.
Point config at the stable path the platform's own activation maintains, and let
the consumer canonicalize.

**Does not apply when.** The value is machine-generated and machine-consumed and
never survives a rebuild — a lockfile, not a config file.

## Derivation

The rule is stated in this project's style tier with #367 as the record; several
worker settings now carry parse-time refusals of store hashes, each tested with
its own case.
