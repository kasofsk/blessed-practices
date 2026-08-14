# Candidate blessed practices — a retro of jobs #1–#577

**Status: CANDIDATES.** Nothing here is adopted. Every file in this directory is
a proposal, to be reviewed one at a time and accepted, amended or rejected.
They were derived from this project's own development history rather than from
general engineering advice, and each one carries the evidence it was derived
from so the derivation can be argued with.

## What this is for

These are rules intended to condition agent behaviour: injected into work and
review prompts, cited by name in rejections, and — where the reasoning permits —
turned into gates. They are written to be portable to other agent-directed
systems, with the chuggernaut-specific evidence kept in each file's
`## Derivation` section rather than in the rule itself.

This corpus was built deliberately parallel to chuggernaut's own adopted rule
set (`docs/reference/style.md` in that repo) rather than as an extension of it.
Some candidates restate a rule that already lives there; those are kept because
the retro found fresh evidence for them, and because deciding what the two
corpora do with each other is part of the review.

## Method

The whole run of chuggernaut developing itself, as of 2026-08-14:

| Quantity | Value | Source |
| --- | --- | --- |
| Jobs filed | 577 | platform job records |
| Jobs merged | 411 | `git log --format=%s \| grep -c '^job/'` |
| Merged by type | 261 code, 62 web, 45 docs, 33 design, 8 manual, 1 molt | same |
| Task records | 2 940 | platform task records |
| Evaluator rejections | 355 | task results with a false verdict |
| Jobs needing no rework | 284 of 497 | max cycle per job |
| Jobs needing 3+ cycles | 86 | same |
| Tasks lost to infrastructure | 38 | `infra_loss` flag |

The rejection corpus — 355 findings, most of them several hundred words with
file, line, mechanism and suggested fix — is the primary evidence. Commit
bodies, the design corpus and the gate scripts are secondary. Numbers were taken
on 2026-08-14; re-derive rather than trust them.

## What the history actually says

**1. Stale prose is the dominant defect, by a wide margin.** 98 of the 355
rejections came from the two documentation evaluators, and almost all of them
say the same thing: a sentence in the present tense describes behaviour the
change just altered. Nothing else in the corpus is close. Candidates:
[present-tense-prose-is-a-claim](present-tense-prose-is-a-claim.md),
[docs-updated-in-the-same-commit](docs-updated-in-the-same-commit.md),
[cross-doc-state-claims](cross-doc-state-claims.md),
[sweep-the-class-not-the-instance](sweep-the-class-not-the-instance.md).

**2. The second-largest class is the check that cannot fail.** Guards that
cannot fire, tests green against the unfixed code, assertions on values the
function never reads, announcements broader than the run, and a coverage claim
that a whole tier executed when it self-skipped. Candidates:
[assertions-that-can-fail](assertions-that-can-fail.md),
[no-vacuous-assertions](no-vacuous-assertions.md),
[announce-exactly-what-ran](announce-exactly-what-ran.md),
[a-check-that-cannot-run-exits-distinctly](a-check-that-cannot-run-exits-distinctly.md).

**3. The most expensive architectural defect is the namespace question.** A
fact about a machine established from the wrong view — a container's instead of
the host's, the staging machine's instead of the executor's, the operator's uid
instead of the task's. It produced rework cycles across at least six jobs and
survived a repackaging of the whole worker. Candidates:
[re-derive-facts-in-the-executing-namespace](re-derive-facts-in-the-executing-namespace.md)
and its four refinements.

**4. Silent success is the failure mode that costs most per incident.** A
launch error that left a task Running forever; a broker permission that made a
whole feature no-op in production; a rule about socket access that was believed
for eleven days and was false the whole time. Candidates:
[refuse-loudly](refuse-loudly.md),
[unenforced-intentions-become-believed-facts](unenforced-intentions-become-believed-facts.md),
[silent-filters-hide-rows](silent-filters-hide-rows.md).

