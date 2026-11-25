---
orb_id: "ORB-N01"
orb_domain: root
tags:
  - orb/root
---

# Trade Vision ORB research workspace

Start here for the 20-file planning scaffold. The exact user-supplied blueprint follows below. Its delivery-state text records the original blueprint stage. The companion notes and reserved folders now exist in this repository. Research, implementation and strategy test status belong to the current checkpoints and evidence ledger.

## GitHub navigation

| ID | Organizer note |
|---|---|
| 01 | [Master plan](ORB-strategy-research-plan.md) |
| 02 | [Governance and checkpoints](01-control/02-governance-and-checkpoints.md) |
| 03 | [Source register](01-control/03-source-register.md) |
| 04 | [Whole-source read receipts](01-control/04-whole-source-read-receipts.md) |
| 05 | [Market and session contract](02-market/05-market-and-session-contract.md) |
| 06 | [Data and point-in-time contract](02-market/06-data-and-point-in-time-contract.md) |
| 07 | [Opening range and signal specification](02-market/07-opening-range-and-signal-spec.md) |
| 08 | [Features and regimes](02-market/08-features-and-regimes.md) |
| 09 | [Research notebook and evidence map](03-research/09-research-notebook-and-evidence-map.md) |
| 10 | [Hypotheses and falsifiers](03-research/10-hypotheses-and-falsifiers.md) |
| 11 | [Experiment preregistration](03-research/11-experiment-preregistration.md) |
| 12 | [Backtest and replay contract](04-simulation/12-backtest-and-replay-contract.md) |
| 13 | [Execution costs and capacity](04-simulation/13-execution-costs-and-capacity.md) |
| 14 | [Risk and portfolio contract](04-simulation/14-risk-and-portfolio-contract.md) |
| 15 | [Test oracles and fault cases](04-simulation/15-test-oracles-and-fault-cases.md) |
| 16 | [Statistical validation](05-review/16-statistical-validation.md) |
| 17 | [Results and negative findings](05-review/17-results-and-negative-findings.md) |
| 18 | [Decision and release log](05-review/18-decision-and-release-log.md) |
| 19 | [Recovery and preservation runbook](05-review/19-recovery-and-preservation-runbook.md) |
| 20 | [Audit and acceptance ledger](05-review/20-audit-and-acceptance-ledger.md) |

## Obsidian navigation

Open `orb-research/` as the vault. These links are the entry points for Obsidian graph navigation. Use a local graph or backlinks on an individual note to follow its dependencies.

- **Control** — [[01-control/02-governance-and-checkpoints|02 Governance and checkpoints]] · [[01-control/03-source-register|03 Source register]] · [[01-control/04-whole-source-read-receipts|04 Whole-source read receipts]]
- **Market** — [[02-market/05-market-and-session-contract|05 Market and session contract]] · [[02-market/06-data-and-point-in-time-contract|06 Data and point-in-time contract]] · [[02-market/07-opening-range-and-signal-spec|07 Opening range and signal specification]] · [[02-market/08-features-and-regimes|08 Features and regimes]]
- **Research** — [[03-research/09-research-notebook-and-evidence-map|09 Research notebook and evidence map]] · [[03-research/10-hypotheses-and-falsifiers|10 Hypotheses and falsifiers]] · [[03-research/11-experiment-preregistration|11 Experiment preregistration]]
- **Simulation** — [[04-simulation/12-backtest-and-replay-contract|12 Backtest and replay contract]] · [[04-simulation/13-execution-costs-and-capacity|13 Execution costs and capacity]] · [[04-simulation/14-risk-and-portfolio-contract|14 Risk and portfolio contract]] · [[04-simulation/15-test-oracles-and-fault-cases|15 Test oracles and fault cases]]
- **Review** — [[05-review/16-statistical-validation|16 Statistical validation]] · [[05-review/17-results-and-negative-findings|17 Results and negative findings]] · [[05-review/18-decision-and-release-log|18 Decision and release log]] · [[05-review/19-recovery-and-preservation-runbook|19 Recovery and preservation runbook]] · [[05-review/20-audit-and-acceptance-ledger|20 Audit and acceptance ledger]]

## Current repository basis

The preserved archive and its source map remain at the repository root. Note 03 identifies them at the intake commit and separates original-byte checks from research coverage. File paths for future data and run artifacts are outside this vault and are recorded in note 06. No target market, dataset, strategy result or future transfer destination was selected for this scaffold.

The blueprint begins after the marker below. Its UTF-8 body is retained byte for byte.

<!-- BEGIN EXACT ORB BLUEPRINT -->
# Opening Range Breakout research engine

**Format** — One UTF-8 Markdown master plan for a 20-file research workspace. This document is file 01. Each of the other 19 entries specifies a file to create, its owner, its records and its acceptance check. Findings, decisions and evidence remain readable after a new session starts.

**ASSUMPTION A-01** — ORB means Opening Range Breakout. **UNKNOWN U-01** — Venue, instrument, trading session, dataset, research period, execution restrictions, capital and risk limits. The market profile in file 05 must resolve the inputs a run needs. Examples below leave those values open.

**Status at delivery** — Architecture proposed. Source links identify research starting points. The plan includes an executable document check. Permission for paid data, external model transfers, paper broker connections and live execution is outside this plan.

**Objective** — Build a research engine capable of finding, explaining, rejecting and later reproducing an ORB edge. Define “edge” in a frozen research protocol as an improvement over a named executable baseline, net of applicable costs, with enough independent or dependence-adjusted evidence and with stability, risk and capacity inside predeclared bounds. **UNKNOWN U-02** — Whether any candidate has that edge.

> Complexity must earn its place. Every layer needs an economic mechanism, a decision-time input, an incremental test and a reason to remove or disable it. Keep the full history even when the layer is retired.

## 1. Scope and acceptance criteria

