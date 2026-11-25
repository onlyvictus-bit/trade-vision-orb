---
orb_id: "ORB-N17"
orb_domain: review
tags:
  - orb/review
---

# Results and negative findings

[[ORB-strategy-research-plan|01 Master plan]] · [[02-market/06-data-and-point-in-time-contract|06 Data and point-in-time contract]] · [[03-research/11-experiment-preregistration|11 Experiment preregistration]] · [[05-review/16-statistical-validation|16 Statistical validation]] · [[05-review/18-decision-and-release-log|18 Decision and release log]]

## File contract

- **Owner** — Results steward. **Reads** — 11–16. **Writes** — Append-only results for valid runs, failures, nulls, aborted and inconclusive trials. Keep per-session, per-symbol and per-regime results linked to the underlying exact run.
- **Record** — `trial_id, run_id, result_ref, validity, split, metrics_with_units, uncertainty, sample_coverage, failure_reason, supersedes`.
- **Change entry** — `change_id, change_kind, description, source_ids, before_artifact_ref, after_artifact_ref, delta_details, run_ids, test_evidence, export_status`. Reconcile with 06 for dataset content and 18 for what is eligible for handoff.
- [ ] Every registered trial has a traceable state. Report gross and net, denominators, eligible/excluded opportunities and sensitivity. Missing observations retain an explicit reason.

## Change ledger

| Change ID | What changed | Before and after locations | Verification |
|---|---|---|---|
| `ORB-SCAF-001` | Added the 20-note planning vault and six reserved runtime directories. Added the repository entry link | Compared with `41a297ca8d3837e36056629afda84d3caccbb7bd`. See this note’s Git history and the root README link | Organizer inventory, blueprint byte identity, graph references, ignored runtime test paths and archive verification are the acceptance checks |

No market data, strategies or trial outcomes have been added. Follow-on entries record dataset coverage and counts when measured, source and destination paths, before/after immutable refs and test evidence. Keep failed, superseded and excluded records.
