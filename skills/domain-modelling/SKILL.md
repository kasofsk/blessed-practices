---
name: domain-modelling
description: Shape the contents of the domain core — ubiquitous language, aggregates as consistency boundaries, entities versus value objects, making illegal states unrepresentable, where behaviour lives, persistence ignorance, events versus effects, and bounded contexts. Use when modelling a business concept, designing domain types or an aggregate, choosing between an optional field and a variant, naming a domain concept, or reviewing a domain model.
---

# Domain modelling

What goes inside the core, and what shape it takes. The **layering** practice (`layering@blessed-practices`) is the structure; this is the content.

## The language is the model

A term means one thing everywhere it appears — in the code, in the docs, and in the sentence someone says out loud.

- **The same noun, or a different noun.** A concept called `Ticket` in the core and `Job` in an adapter has two names because somebody declined to decide whether they are the same thing. A translation table between layers is a permanent tax on every future reader.
- **A qualifier is a missing distinction.** When prose has to say "the *scheduler's* ready set" to be unambiguous, the model is short a concept or carrying an overloaded one.

## Invariants first, records second

An aggregate is a cluster of data treated as one unit for consistency: it has a root, outside references address only the root, and every invariant it claims holds at the end of every operation that touches it.

- **Model true invariants in consistency boundaries.** Data with no invariant binding it together does not need to be one unit, and making it one buys contention for nothing.
- **Design small aggregates.** The correct size is however much the invariants require, and no more. A large aggregate is a large lock and a large replay.
- **Reference other aggregates by identity.** Hold the id, not the object: a live reference is an invitation to traverse and mutate across a boundary the invariants do not cover.
- **One consistency argument per commit.** Whatever commits — a transaction, a journaled decision, an append to a log — carries the whole argument or does not happen. What is forbidden is spreading one invariant across two commits and trusting the second to arrive.
- **Outside the boundary, consistency is eventual by design.** Say which invariants are immediate and which are eventual; the ones nobody classified are the ones that break.

## Entities, values, and identifiers

- An **entity** has an identity that survives change: two are the same when their identifiers match, whatever their fields say.
- A **value object** has no identity. It is equal by its contents, it is immutable, and it is where an invariant about a value lives.
- **Prefer the value object to the primitive.** A concept carried as a bare string or number is one the compiler cannot check and grep cannot find, and it is how one id gets passed where another belongs.

In a structurally typed language two aliases of the same primitive are the same type, so the distinction has to be branded to exist at all.

## Make illegal states unrepresentable

- **A field meaningful in only one state belongs to that state's variant**, not to the record as an optional. An optional is a runtime question asked at every use site; a variant is a compile-time answer given once.
- **Switch every discriminated union exhaustively**, with a default arm that proves the switch total. Adding a case is then a compile error at every site that must change.
- **A constructor that cannot refuse is a constructor that lies.** Build the refusal into the type — a parse returning either the value or a reason — and prefer a returned refusal to a thrown one, which the compiler cannot insist the caller handle.

## Behaviour belongs with the data

A model with no behaviour on it — records that are bags of getters and setters, with every rule in a service — pays all the costs of a domain model and collects none of the benefits.

**The smell is dispersal, not the absence of methods.** A rule about an order living in a request handler, an adapter or an orchestration loop is the anti-pattern in any paradigm; the same rule as a pure function beside the type it governs is not. What methods buy — the state a rule guards is reachable only through it — has to be bought some other way in a functional core, usually by an enforced boundary plus a single writer.

*The test:* can the rule be stated by naming one module? If answering needs an adapter or a loop, it has leaked.

## Domain services and application services

- A **domain service** is a domain operation belonging to no single entity — it reads several, and it stays inside the domain, ideally pure.
- An **application service** orchestrates: gather, call, commit, dispatch. It is thin, it holds no rules, and it holds no domain state.

An application service that has grown a conditional over domain state has stopped being one.

## Persistence

The domain takes no dependency on storage: no ORM base classes, no schema-shaped records, no field that exists because a serializer wanted it.

A repository is one way to buy that ignorance, and it is worth the indirection only when there is real storage to be ignorant of. Over an in-memory structure, or over a log the core already folds, it is an abstraction with nothing on the far side.

When something other than the writer needs to query state, give it a projection with its own shape rather than a query interface into the aggregate.

## Events and effects

An **event** is a fact: something that happened, named in the past tense. An **effect** is an instruction to the world.

`OrderPlaced` stays true forever; `ChargeCard` can fail, be retried, or arrive twice. A record of instructions cannot be replayed into state, and a stream of facts cannot be executed.

## Bounded contexts

A bounded context is the boundary within which one model and one language apply. Draw a second one when a modelled word has a second meaning that cannot be renamed away — the same noun genuinely meaning two things to two audiences. Earlier than that puts the boundary in the wrong place.

Every external system is a foreign context: its identifiers enter as your own types, not as theirs.