| ID | Required outcome | Design location | How to verify | Delivery status |
|---|---|---|---|---|
| R01 | One Markdown plan with exactly 20 fixed organizer paths and a single entry point | Sections 2 and 3 | V01 inventory and file-contract check | Document check supplied |
| R02 | Preserve complete originals, decisions, negative results and corrections. No source chunking or routine deletion | 02–04, 19, sections 4 and 7 | V02 byte-preservation and restart fault injection | Specified |
| R03 | Verify every material assumption and gate using current evidence | 02–04, 19–20, section 4 | V03 force stale evidence, missing receipts and duplicates | Specified |
| R04 | Research multiple dimensions of ORB with falsifiable hypotheses and a frozen baseline | 05–11, sections 5 and 6 | V04 trace each registered hypothesis to an ablation, baseline and stop rule | Specified |
| R05 | Reproduce decisions and simulated fills under realistic data, timing, costs and portfolio constraints | 06–09, 12–15 | V05 compare full-run outputs with an independently derived fixture and repeat the run | Specified |
| R06 | Control leakage, multiple testing, fragile results and holdout reuse | 10–11, 16–17 | V06 inject future data, substitute a different trial family and attempt a second holdout release | Specified |
| R07 | Resume with durable state, history and explicit boundaries | 01–04, 18–20, section 7 | V07 interrupt a run, restart, replay state and verify authorization boundaries | Specified |
| R08 | Report when a result is rejected, inconclusive or eligible for the next stage | 16–20, section 8 | V08 trace decision in both directions and try to promote a failed run | Specified |
| R09 | Identify every GitHub repository and exact revision used as a research input | 03, section 7.1 | V09 resolve pinned paths and verify their content hashes against the registered copies | Specified |
| R10 | Record where data is stored and what was added, modified, renamed or superseded | 06, 17, section 7.2 | V10 reconcile the change log against two frozen snapshots and verify each storage reference | Specified |
| R11 | Produce a verified copy of approved changes for a separately identified destination repository | 18–20, section 7.3 | V11 compare the proposed copy with the tested manifest and exercise a destination conflict | Specified |

## 2. Folder layout

```text
orb-research/
├── ORB-strategy-research-plan.md
├── 01-control/
│   ├── 02-governance-and-checkpoints.md
│   ├── 03-source-register.md
│   └── 04-whole-source-read-receipts.md
├── 02-market/
│   ├── 05-market-and-session-contract.md
│   ├── 06-data-and-point-in-time-contract.md
│   ├── 07-opening-range-and-signal-spec.md
│   └── 08-features-and-regimes.md
├── 03-research/
│   ├── 09-research-notebook-and-evidence-map.md
│   ├── 10-hypotheses-and-falsifiers.md
│   └── 11-experiment-preregistration.md
├── 04-simulation/
│   ├── 12-backtest-and-replay-contract.md
│   ├── 13-execution-costs-and-capacity.md
│   ├── 14-risk-and-portfolio-contract.md
│   └── 15-test-oracles-and-fault-cases.md
└── 05-review/
    ├── 16-statistical-validation.md
    ├── 17-results-and-negative-findings.md
    ├── 18-decision-and-release-log.md
    ├── 19-recovery-and-preservation-runbook.md
    └── 20-audit-and-acceptance-ledger.md
```

The count covers the fixed, human-maintained organizing workspace, including this plan. Whole source originals, immutable versions, market datasets, run output and native governance records belong in separately addressed runtime storage. Its contents grow with the evidence. A future governed implementation uses its canonical project records under `docs/fable/`. Entries in the twenty-file workspace link to those IDs and outcomes. In particular, 02 and 20 display canonical status and 18 cites the decision and authorization record. There is one authority for each approval and gate.

## 3. Twenty file contracts

The owner is a role, which may be filled by one person or separated in a later implementation. “Writes” specifies where each decision or record belongs. Evidence IDs resolve to exact immutable versions.

### 01 · `ORB-strategy-research-plan.md`

- **Owner** — Research owner. **Reads** — User scope, current gate status and open blockers. **Writes** — Objective, scope, file inventory, navigation order and acceptance map.
- **Record** — `requirement_id, owning_file, test_id, evidence_id, status`.
- [ ] Exactly 20 distinct paths exist in the design. Each requirement has a named file and test. The entry point identifies the current canonical checkpoint without copying its truth.

### 02 · `01-control/02-governance-and-checkpoints.md`

- **Owner** — Project operator. **Reads** — Approved scope, canonical project state, source registry and audit. **Writes** — Gate rules, who can approve changes, stop-and-resume instructions and the linked current checkpoint. Native approval and execution status stay in the canonical project records.
- **Record** — `checkpoint_id, scope_ref, next_action, dependency_ids, basis_digest, gate_result_ref, blocker`.
- [ ] Reopen the current baseline and verify authorized scope, exact versions and pending blockers before working. A changed basis reopens downstream gates.

### 03 · `01-control/03-source-register.md`

- **Owner** — Source steward. **Reads** — Official market rules, provider specs, original papers, user instructions and dataset deliveries. **Writes** — Immutable origin and version registrations, access constraints and dependencies.
- **Record** — `source_id, version_id, retrieval_utc, effective_period, canonical_uri, original_bytes_ref, byte_count, sha256, scope, rights, evidence_family, supersedes`.
- **GitHub entry** — Add `repository_url, repository_role, requested_ref, resolved_commit, repository_path, saved_path, use_reason, license_evidence`. Register each distinct repo/commit/path used. Use the same source ID in the read receipt and downstream change log.
- [ ] Recompute byte count and SHA-256 from the stored original. Review effective dates, authority, permissions and required scope. Investigate conflicting versions without losing either.

### 04 · `01-control/04-whole-source-read-receipts.md`

- **Owner** — Source coverage reviewer. **Reads** — 03, exact task specification and exact processor input. **Writes** — Receipt, coverage verdict, semantic review reference and any missing scope or truncation report.
- **Record** — `receipt_id, source_version, representation_id, task_hash, payload_hash, input_bytes, processor, output_ref, output_hash, evidence_class, verdict, utc`.
- [ ] Every required source has one current accepted receipt per task basis. A separate reviewer checks cited passages and any tables or figures the decision actually depends on.

### 05 · `02-market/05-market-and-session-contract.md`

