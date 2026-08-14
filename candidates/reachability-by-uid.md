---
name: reachability-by-uid
title: What a process is told is not what its uid may open
scope: architecture
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "design #517 — a host task inheriting only PATH and HOME still resolved a docker client's active context under that HOME to a socket its own user owned"
  - "job #516 — a read-only probe measured on a real node what a rule had asserted for eleven days"
rationale: >
  A security boundary was stated, believed, and false the whole time on the one
  node that mattered. The finding generalises: environment composition bounds
  disclosure, never capability.
related: [re-derive-facts-in-the-executing-namespace, unenforced-intentions-become-believed-facts, fail-closed-allow-lists]
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

## Derivation

Design #517 records the eleven days between a rule entering the tree and job
#516's probe measuring it false. The mechanism was ordinary: the client read its
own configuration from `HOME` and found a socket owned by the same user.
