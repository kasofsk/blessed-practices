---
name: idiomatic-by-default
description: Take the community-standard path for the language, framework, or ecosystem unless there is an articulable reason not to, and don't escalate a decision the idiom already answers. Use when choosing a library, project layout, API shape, or tooling approach, when about to hand-roll something the ecosystem already provides, or before asking the operator to decide a question the ecosystem has settled.
---

# Idiomatic by Default

## Core principle

Virtually always do things the idiomatic way. We never want to get caught with
our pants down having built something more complicated or more brittle when an
idiomatic path was available to us.

## How we get there

### 1. The idiomatic path is the default path

For any given language, framework, or ecosystem, the community-standard way of
doing something is the presumptive choice. Idioms are battle-tested: they
encode years of collective debugging, and every future reader (human or agent)
already knows how they work.

### 2. Deviation requires a very good reason

This is not an absolute rule — we are allowed to leave the idiomatic path. But
if we do, we should have *very good reasons*, and those reasons should be
articulable. "It seemed cleaner to me" or "I didn't check what the standard
approach was" don't qualify. The failure mode we're guarding against is
discovering, after the fact, that we hand-rolled something complicated and
brittle where a well-worn idiom existed all along.

### 3. Don't escalate decisions an idiom already answers

When making architectural or technical decisions — including deciding whether
to send a question back to the human operator — check whether one of the
options is the tried-and-true idiomatic path. If it is, **default to it**
rather than forcing the operator to make that call. Operator attention is a
scarce resource; spend it on genuinely open questions, not on choices the
ecosystem has already settled.

## Why this matters

Idioms are a form of pre-paid knowledge: choosing them means inheriting the
ecosystem's testing, tooling, documentation, and reader familiarity for free.
Non-idiomatic code taxes every future change — and every escalation of an
already-settled question taxes the operator. Both are costs we should only pay
deliberately, never by accident.
