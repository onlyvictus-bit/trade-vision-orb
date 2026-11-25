---
orb_id: "ORB-N04"
orb_domain: control
tags:
  - orb/control
---

# Whole-source read receipts

[[ORB-strategy-research-plan|01 Master plan]] · [[01-control/03-source-register|03 Source register]] · [[03-research/09-research-notebook-and-evidence-map|09 Research notebook and evidence map]] · [[05-review/20-audit-and-acceptance-ledger|20 Audit and acceptance ledger]]

## File contract

- **Owner** — Source coverage reviewer. **Reads** — 03, exact task specification and exact processor input. **Writes** — Receipt, coverage verdict, semantic review reference and any missing scope or truncation report.
- **Record** — `receipt_id, source_version, representation_id, task_hash, payload_hash, input_bytes, processor, output_ref, output_hash, evidence_class, verdict, utc`.
- [ ] Every required source has one current accepted receipt per task basis. A separate reviewer checks cited passages and any tables or figures the decision actually depends on.

## Coverage register

Capture one whole-file outcome per source, representation and task basis. Track processing evidence and semantic review separately.

| Source | Current coverage evidence | Open check |
|---|---|---|
| `SRC-ORB-BLUEPRINT` | Exact blueprint bytes are retained inside note 01, with the source hash in note 03 | Apply task-specific interpretation checks when deriving strategy requirements |
| `SRC-ORB-ARCHIVE` | Repository `verify.py` checks the archive against its declared per-file byte counts, Git blob IDs and SHA-256 values | Whole-source task receipts and semantic disposition for research inputs are pending |

Create concrete receipts only when an actual processor outcome exists. Report `PARTIAL`, `TRUNCATED`, `ERROR` or `STALE` on the appropriate basis. Source-hash parity alone proves byte identity.
