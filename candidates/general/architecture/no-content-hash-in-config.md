---
type: Blessed Practice
title: "A content hash never enters operator-typed config"
description: "Configuration a human types names stable paths."
status: draft
tags:
  - bucket/general
  - scope/architecture
  - altitude/low
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  A narrow rule with a distinctive failure signature: it keeps working against
  the previous artifact until a garbage collection, then fails with a not-found
  on a path nobody typed recently.
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

## Where this comes from

A content-addressed toolchain path in operator-typed configuration kept
working against the previous artifact until a garbage collection removed it,
at which point it failed with a not-found on a path nobody had typed recently.
The durable answer was parse-time refusal of hash-shaped values, with the
setting named in the message.

## Related

- [Prefer a loud refusal to a silent degradation](refuse-loudly.md)
- [Re-derive every host fact inside the namespace that will use it](re-derive-facts-in-the-executing-namespace.md)
