---
name: a-tool-outcome-measures-the-tool
title: A tool's outcome measures the tool, not your claim
scope: testing
altitude: mid
portability: universal
confidence: high
status: candidate
evidence:
  - "docs/reference/style.md Tier 2 rule 8 — this shape has produced three recorded errors in this corpus"
  - "design #529 — a profiler succeeding against another process measures the entitlement on the profiler, not what the caller may reach"
rationale: >
  A precise epistemic rule extracted from three separate measurement errors,
  each of which looked conclusive and established something adjacent to what it
  was cited for. It generalises far beyond the case that produced it.
related: [a-denial-with-no-control, verification-is-reported-with-its-command, unenforced-intentions-become-believed-facts]
---

**Rule.** Before citing a measurement, state exactly what it measured. A
privileged tool succeeding tells you about that tool's privileges. A command
failing tells you about that command. Neither is a statement about the general
capability you are arguing over.

**Why.** Measurements are cited by their conclusion, not their method, and the
conclusion drifts one step from what the method supports each time it is quoted.
Two steps later the citation is load-bearing and wrong.

**How to apply.** Write the measurement as "X, run as Y, under Z, produced W",
and derive the claim from that sentence rather than from memory. When the claim
is about what a *task* can do, run the probe as the task, not as an operator
with a debugger.

**Does not apply when.** The tool and the subject of the claim are the same
thing.

## Derivation

Design #529's finding is the template: a load-bearing premise about process
memory isolation rested on a measurement taken with a privileged tool, while the
adjacent measurement in the same document was evidence the other way. The rule
was written into the style tier from that case.