**5. Rework is the normal path, so its economics dominate.** 43% of jobs with
tasks needed at least one rework cycle. The practices that shorten cycles —
preserving the branch, passing the evidence forward, scoping what not to touch,
sweeping the class — are worth more than any individual code rule. Candidates:
[branch-preserved-across-rework](branch-preserved-across-rework.md),
[rework-context-carries-the-evidence](rework-context-carries-the-evidence.md),
[scope-the-rework-explicitly](scope-the-rework-explicitly.md).

**6. Several late-corpus cycles were lost to mechanical gate traps, not to bad
work.** Commit ordering against a staleness ledger accounted for at least six.
Candidates: [one-commit-when-ordering-matters](one-commit-when-ordering-matters.md),
[assertion-of-attention-over-timestamp](assertion-of-attention-over-timestamp.md),
[staleness-is-suspect-not-wrong](staleness-is-suspect-not-wrong.md).

## The architectural decisions worth preserving as rules

Six choices shaped everything downstream, and each is proposed here as a rule
rather than as a description: a single writer per record class; pure deciders
returning effects for one interpreter; one crate per external system; project-
owned, repo-versioned configuration; reading reviewers separated from executing
gates; and a mutable head over an append-only body for every decision document.

## How to read a candidate

Each file has frontmatter (`scope`, `altitude`, `portability`, `confidence`, and
a `rationale` saying why it was nominated), then four sections — the rule, the
why, how to apply it, and when it does not apply — then a `## Derivation`
section naming the jobs it came from. The rule is written to be injectable
verbatim; the derivation is not.

`confidence` reflects how strongly the evidence supports the rule, not how
strongly it is recommended. `portability: universal` means the rule as written
should transfer to another agent-directed repository; `project` means it
encodes something specific to this platform's shape.

## Suggested review order

1. The six architectural decisions above — they constrain the rest.
2. The four documentation practices in finding 1, which address a third of all
   rejections and are the cheapest to adopt.
3. The rework-economics group in finding 5.
4. Everything else, by scope.

Reject freely. A corpus of 110 rules is not a target; it is the widest honest
net over the evidence, and the useful output of the review is a much smaller set
that is actually enforced.

## Where these sit in this repo

`general/` holds the adopted practices: short, prose, no frontmatter, one topic
per file. This directory holds candidates in a heavier format, because a
candidate has to carry its evidence in order to be argued with and an adopted
rule does not.

The intended path is therefore one-way: review a candidate, and if it is
accepted, rewrite it into `general/` in that directory's plain style — dropping
the frontmatter and the derivation, keeping the rule and its why — then delete
the candidate. A candidate that is rejected is deleted with a line in the PR
saying why. What should not happen is this directory becoming a second adopted
corpus that nobody promotes out of.

Two open questions this PR does not settle: whether `general/` should grow
subdirectories by scope once it holds more than a handful of files, and whether
the adopted files should keep a pointer back to the evidence that produced them.

## Index

### architecture (28)

