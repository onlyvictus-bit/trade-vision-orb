# Trade Vision ORB preservation and handoff

This is a staged baseline and migration plan. `baseline/` contains intact source files, `SOURCE_MAP.json` records their provenance and review status, and `FOLLOW_UP.md` is the handoff queue. `changes/` is reserved for new decisions with separate IDs. No implementation or semantic review is implied by an imported file.

## ORB research workspace

Open the [ORB research plan](orb-research/ORB-strategy-research-plan.md) for the 20-note planning scaffold, source and data registers, research gates, and Git handoff paths. Open `orb-research/` as a vault to navigate the linked notes in Obsidian.

## Acceptance criteria

1. Every expected source version has an exact copy or an explicit recovery gap. Raw originals and attachments are retained whole. The same path can have different versions. Identical bytes can share storage only when every original location and message identity is still listed.
2. Each copied original matches the pinned source bytes, byte count, and hash. Recheck after import and again after restoring from an independently stored copy.
3. Every sentence and meaningful element has an ordered locator in the intact original and a review disposition. Account for all bytes, including formatting, through explicit contiguous coverage ranges. Record lists, tables, formulas, code, footnotes, messages, and attachments. Links point into intact originals. The review ledger contains pointers and decisions, never substitute excerpts.
4. Every build-relevant passage has an implementation reference, a pending action, an explicitly approved replacement, or a recorded conflict. Missing sources, unreadable text, unknown authorship, and ambiguous wording stay visible. A source-health check does not certify interpretation.
5. Every Trade Vision action points back to the exact source version or approved change. Its target branch, PR, merged commit, and acceptance evidence are linked before its status becomes Verified.

## Execution order

1. Close the source inventory. Start with the pinned Git snapshots in the source map. Compare all relevant branch heads and history for additional versions, then reconcile relevant chat export indexes and attachment inventories with the user's thread list. Keep original export files and conversation structure, including alternate visible replies where available. Identify user messages, AI proposals, later corrections, and user-approved decisions from the source. Record missing or truncated exports with their recovery owner and available locator. Keep unrelated or sensitive export contents in an authorized restricted location. Decide which conversation and attachment files may enter the private GitHub repository before uploading them.
2. Preserve without chunking. Archive each complete source version as one file. Hash raw bytes before parsing or editing. Use raw Git blob identity and SHA-256 for Git imports. For rich documents, preserve originals and verify any derived extraction against the rendered pages and elements. Large originals stay intact. If a reviewer cannot review a whole source reliably, assign a qualified direct review and keep semantic coverage pending.
3. Review by reference. Bind the coverage ledger to the source hash. Enumerate locators deterministically, including structural content and formatting ranges. Reject gaps, duplicate locators, stale versions, and overlapping coverage ranges. Distinct requirements may cite the same locator. Duplicate ideas retain all origin IDs. Check negations, qualifiers, dates, units, dependencies, and conflicting versions against the originals. Keep superseded or rejected wording and its disposition.
4. Resolve and transfer. For each accepted change, record its ID, origin, exact before and approved after wording, reason, decision evidence, dependencies, target, and acceptance test. Compare the target branch first so an already implemented action is linked instead of repeated. Move pending actions through Proposed, Approved, Merged, and Verified. Do not merge a build that depends on unresolved source gaps or conflicts.
5. Publish the approved baseline in the private ORB repository. Confirm account and private visibility before uploading. Verify the complete manifest in a fresh checkout, then verify a restore from a separate approved backup. Preserve previous immutable snapshots and their provenance. Add a Trade Vision pointer only after its destination is verified.

## Verification and recovery

```sh
python3 verify.py
```

The verifier checks the staged baseline against its inventory, including extra, missing, renamed, or altered source files. A restore test must extract into a clean directory and run the same verifier. A negative test must reject an altered byte and a removed file. Before enabling build handoff, separately test that semantic coverage rejects a missing locator, duplicate locator, stale source version, and an unresolved conflict on an affected requirement.

Coverage states are separate. **Preserved** means exact bytes for the declared source. **Reviewed** means the sentence-level ledger and source-linked review passed. **Delivered** means Trade Vision acceptance evidence passed. No state automatically promotes another.

Unknown historical material cannot be counted as recovered. The staged Git inventory is deliberately scoped to the refs and paths listed in the source map. Unknown chats, attachments, and additional versions remain visible in the follow-up queue.
