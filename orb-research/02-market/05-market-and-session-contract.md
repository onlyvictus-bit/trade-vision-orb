---
orb_id: "ORB-N05"
orb_domain: market
tags:
  - orb/market
---

# Market and session contract

[[ORB-strategy-research-plan|01 Master plan]] · [[01-control/03-source-register|03 Source register]] · [[02-market/06-data-and-point-in-time-contract|06 Data and point-in-time contract]] · [[02-market/07-opening-range-and-signal-spec|07 Opening range and signal specification]] · [[04-simulation/13-execution-costs-and-capacity|13 Execution costs and capacity]]

## File contract

- **Owner** — Market structure researcher. **Reads** — Time-effective exchange notices, instrument specification and feed documentation. **Writes** — Universe, venue, segment, calendar, auction policy, opening event, settlement/roll conventions and exceptional session handling.
- **Record** — `profile_id, venue, segment, tz_name, session_id_rule, open_anchor, eligible_trade_flags, effective_from, source_version`.
- [ ] Verify an ordinary day, shortened/special day, closure, halt or delayed reopen, and daylight saving where applicable. Assert exact boundary times against current authoritative sources for the intended era.

## Market profile inputs

| Decision | State | Evidence to record |
|---|---|---|
| Venue, segment and instrument class | UNKNOWN | Current and historically applicable exchange rules |
| Session, time zone and open reference | UNKNOWN | Trading calendar, auction rules and selected eligible events |
| Delayed, special or halted sessions | UNKNOWN | Applicable historical notices and provider event flags |
| Tick, lot, currency and contract units | UNKNOWN | Time-effective specifications and sample validation |

A synthetic profile can exercise the boundary rules while market and feed selection remains open.
