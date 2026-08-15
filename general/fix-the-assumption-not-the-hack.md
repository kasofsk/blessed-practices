# Fix the Assumption, Not the Hack

## Core principle

Constantly be thinking about minor refactors and architectural improvements.
When a new feature invalidates an assumption the current design was built on,
the default move is to **fix the assumption** — rethink the pattern — rather
than land a tweaky hack that technically satisfies the request.

## How we get there

### 1. Recognize the fork in the road

Modern software development has humans writing very little code directly, with
agents both writing and increasingly reviewing it. In that world, this
situation will arise many, many times: a feature wants to be added, and the
agent is presented with two options —

- **The hack**: a tweak that gets exactly to where the request was, typically
  needing a long comment to explain and justify itself (see
  [Comments Describe the Code](comments-describe-the-code.md) — that comment
  is the tell).
- **The rethink**: a slightly more expensive change that revisits the pattern,
  because this new feature has invalidated an assumption the old pattern
  rested on.

The first skill is simply noticing that you're standing at this fork.

### 2. Default to the rethink

When these situations arise, we typically want to fix the assumption. The
extra cost is real but bounded and paid once; the hack's cost compounds — it
misleads every future reader about how the system actually works, and it
invites the next change to stack another tweak on top.

### 3. Design for beyond the prompt's lifetime

The system being manipulated will extend far beyond this prompt's lifetime.
The goal is not "exactly what was requested, as cheaply as possible" — it is a
system that is **maximally maintainable at any point in time**. A change is
finished when the codebase afterward looks like it was designed with the new
requirement in mind, not patched to tolerate it.

## Why this matters

Every hack encodes a lie: it leaves the old assumption in place while the
system quietly violates it. Agents working at high velocity can accumulate
these lies far faster than humans ever could — or, with a habit of small
continuous refactors, can pay down assumptions the moment they break, keeping
the architecture honest at every commit.
