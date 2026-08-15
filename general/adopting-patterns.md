# Adopting patterns

The patterns in [layering.md](./layering.md) and [domain-modelling.md](./domain-modelling.md) are answers. Each answers a question some codebase actually had, and adopting one before that question arrives buys the cost immediately and the benefit never.

## Adopt on evidence

| Pattern | Answers | Adopt when |
|---|---|---|
| **Repository** | how does the domain stay ignorant of storage? | there is real storage to be ignorant of, and more than one caller needs the same access shape |
| **DTO tier** | how do wire shapes stay out of the domain? | the wire and the domain genuinely differ in structure — not when the mapping is a rename |
| **In-process event bus** | how do parts of the domain react to each other without coupling? | the reacting part observes rather than decides; a handler that decides is a second writer |
| **Read model** | how does a reader ask a question the write model answers expensively? | a second consumer exists and its query is genuinely different; one consumer is a cache with extra steps |
| **DI container** | how does wiring stay manageable across many variants? | there are more wiring variants than a person can hold, and the first attempt is still a function per deployment |
| **Service class per use case** | where does an orchestration with real internal structure live? | the orchestration survives across several events, rather than being one turn of a loop |

## Both failure modes are real

Under-adoption hurts continuously and is therefore easy to see: business rules in request handlers, a core that cannot be tested without infrastructure, a schema change that touches every file.

Over-adoption hides, because every individual piece looks like good practice: ports with one side, records mapped to structurally identical records, an interface per class, a folder per noun. It is a tax paid on every change for an option nobody exercises. Under-adoption is discovered by working in the code; over-adoption only by someone asking.

## Rules of thumb

- **A pattern's name is not an argument.** "It's the standard approach" describes adoption elsewhere, not a problem here.
- **Prefer deleting an abstraction to routing around it.** An abstraction bypassed once will be bypassed again, and the second bypass is quieter than the first.
