---
orb_id: "ORB-N03"
orb_domain: control
tags:
  - orb/control
---

# Source register

[[ORB-strategy-research-plan|01 Master plan]] · [[01-control/04-whole-source-read-receipts|04 Whole-source read receipts]] · [[02-market/06-data-and-point-in-time-contract|06 Data and point-in-time contract]] · [[03-research/09-research-notebook-and-evidence-map|09 Research notebook and evidence map]] · [[05-review/17-results-and-negative-findings|17 Results and negative findings]]

## File contract

- **Owner** — Source steward. **Reads** — Official market rules, provider specs, original papers, user instructions and dataset deliveries. **Writes** — Immutable origin and version registrations, access constraints and dependencies.
- **Record** — `source_id, version_id, retrieval_utc, effective_period, canonical_uri, original_bytes_ref, byte_count, sha256, scope, rights, evidence_family, supersedes`.
- **GitHub entry** — Add `repository_url, repository_role, requested_ref, resolved_commit, repository_path, saved_path, use_reason, license_evidence`. Register each distinct repo/commit/path used. Use the same source ID in the read receipt and downstream change log.
- [ ] Recompute byte count and SHA-256 from the stored original. Review effective dates, authority, permissions and required scope. Investigate conflicting versions without losing either.

## Registered planning inputs

| Source ID | Exact input and version | Saved location and scope |
|---|---|---|
| `SRC-ORB-BLUEPRINT` | User-supplied Markdown, SHA-256 `b8d2d63c7e91ba6913569b9b63df650c1b5c73d5fcc5acbdf366a56818773b96` | Complete original text under the blueprint markers in note 01. Authority for this layout |
| `SRC-ORB-ARCHIVE` | `onlyvictus-bit/trade-vision-orb` at [`41a297c`](https://github.com/onlyvictus-bit/trade-vision-orb/commit/41a297ca8d3837e36056629afda84d3caccbb7bd) | `baseline/` and its `SOURCE_MAP.json` at the repository root. The source map carries per-file upstream paths, revisions and identity evidence |

Treat further upstream repositories, individual sources and versions as open until verified for a named research task. The archive's source map names `onlyvictus-bit/trade-vision-app` as its upstream repository. That provenance does not establish a fresh upstream read or select a future handoff target.
