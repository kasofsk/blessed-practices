---
name: config-travels-with-the-project
title: Configuration is project-owned and repo-versioned
scope: architecture
altitude: high
portability: universal
confidence: high
status: candidate
evidence:
  - "Job types, prompts, tasks, tags and schedules all live under a single configuration root in the project repository"
  - "job #306 — the move to that root, with one resolver owning the lookup and a fallback for the older layout"
rationale: >
  A structural decision that shapes everything else: the platform reads its
  behaviour from the repository it is operating on, so a change to how work is
  done is reviewed by the same process as a change to the code.
related: [one-resolver-per-question, additive-wire-evolution, gates-are-cheap-first]
---

**Rule.** Everything that defines how the platform treats a project — job
definitions, prompts, gate scripts, schedules — lives in that project's
repository, under one configuration root, and is versioned with the code.

**Why.** Config in the platform is invisible to the people changing the code and
cannot be reviewed alongside it. Config in the repository means a change to the
review criteria goes through review, a change to a gate is tested by the gate,
and rolling back the code rolls back its process.

**How to apply.** Pick one root directory and put everything under it. Write one
resolver for the lookup, with the compatibility fallback in that one place.
Never write outside the new root, even when reading tolerates the old one.

**Does not apply when.** The setting is genuinely about the platform's own
deployment rather than about the project.

## Derivation

Job #306 moved five directories under one root, with a single resolver owning
the two-layout lookup and tests pinning both plus the shadowing order. Its
review found the predictable residue: the front end hard-coded the new path
while the backend deliberately resolved both.
