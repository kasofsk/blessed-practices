---
type: Blessed Practice
title: "Grants are allow-lists, fail-closed, refused at three layers"
description: "A capability is granted by an explicit allow-list."
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
  The grant mechanisms that landed cleanly all share one shape, arrived at
  independently three times. Naming the shape saves the next author from
  re-deriving it and from getting the empty case backwards.
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

## Where this comes from

Three grant mechanisms in the source retrospective arrived independently at
the same three-layer shape, and reviews credited the later ones for copying
the earlier shape exactly rather than inventing a second style. The deploy-
side pre-flight was added after a case where an operator following the
documented procedure would have got a booting daemon without the capability
instead of a named refusal.

## Related

- [One decision site per question](one-decision-site.md)
- [Prefer a loud refusal to a silent degradation](refuse-loudly.md)
- [Validate everything first, then mutate](validate-before-you-mutate.md)
