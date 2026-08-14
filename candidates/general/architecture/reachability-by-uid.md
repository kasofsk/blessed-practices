---
type: Blessed Practice
title: "What a process is told is not what its uid may open"
description: "An environment-composition guarantee bounds what a process is *told*. It never bounds what its uid may *open*. Capability questions are answered by probing as that uid, on that machine."
status: draft
tags:
  - bucket/general
  - scope/architecture
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  A security boundary was stated, believed, and false the whole time on the one
  node that mattered. The finding generalises: environment composition bounds
  disclosure, never capability.
---

**Rule.** An environment-composition guarantee bounds what a process is *told*.
It never bounds what its uid may *open*. Capability questions are answered by
probing as that uid, on that machine.

**Why.** Filesystem ownership, group membership, keychains, sockets and agent
sockets are all reachable without any environment variable naming them. A
launch audit sees flags, and a capability that arrives by ownership was never a
flag.

**How to apply.** When you claim a task cannot reach something, write the probe
that tries to reach it as the task's own uid, on a real node, and record the
result with a date. Prefer removing the capability (a different uid, a
namespace) over documenting that nobody will use it.

**Does not apply when.** The isolation boundary is a kernel one you have
already tested — then cite the test, not the intention.

## Where this comes from

A rule stating that a class of task could not reach a particular socket
entered the codebase, was cited by later designs, and was false the whole time
on the one machine that had one. The mechanism was ordinary: the client read
its own configuration from the home directory and found a socket owned by the
same user. Eleven days passed between the claim and the probe that measured
it.

## Related

- [An unenforced intention gets read as a statement of fact](unenforced-intentions-become-believed-facts.md)
- [Grants are allow-lists, fail-closed, refused at three layers](fail-closed-allow-lists.md)
- [Re-derive every host fact inside the namespace that will use it](re-derive-facts-in-the-executing-namespace.md)
