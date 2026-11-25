---
orb_id: "ORB-N13"
orb_domain: simulation
tags:
  - orb/simulation
---

# Execution costs and capacity

[[ORB-strategy-research-plan|01 Master plan]] · [[02-market/05-market-and-session-contract|05 Market and session contract]] · [[02-market/06-data-and-point-in-time-contract|06 Data and point-in-time contract]] · [[04-simulation/12-backtest-and-replay-contract|12 Backtest and replay contract]] · [[04-simulation/14-risk-and-portfolio-contract|14 Risk and portfolio contract]] · [[05-review/16-statistical-validation|16 Statistical validation]]

## File contract

- **Owner** — Execution researcher. **Reads** — Venue rules, feed resolution, quotes and fee schedules. **Writes** — Executable fill assumptions, fees, taxes, spread, slippage, latency, borrow, impact and participation constraints. Mark applicability and how each cost component is counted.
- **Record** — `execution_model_id, instrument_scope, quote_basis, fill_policy, cost_components, latency_basis, stress_scenarios, calibration_evidence`.
- [ ] Reconcile a hand-calculated round trip through the actual cost model. Test gap-through, unavailable liquidity, and a partial fill with remainder cancellation. An OHLC-only run follows a frozen pessimistic rule or reports feasible bounds when intrabar path is ambiguous.

## Execution model inputs

Record quote convention, feasible event resolution, commissions and exchange fees, spread crossing, slippage, latency, lot constraints and participation. Add borrow, margin, impact and taxes where applicable and supported. Declare each applicable component’s units and avoid charging spread twice.

Test gap-through, stale quote, partial fill and insufficient volume. For bars with conflicting intrabar paths, freeze a conservative outcome or report feasible bounds. Calibrate after the market and feed are selected.
