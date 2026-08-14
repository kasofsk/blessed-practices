---
type: Blessed Practice
title: "Do not buy a display detail with a request per row"
description: "A list view fetches per list, not per row."
status: draft
tags:
  - bucket/general
  - scope/code
  - altitude/low
  - portability/universal
  - confidence/medium
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  A recurring front-end failure with an unusual amplification here: the
  requests land on a single-threaded actor that is also running the platform, so
  a cosmetic feature becomes a load problem for everything else.
---

**Rule.** A list view fetches per list, not per row. If a detail is not in the
list payload, either add it to the payload or do not display it.

**Why.** Per-row fetching scales with data volume and lands hardest on the
largest, most-used views. Where the backend is a single writer or a shared
actor, the cost is not confined to the page — it competes with the system's real
work.

**How to apply.** Measure the request count for the view before and after.
Prefer extending the list payload with a computed field over fanning out. Where
a fan-out is genuinely needed, bound it and say what the bound is in the code.

**Does not apply when.** The view is a detail page for a single entity.

## Where this comes from

One review accepted a feature's arithmetic and its interface and rejected its
fetch policy: the primary view fired up to two hundred requests through a
single-threaded component to render one grey hint. A separate change shows the
corrective shape — three serialized rounds flattened into one, with the
request counts measured before and after and reported.

## Related

- [An interface that cannot prove freshness must not imply it](surface-staleness-in-the-ui.md)
- [Everything is bounded, and the bound is loud](../architecture/bounded-and-loud.md)
- [One decision site per question](../architecture/one-decision-site.md)
