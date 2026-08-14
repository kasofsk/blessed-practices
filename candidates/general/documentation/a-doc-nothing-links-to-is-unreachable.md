---
type: Blessed Practice
title: "A document nothing links to is unreachable, however true it is"
description: "Every document is reached by at least one other document that a reader would plausibly be reading."
status: draft
tags:
  - bucket/general
  - scope/documentation
  - altitude/mid
  - portability/universal
  - confidence/high
generated:
  by: claude-opus-5/1m
  at: 2026-08-14
rationale: >
  Reachability is a property of a corpus, not of a document, and it is invisible
  to every per-document check. The measurement design is also instructive: the
  index does not count as a link, because a required row would make the answer
  constant.
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

## Where this comes from

The measurement design is the instructive part. Counted over the whole corpus
the orphan finding is zero — against seven false positives if relative links
are not counted as reachability, and eleven if the population is every
markdown file rather than only the documentation tree. Narrowing the
population is what turned noise into a signal.

## Related

- [Knowledge lives in docs; code carries pointers](docs-are-the-knowledge-store.md)
- [Mechanise the checkable half; route the rest to judgement](../process/mechanise-the-checkable-half.md)
- [One definition per concept, and a registry that says where](one-definition-per-concept.md)