- **Owner** — Market structure researcher. **Reads** — Time-effective exchange notices, instrument specification and feed documentation. **Writes** — Universe, venue, segment, calendar, auction policy, opening event, settlement/roll conventions and exceptional session handling.
- **Record** — `profile_id, venue, segment, tz_name, session_id_rule, open_anchor, eligible_trade_flags, effective_from, source_version`.
- [ ] Verify an ordinary day, shortened/special day, closure, halt or delayed reopen, and daylight saving where applicable. Assert exact boundary times against current authoritative sources for the intended era.

### 06 · `02-market/06-data-and-point-in-time-contract.md`

- **Owner** — Data steward. **Reads** — 03 and 05. **Writes** — Schema, units, prices versus ticks, lot and currency conventions, event/receive clocks, instrument mapping, corporate actions or rolls, correction policy, lineage and data-quality reports.
- **Record** — `dataset_version, schema_version, instrument_id, event_time, available_at, sequence, revision_id, quality_flag, source_ref`.
- **Storage entry** — `dataset_id, version_id, layer, workspace_relative_path, durable_uri, content_hash, coverage, schema_version, ingest_run, source_ids, export_status`. Capture a stable URI or an approved retrieval method when the working copy is ephemeral.
- [ ] Verify point-in-time universe membership, realistic availability timestamps, units, empty/gapped ranges and duplicates. Identical duplicates are idempotent in normalized data. Conflicting duplicates are quarantined with both raw records preserved. Bad coverage never turns into zero volume.

### 07 · `02-market/07-opening-range-and-signal-spec.md`

- **Owner** — Strategy researcher. **Reads** — 05 and 06. **Writes** — Baseline, range construction, state transitions, entry/exit semantics, valid order intent and no-trade reasons.
- **Record** — `strategy_version, range_anchor, range_end_rule, price_eligibility, trigger_rule, direction, expiry_rule, reentry_rule, exit_priority, no_trade_reason`.
- [ ] Two implementers can hand-trace the same synthetic session to identical range, signal and order intent. Include an exact end-boundary event, a gap through the trigger and empty range behavior.

### 08 · `02-market/08-features-and-regimes.md`

- **Owner** — Feature researcher. **Reads** — 05–07 and 10. **Writes** — Feature definitions, clocks, fit windows, missing behavior, regimes and whether features are eligible for production-style replay or diagnostics only.
- **Record** — `feature_id, formula_ref, unit, lookback, fit_fold, available_at_rule, missing_policy, mechanism, ablation_id`.
- [ ] For every input, prove availability by decision time. Fit transformations on training data only. A later event or correction leaves the historical decision unchanged.

### 09 · `03-research/09-research-notebook-and-evidence-map.md`

- **Owner** — Research analyst. **Reads** — 03–04, papers, official rules, method notes and contrary sources. **Writes** — Research questions, searches, reading outcomes, claim-to-source links, disagreements and concise decision rationale.
- **Record** — `claim_id, class, claim, exact_locator, source_version, receipt_id, evidence_family, counterevidence, limitation`.
- [ ] Decision-critical external claims link to exact passages and current receipts. Agreement between reprints, mirrors or analyses of the same raw sample counts as one evidence family.

### 10 · `03-research/10-hypotheses-and-falsifiers.md`

- **Owner** — Research lead. **Reads** — 07–09. **Writes** — Economic mechanisms, predictions, counter-hypotheses, cheapest decisive tests, test families and pivot conditions.
- **Record** — `hypothesis_id, mechanism, prediction, comparator, counter_hypothesis, falsifier, family_id, next_action`.
- [ ] Every candidate can lose. Specify what outcome eliminates the feature, which result is inconclusive, and what observation would justify rerunning with new evidence.

### 11 · `03-research/11-experiment-preregistration.md`

- **Owner** — Experiment operator. **Reads** — 05–10, 13–16. **Writes** — Frozen trial roster, splits, holdout permissions, analysis and risk thresholds, maximum trials and stopping rules.
- **Record** — `experiment_id, protocol_hash, candidate_ids, baseline_id, data_hash, split_id, metric_spec, trial_budget, selection_rule, holdout_policy`.
- [ ] Freeze the protocol before scoring. Preserve every tried specification, including abandoned runs and manual deviations. A changed rule creates a linked new protocol and leaves old results visible.

### 12 · `04-simulation/12-backtest-and-replay-contract.md`

- **Owner** — Simulation engineer. **Reads** — 05–08, 11, 13–15. **Writes** — Input/event ordering, deterministic run identity, strategy lifecycle, order lifecycle, cash and position reconciliation, run manifest and output contract.
- **Record** — `run_id, environment_ref, config_hash, source_hashes, protocol_hash, seed, lifecycle_events_ref, ledger_ref, report_ref`.
- [ ] Trace fixture data → features → eligibility → order intent → cash/position changes → metrics. A repeat on the frozen inputs matches the canonical event sequence exactly and produces metrics within predeclared tolerances.

### 13 · `04-simulation/13-execution-costs-and-capacity.md`

- **Owner** — Execution researcher. **Reads** — Venue rules, feed resolution, quotes and fee schedules. **Writes** — Executable fill assumptions, fees, taxes, spread, slippage, latency, borrow, impact and participation constraints. Mark applicability and how each cost component is counted.
- **Record** — `execution_model_id, instrument_scope, quote_basis, fill_policy, cost_components, latency_basis, stress_scenarios, calibration_evidence`.
- [ ] Reconcile a hand-calculated round trip through the actual cost model. Test gap-through, unavailable liquidity, and a partial fill with remainder cancellation. An OHLC-only run follows a frozen pessimistic rule or reports feasible bounds when intrabar path is ambiguous.

### 14 · `04-simulation/14-risk-and-portfolio-contract.md`

- **Owner** — Risk reviewer. **Reads** — 05, 07, 08, 12 and 13. **Writes** — Position sizing, simultaneous exposures, correlation and concentration limits, portfolio cash and margin rules, daily loss controls and invalidation policy.
- **Record** — `risk_version, constraint_id, scope, units, bound_ref, evaluation_time, breach_action, replay_fixture_id`.
- [ ] Stress simultaneous breakouts, invalid sizing inputs, adverse gaps and deferred fills. Check realized and pending exposure. Define whether each breach blocks entry, reduces exposure or halts the run.

### 15 · `04-simulation/15-test-oracles-and-fault-cases.md`

