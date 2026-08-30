---
name: diminishing-returns
description: Pursue the highest-value work first and stop when the expected value of the next improvement no longer justifies its full cost. Use when choosing scope, comparing implementations, planning iterations, reviewing polish or hardening work, or deciding whether an edge case warrants added complexity.
---

# Diminishing Returns

## Core principle

Pursue the highest-value work first. Unless the operator explicitly asks for a
more complete, optimized, or exhaustive result, stop when the expected value of
the next improvement no longer justifies its full cost.

## Find the value-dense path

Before expanding the solution, identify the outcome that matters and the
smallest coherent approach that delivers it. Prefer work that unlocks the main
use case, removes the largest constraint, reduces the most credible risk, or
creates the clearest feedback. Defer polish, flexibility, abstraction, and rare
edge cases when their cost is disproportionate to their present value.

When several approaches satisfy the request, prefer the one with the best
value-to-effort tradeoff, including future maintenance and operational
complexity. Do not build speculative capability merely because it might
eventually be useful.

## Stop when the next increment is not worthwhile

Once the requested outcome works well for the dominant cases, assess further
improvements separately. Continue only when their likely benefit justifies
their design, implementation, complexity, runtime, and maintenance costs. It is
acceptable by default to leave lower-value improvements undone; briefly name a
material omission when the operator could otherwise mistake the result for
exhaustive coverage.

Do not turn this into a license for incomplete core behavior, hidden hazards,
or knowingly fragile shortcuts. Explicit requirements, security boundaries,
data integrity, irreversible harm, and inexpensive safeguards against credible
failures can outweigh the default stopping rule.

## Work with known limits

Apply `design-with-known-limits` when the stopping point creates a meaningful
correctness, reliability, or operational boundary. Diminishing-returns thinking
chooses where investment stops; known-limits thinking makes that boundary and
its consequences honest. Accepting a stopping point does not justify concealing
the resulting limit.

## Why this matters

Engineering effort is finite, while possible improvement is not. Concentrating
on the value-dense portion of the problem produces useful outcomes sooner and
preserves attention for work with greater leverage. A deliberately sufficient
solution is often better than a theoretically complete one whose marginal gains
do not repay its complexity and delay.
