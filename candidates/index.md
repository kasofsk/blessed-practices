---
okf_version: "0.2"
title: Candidate blessed practices
description: Practices for directing coding agents, derived from a retrospective of one agent-run project and offered as reviewable candidates.
---

# Candidate blessed practices

**Nothing in this bundle is adopted.** Every concept here carries `status: draft`.
A practice becomes adopted by review: flip `status` to `stable` and add a
`verified` entry naming who accepted it and when. A rejected practice is deleted
with a line in [`log.md`](log.md) saying why.

Start with [the retrospective](retrospective.md) — it explains where these came
from, what the evidence says, and the order worth reviewing them in.

Two buckets. `chug/` holds practices specific to how an agent-orchestration
platform works within its own framework; they name the source platform. Everything
under `general/` is written to stand alone and mentions no particular project.

## chug (14)

Practices about how this kind of platform works inside its own framework — the unit-of-work lifecycle, the review loop, and configuration ownership. These name the source platform and its flow.

- [A verdict says what to change and what not to touch](chug/scope-the-rework-explicitly.md) — Every rejecting verdict has two parts: what is accepted and must not change, and what must change.
- [An empty diff is a first-class finding, verified not assumed](chug/empty-diff-is-a-verdict.md) — A review's first step is to establish the diff and confirm it is non-empty.
- [An escalation preserves the operator's distinct choices](chug/escalation-preserves-the-operator-choice.md) — Reusing existing machinery to implement an operator choice is fine; collapsing two distinct operator intents into one is not.
- [Configuration is project-owned and repo-versioned](chug/config-travels-with-the-project.md) — Everything that defines how the platform treats a project — job definitions, prompts, gate scripts, schedules — lives in that project's repository, under one configuration root, and is versioned with the code.
- [Distinguish a stale base from a bad attempt](chug/stale-base-is-not-an-authoring-failure.md) — When a finding is caused by the branch's base rather than by the change, say so and name the remedy: rebase, wait for a dependency, or re-cut the ticket.
- [Escalate an unsatisfiable brief instead of reworking it](chug/escalate-when-the-brief-is-unsatisfiable.md) — If the brief cannot be satisfied on this base — its premise is false, its scope excludes the change it requires, its target does not exist — say so and escalate.
- [Reserve human approval for what no gate and no reader can judge](chug/human-approval-only-where-no-gate-can-judge.md) — Put a human approval step only where the failure mode is invisible to both a gate and a reading reviewer.
- [Reviewers read; gates run](chug/reviewers-read-they-do-not-run.md) — Separate judgement from execution.
- [Rework builds on the previous attempt; it does not restart it](chug/branch-preserved-across-rework.md) — A rework cycle continues the same branch.
- [The rework brief carries the evidence, not just the verdict](chug/rework-context-carries-the-evidence.md) — Whatever produced the failure — compiler output, test output, the reviewer's findings with file and line — is included verbatim in the brief the next attempt receives.
- [The ticket is the contract, and both sides read it verbatim](chug/the-ticket-is-the-contract.md) — Write the ticket as the contract both the implementer and the reviewer are held to.
- [The unit of work carries the type its change actually needs](chug/job-type-matches-the-work.md) — Type the unit of work by what the change actually requires, not by where the visible symptom is.
- [When a gate reads commit order, ship one commit](chug/one-commit-when-ordering-matters.md) — If any gate derives meaning from commit timestamps or commit membership, keep the branch to one commit — or make every commit that touches a subject also touch the docs that name it.
- [Write the summary for whoever has to judge it, close calls first](chug/the-work-summary-is-for-the-approver.md) — Write the work summary for the person or agent who must approve it.

## architecture (27)

System shape: writers, boundaries, effects, state, and the machine facts a component may rely on.

- [A content hash never enters operator-typed config](general/architecture/no-content-hash-in-config.md) — Configuration a human types names stable paths.
- [A re-queued item keeps its original clock](general/architecture/a-queue-entry-keeps-its-clock.md) — When an item goes back on a queue, it carries its original enqueue time and its original priority.
- [An architectural boundary that nothing checks is a comment](general/architecture/boundaries-are-asserted-not-documented.md) — State every architectural boundary as an executable assertion, and prove the assertion can fail by making it fail on purpose before you ship it.
- [An unenforced intention gets read as a statement of fact](general/architecture/unenforced-intentions-become-believed-facts.md) — Do not write a constraint you are not enforcing.
- [Ask each artifact the question its own executor asks](general/architecture/which-kernel-execs-it.md) — Every staged artifact is proved runnable on the machine that will exec it, before the first install — not on the machine that built it.
- [Build aside, then swap atomically](general/architecture/stage-then-swap.md) — Produce the new artifact beside the live one under a distinct name, verify it, then make it live with a single rename or retag.
- [Credential teardown runs after every consumer, not before](general/architecture/credential-lifetime-and-teardown-order.md) — Scope credential material to its own directory, never one shared with artifacts you need afterwards, and order teardown after every consumer — including harvest.
- [Deciders return effects; interpreters perform them](general/architecture/pure-decider-effects.md) — Decision logic is a pure function from a read-only view and an event to a list of transitions and effects.
- [Every in-flight state has a restart arm](general/architecture/restart-reconciliation-is-first-class.md) — Adding a state a task can be in while a process is alive obliges you to add its recovery arm in the same change: what the process does with a record found in that state at startup, and a test that restarts mid-state.
- [Everything is bounded, and the bound is loud](general/architecture/bounded-and-loud.md) — Every loop has an iteration cap, every queue a depth limit, every wait a deadline.
- [Existence, identity and provenance are three separate questions](general/architecture/existence-identity-provenance.md) — For any external artifact, ask three questions and write three checks: is it there, is it the thing it claims to be, and did it arrive by a route that survives the next rebuild.
- [Grants are allow-lists, fail-closed, refused at three layers](general/architecture/fail-closed-allow-lists.md) — A capability is granted by an explicit allow-list.
- [Harvest before you reclaim, and never fail a job on cleanup](general/architecture/capture-before-disposal.md) — Collect every artifact before disposing of the thing that holds it.
- [Keep declared intent and observed state in separate fields](general/architecture/separate-intent-from-observation.md) — When a value can be both requested and reported, store two values: what was asked for, and what was last observed.
- [One crate owns each external system](general/architecture/one-integration-point-per-dependency.md) — Each external system — broker, container runtime, VCS, cloud API — has exactly one module or crate that speaks to it.
- [One decision site per question](general/architecture/one-decision-site.md) — Each policy question is answered by exactly one function.
- [One resolver per lookup question](general/architecture/one-resolver-per-question.md) — Each "where does this live" or "which one applies" question has one function.
- [One writer per record class](general/architecture/single-writer-per-record.md) — For each class of record, exactly one component may write it, and that component writes it from one place.
- [Prefer a loud refusal to a silent degradation](general/architecture/refuse-loudly.md) — When a component cannot do what it was asked, it says so, by name, at the moment of the request.
- [Re-derive every host fact inside the namespace that will use it](general/architecture/re-derive-facts-in-the-executing-namespace.md) — A fact about a machine — a path, a device, a socket, a binary, a user — is only established by asking it from the namespace that will actually run the code.
- [Re-read before you write back](general/architecture/read-modify-write-reads-again.md) — If you clone a record, call anything that may persist a change, and then write your clone back, you have overwritten that change.
- [Reserve a prefix for platform-owned names](general/architecture/reserved-namespace-prefixes.md) — Platform-injected names live under a reserved prefix.
- [Terminal states are terminal, and nothing self-heals after them](general/architecture/terminal-means-terminal.md) — Treat the transition into a terminal state as the last chance to be correct.
- [The shared types layer has no I/O and no runtime](general/architecture/pure-data-layer.md) — The crate that defines the shared data types also defines their validation rules, and depends on no async runtime, no I/O, and no transport.
- [Validate everything first, then mutate](general/architecture/validate-before-you-mutate.md) — A procedure that mutates external state does all of its checking first, in one block, before the first mutation.
- [What a process is told is not what its uid may open](general/architecture/reachability-by-uid.md) — An environment-composition guarantee bounds what a process is *told*. It never bounds what its uid may *open*. Capability questions are answered by probing as that uid, on that machine.
- [Wire changes are additive, epoch-gated, and tolerated by N-1](general/architecture/additive-wire-evolution.md) — New wire and config fields are optional and additive.

## process (17)

How work is specified, reviewed, gated and corrected.

- [A dropped row reads like a negative result](general/process/silent-filters-hide-rows.md) — Any filter, selector or query that can silently match nothing must say so.
- [A gate is code, so it has tests, and the tests are discovered](general/process/every-gate-has-a-test-suite.md) — Every gate script has a test suite that drives the real script against fixtures, including at least one case that must fail.
- [A refactor proves parity; it does not assert it](general/process/behaviour-parity-is-proved-not-asserted.md) — A change that claims to preserve behaviour ships the evidence: a characterisation test or trace landed *before* the refactor and unchanged by it, or a line-by-line correspondence the reviewer can check.
- [A rejection names the rule it rejects under](general/process/verdict-names-the-rule.md) — Every blocking finding cites the rule, criterion or ticket item it violates, by name or number, and quotes the clause.
- [Acceptance criteria name an observation, not an intention](general/process/acceptance-criteria-are-checkable.md) — Every acceptance criterion is a specific observation someone can make: a command and its expected output, a file that must not exist, a string that must not appear in the tree.
- [Announce exactly what ran — never a tier you did not execute](general/process/announce-exactly-what-ran.md) — Any line a gate prints about what it covered is a factual claim.
- [Cannot-run and passed must not print the same](general/process/a-check-that-cannot-run-exits-distinctly.md) — A check has three outcomes, not two: passed, failed, and could not run.
- [Cheap checks run whole-tree, not only over the diff](general/process/whole-tree-not-just-the-diff.md) — If a check is cheap enough, run it over the whole tree on every change.
- [Fix the class, and sweep the tree for its other instances](general/process/sweep-the-class-not-the-instance.md) — When you find a defect, name its class, search the whole tree for other instances, and fix them in the same change.
- [Land a new rule as a ratchet, and make the debt greppable](general/process/ratchet-dont-sweep.md) — A new rule lands enforcing on new code immediately, with existing violations individually marked and the marker naming the work that removes them.
- [Mechanise the checkable half; route the rest to judgement](general/process/mechanise-the-checkable-half.md) — For each rule you care about, separate the part that resolves against the tree from the part that needs judgement.
- [Order gates cheapest-first and diff-aware](general/process/gates-are-cheap-first.md) — Run gates in ascending cost.
- [Practices are numbered, tiered, injectable, and carry their why](general/process/blessed-practices-are-numbered-and-cited.md) — Write practices so they can be cited and injected: numbered or named, tiered by how strictly they bind, short enough to include in a prompt, and each carrying its reasoning inline.
- [Prove a capability with a ladder of rungs, each one falsifiable](general/process/prove-with-a-ladder.md) — To establish an end-to-end capability, write a ladder: numbered rungs, each asserting one fact, each able to fail independently, with a summary that cannot report success unless every rung passed.
- [Record every deviation from the brief, with its reason](general/process/deviation-is-recorded-not-silent.md) — When you implement something other than what the ticket specified, say so in the commit message and in the durable record: what the ticket asked, what you did, and why.
- [Report verification as commands and outputs, not as adjectives](general/process/verification-is-reported-with-its-command.md) — State how you verified, not that you did: the command, its output or exit status, and what you did not exercise.
- [Resolve record conflicts by keeping both, in landing order](general/process/merge-conflicts-keep-both-records.md) — When two branches append independent records to the same file, the resolution is the union in landing order — never a choice between them.

## documentation (21)

Keeping a written corpus true, reachable, and small enough to read.

- [A change updates the docs it makes stale, in the same commit](general/documentation/docs-updated-in-the-same-commit.md) — The commit that changes behaviour also changes every document the new behaviour makes false.
- [A count in prose is a liability; give the command instead](general/documentation/counts-in-prose-are-liabilities.md) — Prefer naming the command that produces a count over stating the count.
- [A design decides the central question](general/documentation/decide-do-not-straddle.md) — Identify the question the document exists to settle and settle it, in its own numbered decision, early.
- [A doc asserting another doc's status is the most fragile sentence you can write](general/documentation/cross-doc-state-claims.md) — Avoid asserting another document's implementation status.
- [A document nothing links to is unreachable, however true it is](general/documentation/a-doc-nothing-links-to-is-unreachable.md) — Every document is reached by at least one other document that a reader would plausibly be reading.
- [A knowledge corpus needs a shedding process, not only an appending one](general/documentation/shed-the-corpus-at-milestones.md) — Periodically and deliberately remove knowledge that has stopped earning its place: heads compacted, fully-implemented designs deleted outright, every referrer repointed or stubbed.
- [A mutable head over an append-only body](general/documentation/mutable-head-append-only-body.md) — A decision document has two parts.
- [An exemption mechanism must be narrower than the thing it exempts](general/documentation/a-marker-is-not-a-silencer.md) — Design every exemption to be narrower than the rule it escapes: line-scoped rather than file-scoped, per-instance rather than per-threshold, and requiring a written reason at the point of use.
- [Clear an attention gate with an assertion of attention, not a timestamp](general/documentation/assertion-of-attention-over-timestamp.md) — When a gate exists to make someone look at something, let them clear it by asserting that they looked — naming what they looked at — rather than by performing the mechanical act the gate measures.
- [Corrections are appended, dated, and name their job](general/documentation/corrections-are-appended-and-dated.md) — A correction is a new dated section naming the change that wrote it, what it corrects, and what evidence changed the answer.
- [Date every measurement, and name the host it was taken on](general/documentation/date-the-measurement.md) — Every measured figure carries its date, the command that produced it, and — where it depends on the machine — the host and its relevant state.
- [Deletion is reviewed by accounting, because the usual gates go green](general/documentation/deletion-needs-accounting.md) — When a change's product is removal, review it by accounting: what was removed, what referenced it, what replaced the reference, and what the ledger records.
- [Knowledge lives in docs; code carries pointers](general/documentation/docs-are-the-knowledge-store.md) — The knowledge a comment would carry goes in a document; the code carries at most a two-sentence doc comment pointing at it.
- [Marking is a syntax, and the markers are not interchangeable](general/documentation/mark-unbuilt-intent.md) — When a document names something that does not resolve, mark why on the same line, with a marker whose meaning matches the tense: it will exist later, it exists on a machine but not in version control, or it exists nowhere and that is the sentence's point.
- [Measure corpus growth; do not set a threshold for it](general/documentation/growth-is-measured-not-felt.md) — Build the measurement that informs a judgement, and do not encode the judgement as a threshold.
- [One definition per concept, and a registry that says where](general/documentation/one-definition-per-concept.md) — Each concept is defined in exactly one document.
- [Present-tense prose about the tree is a factual claim](general/documentation/present-tense-prose-is-a-claim.md) — A sentence in the present tense about what the system does, what a gate checks, what a path holds or what a constant equals is a factual claim about the tree.
- [Suspect is not wrong — publish a reading list, block almost nowhere](general/documentation/staleness-is-suspect-not-wrong.md) — Derive staleness from history rather than from declarations, report it as a reading list, and block only where the author is in a position to act.
- [The change that implements a planned unit writes its status row](general/documentation/the-implementing-change-owns-the-status.md) — The commit that implements a planned unit of work flips that unit's status row and adjusts the document's status line, in the same commit.
- [The commit message carries the why](general/documentation/commit-messages-carry-the-why.md) — The commit message explains why the change is shaped the way it is: what changed, why this shape, what was deliberately not done, and how it was verified.
- [The rejected alternatives are the part that cannot be re-derived](general/documentation/rejected-alternatives-are-part-of-the-record.md) — A decision document states each rejected alternative at its strongest, with its real costs, before rejecting it — and keeps that section forever.

## testing (11)

Making sure a check can fail, and that its result means what it says.

- [A denial with no control identifies no mechanism](general/testing/a-denial-with-no-control.md) — A single failed attempt does not identify why it failed.
- [A test must be able to observe what its name claims](general/testing/no-vacuous-assertions.md) — Check that the test can observe the thing it names: the function under test must read the input you are varying, the fixture must be able to produce the state you assert, and the assertion must be reached and drained.
- [A test that cannot run says so; it never passes vacuously](general/testing/self-skip-loudly.md) — A test that cannot run in this environment prints that it did not run, naming what was missing.
- [A tool's outcome measures the tool, not your claim](general/testing/a-tool-outcome-measures-the-tool.md) — Before citing a measurement, state exactly what it measured.
- [Break it on purpose and watch the named case go red](general/testing/assertions-that-can-fail.md) — Before you rely on a test or a guard, make it fail.
- [Measure on a fresh fixture, or the numbers lie](general/testing/measure-on-a-clean-fixture.md) — Take timing and coverage measurements against a freshly created fixture, with the environment stated.
- [New behaviour lands with a test at the lowest tier that can express it](general/testing/lowest-tier-that-expresses-it.md) — Every behaviour change lands with a regression test at the cheapest tier that can express it.
- [Regenerate golden artifacts; never hand-patch them](general/testing/golden-artifacts-are-regenerated.md) — When a change alters what a generator emits, re-run the generator and commit its output.
- [Test the premise, not only the behaviour](general/testing/test-the-premise.md) — Where a check exists because of an external fact, assert that fact in the suite too.
- [The gate's environment is the authority; local runs produce false reds](general/testing/the-gate-container-is-the-authority.md) — Name one environment as authoritative for gate results, and say so where people will run the gates.
- [Wait on the observable, never on the clock](general/testing/determinism-over-timing.md) — Synchronise on the observable the assertion depends on, not on time and not on a proxy signal that fires earlier.

## code (14)

Craft rules at the level of a file, a function, a name or a message.

- [A numeric function-length cap, enforced](general/code/function-length-cap.md) — Cap function length with a number, enforced by the linter, so a function one line over the cap fails the build.
- [An error names one cause and one action, and only when it is that cause](general/code/errors-name-the-actionable-thing.md) — An error message names the cause it actually detected and the action that follows from it.
- [An exit status is not an existence oracle](general/code/do-not-use-exit-status-as-an-oracle.md) — Do not infer existence, absence or identity from a command's exit status unless the command documents that mapping.
- [An interface that cannot prove freshness must not imply it](general/code/surface-staleness-in-the-ui.md) — Any display of live state shows its own freshness, and its freshness clock runs unconditionally.
- [Assert what must never happen](general/code/assert-negative-space.md) — Alongside asserting what should hold, assert what must never happen — no transition out of a terminal state, no second writer, no read of this value from that path.
- [Do not buy a display detail with a request per row](general/code/no-per-row-fetching.md) — A list view fetches per list, not per row.
- [Every new dependency states its justification in the commit](general/code/dependencies-need-a-justification.md) — Adding a dependency requires a sentence in the commit message: what it does, why the standard library or an existing dependency does not, and what would let it be removed.
- [Match exhaustively; a new variant should break the build](general/code/exhaustive-matches-no-wildcard.md) — Match every variant explicitly.
- [Names are the index an agent navigates by](general/code/naming-is-the-index.md) — Units and qualifiers are suffixes in descending significance, so related names sort together.
- [No comments except doc comments, capped at two sentences](general/code/comments-are-banned-docs-are-not.md) — Source files carry doc comments only, each at most two sentences, plus machine-read directives.
- [No unwrap or expect outside tests, especially in the core](general/code/no-panics-outside-tests.md) — No panicking unwraps in production code.
- [Pin the locale and know which shell binds your line](general/code/locale-and-shell-portability.md) — Any script that classifies text pins its locale explicitly.
- [Regenerate every committed derivative in the same commit](general/code/generated-artifacts-are-regenerated.md) — Any artifact generated from the source and committed to the repository is regenerated and committed in the same change that alters its source.
- [Zero duplication, because agent-written code clones readily](general/code/no-duplication-threshold.md) — Zero tolerated clones.

## operations (6)

Deploying, publishing, and acting on live systems.

- [A multi-leg operation reports every leg, including the ones it skipped](general/operations/deploy-legs-report-skipped.md) — A multi-step operation emits a record for every step, always, including on failure: which succeeded, which failed with what error, and which were skipped because an earlier one failed.
- [An automated change is gated on the health of what it changed](general/operations/health-gated-changes.md) — After an automated change to a running system, assert that the system can do its work — not merely that its processes answer.
- [Design for the mixed-version window, because you are always in one](general/operations/mixed-version-windows-are-designed-for.md) — Assume both versions are running simultaneously.
- [Destructive and outward-facing actions are confirmed, every time](general/operations/destructive-actions-need-confirmation.md) — Ask before anything destructive or outward-facing: deploys, restarts, revocations, data resets, anything that sends content off the machine.
- [Thread identifiers from responses; never predict them](general/operations/never-guess-resource-ids.md) — Take every server-assigned identifier from the response that created the resource.
- [Treat a merge as publication, and know your disclosure boundary](general/operations/a-commit-is-a-publication.md) — Know how long it takes for a merge to become public, and treat the ignore rules that keep secrets out as a security control with its own review — not as housekeeping.