- **Owner** — Independent verifier. **Reads** — 05–08 and 11–14. **Writes** — Hand-computed fixtures, expected event traces, adversarial scenarios and independent regression checks.
- **Record** — `test_id, invariant, fixture_ref, expected_events, expected_ledger, failure_mutation, observed_run_ref`.
- [ ] For every blocking invariant, execute a valid case and a seeded failure. Verify that the latter actually fails. One fixture crosses ingestion, signal, fill, ledger and report.

### 16 · `05-review/16-statistical-validation.md`

- **Owner** — Validation reviewer. **Reads** — 10–15 and all registered trial results. **Writes** — Split hygiene, minimum effective sample, dependence-aware inference, multiplicity correction, uncertainty, robustness lenses and unsealing record.
- **Record** — `validation_id, protocol_hash, trial_family, split_ref, method_ref, diagnostic_ref, verdict, limitations`.
- [ ] Check overlap and embargo rationale, fit scope, locked holdout access and all-trial coverage. Challenge time, symbol and regime concentration and performance under less favorable execution.

### 17 · `05-review/17-results-and-negative-findings.md`

- **Owner** — Results steward. **Reads** — 11–16. **Writes** — Append-only results for valid runs, failures, nulls, aborted and inconclusive trials. Keep per-session, per-symbol and per-regime results linked to the underlying exact run.
- **Record** — `trial_id, run_id, result_ref, validity, split, metrics_with_units, uncertainty, sample_coverage, failure_reason, supersedes`.
- **Change entry** — `change_id, change_kind, description, source_ids, before_artifact_ref, after_artifact_ref, delta_details, run_ids, test_evidence, export_status`. Reconcile with 06 for dataset content and 18 for what is eligible for handoff.
- [ ] Every registered trial has a traceable state. Report gross and net, denominators, eligible/excluded opportunities and sensitivity. Missing observations retain an explicit reason.

### 18 · `05-review/18-decision-and-release-log.md`

- **Owner** — Research owner plus independent approver where required. **Reads** — 02, 16–17 and 20. **Writes** — Linked verdict, reasons, counterevidence, permitted next stage, reopening trigger and exact approval reference.
- **Record** — `decision_id, candidate_version, verdict, run_ids, counterevidence, approval_ref, conditions, supersedes`.
- **Git handoff entry** — `handoff_id, tested_snapshot, baseline_snapshot, destination_repo, target_branch, target_base_commit, manifest_ref, exclusions_ref, verification_ref, approval_ref, status, destination_commit_or_pr`. Update by adding a dated event when the handoff advances.
- [ ] A reviewer can reconstruct the verdict from primary artifacts and current checks. Promotion, holdout release, and any external action are distinct decisions.

### 19 · `05-review/19-recovery-and-preservation-runbook.md`

- **Owner** — Project operator. **Reads** — 02–04, current append-only history and an independently retained checkpoint when available. **Writes** — Restore procedure, duplicate-attempt handling, supersession policy and recovery drill results.
- **Record** — `event_id, step_id, prior_head, version_basis, artifact_hashes, outcome, checkpoint_ref, retry_of`.
- [ ] Interrupt in the middle of a write, during work and after artifact creation but before acceptance. Prove replay recovers the last known complete state without duplicating acceptance or losing evidence.

### 20 · `05-review/20-audit-and-acceptance-ledger.md`

- **Owner** — Independent reviewer. **Reads** — 01–19 and current canonical evidence. **Writes** — Derived requirement-by-requirement gate status, independent reruns and observed failures. Links to canonical decisions and checks.
- **Record** — `requirement_id, file_id, test_id, expected, observed_ref, basis_digest, status, reviewed_at_utc`.
- [ ] Run a two-way audit. Every requirement reaches a test and observation. Every material behavior and result has a requirement and scope. Stale and unaudited items remain open.

## 4. Verification every time

### 4.1 Evidence classes and scope

| Label | Meaning in this workspace | Evidence requirement |
|---|---|---|
| FACT | Externally sourced fact or directly observed result | Source/version and precise locator, or exact input, command, output and timestamp |
| ASSUMPTION | Research premise or chosen convention awaiting confirmation | Owner, impact, cheapest falsifier and next decision |
| ESTIMATE | Quantified inference derived from observations | Estimator, input basis, units, uncertainty and limitation |
| UNKNOWN | Required information or capability that has not been established | Resolve through a named source or experiment. Block decisions that depend on it |

A research decision retains its supporting and opposing evidence, alternatives, assumptions and reproducible reasoning summary. A hash binds bytes and a current receipt binds a processing claim. Independent checks of the original evidence and calculations establish the quality of the interpretation.

### 4.2 Whole-source protocol

1. **Freeze.** Inventory the exact required source versions for a named task. Identify the source-of-authority and effective date. Preserve the complete original once per distinct content version and byte-hash it. Revised and superseded versions remain retrievable.
2. **Measure.** Confirm access to the exact original, coverage of the full representation and feasibility of sending the whole source as one input. Budget for instructions, input, output and safety margin. If the whole source exceeds the verified limit, stop that dependent processing step, keep the entire source and mark the blocker. A compatible whole-file tool may complete the task when it can provide the needed evidence.
3. **Observe.** Deliver one complete original or one separately identified complete representation to the confirmed processor. Record the delivery hash, task hash, byte count, processor observation, result hash and truncation signals. Whole-file deterministic validation may stream bytes internally to hash or validate them. The source remains a whole file with no subset submissions, replacement summaries or content pruning.
4. **Reconcile.** Require current source and task hashes, exact required source inventory and one accepted outcome per source/representation/task basis. Mark missing outcomes `PARTIAL`, observed clipping `TRUNCATED`, contradictory receipts or hash mismatches `ERROR`, and superseded bases `STALE`. Use `COMPLETE` only for observed whole-source coverage at the stated evidence level.
5. **Review.** Cite exact pages or spans in accepted Markdown. For PDF, image or extracted content, record original and representation as separate identities and verify page counts, meaningful images, tables and extraction omissions. A manual receipt records what the reviewer observed. A runner-observed receipt requires execution evidence from the applicable supported runner.
6. **Resume.** Recompute hashes and re-derive statuses before relying on prior decisions. Maintain the historical source and its receipts. A changed version requires a new receipt and fresh dependent decisions on that basis.