| Practice | Rule | Alt. | Conf. | Port. |
| --- | --- | --- | --- | --- |
| [no-content-hash-in-config](no-content-hash-in-config.md) | A content hash never enters operator-typed config | low | high | universal |
| [a-queue-entry-keeps-its-clock](a-queue-entry-keeps-its-clock.md) | A re-queued item keeps its original clock | low | high | universal |
| [boundaries-are-asserted-not-documented](boundaries-are-asserted-not-documented.md) | An architectural boundary that nothing checks is a comment | high | high | universal |
| [unenforced-intentions-become-believed-facts](unenforced-intentions-become-believed-facts.md) | An unenforced intention gets read as a statement of fact | high | high | universal |
| [which-kernel-execs-it](which-kernel-execs-it.md) | Ask each artifact the question its own executor asks | mid | medium | universal |
| [stage-then-swap](stage-then-swap.md) | Build aside, then swap atomically | mid | high | universal |
| [config-travels-with-the-project](config-travels-with-the-project.md) | Configuration is project-owned and repo-versioned | high | high | universal |
| [credential-lifetime-and-teardown-order](credential-lifetime-and-teardown-order.md) | Credential teardown runs after every consumer, not before | mid | medium | universal |
| [pure-decider-effects](pure-decider-effects.md) | Deciders return effects; interpreters perform them | high | high | universal |
| [restart-reconciliation-is-first-class](restart-reconciliation-is-first-class.md) | Every in-flight state has a restart arm | high | high | universal |
| [bounded-and-loud](bounded-and-loud.md) | Everything is bounded, and the bound is loud | mid | high | universal |
| [existence-identity-provenance](existence-identity-provenance.md) | Existence, identity and provenance are three separate questions | mid | high | universal |
| [fail-closed-allow-lists](fail-closed-allow-lists.md) | Grants are allow-lists, fail-closed, refused at three layers | mid | high | universal |
| [capture-before-disposal](capture-before-disposal.md) | Harvest before you reclaim, and never fail a job on cleanup | mid | high | universal |
| [separate-intent-from-observation](separate-intent-from-observation.md) | Keep declared intent and observed state in separate fields | mid | high | universal |
| [one-integration-point-per-dependency](one-integration-point-per-dependency.md) | One crate owns each external system | high | high | universal |
| [one-decision-site](one-decision-site.md) | One decision site per question | mid | high | universal |
| [one-resolver-per-question](one-resolver-per-question.md) | One resolver per lookup question | mid | high | universal |
| [single-writer-per-record](single-writer-per-record.md) | One writer per record class | high | high | universal |
| [refuse-loudly](refuse-loudly.md) | Prefer a loud refusal to a silent degradation | high | high | universal |
| [re-derive-facts-in-the-executing-namespace](re-derive-facts-in-the-executing-namespace.md) | Re-derive every host fact inside the namespace that will use it | high | high | universal |
| [read-modify-write-reads-again](read-modify-write-reads-again.md) | Re-read before you write back | low | high | universal |
| [reserved-namespace-prefixes](reserved-namespace-prefixes.md) | Reserve a prefix for platform-owned names | low | high | universal |
| [terminal-means-terminal](terminal-means-terminal.md) | Terminal states are terminal, and nothing self-heals after them | mid | medium | universal |
| [pure-data-layer](pure-data-layer.md) | The shared types layer has no I/O and no runtime | high | high | universal |
| [validate-before-you-mutate](validate-before-you-mutate.md) | Validate everything first, then mutate | mid | high | universal |
| [reachability-by-uid](reachability-by-uid.md) | What a process is told is not what its uid may open | mid | high | universal |
| [additive-wire-evolution](additive-wire-evolution.md) | Wire changes are additive, epoch-gated, and tolerated by N-1 | high | high | universal |

### process (30)

