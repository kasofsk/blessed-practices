# Layering

Where code goes, and which way its dependencies point.

## The rule: dependencies point inward

Source dependencies point only inward. Nothing in an inner layer knows anything at all about an outer one.

Four things follow.

**Control flow may point outward; the dependency may not.** The core reaches the world constantly, through an interface the core declares and something outside implements. That inversion is the entire mechanism.

**A type is a dependency, and so is a name.** A core function whose parameter is a vendor's handle is coupled to that vendor without importing it, and a field named after their concept has taken their vocabulary.

**The rule is about the graph, not the file.** Enforce reachability over the module graph rather than per-file imports: every per-file check passes on a small path-joining utility that touches the filesystem and is called by the core.

**Inward is a direction, not a folder count.** Two layers with an enforced boundary beat five with nominal ones; a boundary nothing checks forbids nothing.

## The layers

| Layer | Owns |
|---|---|
| **Domain** | business concepts, rules and decisions, and the state that reflects them — with the technical details of storing it delegated outward |
| **Application** | the jobs the software does: gather, call into the domain, commit, dispatch. Thin, and holding no business rules |
| **Adapters** | translation in both directions, one per external system, and no rules of its own |
| **Infrastructure** | the world itself — databases, queues, clocks, other people's services |

**The application layer decides nothing.** A conditional there that inspects domain state is a decision in the wrong place: invisible to whatever tests the domain, and duplicated the day a second caller appears.

**Adapters hold no rules.** Protocol, encoding, transport-level retry, translation — nothing a domain expert would recognise as a decision.

**A layer is logical; a tier is physical.** Whether two layers share a process, a host or neither is a deployment question, and it moves no boundary here.

## Strict, not relaxed

Each layer depends only on the one below it. Three forms the violation actually takes:

- the domain imports no adapter, no framework, no I/O library, and no ambient capability — clock, randomness, environment, network;
- an adapter never imports another adapter: two adapters that need each other are either one adapter or a coordination belonging above both;
- nothing reaches the world except through the layer that owns that boundary.

Relaxed layering — anything may call anything below it — is not a weaker rule but the absence of one: the import graph becomes the only statement of the structure, and nobody reads it.

## What crosses a boundary

**Plain data.** A live object carries behaviour, identity and lazily-reachable state across a seam the reader cannot audit.

**Parsed, not validated.** Get data into its most precise representation at the boundary, before any of it is acted upon. A re-check deep inside is both a duplicate and an admission that the type does not say what the code believes.

**One mapping site per boundary.** Mapping scattered across call sites drifts one call site at a time, so the bug appears in the path nobody changed.

**Never a foreign model.** Where an external system's shape would reach inward, the boundary translates it. An imported schema is an imported design, and it is one you do not control.

**A refusal is not an error.** A refusal to serve *this work now* is an input to a decision; a missing precondition for serving a *kind* of work at all is a failure at start-up.

## Ports and adapters

A port is an interface named for a contract the core needs. An adapter implements it for one concrete external system.

- **The inner layer declares the port; the outer implements it.** A port declared beside its only implementation is a header file: the dependency still points outward and only the file count changed.
- **Name the port for its contract**, not for the vendor, protocol or library that arrived first. The name is what stops the second implementation from being a fight.
- **A port per contract, not per class.** An interface with one implementation, no test double and no prospect of a second is ceremony.
- **Substitution happens at the port**, and that is where testability comes from. If a unit test needs a running broker, the boundary is somewhere other than where the diagram says.

## What layering costs

The reason to layer is a reduced scope of attention: each part can be thought about without the others. Testability and substitutability are the bonus, not the justification.

It is a small-granularity technique. Once a layer grows too big, the top-level split becomes domain-oriented modules that are internally layered — not more layers.

Both failure modes are real. Under-layering puts business rules in request handlers and leaves a core that cannot be tested without infrastructure. Over-layering leaves ports with no second side, records mapped to structurally identical records, and a folder per noun.

If adding one field routinely touches four files that differ only in the name of the type, that boundary is not carrying a decision. Collapse it.
