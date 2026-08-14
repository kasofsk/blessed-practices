---
name: which-kernel-execs-it
title: Ask each artifact the question its own executor asks
scope: architecture
altitude: mid
portability: universal
confidence: medium
status: candidate
evidence:
  - "job #480 — a channel binary extracted from a Linux image was staged onto a macOS node; the image build was correct and the artifact could not run"
  - "job #476 — a node's own toolchain had to be probed, named and forwarded before any build"
rationale: >
  A late-arriving member of the namespace family, and the least intuitive: the
  premise that failed was never expressed as a flag, so no audit of the launch
  configuration could have seen it.
related: [re-derive-facts-in-the-executing-namespace, existence-identity-provenance]
---

**Rule.** Every staged artifact is proved runnable on the machine that will
exec it, before the first install — not on the machine that built it.

**Why.** A property true by construction inside a build context stops being
guaranteed the moment the artifact leaves it. Architecture, libc, code signing
and interpreter paths are all invisible to a review of the staging code, because
none of them is a parameter of the staging code.

**How to apply.** Add an exec probe to the install path: run the artifact with a
harmless argument on the target and require a specific exit or output. Where a
probe is impossible, inspect the artifact's own header for the target's
architecture and refuse a mismatch by name.

**Does not apply when.** The build and the execution genuinely happen in the
same image on the same host.

## Derivation

Job #480 fixed a Darwin node receiving a Linux binary from an image built for
containers, and the fix included both an ELF/Mach-O header guard and an exec
probe. The reviewer's note is the general form: the guard exists because "an
audit of the launch flags cannot see a premise that was never a flag".
