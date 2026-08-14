---
type: Blessed Practice
title: "Re-derive every host fact inside the namespace that will use it"
description: "A fact about a machine — a path, a device, a socket, a binary, a user — is only established by asking it from the namespace that will actually run the code."
status: draft
tags:
  - bucket/general
  - scope/architecture
  - altitude/high
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  The single most expensive recurring defect class in this corpus, spanning at
  least six jobs and three designs. It survives repackaging — the namespaces
  changed from containers to native processes and the rule kept biting.
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

## Where this comes from

This single root cause produced rework across at least six changes in the
source retrospective and survived a complete repackaging of the component
involved. The clearest instance: a path was resolved by a client running
inside a container where that path was never mounted, so every admitted
request failed — and the follow-up fix bound the wrong end of a symlink, so
the path then existed but was not the artifact it claimed to be.

## Related

- [A content hash never enters operator-typed config](no-content-hash-in-config.md)
- [Ask each artifact the question its own executor asks](which-kernel-execs-it.md)
- [Existence, identity and provenance are three separate questions](existence-identity-provenance.md)
- [What a process is told is not what its uid may open](reachability-by-uid.md)
