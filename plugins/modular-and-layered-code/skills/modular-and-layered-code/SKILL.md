---
name: modular-and-layered-code
description: Architect so a future agent can act at a single layer — strict tested contracts between layers, testing concentrated at domain boundaries, pure logic kept free of I/O, and impurity confined to the edges. Use when designing module boundaries or abstractions, deciding where to concentrate test effort, extracting side effects out of logic, or judging whether an abstraction is worth building before it is needed.
---

# Modular and Layered Code

## Core principle

Architect code so that a future agent (human or AI) making a modification or
improvement can **act at a single layer**. A change to one concern should land
in one place, behind one contract — without the agent needing to understand or
touch the rest of the system.

## How we get there

### 1. Strict contracts between layers

Layer boundaries are defined by explicit, well-specified contracts — not by
convention or tribal knowledge. An agent working inside a layer should be able
to trust the contract above and below it completely, so the contract itself
carries the knowledge that would otherwise require reading the whole codebase.

### 2. Well-defined, well-tested abstractions

Abstractions at these boundaries are first-class artifacts: deliberately
designed, documented, and covered by tests that pin down their behavior. The
tests are what make the contract *strict* rather than aspirational.

### 3. Accept some "premature" abstraction — selectively

We are okay with a little premature optimization in this specific regard: when
it's likely that future iterations or feature fixes will be touching a system,
investing early in its contracts and abstractions pays off. This is a
calibrated bet, not a license to abstract everything — the trigger is
*expected future churn*.

### 4. Test hardest at domain boundaries

Concentrate testing effort at the domain boundaries. Boundary tests are what
let an agent modify one layer with confidence that it hasn't broken its
neighbors — they are the enforcement mechanism for the contracts in (1).

### 5. Keep impure stuff out of pure logic

Do as good a job as possible of keeping I/O and other impure, side-effecting
concerns (network calls, disk, auth, clocks, randomness, etc.) out of pure
logic functions. Pure functions are the easiest code for any agent to reason
about, test, and safely change.

### 6. Contain the blast radius of impurity

Where I/O and non-pure code *must* exist, be thoughtful about confining it to
deliberate, well-known locations (edges/shells of the system). The goal is
that the impure surface area is small, obvious, and doesn't leak into — or
destabilize — the pure core.

## Why this matters

Every one of these points serves the same end: minimizing how much of the
system an agent must load into its head (or context window) to make a correct
change. Strict contracts and boundary tests localize *knowledge*; purity and
blast-radius containment localize *risk*.
