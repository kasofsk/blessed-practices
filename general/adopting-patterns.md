# Adopting patterns

When to take a pattern out of the catalogue, and how to record the ones you decline.

The patterns in [layering.md](./layering.md) and [domain-modelling.md](./domain-modelling.md) are answers. Each one answers a question some codebase actually had, and adopting it before that question arrives buys the cost immediately and the benefit never.

## A refusal leaves no trace, so write it down

A pattern that was added is visible in the tree. A pattern that was considered and declined is visible nowhere: nobody can see the repository that was not added, so the next author adds one, in good faith, citing the same books. The argument gets paid for once or every time.

So a declined pattern gets a short written decision — what was declined, the argument, and the condition that would revive it. Three sentences is usually enough. This is the only defence against a decision being relitigated on the first inconvenience, and it is worth more than the rule it declines.

**Every deferral carries its revival condition.** A deferral with no recorded trigger becomes permanent by default, and the difference between "not yet" and "never" is written down or lost.

## Adopt on evidence, not on reputation

For each pattern, the question it answers — and the evidence that it has arrived.

| Pattern | Answers | Adopt when |
|---|---|---|
| **Repository** | how does the domain stay ignorant of storage? | there is real storage to be ignorant of, and more than one caller needs the same access shape |
| **DTO tier** | how do wire shapes stay out of the domain? | the wire and the domain genuinely differ in structure — not when the mapping is a rename |
| **In-process event bus** | how do parts of the domain react to each other without coupling? | the reacting part observes rather than decides; a handler that decides is a second writer wearing a hat |
| **CQRS read model** | how does a reader ask a question the write model answers expensively? | a second consumer exists and its query is genuinely different; one consumer is a cache with extra steps |
| **DI container** | how does wiring stay manageable across many variants? | there are more wiring variants than a person can hold — and the first attempt is still a function per deployment |
| **Service class per use case** | where does an orchestration with real internal structure live? | the orchestration survives across several events, rather than being one turn of a loop |
| **Context map, subdomain classification** | how do several teams' models relate? | there are several models and several teams; before that it is a picture nobody re-runs |

Two that are usually a mistake rather than a deferral: **an anemic service layer** holding rules that belong beside the data, and **always-valid enforced by throwing constructors** — keep the property, replace the mechanism with a parse that returns a refusal ([domain-modelling.md](./domain-modelling.md)).

## Both failure modes are real, and symmetric

Under-adoption is easy to see because it hurts continuously: business rules in request handlers, a core that cannot be tested without infrastructure, a schema change that touches every file.

Over-adoption hides, because every individual piece looks like good practice: ports with one side, records mapped to structurally identical records, an interface per class, a folder per noun. It is an abstraction tax paid on every change, for an option nobody exercises.

The asymmetry worth knowing: under-adoption is discovered by working in the code, over-adoption is discovered only by someone asking. Ask.

## Write down what would refute you

A decision with no failure symptom attached is a belief. For each pattern adopted or declined, name the observation that would overturn it — and prefer symptoms to positions, because a symptom can be noticed by someone who was not in the argument.

Worked examples of the shape:

- *Declined a repository.* Refuted by state that stops fitting in memory or stops being cheap to rebuild. The symptom is start-up time, and the first answer is a snapshot, not the pattern.
- *Declined a DTO tier.* Refuted by mapping code that grows branches. The symptom is a conditional in a mapper; at that point the translation is a model of its own and deserves a name.
- *Adopted a three-part layout.* Refuted by a fourth home appearing that is none of the three. The symptom is a directory whose name is a technology.

## Rules of thumb

- **A pattern's name is not an argument.** "It's the standard approach" describes adoption elsewhere, not a problem here.
- **The catalogue is not a checklist.** Nothing is missing merely because it is absent; something is missing when a real problem has no answer.
- **Prefer deleting an abstraction to routing around it.** An abstraction that is bypassed once will be bypassed again, and the second bypass is the one nobody documents.
- **Cite the failure, not the book.** A rule adopted with its motivating failure attached can be generalised correctly by the next reader; one adopted with a citation can only be obeyed or ignored.

## Sources

- [Fowler, *PresentationDomainDataLayering*](https://martinfowler.com/bliki/PresentationDomainDataLayering.html) — why layer, and at what granularity, including where it is overkill.
- [Vernon, *Effective Aggregate Design*](https://www.dddcommunity.org/library/vernon_2011/) — the source of the "just because a use case calls for it" caution.
- [Anti-corruption layer](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer) — a catalogue entry that states its own "might not be suitable when", which is the shape every entry should have.
