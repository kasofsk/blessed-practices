---
name: no-per-row-fetching
title: Do not buy a display detail with a request per row
scope: code
altitude: low
portability: universal
confidence: medium
status: candidate
evidence:
  - "job #289 cycle 2 — a grey duration hint that fired up to two hundred task-list requests through the single-threaded core to render one column"
  - "job #256 — a request waterfall flattened from three serialized rounds to one, measured before and after"
rationale: >
  A recurring front-end failure with an unusual amplification here: the
  requests land on a single-threaded actor that is also running the platform, so
  a cosmetic feature becomes a load problem for everything else.
related: [surface-staleness-in-the-ui, one-decision-site, bounded-and-loud]
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

## Derivation

Job #289's cycle-2 review accepted the arithmetic and the interface and rejected
the fetch policy: the feature's primary view "fires up to 200 full task-list
requests through the dispatcher to render a grey duration hint". Job #256 shows
the corrective shape — parallel rounds, measured, with the counts reported.