| Practice | Rule | Alt. | Conf. | Port. |
| --- | --- | --- | --- | --- |
| [silent-filters-hide-rows](silent-filters-hide-rows.md) | A dropped row reads like a negative result | mid | high | universal |
| [every-gate-has-a-test-suite](every-gate-has-a-test-suite.md) | A gate is code, so it has tests, and the tests are discovered | mid | high | universal |
| [behaviour-parity-is-proved-not-asserted](behaviour-parity-is-proved-not-asserted.md) | A refactor proves parity; it does not assert it | high | high | universal |
| [verdict-names-the-rule](verdict-names-the-rule.md) | A rejection names the rule it rejects under | mid | high | universal |
| [scope-the-rework-explicitly](scope-the-rework-explicitly.md) | A verdict says what to change and what not to touch | mid | high | universal |
| [acceptance-criteria-are-checkable](acceptance-criteria-are-checkable.md) | Acceptance criteria name an observation, not an intention | mid | high | universal |
| [empty-diff-is-a-verdict](empty-diff-is-a-verdict.md) | An empty diff is a first-class finding, verified not assumed | mid | high | universal |
| [escalation-preserves-the-operator-choice](escalation-preserves-the-operator-choice.md) | An escalation preserves the operator's distinct choices | mid | medium | project |
| [announce-exactly-what-ran](announce-exactly-what-ran.md) | Announce exactly what ran — never a tier you did not execute | mid | high | universal |
| [a-check-that-cannot-run-exits-distinctly](a-check-that-cannot-run-exits-distinctly.md) | Cannot-run and passed must not print the same | mid | high | universal |
| [whole-tree-not-just-the-diff](whole-tree-not-just-the-diff.md) | Cheap checks run whole-tree, not only over the diff | mid | high | universal |
| [stale-base-is-not-an-authoring-failure](stale-base-is-not-an-authoring-failure.md) | Distinguish a stale base from a bad attempt | mid | medium | project |
| [escalate-when-the-brief-is-unsatisfiable](escalate-when-the-brief-is-unsatisfiable.md) | Escalate an unsatisfiable brief instead of reworking it | mid | high | universal |
| [sweep-the-class-not-the-instance](sweep-the-class-not-the-instance.md) | Fix the class, and sweep the tree for its other instances | high | high | universal |
| [ratchet-dont-sweep](ratchet-dont-sweep.md) | Land a new rule as a ratchet, and make the debt greppable | mid | high | universal |
| [mechanise-the-checkable-half](mechanise-the-checkable-half.md) | Mechanise the checkable half; route the rest to judgement | high | high | universal |
| [gates-are-cheap-first](gates-are-cheap-first.md) | Order gates cheapest-first and diff-aware | mid | high | universal |
| [blessed-practices-are-numbered-and-cited](blessed-practices-are-numbered-and-cited.md) | Practices are numbered, tiered, injectable, and carry their why | high | high | universal |
| [prove-with-a-ladder](prove-with-a-ladder.md) | Prove a capability with a ladder of rungs, each one falsifiable | mid | medium | universal |
| [deviation-is-recorded-not-silent](deviation-is-recorded-not-silent.md) | Record every deviation from the brief, with its reason | high | high | universal |
| [verification-is-reported-with-its-command](verification-is-reported-with-its-command.md) | Report verification as commands and outputs, not as adjectives | mid | high | universal |
| [human-approval-only-where-no-gate-can-judge](human-approval-only-where-no-gate-can-judge.md) | Reserve human approval for what no gate and no reader can judge | high | medium | universal |
| [merge-conflicts-keep-both-records](merge-conflicts-keep-both-records.md) | Resolve record conflicts by keeping both, in landing order | mid | high | project |
| [reviewers-read-they-do-not-run](reviewers-read-they-do-not-run.md) | Reviewers read; gates run | high | high | universal |
| [branch-preserved-across-rework](branch-preserved-across-rework.md) | Rework builds on the previous attempt; it does not restart it | high | high | project |
| [rework-context-carries-the-evidence](rework-context-carries-the-evidence.md) | The rework brief carries the evidence, not just the verdict | high | high | universal |
| [the-ticket-is-the-contract](the-ticket-is-the-contract.md) | The ticket is the contract, and both sides read it verbatim | high | high | universal |
| [job-type-matches-the-work](job-type-matches-the-work.md) | The unit of work carries the type its change actually needs | mid | medium | project |
| [one-commit-when-ordering-matters](one-commit-when-ordering-matters.md) | When a gate reads commit order, ship one commit | low | high | project |
| [the-work-summary-is-for-the-approver](the-work-summary-is-for-the-approver.md) | Write the summary for whoever has to judge it, close calls first | mid | medium | universal |

### documentation (21)

