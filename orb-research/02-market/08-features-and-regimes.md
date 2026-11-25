---
orb_id: "ORB-N08"
orb_domain: market
tags:
  - orb/market
---

# Features and regimes

[[ORB-strategy-research-plan|01 Master plan]] · [[02-market/06-data-and-point-in-time-contract|06 Data and point-in-time contract]] · [[02-market/07-opening-range-and-signal-spec|07 Opening range and signal specification]] · [[03-research/10-hypotheses-and-falsifiers|10 Hypotheses and falsifiers]] · [[03-research/11-experiment-preregistration|11 Experiment preregistration]]

## File contract

- **Owner** — Feature researcher. **Reads** — 05–07 and 10. **Writes** — Feature definitions, clocks, fit windows, missing behavior, regimes and whether features are eligible for production-style replay or diagnostics only.
- **Record** — `feature_id, formula_ref, unit, lookback, fit_fold, available_at_rule, missing_policy, mechanism, ablation_id`.
- [ ] For every input, prove availability by decision time. Fit transformations on training data only. A later event or correction leaves the historical decision unchanged.

## Feature intake

| Family | Admission evidence |
|---|---|
| Geometry, gaps and prior session | Eligible range and comparable prior-period units |
| Relative volume, liquidity and spread | Same elapsed-session baseline, executable quote semantics and a known-at clock |
| Auction and order flow | Publication-time data and valid venue flags |
| Breadth, market and sector | Timestamp-safe point-in-time joins and membership |
| Regime, volatility and event context | Training-only fit, validated announcement clocks and observable support |

Every candidate needs a baseline comparison, ablation, missing value policy and a test that future values cannot change a prior decision.
