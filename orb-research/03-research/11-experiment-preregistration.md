---
orb_id: "ORB-N11"
orb_domain: research
tags:
  - orb/research
---

# Experiment preregistration

[[ORB-strategy-research-plan|01 Master plan]] · [[03-research/10-hypotheses-and-falsifiers|10 Hypotheses and falsifiers]] · [[04-simulation/12-backtest-and-replay-contract|12 Backtest and replay contract]] · [[04-simulation/15-test-oracles-and-fault-cases|15 Test oracles and fault cases]] · [[05-review/16-statistical-validation|16 Statistical validation]] · [[05-review/17-results-and-negative-findings|17 Results and negative findings]]

## File contract

- **Owner** — Experiment operator. **Reads** — 05–10, 13–16. **Writes** — Frozen trial roster, splits, holdout permissions, analysis and risk thresholds, maximum trials and stopping rules.
- **Record** — `experiment_id, protocol_hash, candidate_ids, baseline_id, data_hash, split_id, metric_spec, trial_budget, selection_rule, holdout_policy`.
- [ ] Freeze the protocol before scoring. Preserve every tried specification, including abandoned runs and manual deviations. A changed rule creates a linked new protocol and leaves old results visible.

## Freeze checklist

- [ ] Fix the data, session and strategy versions, baseline and candidate IDs, research family, trial limit and cost/risk basis.
- [ ] Record chronology, fit windows, purging rationale, holdout access rules, metrics, uncertainty and acceptance thresholds.
- [ ] Preserve rejected, failed and manually changed specifications as separate trial outcomes.
- [ ] Bind the holdout opening and verdict to the exact protocol hash.

No protocol, fold calendar or holdout is registered. The registered trial log starts after the synthetic replay and source gates are met.
