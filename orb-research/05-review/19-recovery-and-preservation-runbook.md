---
orb_id: "ORB-N19"
orb_domain: review
tags:
  - orb/review
---

# Recovery and preservation runbook

[[ORB-strategy-research-plan|01 Master plan]] · [[01-control/02-governance-and-checkpoints|02 Governance and checkpoints]] · [[01-control/03-source-register|03 Source register]] · [[05-review/17-results-and-negative-findings|17 Results and negative findings]] · [[05-review/18-decision-and-release-log|18 Decision and release log]] · [[05-review/20-audit-and-acceptance-ledger|20 Audit and acceptance ledger]]

## File contract

- **Owner** — Project operator. **Reads** — 02–04, current append-only history and an independently retained checkpoint when available. **Writes** — Restore procedure, duplicate-attempt handling, supersession policy and recovery drill results.
- **Record** — `event_id, step_id, prior_head, version_basis, artifact_hashes, outcome, checkpoint_ref, retry_of`.
- [ ] Interrupt in the middle of a write, during work and after artifact creation but before acceptance. Prove replay recovers the last known complete state without duplicating acceptance or losing evidence.

## Resume and restore procedure

1. Open note 01, note 02 and the last accepted checkpoint. Compare Git identity, source hashes, approvals and evidence versions.
2. Reconcile isolated interrupted attempts with the accepted ledger before retry. Preserve partial or conflicting payloads and record which outputs may be used.
3. Restore approved originals and run artifacts into a clean location. Run `python3 verify.py` from the repository root for the staged archive and reconcile external storage against its own manifest.
4. Verify affected dependent checks and publish the next authorized action. Record any backup or checkpoint coverage gap.

The repository archive manifest covers its declared files. An independent restore and semantic review require separate observation.
