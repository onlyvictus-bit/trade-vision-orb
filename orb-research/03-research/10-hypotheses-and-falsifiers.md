---
orb_id: "ORB-N10"
orb_domain: research
tags:
  - orb/research
---

# Hypotheses and falsifiers

[[ORB-strategy-research-plan|01 Master plan]] · [[02-market/07-opening-range-and-signal-spec|07 Opening range and signal specification]] · [[02-market/08-features-and-regimes|08 Features and regimes]] · [[03-research/09-research-notebook-and-evidence-map|09 Research notebook and evidence map]] · [[03-research/11-experiment-preregistration|11 Experiment preregistration]]

## File contract

- **Owner** — Research lead. **Reads** — 07–09. **Writes** — Economic mechanisms, predictions, counter-hypotheses, cheapest decisive tests, test families and pivot conditions.
- **Record** — `hypothesis_id, mechanism, prediction, comparator, counter_hypothesis, falsifier, family_id, next_action`.
- [ ] Every candidate can lose. Specify what outcome eliminates the feature, which result is inconclusive, and what observation would justify rerunning with new evidence.

## Proposed research tests

| ID | Candidate mechanism | Baseline comparison and falsifier |
|---|---|---|
| `HYP-LIQUIDITY` | Decision-time liquidity may affect continuation economics | Compare matched opportunities with identical costs. Reject or mark inconclusive using the frozen threshold if the net effect fails or coverage is inadequate |
| `HYP-AUCTION` | Opening imbalance may add information beyond liquidity | Compare baseline, liquidity-only, imbalance-only and combined. Block the arm when publication times are unavailable |
| `HYP-REGIME` | Breakout behavior may vary across volatility states | Fit the regime on training data. Evaluate the preregistered effect out of sample and inspect concentration |

These are hypotheses. Freeze the comparator, mechanism, family, support and adjudication rule in note 11.
