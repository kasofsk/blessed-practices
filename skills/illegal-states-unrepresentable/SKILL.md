---
name: illegal-states-unrepresentable
description: Make illegal states unrepresentable with precise types, discriminated variants, and boundary parsing. Use when a record has state-dependent optional fields, code repeatedly checks that fields agree, constructors can produce invalid values, or persistence-shaped nullability leaks into domain logic.
---

# Illegal States Unrepresentable

## Core principle

Represent domain rules in types so callers cannot construct invalid combinations.
Use runtime validation at untyped boundaries, then pass only valid domain values
inward.

## Model states as variants

Give each meaningful state its own discriminated variant containing exactly the
fields that state requires. Do not combine a status with optional fields whose
presence depends on that status, or encode mutually exclusive states as
independent booleans.

Use an optional only when a value may be independently absent. Do not copy
persistence nullability into the domain model when absence has a state-specific
meaning.

## Parse at boundaries

Parse external data into precise internal types once, at the boundary. Return a
valid domain value or an explicit failure; do not pass partially validated data
inward for each consumer to check again.

Keep database rows, wire schemas, and vendor types at the edge. Map their nullable
or stringly typed fields into domain variants and values. Preserve useful database
constraints as an additional defense for stored data.

## Enforce invariants during construction

Use constructors and parsers for values with rules. Reject invalid input during
construction and make recoverable failure visible in the return type. Once
constructed, a value should not require repeated validation.

Use distinct value types for distinct concepts such as identifiers, units, and
bounded values. In structurally typed languages, use branding or the idiomatic
equivalent when aliases do not create a real distinction.

## Make branching exhaustive

Switch over discriminated variants exhaustively so adding a state exposes every
decision that must handle it. Avoid fallback branches that silently treat a new
state as an existing one.

Use assertions for contradictions at trusted boundaries and invariants the type
system cannot express. Repeated assertions in ordinary domain logic indicate
that the representation is too broad.