A strict native coverage gate requires a compatible, qualified whole-file path. A partition-dependent workflow conflicts with this plan’s source-handling constraint. If the available integration cannot supply whole-file proof, retain the work and block any claim that needs the strict gate. Market dataset validation uses complete dataset integrity checks, provider checksums or snapshot manifests when available, and full-universe/period reconciliation. A sample visual check is recorded as a sample.

### 4.3 Preflight and postflight checkboxes

Create one checklist per material decision, experiment or resumed attempt. Compute the check from evidence. Each checked item links to `observed_ref` stored for the current `basis_digest`.

- [ ] Current scope, checkpoint and next step match the approved task.
- [ ] Required sources reopened and verified on the current basis. Missing, stale, failed and truncated receipts reviewed.
- [ ] Every load-bearing claim classified and tied to evidence or an explicit assumption and falsifier. Contradictions carried forward.
- [ ] Venue rules, clocks, dataset and feature availability are current for the periods used.
- [ ] Baseline, experiment, costs, splits, test family and holdout state match the frozen protocol.
- [ ] Execution records exact inputs, environment and outcomes. Retries and rejected attempts remain linked.
- [ ] Independent check confirms any material interpretation and reproduces the declared oracle at its required level.
- [ ] Outputs and new checkpoint committed consistently. Downstream gates reopened if the basis changed.

**Checklist row format** — `check_id | requirement_id | expected | observed_ref | basis_digest | checked_at_utc | status | blocker_or_next_action`. Set status to `PASS`, `FAIL`, `UNKNOWN`, `STALE` or `NOT_APPLICABLE` with a reason and approver for applicability exceptions. A check has no evidentiary weight when its underlying observation is missing.

## 5. Strategy and research engine

### 5.1 Reference strategy to beat

Use a single selected universe, one session profile, one preregistered opening window and one fixed trigger/exit policy. Define the range over eligible events in the half-open interval `[anchor, range_end)`. Freeze it when the decision engine can know the range is ready. Use a separate eligibility rule for the first post-range event, including arrival ordering, delayed events and exact-boundary ties. Define long and short scope independently and record a no-trade reason for each blocked opportunity.

The state machine starts at `WAIT_SESSION`, builds in `BUILD_RANGE`, transitions to `READY` after validation, and records `SIGNALLED`, `ORDER_PENDING`, `POSITION_OPEN` and `DONE` where applicable. Define transition priority for late or invalid data, gap-throughs, opposing triggers, pending cancels, cutoffs and risk interventions. Keep decision rules in 07 and fill mechanics in 13 so candidate and reference share the same execution assumptions.

