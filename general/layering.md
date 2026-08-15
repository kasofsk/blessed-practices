# Layering

Where code goes, and which way its dependencies point.

## The rule: dependencies point inward

Source dependencies point only inward. Nothing in an inner layer knows anything at all about an outer one.

Four things follow, and between them they are the whole of the discipline.

**Control flow may point outward; the dependency may not.** The core reaches the world constantly, through an interface the core declares and something outside implements. That inversion is the entire mechanism.

**A type is a dependency, and so is a name.** A core function whose parameter is a vendor's handle is coupled to that vendor without importing it, and a field named after their concept has taken their vocabulary. Both change when they change.

**The rule is about the graph, not the file.** A helper three imports deep leaks as effectively as a direct import, so enforce reachability over the module graph rather than a per-file import lint. Every per-file check passes on a small path-joining utility that touches the filesystem and is called by the core.

**Inward is a direction, not a folder count.** Two layers with a boundary that is actually enforced beat five with nominal ones. The value is in what the rule forbids, and a boundary nothing checks forbids nothing.

## The layers

| Layer | Owns |
|---|---|
| **Domain** | business concepts, rules and decisions, and the state that reflects them — with the technical details of storing it delegated outward |
| **Application** | the jobs the software does: gather, call into the domain, commit, dispatch. Thin, and holding no business rules |
| **Adapters** | translation in both directions, one per external system, and no rules of its own |
| **Infrastructure** | the world itself — databases, queues, clocks, other people's services |

**The application layer decides nothing.** A conditional there that inspects domain state is a decision in the wrong place: invisible to whatever tests the domain, and duplicated the day a second caller appears.

**Adapters hold no rules.** Protocol, encoding, transport-level retry, translation — nothing a domain expert would recognise as a decision. A rule in an adapter is one nobody can find and nobody can test.

**A layer is logical; a tier is physical.** Whether two layers share a process, a host or neither is a deployment question and it moves no boundary here. Conflating the two is how both "we are not distributed, so we do not need layers" and "we are distributed, so the network is our boundary" get argued.

## Strict, not relaxed

A strict layering lets each layer depend only on the one below it; a relaxed one lets it depend on everything below. Prefer strict, in the three forms a violation actually takes:

- the domain imports no adapter, no framework, no I/O library, and no ambient capability — clock, randomness, environment, network;
- an adapter never imports another adapter: two adapters that need each other are either one adapter or a coordination belonging above both;
- nothing reaches the world except through the layer that owns that boundary.

Relaxed layering is not a weaker rule, it is the absence of one. Once any module may call anything below it, the import graph is the documentation, and the import graph is what nobody reads.

## What crosses a boundary

**Plain data.** A live object carries behaviour, identity and lazily-reachable state across a seam the reader cannot audit, and it makes the receiving side depend on the sender's class rather than on its data.

**Parsed, not validated.** Get data into its most precise representation at the boundary, before any of it is acted upon. A validator returns nothing and discards what it learned; a parser returns the refined type and keeps it. A re-check deep inside the core is both a duplicate and an admission that the type does not say what the code believes.

**One mapping site per boundary.** Mapping scattered across call sites is duplicated by construction and drifts one call site at a time, so the bug appears in the path nobody changed.

**Never a foreign model.** Where an external system's shape would otherwise reach inward, the boundary is an anti-corruption layer: translation only, no rules and no orchestration. An imported schema is an imported design, and it is one you do not control.

**A refusal is not an error.** A refusal to serve *this work now* is an input to a decision; a missing precondition for serving a *kind* of work at all is a failure at start-up. Collapsing them turns an ordinary day into an exception, and a real misconfiguration into a retry loop.

## Ports and adapters

A port is an interface named for a contract the core needs. An adapter implements it for one concrete external system.

- **The inner layer declares the port; the outer implements it.** A port declared beside its only implementation is a header file: the dependency still points outward and only the file count changed.
- **Name the port for its contract**, not for the vendor, protocol or library that happened to arrive first. The name is what stops the second implementation from being a fight.
- **Driving and driven are the same shape.** A driving adapter calls in on behalf of something that starts work; a driven one is called out to for an answer or a notification. The symmetry is the payoff: a test harness substitutes for the first exactly as a stub substitutes for the second, and neither touches the core.
- **A port per contract, not per class.** An interface with one implementation, no test double and no prospect of a second is ceremony. The deliberate exception is a port whose promises carry an invariant — a second implementation then satisfies it by construction, where an inline branch satisfies it only by review.
- **Substitution happens at the port.** The core is testable *because* of the boundary, not merely alongside it. If a unit test needs a running broker, the boundary is somewhere other than where the diagram says.

## What layering costs

The reason to layer is the modest one: a reduced scope of attention, so each part can be thought about without the others. Testability and substitutability are the bonus, not the justification.

It is also a small-granularity technique. Once a layer grows too big, the top-level split becomes domain-oriented modules that are internally layered — not more layers.

Both failure modes are real and symmetric. Under-layering puts business rules in request handlers and leaves a core that cannot be tested without infrastructure. Over-layering leaves ports with no second side, records mapped to structurally identical records, and a folder per noun — an abstraction tax paid every change for an option nobody exercises.

If adding one field routinely touches four files that differ only in the name of the type, the boundary those files cross is not carrying a decision. Collapse it.
