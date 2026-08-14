---
name: fail-closed-allow-lists
title: Grants are allow-lists, fail-closed, refused at three layers
scope: architecture
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "job #522 — a node-side grant fail-closed at parse, boot and launch, each layer reporting"
  - "job #525 — an empty allow-list grants nobody, and the deploy refuses rather than restarting a daemon that would"
  - "job #403 — an allow-list shaped after an existing one rather than invented fresh"
rationale: >
  The grant mechanisms that landed cleanly all share one shape, arrived at
  independently three times. Naming the shape saves the next author from
  re-deriving it and from getting the empty case backwards.
related: [refuse-loudly, validate-before-you-mutate, one-decision-site]
---

**Rule.** A capability is granted by an explicit allow-list. An absent or empty
list grants nobody. The grant is refused at parse (malformed config is a hard
error), at boot (the declared resource is absent from the granting component's
own view), and at launch (no match means no grant) — and each refusal is
reported.

**Why.** Fail-open allow-lists are indistinguishable from correct ones until the
day they matter. Three layers exist because each catches a different author
error: a typo, a mis-provisioned node, and a mis-scoped request.

**How to apply.** Parse into a typed list, refusing malformed and repeated
entries by name. At boot, check the granted resource exists in the view that
will bind it, and refuse the boot if not. At launch, match on the full key and
mount nothing on a miss. Reuse the parser and the shape of the existing grant
rather than writing a second style.

**Does not apply when.** The capability is universal by design — then it is not
a grant and should not be spelled like one.

## Derivation

Job #522's review lists the three layers as the accepted design and credits the
change for following an existing grant's shape "exactly", with each divergence
stated and justified in the commit message. Job #525 added the deploy-side
pre-flight so an operator gets a named refusal instead of a daemon that boots
without the capability.
