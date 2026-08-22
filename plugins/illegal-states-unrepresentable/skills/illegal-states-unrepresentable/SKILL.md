---
name: illegal-states-unrepresentable
description: Make illegal states unrepresentable with precise types, discriminated variants and boundary parsing. Use when a record has state-dependent optional fields, code repeatedly checks that fields agree, constructors can produce invalid values, or persistence-shaped nullability leaks into domain logic.
---

# Make illegal states unrepresentable

If the program knows that a combination of values is invalid, its types should
not offer that combination to callers. A runtime assertion is the last line of
defence at an untyped boundary, not the representation of a rule the program
already understands.

## One variant per meaningful state

A field that exists only in one state belongs to that state's variant. Prefer a
discriminated union whose arms contain everything required in that state over a
record combining a status with optional fields.

The test is the number of questions every consumer must ask. If code checks
`status`, then asks whether the fields implied by that status are present, the
type has represented the status twice. Put the fields under the discriminant so
one exhaustive switch answers both questions.

Do not encode mutually exclusive concepts as independent booleans. Do not use
an optional merely because persistence represents absence as `NULL`. Optional
means independently absent; a variant means absent for a reason.

## Parse once at the boundary

External data may be incomplete, contradictory or loosely typed. Keep that
shape at the edge and translate it once into the precise internal type. The
parser either returns a legal value or a refusal; it never hands partially
validated data inward for every consumer to check again.

Database row types, wire schemas and vendor objects describe transports, not
the domain. Their nullability and stringly-typed states should end at the
mapping boundary. A valid database constraint is still worth expressing in the
application type: the constraint protects stored data, while the type protects
code that constructs and transforms it.

## Put invariants in construction

Use constructors and parsers for values with rules. A constructor that can
receive invalid input must refuse it, and its return type should make that
refusal visible when callers are expected to recover. Once constructed, the
value should need no repeated validation.

Prefer distinct value types for distinct concepts, especially identifiers,
units and bounded values. In structurally typed languages, use branding or an
equivalent mechanism when aliases alone do not create a distinction.

## Let control flow follow the type

Switch discriminated unions exhaustively. Adding a state should make every
decision that must understand it fail to compile. Avoid fallback branches that
silently reinterpret a new state as an old one.

Assertions remain appropriate for contradictions at trusted boundaries and
for invariants the type system cannot express. An assertion repeated across
ordinary business logic is evidence that the representation is too broad.

## The cost of a broad representation

Every representable illegal state multiplies the paths readers, tests and
future changes must consider. It invites defensive checks, contradictory
fallbacks and fixtures for combinations that should never compile. Precise
types pay the validation cost once and let the rest of the program reason only
about states that can actually exist.