| Practice | Rule | Alt. | Conf. | Port. |
| --- | --- | --- | --- | --- |
| [docs-updated-in-the-same-commit](docs-updated-in-the-same-commit.md) | A change updates the docs it makes stale, in the same commit | high | high | universal |
| [counts-in-prose-are-liabilities](counts-in-prose-are-liabilities.md) | A count in prose is a liability; give the command instead | mid | high | universal |
| [decide-do-not-straddle](decide-do-not-straddle.md) | A design decides the central question | high | high | universal |
| [cross-doc-state-claims](cross-doc-state-claims.md) | A doc asserting another doc's status is the most fragile sentence you can write | high | high | universal |
| [a-doc-nothing-links-to-is-unreachable](a-doc-nothing-links-to-is-unreachable.md) | A document nothing links to is unreachable, however true it is | mid | high | universal |
| [shed-the-corpus-at-milestones](shed-the-corpus-at-milestones.md) | A knowledge corpus needs a shedding process, not only an appending one | high | medium | universal |
| [mutable-head-append-only-body](mutable-head-append-only-body.md) | A mutable head over an append-only body | high | high | universal |
| [a-marker-is-not-a-silencer](a-marker-is-not-a-silencer.md) | An exemption mechanism must be narrower than the thing it exempts | mid | medium | universal |
| [assertion-of-attention-over-timestamp](assertion-of-attention-over-timestamp.md) | Clear an attention gate with an assertion of attention, not a timestamp | mid | medium | universal |
| [corrections-are-appended-and-dated](corrections-are-appended-and-dated.md) | Corrections are appended, dated, and name their job | mid | high | universal |
| [date-the-measurement](date-the-measurement.md) | Date every measurement, and name the host it was taken on | mid | high | universal |
| [deletion-needs-accounting](deletion-needs-accounting.md) | Deletion is reviewed by accounting, because the usual gates go green | mid | medium | universal |
| [docs-are-the-knowledge-store](docs-are-the-knowledge-store.md) | Knowledge lives in docs; code carries pointers | high | high | universal |
| [mark-unbuilt-intent](mark-unbuilt-intent.md) | Marking is a syntax, and the markers are not interchangeable | mid | high | project |
| [growth-is-measured-not-felt](growth-is-measured-not-felt.md) | Measure corpus growth; do not set a threshold for it | low | medium | universal |
| [one-definition-per-concept](one-definition-per-concept.md) | One definition per concept, and a registry that says where | high | high | universal |
| [present-tense-prose-is-a-claim](present-tense-prose-is-a-claim.md) | Present-tense prose about the tree is a factual claim | high | high | universal |
| [staleness-is-suspect-not-wrong](staleness-is-suspect-not-wrong.md) | Suspect is not wrong — publish a reading list, block almost nowhere | mid | high | universal |
| [commit-messages-carry-the-why](commit-messages-carry-the-why.md) | The commit message carries the why | high | high | universal |
| [the-landing-job-owns-the-doc-update](the-landing-job-owns-the-doc-update.md) | The job that lands a slice writes its status row | mid | high | project |
| [rejected-alternatives-are-part-of-the-record](rejected-alternatives-are-part-of-the-record.md) | The rejected alternatives are the part that cannot be re-derived | high | high | universal |

### testing (11)

