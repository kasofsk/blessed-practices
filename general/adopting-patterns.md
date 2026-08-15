# Adopting patterns

When to take a pattern out of the catalogue.

The patterns in [layering.md](./layering.md) and [domain-modelling.md](./domain-modelling.md) are answers. Each one answers a question some codebase actually had, and adopting it before that question arrives buys the cost immediately and the benefit never.

## Adopt on evidence, not on reputation

| Pattern | Answers | Adopt when |
|---|---|---|
| **Repository** | how does the domain stay ignorant of storage? | there is real storage to be ignorant of, and more than one caller needs the same access shape |
| **DTO tier** | how do wire shapes stay out of the domain? | the wire and the domain genuinely differ in structure — not when the mapping is a rename |
| **In-process event bus** | how do parts of the domain react to each other without coupling? | the reacting part observes rather than decides; a handler that decides is a second writer wearing a hat |
| **Read model** | how does a reader ask a question the write model answers expensively? | a second consumer exists and its query is genuinely different; one consumer is a cache with extra steps |
| **DI container** | how does wiring stay manageable across many variants? | there are more wiring variants than a person can hold — and the first attempt is still a function per deployment |
| **Service class per use case** | where does an orchestration with real internal structure live? | the orchestration survives across several events, rather than being one turn of a loop |

Two are usually a mistake rather than a deferral. **An anemic service layer** holds rules that belong beside the data. **Always-valid enforced by throwing constructors** keeps a property worth having by a mechanism worth replacing — a parse that returns a refusal does the same job without the invisible control-flow edge.

## Both failure modes are real, and symmetric

Under-adoption hurts continuously and is therefore easy to see: business rules in request handlers, a core that cannot be tested without infrastructure, a schema change that touches every file.

Over-adoption hides, because every individual piece looks like good practice: ports with one side, records mapped to structurally identical records, an interface per class, a folder per noun. It is a tax paid on every change for an option nobody exercises.

The asymmetry worth knowing: under-adoption is discovered by working in the code, over-adoption only by someone asking. Ask.

## Rules of thumb

- **A pattern's name is not an argument.** "It's the standard approach" describes adoption elsewhere, not a problem here.
- **The catalogue is not a checklist.** Nothing is missing merely because it is absent; something is missing when a real problem has no answer.
- **Prefer deleting an abstraction to routing around it.** An abstraction bypassed once will be bypassed again, and the second bypass is quieter than the first.
- **A rule travels with the failure it prevents.** A rule stated with its motivating failure can be generalised correctly to a case it did not anticipate; a rule stated as an authority can only be obeyed or ignored.
