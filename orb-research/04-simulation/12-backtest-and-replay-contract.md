---
orb_id: "ORB-N12"
orb_domain: simulation
tags:
  - orb/simulation
---

# Backtest and replay contract

[[ORB-strategy-research-plan|01 Master plan]] · [[02-market/06-data-and-point-in-time-contract|06 Data and point-in-time contract]] · [[02-market/07-opening-range-and-signal-spec|07 Opening range and signal specification]] · [[04-simulation/13-execution-costs-and-capacity|13 Execution costs and capacity]] · [[04-simulation/14-risk-and-portfolio-contract|14 Risk and portfolio contract]] · [[04-simulation/15-test-oracles-and-fault-cases|15 Test oracles and fault cases]] · [[05-review/17-results-and-negative-findings|17 Results and negative findings]]

## File contract

- **Owner** — Simulation engineer. **Reads** — 05–08, 11, 13–15. **Writes** — Input/event ordering, deterministic run identity, strategy lifecycle, order lifecycle, cash and position reconciliation, run manifest and output contract.
- **Record** — `run_id, environment_ref, config_hash, source_hashes, protocol_hash, seed, lifecycle_events_ref, ledger_ref, report_ref`.
- [ ] Trace fixture data → features → eligibility → order intent → cash/position changes → metrics. A repeat on the frozen inputs matches the canonical event sequence exactly and produces metrics within predeclared tolerances.

## First replay path

Whole snapshot → validation → ordered events with availability times → frozen opening range → order intent → feasible fill or reason-coded miss → cash and position ledger → metrics and run manifest.

The first run needs independently known outputs for one eligible action and one blocked opportunity. Compare each transition, fee, quantity, and observable result. Repeat on the same frozen inputs with an exact event sequence and preregistered metric tolerances. Keep malformed and interrupted attempts visible. No engine implementation or run exists in this scaffold.
