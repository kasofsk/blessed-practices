# Domain modelling

What goes inside the core, and what shape it takes. [layering.md](./layering.md) is the structure; this is the content.

The tactical patterns below were written for an object model in which behaviour hangs off entities. Most of them survive a move to a functional core unaltered, because most of them are about *where a rule lives* rather than about method dispatch. Where the object-oriented spelling is doing real work, it is said so explicitly.

## The language is the model

**A term means one thing, everywhere it appears** — in the code, in the docs, and in the sentence someone says out loud. This is the ubiquitous language, and it is the cheapest correctness tool available: a disagreement about a word is a disagreement about the machine, surfaced before it is built.

- **The same noun, or a different noun.** A concept called `Ticket` in the core and `Job` in an adapter has two names because somebody declined to decide whether they are the same thing. Rename in one change; a translation table between layers is a permanent tax on every future reader.
- **A qualifier is a missing distinction.** When prose has to say "the *scheduler's* ready set" to be unambiguous, the model is short a concept or carrying an overloaded one. The prose is doing work the types should do.
- **A concept is defined once and mentioned freely.** A term explained in two places drifts in one of them, and the reader cannot tell which. Mentions are free; second definitions are not.

## Invariants first, records second

An **aggregate** is a cluster of data treated as one unit for the purpose of consistency: it has a root, outside references address only the root, and every invariant it claims holds at the end of every operation that touches it.

- **Model true invariants in consistency boundaries.** The point of the pattern is the boundary, not the clustering. Data with no invariant binding it together does not need to be one unit, and making it one buys contention for nothing.
- **Design small aggregates.** "Limit the Aggregate to just the Root Entity and a minimal number of attributes … The correct minimum is however many are necessary, and no more" (Vernon). A large aggregate is a large lock, a large replay, and unrelated changes queueing behind each other.
- **Reference other aggregates by identity.** Hold the id, not the object. A live reference is an invitation to traverse and mutate across a boundary the invariants do not cover, and it turns the serialized form into a graph.
- **One consistency argument per commit.** Whatever commits — a database transaction, a journaled decision, an append to a log — either carries the whole argument or does not happen. The canonical form of this rule is one aggregate per transaction; the general form is what matters, because what commits is not always a transaction. What stays forbidden either way is spreading one invariant across two commits and trusting the second to arrive.
- **Outside the boundary, consistency is eventual by design.** "Just because you are given a use case that calls for maintaining consistency in a single transaction doesn't mean you should do that" (Vernon). Say which invariants are immediate and which are eventual — the ones nobody classified are the ones that break.

## Entities, values, and identifiers

- An **entity** has an identity that survives change: two entities are the same when their identifiers match, whatever their fields say.
- A **value object** has no identity. It is equal by its contents, it is immutable, and it is where an invariant *about a value* lives — a quantity that cannot be negative, an identifier that must match a shape.
- **Prefer the value object to the primitive.** A concept carried as a bare string or number is a concept the compiler cannot check and grep cannot find. Primitive obsession is how one id gets passed where another belongs, in a codebase where both are integers and the argument list is positional.

In a structurally typed language two aliases of the same primitive are the same type, so the distinction has to be branded — a nominal wrapper or a phantom tag — to exist at all.

## Make illegal states unrepresentable

> "Use a data structure that makes illegal states unrepresentable. Model your data using the most precise data structure you reasonably can." — Alexis King

- **A field meaningful in only one state belongs to that state's variant**, not to the record as an optional. An optional is a runtime question asked at every use site; a variant is a compile-time answer given once.
- **Switch every discriminated union exhaustively**, with a default arm that proves the switch total. This is what makes adding a case a compile error at every site that must change.
- **A constructor that cannot refuse is a constructor that lies.** Build the refusal into the type — a parse returning either the value or a reason — rather than a validate call the caller is trusted to remember. Prefer a returned refusal to a thrown one: a throw is an invisible control-flow edge, and a returned refusal is one the compiler can insist the caller handle.

## Behaviour belongs with the data

