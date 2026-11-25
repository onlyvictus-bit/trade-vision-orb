---
orb_id: "ORB-N16"
orb_domain: review
tags:
  - orb/review
---

# Statistical validation

[[ORB-strategy-research-plan|01 Master plan]] · [[03-research/11-experiment-preregistration|11 Experiment preregistration]] · [[04-simulation/13-execution-costs-and-capacity|13 Execution costs and capacity]] · [[04-simulation/15-test-oracles-and-fault-cases|15 Test oracles and fault cases]] · [[05-review/17-results-and-negative-findings|17 Results and negative findings]] · [[05-review/18-decision-and-release-log|18 Decision and release log]]

## File contract

- **Owner** — Validation reviewer. **Reads** — 10–15 and all registered trial results. **Writes** — Split hygiene, minimum effective sample, dependence-aware inference, multiplicity correction, uncertainty, robustness lenses and unsealing record.
- **Record** — `validation_id, protocol_hash, trial_family, split_ref, method_ref, diagnostic_ref, verdict, limitations`.
- [ ] Check overlap and embargo rationale, fit scope, locked holdout access and all-trial coverage. Challenge time, symbol and regime concentration and performance under less favorable execution.

## Validation protocol

Use chronological development and walk-forward evaluation, a sealed final holdout, registered metrics and a trial-family-aware inference method. Check training-only fits and overlap. Compare net outcomes, opportunity denominators, exposures, stability around settings and economic stress using the frozen baseline.

Separate a failed integrity check, a valid rejection, insufficient evidence and a passing experiment. Log interval uncertainty, compatible sample size, cost scenarios and concentration. Study handling of multiple tests before selection. Real-data validation remains open.
