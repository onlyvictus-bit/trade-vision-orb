---
orb_id: "ORB-N18"
orb_domain: review
tags:
  - orb/review
---

# Decision and release log

[[ORB-strategy-research-plan|01 Master plan]] · [[01-control/02-governance-and-checkpoints|02 Governance and checkpoints]] · [[05-review/16-statistical-validation|16 Statistical validation]] · [[05-review/17-results-and-negative-findings|17 Results and negative findings]] · [[05-review/19-recovery-and-preservation-runbook|19 Recovery and preservation runbook]] · [[05-review/20-audit-and-acceptance-ledger|20 Audit and acceptance ledger]]

## File contract

- **Owner** — Research owner plus independent approver where required. **Reads** — 02, 16–17 and 20. **Writes** — Linked verdict, reasons, counterevidence, permitted next stage, reopening trigger and exact approval reference.
- **Record** — `decision_id, candidate_version, verdict, run_ids, counterevidence, approval_ref, conditions, supersedes`.
- **Git handoff entry** — `handoff_id, tested_snapshot, baseline_snapshot, destination_repo, target_branch, target_base_commit, manifest_ref, exclusions_ref, verification_ref, approval_ref, status, destination_commit_or_pr`. Update by adding a dated event when the handoff advances.
- [ ] A reviewer can reconstruct the verdict from primary artifacts and current checks. Promotion, holdout release, and any external action are distinct decisions.

## Decision and handoff register

| Item | Current scope |
|---|---|
| `ORB-SCAF-001` | Planning scaffold in `onlyvictus-bit/trade-vision-orb`. Use this file’s Git history to locate the scaffold commit |
| Future tested ORB copy-back | Destination repo, branch, approved manifest and baseline are pending |
| Strategy promotion | Pending valid data, registered protocol, replay, out-of-sample evidence and independent review |

For any future copy-back, freeze the tested snapshot and expected destination base, verify an allowlisted staged diff and hashes, and rerun the applicable tests. Keep copy, commit, remote and PR status distinct.
