---
orb_id: "ORB-N02"
orb_domain: control
tags:
  - orb/control
---

# Governance and checkpoints

[[ORB-strategy-research-plan|01 Master plan]] · [[01-control/03-source-register|03 Source register]] · [[01-control/04-whole-source-read-receipts|04 Whole-source read receipts]] · [[05-review/19-recovery-and-preservation-runbook|19 Recovery and preservation runbook]] · [[05-review/20-audit-and-acceptance-ledger|20 Audit and acceptance ledger]]

## File contract

- **Owner** — Project operator. **Reads** — Approved scope, canonical project state, source registry and audit. **Writes** — Gate rules, who can approve changes, stop-and-resume instructions and the linked current checkpoint. Native approval and execution status stay in the canonical project records.
- **Record** — `checkpoint_id, scope_ref, next_action, dependency_ids, basis_digest, gate_result_ref, blocker`.
- [ ] Reopen the current baseline and verify authorized scope, exact versions and pending blockers before working. A changed basis reopens downstream gates.

## Current checkpoint

| Field | Current basis |
|---|---|
| Scope | Additive planning scaffold for `onlyvictus-bit/trade-vision-orb` |
| Repository intake | `main` at `41a297ca8d3837e36056629afda84d3caccbb7bd` before this scaffold |
| Work item | `ORB-SCAF-001`, recorded in note 17 |
| Next work | Reconcile relevant source versions and choose a research profile. A clearly labeled synthetic replay fixture can proceed independently |
| Open inputs | Selected market and feed, historical timestamps, costs, risk bounds and any downstream build target |

Record task-level source and test bases before acceptance. Maintain one canonical authority for scope and approvals. If a governance runner is adopted later, link its canonical records here. The template checkboxes remain unchecked until the corresponding observation exists.
