# Comments Describe the Code, Not Its History

## Core principle

Comments should be descriptive and clarifying, and they should be about **the
code itself** — not about the moment, the conversation, or the prompt that
produced it.

## How we get there

### 1. No time-capsule comments

Comments should not encode history or context that only makes sense at the
time the code was generated — and in particular, they should not refer to the
prompt or request that created them. A comment like "changed per discussion"
or "as requested, now handles the new case" is meaningless to the next reader.
The test: a reader with no knowledge of how this code came to exist should
find the comment fully intelligible and useful.

### 2. Provenance comments are legitimate scaffolding — temporarily

We do understand that provenance-style comments can be genuinely helpful while
working out larger tasks: coordinating several pull requests into one
significant feature, or navigating a large refactoring. Embedded markers of
"where this came from / what it connects to" can make that work go smoothly,
and that's okay.

### 3. Scaffolding comes down before merge to main

By the time work is merging back onto the main branch, no comment should
remain that only makes sense to the specific operator who asked for the
specific change. Provenance comments are construction scaffolding: essential
during the build, removed before hand-off. Main-branch comments serve every
future reader, not the one who commissioned the work.

### 4. A long justifying comment is a code smell

If a very long comment exists to justify code that seems bad, it's very likely
the code *is* bad. The right move is usually to change the code so that the
comment can be simpler — not to keep polishing the explanation. Comment length
spent on justification is a signal pointing at the code, and the fix belongs
in the code.

## Why this matters

Comments are part of the permanent interface of the code, read far more often
and far later than they are written. History-bound and operator-bound comments
actively mislead future readers by pointing at context that no longer exists;
long apologetic comments paper over problems that should be fixed. Keeping
comments descriptive, self-contained, and short keeps the codebase honest.
