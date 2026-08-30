---
name: 80-20-rule
description: Pursue the small set of work that captures most of the practical value, and stop when additional effort reaches diminishing returns. Use when choosing scope, comparing implementations, planning iterations, reviewing polish or hardening work, or deciding whether an edge case justifies added complexity.
---

# 80/20 Rule

## Core principle

Prefer the solution that captures most of the available value with a modest
share of the total possible effort. Unless the operator explicitly asks for a
more complete, optimized, or exhaustive result, diminishing returns are an
accepted reason to stop.

The numbers are a heuristic, not a measurement requirement. Do not spend time
proving that a choice is literally 80/20; identify the few decisions or pieces
of work that dominate the outcome and prioritize those.

## Find the value-dense path

Before expanding the solution, identify the outcome that matters and the
smallest coherent approach that delivers it. Prefer work that unlocks the main
use case, removes the largest constraint, reduces the most credible risk, or
creates the clearest feedback. Defer polish, flexibility, abstraction, and rare
edge cases when their cost is disproportionate to their present value.

When several approaches satisfy the request, prefer the one with the best
value-to-effort ratio, including future maintenance and operational complexity.
Do not build speculative capability merely because it might eventually be
useful.

## Stop at diminishing returns

Once the requested outcome works well for the dominant cases, assess the next
increment separately. Continue only when its likely benefit justifies its full
cost. It is acceptable by default to leave lower-value improvements undone;
briefly name a material omission when the operator could otherwise mistake the
result for exhaustive coverage.

Do not turn this into a license for incomplete core behavior, hidden hazards,
or knowingly fragile shortcuts. Explicit requirements, security boundaries,
data integrity, irreversible harm, and inexpensive safeguards against credible
failures can outweigh the heuristic.

## Work with known limits

Apply `design-with-known-limits` when the stopping point creates a meaningful
correctness, reliability, or operational boundary. The 80/20 rule chooses where
investment stops; known-limits thinking makes that boundary and its consequences
honest. Accepting diminishing returns does not justify concealing the resulting
limit.

## Why this matters

Engineering effort is finite, while possible improvement is not. Concentrating
on the value-dense portion of the problem produces useful outcomes sooner and
preserves attention for work with greater leverage. A deliberately sufficient
solution is often better than a theoretically complete one whose marginal gains
do not repay its complexity and delay.