Open definitions tested as distinct assumptions include scheduled continuous open versus instrument-specific open, auction inclusion versus continuous-only prices, and eligibility during reopening. **FACT** — NYSE’s auction page says the NYSE opening process begins at 9:30 a.m. Eastern and an individual security can open later. **FACT** — NSE’s equities documentation describes a pre-open session with matching and a transition to continuous trading, alongside exception handling for outages and market-wide circuit events. These are venue examples. [NYSE Auctions](https://www.nyse.com/trade/auctions) · [NSE Pre-Open Session](https://www.nseindia.com/static/products-services/equity-market-pre-open)

### 5.2 Dimensions to investigate

All candidates in this table are **ASSUMPTIONS** to investigate. Each row proposes a feature family and a test. Record all the combinations actually tried, including exploratory results.

| Dimension | Decision-time questions and examples | Cheapest discriminating check |
|---|---|---|
| Session construction | Does delayed instrument opening or auction inclusion alter the tradeable range? | Replay the same sessions with eligibility rules held fixed except for the anchor or print treatment |
| Opening geometry | Do normalized range width, open within the range, gap direction, and prior close or prior-day extrema change continuation? | Hold exits and costs fixed. Compare matched baseline opportunities and quantify retained coverage |
| Volume and liquidity | Does relative volume at the same elapsed session time add information after controlling for spread and tick size? | Compare baseline, volume alone, liquidity gate alone and both on identical data |
| Auction and order flow | Do point-in-time auction imbalance, signed trade flow or depth changes add independent signal? | Verify publication clocks. Lag or perturb the feature and remove it in an ablation. Gate research on usable feed coverage |
| Market and sector context | Does synchronized breadth, sector direction or a reference-market move explain an instrument breakout? | Use a timestamp-safe join. Compare baseline, context-only and combined, with instrument/session matched evaluation |
| Volatility and regimes | Do causal volatility states, gap states and session conditions change continuation versus reversal? | Fit regime boundaries within each training window. Test predeclared regimes out of sample and report effective support |
| Breakout shape | Do immediate crosses, close confirmation, retests or failed breaks improve fill-adjusted outcomes? | Measure wait cost and missed trades on the same opportunities. Separate improvement from changes in exposure and entry price |
| Event risk | Do known-at-the-time calendars, earnings or special sessions invalidate otherwise eligible signals? | Use publication-era schedules and mark unknown times. Compare disabled and enabled event policies in and outside affected windows |
| Exit and sizing | Do a volatility-scaled exit or a time-based exit improve net distribution under equivalent risk and exposure? | Isolate exit and size effects. Audit intrabar ambiguity, tail losses and altered holding-time overlap |
| Portfolio and capacity | Do apparent profits survive common exposure, clustered openings, short constraints and impact? | Replay competing same-time intents with shared cash, feasible size, recorded borrow assumptions and adverse costs |

Study a simple additive filter before allowing an interaction. Register why a particular interaction should exist and how you will distinguish it from lower trade count, concentration or risk scaling. If a feature needs unavailable microstructure data, keep it as an open hypothesis while data-supported families continue. A regime supported only by a small cluster stays inconclusive.

### 5.3 Research inputs and search order

| Starting source | What to extract in a research run | Interpretation boundary |
|---|---|---|
| [NYSE Auctions](https://www.nyse.com/trade/auctions) and [NSE Pre-Open Session](https://www.nseindia.com/static/products-services/equity-market-pre-open) | Effective session definitions, auction status, delays and emergency changes | Check the selected venue, segment and date. Register linked notices and historical versions where rules changed |
| [Holmberg, Lönnbark and Lundström, ORB working paper](https://www.econ.umu.se/ueslpnr/ues845.pdf) | Threshold definition, sample construction, assumptions, data and applicability | **FACT** — Its documented application uses U.S. crude oil futures. Verify transfer empirically for the selected instrument and execution model |
| [White, A Reality Check for Data Snooping](https://doi.org/10.1111/1468-0262.00152) | Candidate-family definition and implications of reusing data during selection | **FACT** — The published abstract describes a test for the best model in a specification search against a benchmark. Verify prerequisites before choosing this or another method |
| [Bailey et al., The Probability of Backtest Overfitting](https://www.risk.net/journal-of-computational-finance/2471206/the-probability-of-backtest-overfitting) | Overfitting diagnostic, input requirements and applicability | Evaluate the diagnostic against trial-family completeness and time-series split rules |

Run discovery in this order. Find the exchange calendar, rulebook and change notices. Read provider schema, timestamps, flags, revision history and sample snapshots. Locate primary papers and replication or null findings. Find fees, taxes, borrow and execution evidence for the market profile. Record search terms, dates and source versions. Group dependent analyses that share the same raw feed or backtest. Stop searching when material decisions have sufficient evidence and contrary findings are accounted for. Keep unresolved evidence in 09.

**Source access for this blueprint, 23 November 2026** — Relevant passages of the exchange pages, the ORB paper’s abstract and application, and White’s abstract informed the references above. These accesses are discovery evidence. Whole-source research receipts and direct market-data evidence are open.

## 6. Build sequence and experiments

| Step | Deliverable | How to check |
|---|---|---|
| 1. Freeze scope | Market profile, required source inventory, acceptable data rights, research question and unknowns | Reconcile 03–06 and V02–V03. Required sources have usable current receipts |
| 2. Prove data and replay | One fully traced session with a hand-calculated baseline and fills | V05 verifies arrival ordering, range boundaries, ledgers, reported result and adverse data/fill cases |
| 3. Register tests | Baseline terms, candidate families, folds, metric formulas and stop rules | V04 checks every hypothesis and comparator. V06 verifies split hygiene and seals final holdout |
| 4. Screen cheaply | Mechanism checks, one-factor ablations and eligible sample coverage in development | Record every trial and open exposure/confounding gaps. Verify all tried families in 17 |
| 5. Validate survivors | Chronological walk-forward with fold-frozen fitting, test-period results and stress scenarios | Verify training and label overlap, future-data sentinel, cost sensitivity, parameter neighborhoods and single-session/symbol dependence |
| 6. Lock and test | Candidate selection frozen before a single confirmatory holdout evaluation | V06 records exact release, prior access and decision rule. A viewed holdout becomes historical and a new independent period is required for renewed confirmation |
| 7. Judge and resume | Verdict, independent reproduction, evidence-backed status and next stage | V07–V08 reopen decisions with invalidated inputs and verify no unsupported promotion is possible |

### Required experimental controls

- **Point-in-time replay.** Compare event time and available time on a normalized clock with deterministic sequence and tie policy. A feature using a fully completed bar is eligible only once the replay can know that bar. Preserve adjustments and original prices separately. Simulate from an as-of view with historical membership or instrument identifiers.
- **Splits.** Use chronological training, validation and final holdout where data permits. Account for label/position interval overlap across boundaries with a documented purge and gap where needed. Fit thresholds and transforms within training. Evaluate each fold with the candidate chosen under the registered procedure. If the untouched sample is insufficient, verdict is inconclusive.
- **Comparators.** Use the executable ORB baseline, no-trade reference, individual ablations and an appropriately matched control when meaningful. Keep data, execution and risk constraints comparable. Report eligible opportunities, selection coverage, exposure and the net incremental effect at the predeclared comparison unit.
- **Metrics.** Specify denominator and units for net expectancy per eligible opportunity and per filled trade, aggregate daily P&L, net basis points or risk-normalized P&L, drawdown, turnover, tail losses, fill rate, time in market and participation. Consider break-even cost and capacity. Define the primary metric, hurdle, downside limits, dependence treatment and minimum effective sample before selection. Report uncertainty using a method suitable for clustered or serially dependent observations. Test parameter stability around the chosen configuration.
- **Falsification.** Stress adverse costs, latency, price resolution, stricter fills, data delays and regime changes. Run future-information and timestamp sentinels. Explain large changes caused by leaving out a large session, symbol, event or regime. Use placebo or shuffled controls only with a design that respects the dependence being tested.
- **Research budget.** Freeze the number of trials and interactions in advance. Select a multiplicity approach suited to the registered trial families. Keep holdout results inaccessible until the candidate, thresholds and adjudication rule are fixed. Forward paper evaluation, if separately authorized, uses the frozen candidate and predeclared comparison windows.

### Research adjudication record

Freeze the comparison unit and a paired effect, such as daily candidate net P&L minus daily baseline net P&L over the same eligible sessions. Include zero activity on eligible sessions in that comparison when the protocol calls for it. Treat excluded sessions and unobservable costs as explicit gaps. Define the economic hurdle, uncertainty rule, minimum support, downside ceiling and acceptable execution stress in 11 before evaluating candidates. A valid result whose uncertainty spans the hurdle is inconclusive unless the frozen decision rule resolves it. Statistical evidence, adverse cost performance, sensitivity to a concentrated period and portfolio risk each receive their own verdict in 16. The combined verdict in 18 requires the predeclared conjunction of passing gates.

### Worked trace

**ASSUMPTION** — “A liquid, tightly quoted instrument with a large opening imbalance in the direction of the breakout has better net continuation than the base ORB.” This is a candidate hypothesis and contains no observed values.

1. `H-IMBALANCE` in 10 cites the auction rules and exact imbalance publication fields in 03–05. The feature in 08 must be visible by the simulated decision.
2. `EXP-IMBALANCE` in 11 freezes range policy, liquidity definition, count of compared specifications, cost stress, metrics and fold calendar before scoring.
3. Compare baseline, liquidity-only, imbalance-only and combined versions on the same replay and report how many opportunities the filters exclude. Report each direction independently if the protocol permits.
4. Cheapest falsifier in 15. Shift availability of selected imbalance messages just after the decision and ensure decisions cannot use them. If the unshifted dataset itself lacks verifiable publication times, block the imbalance arm.
5. If improvement vanishes under preregistered costs, depends on concentrated days, or its interval misses the registered success rule, log the evidence in 17 and verdict in 18. If the execution is invalid, fix the mechanism and rerun under a new linked run ID. Keep the invalid run.

## 7. Continuity and protection of history

1. **Run identity.** Bind each run to content hashes for source versions, code identity, configuration, data, calendar, protocol and environment. Keep each attempt ID even when the run basis is identical. Deduplicate accepted outcomes by work item and exact basis. A duplicate with a different outcome proceeds to quarantine and review.
2. **Write discipline.** Use a single serialized writer or compare-and-swap for canonical accepted event history. Workers write only to isolated attempt outputs. Publish an accepted checkpoint after referenced artifacts are durable and validated. If a process stops, retain incomplete attempts and classify their state before retrying.
3. **Preservation.** Append corrections with a pointer to what they supersede, reason, author and timestamp. Use read-only snapshots for originals, run output and old organizer versions. Check storage budget and use a permitted larger retention tier or pause collection when capacity is insufficient. A genuinely conflicting retention or licensing rule becomes a recorded blocker for ingesting that source.
4. **Resume.** Load 01 → 02 → 03–04 → 19 → 20, then only the necessary complete domain sources and record IDs. Verify version basis, latest accepted checkpoint, open failures, active approval and next step. A changed source reopens exactly the affected dependencies. The ledger retains old evidence and records why it no longer applies.
5. **Recovery test.** Rebuild a checkpoint from the retained evidence in an isolated location. Scan the ledger for gaps and duplicates, compare reconstructed outputs and check the last independently held checkpoint if one exists. A chain’s internal consistency and proof that history is complete are separate evidence claims.
6. **External effects.** The first development stages are research and simulation. Paid subscriptions, provider transfers, connected paper brokerage and live orders each need applicable authorization. Autonomy within an approved stage never advances the stage or changes the authorized scope.

### 7.1 GitHub source log

File 03 owns the input repository register. For each GitHub source, record its canonical `owner/repo` URL, observed branch/tag if one was requested, full resolved commit, exact repository-relative path, commit-pinned browser link, retrieval time, saved location, SHA-256 of the saved bytes and the purpose for which it was used. Record authorization and license evidence for reuse or transfer. If a consumed path comes from a submodule or Git LFS, record the pinned child commit or object ID and verify the actual consumed content. A working-tree edit must be registered as a separate preserved version. A branch name aids navigation. The commit and path identify the source used.

File 18 separately records the **destination repository**. An upstream research repository and the repository receiving the tested ORB work may be different. **UNKNOWN** — no GitHub source repository, destination repository or branch has been selected for this blueprint. An ambiguous or changed destination leaves the handoff pending.

### 7.2 Data locations and change log

These are proposed paths relative to an approved durable evidence root. File 06 records the authoritative location of each actual artifact, including its full relative path and durable URI. The paths below are outside the 20 organizer-file count.

| Proposed location | Contents |
|---|---|
| `sources/github/` | Whole, versioned copies of the GitHub sources actually required for the research |
| `data/raw/` | Original vendor deliveries, preserved by source, dataset and version |
| `data/normalized/` | Validated and normalized snapshots with lineage back to raw inputs |
| `data/derived/` | Versioned feature, label and research datasets linked to the generation run |
| `runs/` | Simulation output, submitted settings, logs, test observations and replay reports |
| `handoff/` | Dated manifests and optional staged copies of explicitly selected deliverables |

File 17 records what changed against a named baseline snapshot. A code, document or config entry records its path, before and after identity and a plain-language description of what was added or changed. A dataset entry records the new time span, symbols, fields or schema changes where applicable, and measured added, updated or quarantined counts when those operations can be determined. Use explicit `UNKNOWN` for unmeasured counts and a reason when a field does not apply. Treat first versions as additions and record prior references for corrections and supersessions. A rename retains both paths in the log. Preserve previous source and data bytes.

Build this log from a diff between frozen snapshots and, for datasets, stable record keys or a versioned provider change feed. Reconcile the log with the actual inventory and flag any unexplained item. Tracking a change and authorizing its export are distinct checks. Keep the full change history and derive a destination-specific manifest from the approved subset.

### 7.3 Copy and handoff to the destination Git repository

1. **Freeze the tested candidate.** Record the before snapshot, exact tested snapshot or authorized candidate commit, completed test IDs and evidence hashes. Include additions that first existed as untracked files by capturing them in the tested snapshot. Link the actual tests to the exact intended payload.
2. **Prepare the manifest.** File 18 links a per-path export manifest with `change_id, source_ref, destination_relative_path, operation, before_hash, after_hash, size_bytes, file_mode, evidence_ref, export_disposition`. Log excluded paths and reasons. Include notes on changes in the tested code, tests, configuration, documentation and approved portable data. Where raw, restricted, sensitive or oversized data will stay in its approved store, include only permitted references, schema and reproduction instructions. Keep credentials out of the export.
3. **Stage an exact copy.** Use an isolated clean checkout of the explicitly chosen target and its recorded base commit. Copy only the manifest’s approved whole files. Verify source and destination hashes, allowed paths and modes, and reject file paths escaping the worktree. Report destination files that changed since the recorded base. A removal or rename that removes a destination path requires explicit authorization. Preserve the prior artifact and change record.
4. **Verify the handoff.** Check the staging diff against the approved manifest, account for every addition and modification, confirm every excluded file stays out, and run the required tests on the staged result. If the target moved or a test fails, keep the attempt and replan against the current target. Record `COPY_VERIFIED` only after the copy and checks pass.
5. **Record transfer status.** An authorized commit, push or pull request is a separate action. File 18 records the branch, commit or PR link, and final destination verification when observed. The original research workspace and evidence remain recoverable. A tested research handoff can include negative findings. It does not establish trading readiness.

- [ ] V09 pin the source repo and commit, advance a branch in a fixture, and prove the research reference still retrieves the original bytes.
- [ ] V10 compare two inventories with an addition, a modification and an excluded data artifact. Verify the log describes them and each included locator resolves to its expected hash.
- [ ] V11 copy the exact approved fixture files into a clean target snapshot, compare bytes and path changes, and run the target tests. Inject destination drift and a tampered payload separately and require each to block acceptance. An external Git action needs the user’s authorization.

## 8. Decision options and promotion rules

**ESTIMATE** — The confidence levels below are qualitative judgments of architectural fit. This plan has no calibrated probability of finding an edge.

| Path | Tradeoff and weakest assumption | Cheapest test and pivot point | Fit |
|---|---|---|---|
| Minimal reference study | A small baseline experiment needs less data and can falsify quickly. It cannot satisfy the requested multidimensional workspace alone | Hand-replay one regular and one exceptional session. Pivot to the full workspace once baseline semantics and costs reconcile | Medium for initial diagnosis |
| Twenty-file evidence-first engine | A market-specific baseline with versioned inputs and gated feature expansion satisfies the research organization scope. It requires usable point-in-time data and consistent record ownership | Run one whole-source check and one independently traced fixture. If data cannot support decision timing, restrict the research family or change the data source | Medium for delivery as a functioning engine, subject to data and runtime validation |
| Multi-feed event-level expansion | Adds order-flow and capacity questions, with higher reconciliation and maintenance burden. Assumes quote or depth histories and trustworthy clocks for the chosen market | Verify a legally usable sample, session coverage and arrival ordering. Defer the expansion if depth, timestamps or rights cannot support the claimed experiment | Low before feed verification |

**Recommended architecture** — Use the 20-file engine. Make the minimal reference study its first end-to-end milestone. Add event-level dimensions only when the market profile, evidence and opportunity set support them.

| Verdict | Conditions | Consequence |
|---|---|---|
| `INVALID` | Leakage, source drift, unverified required data, ledger mismatch or another failed integrity check | Preserve outputs and block conclusions. Repair the evidence path, then rerun |
| `REJECTED` | A valid frozen experiment misses its preregistered economic, stability or risk rule | Preserve the finding. Reopen only with new evidence or a materially new hypothesis |
| `INCONCLUSIVE` | Valid results with insufficient effective sample or uncertainty spanning the admissible outcome | Collect eligible evidence or narrow the claim. Keep any viewed holdout historical |
| `RESEARCH_PASS` | Current source, runtime, statistical, cost and risk checks pass with independent review | Eligible for a separate paper-stage decision |
| `PAPER_PASS` | A separately authorized frozen forward trial meets its monitoring, execution and evidence requirements | Eligible for a separate authorization decision. Live readiness requires its own evidence and approval |

## 9. Verification boundary and reproducible document check

**Status** — This Markdown blueprint is the deliverable. Venue configuration, a 20-file instantiated workspace, datasets, the replay engine, trade results and native project gates are future work. No edge or instrument recommendation has been established.

**UNTESTED — verify before use.** Before relying on the strategy or using an implementation, execute V02–V11 against the chosen runtime, market profile and Git destination. The first replay test must independently assert exact range membership, known-at ordering, side and time of each fill, cost, position/cash ledger, reported net P&L and one no-trade/invalid branch from a hand-computed fixture. Inject a future timestamp, stale original, duplicate outcome, interrupted write and unauthorized holdout reopening. Require each injected defect to fail the intended gate, retain its evidence and then repeat the original fixture from a fresh process. Section 7 gives the Git source and transfer fixture tests.

Run this command from the directory containing the plan for V01 and the whole-file hash smoke test. It verifies the document inventory, one acceptance check per file contract, requirement/test coverage and sample mutation detection. Edge performance needs market data and a replay runtime.

```bash
python3 - ORB-strategy-research-plan.md <<'PY'
from hashlib import sha256
from pathlib import Path
import re
import sys

plan = Path(sys.argv[1])
raw = plan.read_bytes()
document = raw.decode("utf-8")
inventory = re.search(r"orb-research/\n(.*?)^\x60{3}", document, re.M | re.S)
assert inventory, "Missing folder inventory"
tree_paths = []
folder = None
for line in inventory.group(1).splitlines():
    node = re.fullmatch(r"([│ ]   )?[├└]── ([^/]+)(/)?", line)
    assert node, f"Unrecognized tree entry: {line}"
    indent, name, directory = node.groups()
    if directory:
        assert not indent, f"Unexpected nested folder: {name}"
        folder = Path(name)
    elif indent:
        assert folder, f"Missing parent folder for {name}"
        tree_paths.append(folder / name)
    else:
        tree_paths.append(Path(name))
contracts = re.findall(r"^### (\d{2}) · \x60([^\x60]+\.md)\x60$", document, re.M)
assert [number for number, _ in contracts] == [f"{i:02}" for i in range(1, 21)]
paths = [Path(path) for _, path in contracts]
assert len(set(paths)) == 20, "Duplicate file paths"
assert all(not path.is_absolute() and ".." not in path.parts for path in paths)
assert tree_paths == paths, "Inventory differs from contracts"
contract_section = document.split("## 3. Twenty file contracts", 1)[1]
contract_section = contract_section.split("## 4. Verification every time", 1)[0]
for number, block in enumerate(re.split(r"(?m)^### ", contract_section)[1:], 1):
    assert re.search(r"(?m)^- \[ \] \S", block), f"Missing checkbox for file {number}"
rows = re.findall(r"^\| (R\d{2}) \|[^\n]+\b(V\d{2})\b", document, re.M)
assert rows == [(f"R{i:02}", f"V{i:02}") for i in range(1, 12)]
print("PASS: 20 numbered file contracts match inventory and include checkboxes")
print("PASS: 11 requirements map to 11 verification IDs")

original = b"complete source\n"
revised = original + b"new material\n"
version = sha256(original).hexdigest()
snapshots = {version: original, sha256(revised).hexdigest(): revised}
assert len(snapshots) == 2 and snapshots[version] == original
print("PASS: a whole-source edit has a distinct identity and preserves prior bytes")
print("SHA-256:", sha256(raw).hexdigest())
PY
```
<!-- END EXACT ORB BLUEPRINT -->
