---
orb_id: "ORB-N15"
orb_domain: simulation
tags:
  - orb/simulation
---

# Test oracles and fault cases

[[ORB-strategy-research-plan|01 Master plan]] · [[02-market/07-opening-range-and-signal-spec|07 Opening range and signal specification]] · [[04-simulation/12-backtest-and-replay-contract|12 Backtest and replay contract]] · [[04-simulation/13-execution-costs-and-capacity|13 Execution costs and capacity]] · [[04-simulation/14-risk-and-portfolio-contract|14 Risk and portfolio contract]] · [[05-review/20-audit-and-acceptance-ledger|20 Audit and acceptance ledger]]

## File contract

- **Owner** — Independent verifier. **Reads** — 05–08 and 11–14. **Writes** — Hand-computed fixtures, expected event traces, adversarial scenarios and independent regression checks.
- **Record** — `test_id, invariant, fixture_ref, expected_events, expected_ledger, failure_mutation, observed_run_ref`.
- [ ] For every blocking invariant, execute a valid case and a seeded failure. Verify that the latter actually fails. One fixture crosses ingestion, signal, fill, ledger and report.

## Initial oracle matrix

| Planned fixture | Independently expected observation |
|---|---|
| Opening range boundary and delayed open | Correct eligible events, frozen high/low and exact readiness time |
| Eligible trade and blocked opportunity | Correct signal, fill or rejection, fees, cash/position changes and net result |
| Same-bar ambiguity and partial fill | Frozen ambiguity policy, feasible quantity and residue handling |
| Future feature and late correction | Earlier decision unaffected or invalid input explicitly rejected |
| Stale ingestion, duplicate acceptance and interruption | Correct failure state, reproducible replay and retained attempt |
| Handoff mismatch | Changed base, altered hash or extra export path blocks acceptance |

Record exact fixture values before implementing the replay path. No strategy fixture has been run for this scaffold.
