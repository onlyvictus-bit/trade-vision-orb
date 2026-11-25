---
orb_id: "ORB-N14"
orb_domain: simulation
tags:
  - orb/simulation
---

# Risk and portfolio contract

[[ORB-strategy-research-plan|01 Master plan]] · [[02-market/07-opening-range-and-signal-spec|07 Opening range and signal specification]] · [[04-simulation/12-backtest-and-replay-contract|12 Backtest and replay contract]] · [[04-simulation/13-execution-costs-and-capacity|13 Execution costs and capacity]] · [[04-simulation/15-test-oracles-and-fault-cases|15 Test oracles and fault cases]] · [[05-review/16-statistical-validation|16 Statistical validation]]

## File contract

- **Owner** — Risk reviewer. **Reads** — 05, 07, 08, 12 and 13. **Writes** — Position sizing, simultaneous exposures, correlation and concentration limits, portfolio cash and margin rules, daily loss controls and invalidation policy.
- **Record** — `risk_version, constraint_id, scope, units, bound_ref, evaluation_time, breach_action, replay_fixture_id`.
- [ ] Stress simultaneous breakouts, invalid sizing inputs, adverse gaps and deferred fills. Check realized and pending exposure. Define whether each breach blocks entry, reduces exposure or halts the run.

## Risk decisions to freeze

Record units and independent limits for per-order size, total and directional exposure, concentration, correlated and simultaneous positions, realized loss, pending fills, liquidity participation and any applicable short or margin constraints. Name the breach action and time of evaluation. Missing parameters block any risk-dependent real run.

Verify simultaneous orders, invalid sizing, adverse gaps and fills after an attempted cancel. Reconcile pending obligations with realized positions and cash.
