---
orb_id: "ORB-N07"
orb_domain: market
tags:
  - orb/market
---

# Opening range and signal specification

[[ORB-strategy-research-plan|01 Master plan]] · [[02-market/05-market-and-session-contract|05 Market and session contract]] · [[02-market/08-features-and-regimes|08 Features and regimes]] · [[04-simulation/12-backtest-and-replay-contract|12 Backtest and replay contract]] · [[04-simulation/15-test-oracles-and-fault-cases|15 Test oracles and fault cases]]

## File contract

- **Owner** — Strategy researcher. **Reads** — 05 and 06. **Writes** — Baseline, range construction, state transitions, entry/exit semantics, valid order intent and no-trade reasons.
- **Record** — `strategy_version, range_anchor, range_end_rule, price_eligibility, trigger_rule, direction, expiry_rule, reentry_rule, exit_priority, no_trade_reason`.
- [ ] Two implementers can hand-trace the same synthetic session to identical range, signal and order intent. Include an exact end-boundary event, a gap through the trigger and empty range behavior.

## Baseline design sequence

1. Select a session anchor and one preregistered window. Document the opening auction and delayed-open policy.
2. Freeze the range over eligible events in `[open, range_end)` only after those events are knowable.
3. Record the first eligible post-range trigger, tie priority, long/short scope, cancellation and expiry.
4. Produce an order intent or reason-coded abstention. Simulate the fill and exit using note 13 and apply risk in note 14.
5. Check exact boundary and ledger values against the independent oracle in note 15.

The reference parameters and execution rules are open. Keep candidates linked to the frozen baseline via note 11.