| Practice | Rule | Alt. | Conf. | Port. |
| --- | --- | --- | --- | --- |
| [a-denial-with-no-control](a-denial-with-no-control.md) | A denial with no control identifies no mechanism | mid | high | universal |
| [no-vacuous-assertions](no-vacuous-assertions.md) | A test must be able to observe what its name claims | mid | high | universal |
| [self-skip-loudly](self-skip-loudly.md) | A test that cannot run says so; it never passes vacuously | mid | high | universal |
| [a-tool-outcome-measures-the-tool](a-tool-outcome-measures-the-tool.md) | A tool's outcome measures the tool, not your claim | mid | high | universal |
| [assertions-that-can-fail](assertions-that-can-fail.md) | Break it on purpose and watch the named case go red | high | high | universal |
| [measure-on-a-clean-fixture](measure-on-a-clean-fixture.md) | Measure on a fresh fixture, or the numbers lie | low | high | universal |
| [lowest-tier-that-expresses-it](lowest-tier-that-expresses-it.md) | New behaviour lands with a test at the lowest tier that can express it | high | high | universal |
| [golden-artifacts-are-regenerated](golden-artifacts-are-regenerated.md) | Regenerate golden artifacts; never hand-patch them | mid | high | universal |
| [test-the-premise](test-the-premise.md) | Test the premise, not only the behaviour | mid | high | universal |
| [the-gate-container-is-the-authority](the-gate-container-is-the-authority.md) | The gate's environment is the authority; local runs produce false reds | mid | high | project |
| [determinism-over-timing](determinism-over-timing.md) | Wait on the observable, never on the clock | mid | high | universal |

### code (14)

| Practice | Rule | Alt. | Conf. | Port. |
| --- | --- | --- | --- | --- |
| [function-length-cap](function-length-cap.md) | A numeric function-length cap, enforced | low | high | universal |
| [errors-name-the-actionable-thing](errors-name-the-actionable-thing.md) | An error names one cause and one action, and only when it is that cause | mid | high | universal |
| [do-not-use-exit-status-as-an-oracle](do-not-use-exit-status-as-an-oracle.md) | An exit status is not an existence oracle | low | high | universal |
| [surface-staleness-in-the-ui](surface-staleness-in-the-ui.md) | An interface that cannot prove freshness must not imply it | mid | high | universal |
| [assert-negative-space](assert-negative-space.md) | Assert what must never happen | mid | high | universal |
| [no-per-row-fetching](no-per-row-fetching.md) | Do not buy a display detail with a request per row | low | medium | universal |
| [dependencies-need-a-justification](dependencies-need-a-justification.md) | Every new dependency states its justification in the commit | low | medium | universal |
| [exhaustive-matches-no-wildcard](exhaustive-matches-no-wildcard.md) | Match exhaustively; a new variant should break the build | low | high | universal |
| [naming-is-the-index](naming-is-the-index.md) | Names are the index an agent navigates by | mid | high | universal |
| [comments-are-banned-docs-are-not](comments-are-banned-docs-are-not.md) | No comments except doc comments, capped at two sentences | mid | medium | universal |
| [no-panics-outside-tests](no-panics-outside-tests.md) | No unwrap or expect outside tests, especially in the core | mid | high | universal |
| [locale-and-shell-portability](locale-and-shell-portability.md) | Pin the locale and know which shell binds your line | low | high | universal |
| [generated-artifacts-are-regenerated](generated-artifacts-are-regenerated.md) | Regenerate every committed derivative in the same commit | mid | high | universal |
| [no-duplication-threshold](no-duplication-threshold.md) | Zero duplication, because agent-written code clones readily | mid | high | universal |

### operations (6)

| Practice | Rule | Alt. | Conf. | Port. |
| --- | --- | --- | --- | --- |
| [deploy-legs-report-skipped](deploy-legs-report-skipped.md) | A multi-leg operation reports every leg, including the ones it skipped | mid | high | universal |
| [health-gated-changes](health-gated-changes.md) | An automated change is gated on the health of what it changed | mid | high | universal |
| [mixed-version-windows-are-designed-for](mixed-version-windows-are-designed-for.md) | Design for the mixed-version window, because you are always in one | high | high | universal |
| [destructive-actions-need-confirmation](destructive-actions-need-confirmation.md) | Destructive and outward-facing actions are confirmed, every time | high | high | universal |
| [never-guess-resource-ids](never-guess-resource-ids.md) | Thread identifiers from responses; never predict them | mid | high | universal |
| [a-commit-is-a-publication](a-commit-is-a-publication.md) | Treat a merge as publication, and know your disclosure boundary | high | high | universal |
