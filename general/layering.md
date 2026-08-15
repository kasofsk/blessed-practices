# Layering

Where code goes, and which way its dependencies point.

Four traditions describe the same arrangement — Evans' layered architecture, Cockburn's ports and adapters, Palermo's onion, Martin's clean architecture. They disagree about how many rings to draw and what to call them. They agree on the rule below, and the rule is the part that binds.

## The rule: dependencies point inward

> "Source code dependencies can only point inwards. Nothing in an inner circle can know anything at all about something in an outer circle." — Robert C. Martin

Palermo's phrasing is "all coupling is toward the center"; Evans' is that a layer "depends only on the layers below"; Cockburn states the consequence — "Code pertaining to the inside part should not leak into the outside part" — so that the same application can "equally be driven by users, programs, automated test or batch scripts". One rule, four dialects.

Four things follow, and between them they are the whole of the discipline.

**Control flow may point outward; the dependency may not.** The core reaches the world constantly. It does so through an interface the core declares and something outside implements. That inversion is the entire mechanism, and everything else here is a consequence of it.

**A type is a dependency, and so is a name.** A core function whose parameter is a vendor's handle is coupled to that vendor without importing it, and a field named after their concept has taken their vocabulary. Both change when they change.

**The rule is about the graph, not the file.** A helper three imports deep leaks as effectively as a direct import, so enforce reachability over the module graph rather than a per-file import lint. Every per-file check passes on a small path-joining utility that touches the filesystem and is called by the core.

**Inward is a direction, not a folder count.** Two layers with a boundary that is actually enforced beat five with nominal ones. The value is in what the rule forbids, and a boundary nothing checks forbids nothing.

## The layers

| Layer | Owns |
|---|---|
| **Domain** | "representing concepts of the business, information about the business situation, and business rules … the heart of business software" (Evans) |
| **Application** | "Defines the jobs the software is supposed to do and directs the expressive domain objects to work out problems … kept thin. It does not contain business rules or knowledge" (Evans) |
| **Adapters** | translation in both directions, one per external system, no rules of its own |
| **Infrastructure** | the world itself — databases, queues, clocks, other people's services |

**The application layer decides nothing.** Its job is sequencing: gather what the decision needs, call into the domain, commit, dispatch. A conditional there that inspects domain state is a decision in the wrong place — invisible to whatever tests the domain, and duplicated the day a second caller appears.

**Adapters hold no rules.** Protocol, encoding, transport-level retry, translation — nothing a domain expert would recognise as a decision. A rule in an adapter is one nobody can find and nobody can test, and it is duplicated the moment a second adapter appears.

**A layer is logical; a tier is physical.** A layer is a code-structuring device; a tier is where the code runs. Whether two layers share a process, a host or neither is a deployment question and it moves no boundary here. Conflating the two is how both "we are not distributed, so we do not need layers" and "we are distributed, so the network is our boundary" get argued.

## Strict, not relaxed

A strict layered system lets each layer depend only on the one below it; a relaxed one lets it depend on everything below. **Prefer strict**, in the three forms a violation actually takes:

- the domain imports no adapter, no framework, no I/O library, and no ambient capability — clock, randomness, environment, network;
- an adapter never imports another adapter: two adapters that need each other are either one adapter or a coordination that belongs above both;
- nothing reaches the world except through the layer that owns that boundary.

*Why strict:* relaxed layering is not a weaker rule, it is the absence of one. Once any module may call anything below it, the import graph is the documentation, and the import graph is what nobody reads.

## What crosses a boundary

**Plain data.** "Isolated, simple, data structures are passed across the boundaries" (Martin). A live object carries behaviour, identity and lazily-reachable state across a seam the reader cannot audit, and it makes the receiving side depend on the sender's class rather than on its data.

**Parsed, not validated.** "Get your data into the most precise representation you need as quickly as you can. Ideally, this should happen at the boundary of your system, before *any* of the data is acted upon" (King). A validator returns nothing and discards what it learned; a parser returns the refined type and keeps it.

