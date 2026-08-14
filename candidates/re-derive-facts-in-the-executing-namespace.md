---
name: re-derive-facts-in-the-executing-namespace
title: Re-derive every host fact inside the namespace that will use it
scope: architecture
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/style.md Tier 2 rule 7 — this one root cause produced a rework cycle repeatedly"
  - "job #384 — a realise target was resolved by a client inside a container where the path was never mounted"
  - "job #384 cycle 2 — a leaf bind resolved the operator's symlink away, so the path existed but was not the thing it claimed to be"
rationale: >
  The single most expensive recurring defect class in this corpus, spanning at
  least six jobs and three designs. It survives repackaging — the namespaces
  changed from containers to native processes and the rule kept biting.
related: [existence-identity-provenance, reachability-by-uid, which-kernel-execs-it, no-content-hash-in-config]
---

**Rule.** A fact about a machine — a path, a device, a socket, a binary, a user
— is only established by asking it from the namespace that will actually run the
code. A check performed anywhere else is a statement about that other place.

**Why.** Provisioning and execution happen in different views far more often
than the code admits: a daemon in a container, a task under a different uid, a
build on one architecture staged for another. A check on the provisioning side
answers a question nobody asked, and it answers it green.

**How to apply.** Provision host state from the deploy path; check it from the
component that will use it, in that component's own view. When the two views
differ, mount, forward or copy explicitly — and let the check fail loudly if the
crossing was not arranged.

**Does not apply when.** The two namespaces are provably identical for the fact
in question, and you can name why.

## Derivation

Job #384's reviewer found the whole chain: the path the worker resolved was
never mounted into the worker's own namespace, so every admitted launch on an
enabled node failed. Cycle 2 found the successor — the mount bound the leaf of a
symlink, so the kernel resolved it at mount time and the client saw a plain
directory at a non-store path. Existence passed; identity did not.
