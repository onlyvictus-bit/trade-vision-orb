---
orb_id: "ORB-N20"
orb_domain: review
tags:
  - orb/review
---

# Audit and acceptance ledger

[[ORB-strategy-research-plan|01 Master plan]] · [[01-control/02-governance-and-checkpoints|02 Governance and checkpoints]] · [[01-control/04-whole-source-read-receipts|04 Whole-source read receipts]] · [[04-simulation/15-test-oracles-and-fault-cases|15 Test oracles and fault cases]] · [[05-review/16-statistical-validation|16 Statistical validation]] · [[05-review/18-decision-and-release-log|18 Decision and release log]] · [[05-review/19-recovery-and-preservation-runbook|19 Recovery and preservation runbook]]

## File contract

- **Owner** — Independent reviewer. **Reads** — 01–19 and current canonical evidence. **Writes** — Derived requirement-by-requirement gate status, independent reruns and observed failures. Links to canonical decisions and checks.
- **Record** — `requirement_id, file_id, test_id, expected, observed_ref, basis_digest, status, reviewed_at_utc`.
- [ ] Run a two-way audit. Every requirement reaches a test and observation. Every material behavior and result has a requirement and scope. Stale and unaudited items remain open.

## Acceptance boundaries

| Check | Acceptance evidence |
|---|---|
| V01 organizer inventory | Master plan check plus exact Markdown paths and resolvable note navigation |
| Archive preservation | Repository `python3 verify.py` and an additive Git diff with no archive changes |
| Runtime folder structure | Six reserved directories and ignored synthetic test paths within each |
| V02–V11 | Execute the named source, replay, research, recovery and Git handoff verification on the applicable basis |

Do not mark completed strategy research from a scaffold test. Enter observed command, output or artifact reference, basis and result for each checked item. Keep pending gates visible when data, runtime or authorization is missing.
