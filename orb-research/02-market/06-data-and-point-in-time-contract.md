---
orb_id: "ORB-N06"
orb_domain: market
tags:
  - orb/market
---

# Data and point-in-time contract

[[ORB-strategy-research-plan|01 Master plan]] · [[01-control/03-source-register|03 Source register]] · [[02-market/05-market-and-session-contract|05 Market and session contract]] · [[02-market/08-features-and-regimes|08 Features and regimes]] · [[04-simulation/12-backtest-and-replay-contract|12 Backtest and replay contract]] · [[05-review/17-results-and-negative-findings|17 Results and negative findings]]

## File contract

- **Owner** — Data steward. **Reads** — 03 and 05. **Writes** — Schema, units, prices versus ticks, lot and currency conventions, event/receive clocks, instrument mapping, corporate actions or rolls, correction policy, lineage and data-quality reports.
- **Record** — `dataset_version, schema_version, instrument_id, event_time, available_at, sequence, revision_id, quality_flag, source_ref`.
- **Storage entry** — `dataset_id, version_id, layer, workspace_relative_path, durable_uri, content_hash, coverage, schema_version, ingest_run, source_ids, export_status`. Capture a stable URI or an approved retrieval method when the working copy is ephemeral.
- [ ] Verify point-in-time universe membership, realistic availability timestamps, units, empty/gapped ranges and duplicates. Identical duplicates are idempotent in normalized data. Conflicting duplicates are quarantined with both raw records preserved. Bad coverage never turns into zero volume.

## Repository-relative staging paths

| Path | Intended content |
|---|---|
| `sources/github/` | Exact copies of additional approved Git inputs |
| `data/raw/` | Immutable original deliveries |
| `data/normalized/` | Validated point-in-time snapshots |
| `data/derived/` | Versioned features, labels and research outputs |
| `runs/` | Run attempts, manifests and observations |
| `handoff/` | Eligible staged copies and exact export manifests |

No datasets are registered here yet. Record the published approved storage URI, content hash and actual path when an artifact is available. These checkout folders contain Git ignore markers so routine staging excludes their runtime contents. Record vendor rights before collecting or exporting data. Validate event time, known-at time and revision identity separately.
