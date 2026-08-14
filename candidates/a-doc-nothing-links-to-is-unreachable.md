---
name: a-doc-nothing-links-to-is-unreachable
title: A document nothing links to is unreachable, however true it is
scope: documentation
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "design #415 D15 — orphan detection over the doc corpus, counting path claims and relative links but deliberately not the catalogue"
  - "job #210 — four well-written architecture docs rejected in part because the set was unreachable from the knowledge index"
rationale: >
  Reachability is a property of a corpus, not of a document, and it is invisible
  to every per-document check. The measurement design is also instructive: the
  index does not count as a link, because a required row would make the answer
  constant.
related: [one-definition-per-concept, docs-are-the-knowledge-store, mechanise-the-checkable-half]
---

**Rule.** Every document is reached by at least one other document that a reader
would plausibly be reading. A required catalogue row does not count as
reachability.

**Why.** An unreferenced document is not read, so it is not maintained, so it
goes stale, so reading it is worse than not having it. And if a catalogue row is
mandatory, counting it makes every document trivially reachable and the check
meaningless.

**How to apply.** When you add a document, link it from the page whose reader
needs it next, not only from the index. When you measure orphans, exclude the
mandatory index from the population and say you did.

**Does not apply when.** The file is reached by machinery rather than by
citation — a prompt or template named from configuration is reached by the
system, not by a reader.

## Derivation

Design #415 D15 records both the rule and the measurement design: counted
whole-tree the orphan finding is zero, against seven false positives if links
are not counted and eleven if the population is every tracked markdown file.
Narrowing the population is what makes the signal real.