Fowler's warning stands: an anemic model has "hardly any behavior on these objects, making them little more than bags of getters and setters", and it "incur[s] all of the costs of a domain model, without yielding any of the benefits". Evans' diagnosis of how it happens is the sharper half — "the more common mistake is to give up too easily on fitting the behavior into an appropriate object, gradually slipping toward procedural programming".

**The smell is dispersal, not the absence of methods.** A rule about an order that lives in an HTTP handler, an adapter or an orchestration loop is the anti-pattern in any paradigm. A rule expressed as a pure function beside the type it governs is not: data and process are together in the unit that matters, which is the module. What the object-oriented spelling buys — the rule cannot be bypassed, because the state it guards is reachable only through it — has to be bought some other way in a functional core, and the usual way is an enforced boundary plus a single writer.

*The test:* can the rule be stated by naming one module? If answering needs an adapter or a loop, it has leaked, and moving it is the whole fix.

## Domain services and application services

Two things share the word *service*, and conflating them is how business logic ends up in orchestration code.

- A **domain service** is a domain operation that belongs to no single entity — it reads several, and it stays inside the domain, ideally pure.
- An **application service** orchestrates: gather, call, commit, dispatch. It is thin, it holds no rules, and it holds no domain state.

*The trigger to act:* an application service that has grown a conditional over domain state has stopped being one. The conditional is a decision, and it belongs in the domain.

## Persistence

The rule is persistence ignorance: the domain takes no dependency on storage — no ORM base classes, no schema-shaped records, no field that exists because a serializer wanted it. Palermo's version is blunter: "The database is not the center. It is external."

The **repository** is one way to buy that ignorance — a collection-like interface over aggregate roots, implemented outside the domain. It is not the only way, and it is worth the indirection only when there is real storage to be ignorant of. A repository over an in-memory structure, or over a log the core already folds, is an abstraction with nothing on the far side; keep the ignorance and skip the pattern.

When something other than the writer needs to query state, give it a projection with its own shape rather than a query interface into the aggregate. A read model is a different question answered separately, not the same aggregate seen through a wider hole.

## Events and effects

An **event** is a fact: something that happened, named in the past tense, in the language above. An **effect** is an instruction to the world.

Keep them apart in naming and in kind. `OrderPlaced` is a fact and stays true forever; `ChargeCard` is an instruction that can fail, be retried, or arrive twice. A record of instructions cannot be replayed into state, and a stream of facts cannot be executed — collapsing the two produces a log that is neither.

## Bounded contexts

A **bounded context** is the boundary within which one model and one language apply. The pattern exists because "total unification of the domain model for a large system will not be feasible or cost-effective" (Fowler): two groups use the same word for different things, and a single model serving both serves neither.

Every external system is a foreign context, which is why the translation at each port is an anti-corruption layer whether or not it is called one ([layering.md](./layering.md)). A foreign identifier enters as your own type, not as theirs.

*The trigger to draw a second context:* a second meaning for a modelled word that cannot be renamed away — the same noun genuinely meaning two things to two audiences. That is a design decision, not a refactor, and drawing the boundary before the evidence arrives is drawing it in the wrong place.

## Sources

- [Evans, *Domain-Driven Design*](https://www.domainlanguage.com/ddd/) — the source of the language, aggregate, entity, value object, service and bounded context patterns.
- [Vernon, *Effective Aggregate Design*](https://www.dddcommunity.org/library/vernon_2011/) — the four rules of thumb for aggregate boundaries.
- [Fowler, *AnemicDomainModel*](https://martinfowler.com/bliki/AnemicDomainModel.html) — the anti-pattern, and Evans' diagnosis of how it happens.
- [Fowler, *BoundedContext*](https://martinfowler.com/bliki/BoundedContext.html) — why one model does not scale across audiences.
- [King, *Parse, don't validate*](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/) — precise types, and pushing them to the boundary.
- [Chassaing, *Functional event sourcing decider*](https://thinkbeforecoding.com/post/2021/12/17/functional-event-sourcing-decider) — the pure decide/evolve pair, for a core with no methods to hang behaviour on.