A re-check deep inside the core is both a duplicate and an admission that the type does not say what the code believes. That is shotgun parsing — "parsing and input-validating code is mixed with and spread across processing code" — and it survives review because every individual re-check looks defensive and correct.

**In one place per boundary.** Each boundary has one module that maps both directions. Mapping scattered across call sites is duplicated by construction and drifts one call site at a time, so the bug appears in the path nobody changed.

**Never a foreign model.** Where an external system's shape would otherwise reach inward, the boundary is an anti-corruption layer: "Isolate the different subsystems by placing an anti-corruption layer between them", and keep it to translation — "avoid placing business rules or orchestration in the layer". An imported schema is an imported design, and it is one you do not control.

**A refusal is not an error.** Two failure classes must not be conflated: a refusal to serve *this work now* is an input to a decision, while a missing precondition for serving a *kind* of work at all is a failure at start-up. Collapsing them turns an ordinary day into an exception, and a real misconfiguration into a retry loop.

## Ports and adapters

A **port** is an interface named for a contract the core needs — "the word 'port' is supposed to evoke thoughts of ports in an operating system, where any device that adheres to the protocols of a port can be plugged into it" (Cockburn). An **adapter** implements it for one concrete external system.

- **The inner layer declares the port; the outer implements it.** A port declared beside its only implementation is a header file: the dependency still points outward and only the file count changed.
- **Name the port for its contract**, not for the vendor, protocol or library that happened to arrive first. The name is what stops the second implementation from being a fight.
- **Driving and driven are the same shape.** A primary (driving) adapter calls in on behalf of an actor that starts work; a secondary (driven) one is called out to for an answer or a notification. The symmetry is the payoff: a test harness substitutes for the first exactly as a stub substitutes for the second, and neither substitution touches the core.
- **A port per contract, not per class.** An interface with one implementation, no test double and no prospect of a second is ceremony. The deliberate exception is a port whose *promises* carry an invariant — there a second implementation satisfies the invariant by construction, where an inline branch satisfies it only by review.
- **Substitution happens at the port.** That is the testability claim in its honest form: the core is testable *because* of the boundary, not merely alongside it. If a unit test needs a running broker, the boundary is somewhere other than where the diagram says.

## What layering costs, and when to stop

The reason to do this at all is the modest one: "The reduced scope of attention reason is sufficient on its own" (Fowler) — testability and substitutability are the bonus, not the justification. Layering is also a *small-granularity* technique: once a layer grows too big, the top-level split becomes domain-oriented modules that are internally layered, not more layers.

Both failure modes are real and symmetric. Under-layering shows up as business rules in request handlers and a core that cannot be tested without infrastructure. Over-layering shows up as ports with no second side, records mapped to structurally identical records, and a folder per noun — an abstraction tax paid every change for an option nobody exercises.

*The test:* if adding one field routinely touches four files that differ only in the name of the type, the boundary those files cross is not carrying a decision. Collapse it, and say so in the commit message rather than working around it.

## Sources

- [Multitier architecture](https://en.wikipedia.org/wiki/Multitier_architecture) — layers versus tiers, strict versus relaxed.
- [Cockburn, *Hexagonal Architecture*](https://alistair.cockburn.us/hexagonal-architecture/) — ports, adapters, driving versus driven.
- [Martin, *The Clean Architecture*](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) — the dependency rule, and what may cross a boundary.
- [Palermo, *The Onion Architecture*](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/) — coupling toward the centre; the database is external.
- [Fowler, *PresentationDomainDataLayering*](https://martinfowler.com/bliki/PresentationDomainDataLayering.html) — why layer at all, and at what granularity.
- [King, *Parse, don't validate*](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/) — the boundary rule for data.
- [Anti-corruption layer](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer) — Evans' pattern as a catalogue entry.
- [Evans' layer responsibilities](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/ddd-oriented-microservice) — the domain and application layer definitions, quoted from *Domain-Driven Design*.
