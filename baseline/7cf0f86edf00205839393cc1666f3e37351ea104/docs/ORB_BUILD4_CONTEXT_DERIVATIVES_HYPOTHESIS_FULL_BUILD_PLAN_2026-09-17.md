# TRADE VISION — ORB BUILD-4 FULL BUILD PLAN
## Canonical Context + Derivatives Intelligence + Competing Hypothesis Brain

**Repository:** `onlyvictus-bit/trade-vision-app`  
**Planning branch at audit base:** `m4-d6-orchestration-redesign`  
**Verified audit-base SHA:** `29e9e126401a512c13743871206c2ee6b22772b3`  
**Plan branch:** `plan/orb-build4-d0-lock-full-plan`  
**Document date:** 2026-09-17  
**Status:** FORMAL BUILD PLAN / PLAN-ONLY / NO BUILD-4 RUNTIME CODE IMPLEMENTED BY THIS DOCUMENT

---

# 0. Mission

BUILD-4 creates the canonical ORB context and bounded market-deliberation layer.

It must answer, from point-in-time evidence:

- what market facts are known;
- what facts are missing, stale, conflicting, not applicable, or unavailable;
- where price is relative to trusted levels/value;
- what trend/volatility/participation/structure/context state exists;
- what derivatives positioning/volatility facts exist when valid sources exist;
- what competing explanations fit the current situation;
- what evidence supports and attacks each explanation;
- what should happen next if each explanation is correct;
- what failure sequence would weaken/invalidate it;
- what observation would best distinguish unresolved competing explanations;
- when the system must abstain because evidence is insufficient or OOD.

BUILD-4 does **not** execute, route orders, set final guidance, invent support/resistance, manufacture missing values, or publish uncalibrated probabilities.

The intended reasoning chain is:

```text
OBSERVED FACTS
    ↓
SOURCE-DERIVED / LOCAL-DERIVED ANALYTICS
    ↓
INFERRED STATES
    ↓
COMPETING HYPOTHESES
    ↓
SUPPORT / OPPOSITION / UNKNOWN / CONFLICT
    ↓
EXPECTED PATH / FAILURE PATH / INVALIDATION / EXPIRY
    ↓
ABSTAIN when evidence is insufficient
```

Later BUILD-8 proves whether any BUILD-4 feature adds unseen-data value. Later BUILD-11 packages proof-bounded evidence for D6. D6 remains sole final WAIT/WATCH/PAPER-CANDIDATE authority.

---

# 1. Preconditions and exact-base law

BUILD-4 may start only after BUILD-0/1/2/3 are GREEN / LOCKED / INTEGRATED and BUILD-3 has exact post-merge CI proof.

Current verified planning base for this plan:

`m4-d6-orchestration-redesign@29e9e126401a512c13743871206c2ee6b22772b3`

Before each implementation milestone:

1. fetch origin;
2. verify planning head;
3. if planning head moved, stop and review impact;
4. never silently rebase or transplant onto a different base;
5. preserve BUILD-0/1/2/3 locked contracts unless a new approved milestone explicitly changes them.

---

# 2. Absolute authority and safety law

Immutable:

```text
research_only = true
trade_allowed = false
order_routing_enabled = false
live_trading_blocked = true
human_approval_required = true
```

BUILD-4:

```text
may_execute = false
may_set_final_band = false
```

BUILD-4 may not:

- place an order;
- call a broker;
- create a live position;
- set final WAIT/WATCH/PAPER-CANDIDATE;
- bypass D1/D2;
- override BUILD-2 market identity;
- rewrite BUILD-3 session facts;
- bypass or replace `FINAL_CONFLUENCE_ARBITER`;
- self-activate a feed or threshold merely because code exists.

---

# 3. Permanent epistemic laws

Preserve:

```text
missing != neutral
unknown != false
unavailable != safe
synthetic != real
error != zero
no_signal != unavailable
no_output != neutral
NOT_APPLICABLE != AVAILABLE
weak evidence != contradictory evidence
conflict != neutral
future != causal
unfinished != closed
stale != fresh
correlated evidence != independent evidence
source-derived != directly observed
model-inferred != observed
hypothesis != fact
open interest != directional ownership
option concentration != support/resistance fact
gamma concentration != dealer positioning
max pain != causal magnet
close != settlement
raw contract != continuous series
current data != historical PIT data
```

Missing numeric data must never become zero. Observed zero must remain distinguishable from unavailable.

---

# 4. Source and requirement traceability

BUILD-4 must be traced against the current BUILD-0 source ledger before coding.

At minimum, reconcile:

- canonical ORB stage-by-stage plan;
- stock/commodity scope hardening;
- canonical future plan;
- ORB simple/required/research/timing/context/strategy plans;
- external review briefs;
- M4 scenario/failure/counterfactual design;
- M4 Hypothesis Box reference;
- M4 Hypothesis Box v2 implementation plan;
- M4 cognitive architecture reference;
- current D1/config truth;
- Decision Spine authority registry.

Binding accumulated requirements owned or co-owned by B4 include:

- R4 multidimensional evidence;
- R9 calculate once/reuse;
- R10 raw facts first;
- R13 provenance;
- R14 PIT;
- R16 missing != neutral;
- R17 explicit availability;
- R18 identity/hash;
- R19 deterministic replay;
- R20 correlation/independent evidence;
- R22 raw→derived→interpretation one-way flow;
- R24 no authority creep;
- R25 rich context;
- R27 gap/open location;
- R28 CPR;
- R29 daily/weekly/banded VWAP;
- R30 Bollinger;
- R31 ATR via canonical calculation owner;
- R32 volume/RVOL;
- R33 candle patterns;
- R34 levels;
- R35 structure;
- R36 liquidity/sweep/trap;
- R37 benchmark;
- R38 sector;
- R39 relative strength;
- R40 events;
- R41 derivatives/OI;
- R42 expiry;
- R43 roll/settlement;
- all cross-cutting PIT/determinism/missingness/authority requirements.

Second-audit bindings that must be explicit:

- `D003` legacy Z1–Z5 = compatibility/research view only;
- `D004` PDC_TOUCHED != PDC_CLOSED_BEYOND;
- `D010` `OrbHypothesisReceiptV1` must preserve expected sequence, failure sequence, anti-thesis, critical missing evidence, expiry and regime assumptions;
- source-readiness semantics remain explicit and provenance-backed.

---

# 5. Canonical ownership map

BUILD-4 must consume canonical owners rather than recalculate their facts.

## BUILD-1 owns

- candidate identity;
- selector/provenance;
- candidate-universe semantics;
- reference-price identity at intake.

## BUILD-2 owns

- exchange/segment/instrument/contract identity;
- expiry identity;
- multiplier/lot/tick/precision;
- timezone/session/calendar;
- settlement semantics;
- raw vs continuous contract basis.

BUILD-4 must not infer expiry from weekday, symbol text, or modern conventions.

## BUILD-3 owns

- previous completed exchange-session identity;
- trusted/degraded/incomplete session reconstruction;
- prior-session OHLC/volume availability;
- close vs settlement distinction;
- D-1 immutable field provenance;
- precompute-before-split seam.

BUILD-4 must not recreate previous-session truth with `resample("D")`.

## M3.1 owns

Where already canonical:

- trend/price/volatility primitives;
- ATR;
- Bollinger/indicator calculations;
- market structure;
- canonical levels;
- canonical price/indicator evidence.

BUILD-4 interprets their receipts.

## M3.2 owns

Generic context-source and canonical context facts such as:

- session context;
- index context;
- sector context;
- relative strength;
- market regime;
- explicit source availability/freshness/PIT envelope.

BUILD-4 composes these into an ORB-specific world; it must not rewrite generic M3.2.

## M3.3 owns

- real memory;
- 9-candle memory;
- pattern memory;
- analog retrieval;
- independent-episode counts;
- reliability/outcome memory where valid.

BUILD-4 may use these as bounded evidence/challengers. It must not fabricate memory.

---

# 6. Legacy migration map

Initial BUILD-4 is additive and shadow-first.

`orb/context.py`
- legacy compatibility;
- contains duplicate gap/CPR/ATR and unsafe generic daily resample semantics;
- do not use `resample("D")` as canonical generic session truth;
- wrap/shadow, then retire duplicates only after parity.

`behavior/context_engines.py`
- contains useful historical semantics but also scores/block flags and duplicate calculations;
- keep compatibility-only initially;
- shadow against canonical receipts;
- do not promote `context_quality_score`, `relative_strength_score`, `gap_fill_probability`, or local blocking semantics into canonical truth without proof/ownership review.

`behavior/execution_event_oi_risk.py`
- contains spread/slippage/fill proxies, event scoring, gamma-wall/max-pain/pinning interpretations;
- keep compatibility-only initially;
- raw supplied facts may be wrapped if provenance is valid;
- proxy/default-derived values are not canonical derivatives facts;
- manual gamma wall/max pain cannot masquerade as source-proven canonical data.

Migration law:

`STRANGLE → WRAP → PROVE → SHADOW → MIGRATE`

No delete/rewrite of working legacy ORB during initial BUILD-4.

---

# 7. BUILD-4 total target architecture

```text
BUILD-1 candidate identity
        +
BUILD-2 market/contract/session identity
        +
BUILD-3 D-1 facts
        +
D2 closed-candle snapshot
        +
M3.1 canonical price/structure/level/indicator receipts
        +
M3.2 canonical context receipts
        +
M3.3 canonical memory receipts
        +
typed event/derivatives sources where causally valid
        ↓
B4-A SOURCE + PROVENANCE FABRIC
        ↓
B4-B FUTURES POSITIONING FACTS
        ↓
B4-C OPTION-CHAIN FACTS
        ↓
B4-D VOLATILITY + GREEKS
        ↓
B4-E ADVANCED DERIVATIVES INFERENCE
        ↓
B4-F ORB CONTEXT WORLD + MARKET DELIBERATION
        ↓
BUILD-5/6/7/9/10/11/12 consumers
        ↓
BUILD-8 incremental proof
        ↓
BUILD-11 evidence handoff
        ↓
D6 sole final arbitration
```

BUILD-4 is not only a derivatives project. It must also integrate non-derivatives context required by the canonical plan: patterns, levels, location, VWAP families, BB/ATR/volume, benchmark, sector, relative strength, events, expiry/roll, quality, contradictions and missingness.

---

# 8. Epistemic type system

Reuse canonical repository vocabulary where available. Preserve the semantic layers:

1. OBSERVED MARKET FACT
2. SOURCE-DERIVED ANALYTIC
3. LOCAL-DERIVED ANALYTIC
4. INFERRED STATE
5. HYPOTHESIS
6. PREDICTIVE OUTPUT

Examples:

OBSERVED:
- futures price;
- option premium/bid/ask;
- volume;
- open interest;
- strike/expiry;
- source event record.

SOURCE-DERIVED:
- provider/exchange IV;
- provider/exchange Greeks;
- official volatility index.

LOCAL-DERIVED:
- change in OI;
- basis;
- PCR;
- local IV/Greeks;
- skew;
- term structure.

INFERRED:
- fresh-long-participation candidate;
- short-covering candidate;
- OI concentration regime;
- gamma concentration region.

HYPOTHESIS:
- dealer long/short gamma;
- expiry pinning;
- gamma squeeze;
- volatility expansion continuation;
- roll distortion;
- event-driven dislocation.

No layer may silently promote itself upward.

---

# 9. Contract family

Evaluate names against repository conventions before coding, but preserve the invariants.

Candidate contracts:

- `OrbDerivativesSourceContractV1`
- `OrbDerivativesSourceReceiptV1`
- `OrbFuturesPositioningSnapshotV1`
- `OrbOptionContractFactV1`
- `OrbOptionChainSnapshotV1`
- `OrbVolatilitySurfaceV1`
- `OrbGreeksPointV1`
- `OrbAdvancedDerivativesInferenceV1`
- `OrbDerivativesContextV1`
- `OrbEventContextV1` or reuse an existing canonical event receipt if owner exists
- `OrbPatternContextV1` only if canonical pattern receipts need an ORB composition view
- `OrbContextWorldV1`
- `OrbHypothesisReceiptV1`

Do not create wrapper classes without a unique invariant.

Every contract must answer:

- producer;
- consumers;
- identity;
- event/source/observed/published/available/decision timestamps;
- source IDs/hashes;
- calculation/model version;
- units;
- availability/freshness/quality;
- dependencies;
- epistemic level;
- deterministic hash;
- authority = none.

---

# 10. B4-D0 — Discovery / source / owner freeze

Purpose: no runtime code. Freeze repository truth and eliminate ownership ambiguity.

Required work:

- verify exact planning SHA;
- enumerate BUILD-0 source ledger;
- trace B4 requirements and second-audit deltas;
- map current legacy/canonical producers;
- map M3/B1/B2/B3 ownership;
- inventory derivatives/event/source gaps;
- inventory all pattern families required by B4;
- identify duplicated calculations;
- freeze target package and dependency direction;
- identify real-source vs fixture-only vs unavailable states;
- produce implementation/test matrix.

Exit:

- no unresolved owner ambiguity for a calculation being implemented in B4-A..F;
- unresolved real feed questions remain explicit and do not block pure contract/calculator code unless the code would falsely imply source availability.

---

# 11. B4-A — Source contracts, provenance, PIT readiness

## 11.1 Scope

Create the source/provenance fabric for external or versioned context.

It must support separate source modes such as:

- `REALTIME_SNAPSHOT_ONLY`
- `INTRADAY_HISTORICAL_PIT`
- `EOD_ONLY`
- `VERSIONED_HISTORICAL_FILE`
- `RECONSTRUCTED`
- `UNAVAILABLE`

Map to existing `OrbSourceReadinessV1` / repository vocabulary where possible. Do not create a conflicting global state enum.

## 11.2 Required source categories

Not derivatives only. Audit/source-contract needs include:

- futures/OI;
- option chain;
- official volatility index;
- participant-wise OI where justified;
- event/result/macro calendars;
- corporate action/dividend source where needed;
- benchmark/sector/market feeds when existing M3.2 source does not already own them;
- commodity-specific event/context feeds only where applicable;
- expiry/roll/settlement sources through BUILD-2/3 identity rather than local guesses.

## 11.3 Common source receipt fields

As applicable:

```text
source_system
source_provider
source_artifact_id
source_schema_version
source_version
registered_locator
request_parameters
instrument_identity
contract_identity
exchange
segment
underlying_identity
expiry
strike
option_type
event_time
source_as_of
observed_at
published_at
available_at
received_at
decision_as_of
knowledge_cutoff
timezone
currency
units
raw_content_hash
normalized_snapshot_hash
revision_id
supersedes
availability
freshness
quality
field_availability
historical_coverage_mode
```

No random UUID where deterministic identity is possible.

## 11.4 PIT law

Every consumed fact must satisfy:

`available_at <= decision_as_of`

and every dependency must be causal too.

Reject:

- EOD report used in morning context;
- later revision used AS_KNOWN_THEN;
- current option chain used to reconstruct historical 09:30 state;
- future event result;
- future expiry/contract membership;
- modern constituent/master data substituted into history.

## 11.5 Revision law

Old snapshots remain immutable. Corrections create new version/hash with supersession lineage.

Replay default: `AS_KNOWN_THEN`.

If `AS_REVISED_NOW` exists, it must be explicit and never confused with historical decision replay.

## 11.6 CODE_READY != SOURCE_READY

A green contract/calculator does not activate a feed.

Real-source activation requires separate evidence for:

- owner/source legitimacy;
- field semantics;
- publication timing;
- historical depth;
- PIT reconstructability;
- revision policy;
- stable schema/version;
- authentication/licensing/usage constraints;
- reproducible fixture capture.

`DERIVATIVES_OI_CONTEXT` remains `NEEDS_EXTERNAL_FEED` until those conditions are proven.

---

# 12. B4-B — Futures positioning facts

Inputs may include:

- futures price;
- futures volume;
- futures OI;
- previous comparable OI;
- spot/reference price;
- exact front/next contract identity;
- multiplier;
- expiry;
- settlement where applicable;
- dividend/carry context only when causally available.

Derived facts may include:

- OI change absolute/%;
- raw basis/basis bps;
- front/next OI relationship;
- registered rollover metric;
- exact-contract price/OI joint classification.

Rules:

- OI comparisons require comparable contract semantics;
- never compare yesterday front-month OI with today next-month OI and call it directional OI growth;
- raw contract and continuous series remain separate;
- observed OI zero != unavailable;
- price↑/OI↑ may yield `FRESH_LONG_PARTICIPATION_CANDIDATE`, not factual ownership;
- price↑/OI↓ may yield `SHORT_COVERING_CANDIDATE`, not certainty;
- basis annualization/carry requires exact inputs; otherwise unavailable;
- rollover formula/version must be explicit;
- expiry-week/roll context must use BUILD-2 identity and not weekday memory.

Historical strategy-memo thresholds such as basis/OI tilts remain research candidates until BUILD-7/8 proof. They must not be silently promoted as canonical gates during BUILD-4.

---

# 13. B4-C — Option-chain facts

Canonical option fact identity:

- underlying;
- expiry;
- strike;
- CALL/PUT;
- contract identity;
- multiplier;
- bid/ask;
- last price;
- volume;
- OI;
- previous comparable OI;
- source-provided IV when present;
- underlying reference;
- snapshot timestamp;
- source receipt/hash.

Validate:

- same underlying/expiry/strike/type/snapshot/units;
- duplicates;
- contradictory duplicates;
- partial expiry;
- missing strikes;
- stale/no-trade LTP;
- crossed/invalid quotes;
- missing vs observed zero OI/volume;
- wrong multiplier;
- wrong expiry.

## PCR

Never one ambiguous `pcr` field. Distinguish at least:

- OI_PCR;
- CHANGE_OI_PCR;
- VOLUME_PCR.

Each carries expiry scope, strike universe, timestamp, formula/version, missingness and denominator policy.

## Concentration

Descriptive canonical facts may include:

- largest call/put OI strikes;
- largest ΔOI strikes;
- percentage concentration by strike region;
- distance from underlying.

Output `POSITIONING_CONCENTRATION`, not automatic support/resistance.

## Historical ORB rules

DERIV-03/04 etc from older strategy specifications are retained as research candidates/compatibility evidence, not activated gating rules by BUILD-4 alone.

---

# 14. B4-D — IV, volatility surface and Greeks

## 14.1 Source vs local IV

Keep separate:

- `SOURCE_PROVIDED_IV`;
- `LOCAL_MODEL_IV`.

Never silently substitute.

## 14.2 Pricing model identity

Before local IV/Greeks determine:

- option product semantics;
- underlying type;
- spot/futures basis;
- exercise style;
- settlement;
- time to expiry;
- carry/dividend/rate inputs;
- currency.

Do not blindly apply one model to all products.

Record:

```text
model_id
model_version
solver_version
input_fact_ids
solver_tolerance
iterations
convergence_state
```

Invalid/no-arbitrage-domain quotes => explicit invalid/unavailable, never forced convergence.

## 14.3 Bid/mid/ask volatility

Where reliable quotes exist, preserve bid/mid/ask IV separately. Wide spreads degrade precision/quality.

## 14.4 IV rank != IV percentile

Each requires explicit lookback, series, sampling frequency, minimum history and PIT cutoff. Missing history => insufficient history.

## 14.5 Skew

No undefined generic `iv_skew`. Prefer versioned definitions such as 25-delta risk reversal/put skew or registered surface slopes only when required interpolation data exists.

## 14.6 Term structure

Compare like-for-like moneyness/delta points. Preserve expiry pair, DTEs and formula identity.

## 14.7 India VIX / official volatility index

Treat as source-derived market-volatility context. Do not count it as independent confirmation from every NIFTY option-derived IV/skew measure; declare common ancestry/correlation.

## 14.8 Greeks

Candidates:

- Delta;
- Gamma;
- Vega;
- Theta;
- Rho.

Each must preserve:

- source-provided vs locally modelled;
- units;
- model/version;
- option contract identity;
- underlying/reference;
- timestamps;
- availability/quality.

No arbitrary clamping of numerical instability. NaN/inf/non-convergence/error remain explicit.

---

# 15. B4-E — Advanced derivatives inference

Candidates:

- absolute gamma concentration;
- gamma concentration levels/walls;
- zero-gamma-style reference where definition is valid;
- signed dealer-GEX hypothesis;
- max-pain reference;
- expected move;
- expiry-pinning hypothesis;
- volatility-regime hypothesis;
- roll-distortion hypothesis;
- price/derivatives disagreement.

## GEX semantic law

Open interest does not identify dealer ownership/sign.

Separate:

`ABSOLUTE_GAMMA_CONCENTRATION`

from:

`SIGNED_DEALER_GEX_HYPOTHESIS`

Signed dealer GEX requires explicit sign model, version and assumptions. Without one, signed dealer GEX is unavailable/hypothesis-only.

## Gamma wall

Canonical fact should first be a versioned gamma-concentration level. Support/resistance/pinning interpretation is a hypothesis.

## Max pain

May be deterministically calculated from exact strike/OI snapshot with explicit payout/tie rules. Name it `MAX_PAIN_REFERENCE`, never `MAGNET_FACT`.

Historical memo rule DERIV-06 remains research evidence; non-expiry “magnet” claims are not canonical truth.

## Expected move

Method identity required, e.g. ATM straddle, IV-based, source-provided, registered-other. Do not merge methods. Expected-move relationship is context evidence, not automatic target invalidation.

## GEX/charm/participant positioning

Older strategy sources explicitly classify GEX/charm/participant-flow as experimental/ALERT_ONLY until the project’s own OOS evidence proves value. BUILD-4 must preserve that status.

---

# 16. B4-F — Canonical ORB context world

`OrbContextWorldV1` is an ORB-specific composition layer. It consumes, does not duplicate:

- BUILD-1 candidate provenance;
- BUILD-2 identity/session/contract profile;
- BUILD-3 prior-session snapshot;
- D2 snapshot;
- M3.1 price/structure/levels/indicators;
- M3.2 context;
- M3.3 memory where relevant;
- validated event/derivatives context.

Required world axes include as applicable:

- location;
- local/higher-timeframe structure;
- trend horizons;
- momentum;
- volatility/compression/expansion;
- participation/volume/RVOL;
- PDH/PDL/PDC/settlement;
- CPR/location;
- session/daily/weekly VWAP and bands;
- BB state;
- canonical levels/liquidity/sweep/trap;
- benchmark/index;
- sector;
- relative strength;
- event state;
- derivatives/OI;
- expiry/roll;
- data quality/freshness/provenance;
- memory/OOD where relevant.

Instrument applicability is explicit:

- stock-only feature on commodity => NOT_APPLICABLE;
- non-F&O stock-specific options context => NOT_APPLICABLE;
- benchmark NIFTY derivatives may be market context but never masquerade as stock-specific derivatives;
- commodity context uses applicable commodity/FX/global source only when valid.

---

# 17. Mandatory pattern migration registry

BUILD-4 must explicitly account for prior completed-session pattern evidence, not just derivatives.

Legacy daily patterns to inventory/migrate with PIT provenance:

- bullish_harami;
- bullish_engulfing;
- piercing_line;
- bullish_belt;
- bullish_kicker;
- morning_star;
- hammer;
- inverted_hammer;
- bearish_harami;
- bearish_engulfing;
- bearish_kicker;
- hanging_man;
- evening_star;
- shooting_star;
- doji.

Also inventory:

- outside_reversal;
- three_inside;
- three_inside_filtered;
- dark_cloud_piercing;
- cdl_multibar_markers;
- sfp_markers;
- N-bar reversals;
- chart/H&S pattern engines.

Historical priority scores are compatibility baselines only, not future weights.

Pattern presence in a library is not enough. ORB must receive a pattern from the correct completed session/timeframe with source/dependency identity.

---

# 18. Canonical location and CPR laws

Preserve raw location facts.

CPR redundancy law:

```text
P = (PDH + PDL + PDC) / 3
BC = (PDH + PDL) / 2
TC = 2P - BC
CPRW = |TC - BC| = (2/3) * |PDC - BC|
```

CPR width and prior-close location share ancestry. Gap/zone/CPR are not independent evidence simply because they are separate columns.

Legacy Z1–Z5 is optional `LegacyOrbZoneViewV1`, a compatibility/research view only.

Use canonical `CPR_TOP=max(BC,TC)` and `CPR_BOTTOM=min(BC,TC)`.

Missing PDH/PDL/CPR => UNKNOWN/UNAVAILABLE zone, never guessed.

PDC semantics must preserve two different facts:

- `PDC_TOUCHED`;
- `PDC_CLOSED_BEYOND`.

They are not interchangeable. Gap-fill interpretation must name which registered definition it uses.

---

# 19. Market deliberation / hypothesis architecture

BUILD-4 reasoning is a bounded deterministic market-deliberation system, not a score voter.

Target stages:

```text
IMMUTABLE EVIDENCE
    ↓
EPISTEMIC GATE
    ↓
WORLD MODEL
    ↓
MARKET QUESTION DETECTOR
    ↓
DYNAMIC EVIDENCE ROUTER
    ↓
DEPENDENCY GRAPH
    ↓
ARGUMENTATION GRAPH
    ↓
COMPOSITIONAL HYPOTHESIS GENERATOR
    ↓
THESIS + ANTI-THESIS
    ↓
TEMPORAL PATH COMPILER
    ↓
MEMORY / VALIDATED REVIEWER CHALLENGERS
    ↓
ADVERSARIAL FALSIFIER
    ↓
SURPRISE / BELIEF UPDATE
    ↓
OOD / UNCERTAINTY / VALUE-OF-INFORMATION
    ↓
HYPOTHESIS RECEIPT
```

No hidden chain-of-thought is stored. Only structured evidence/arguments/expected observations/reason codes.

---

# 20. Market question detector

Do not start with “bullish or bearish?”. Identify the uncertainty being resolved.

Question classes may include:

- BREAKOUT_ATTEMPT;
- BREAKOUT_ACCEPTANCE;
- RETEST;
- LIQUIDITY_SWEEP;
- TREND_PULLBACK;
- STRUCTURAL_REVERSAL;
- RANGE_EDGE;
- COMPRESSION;
- VOLATILITY_EXPANSION;
- GAP;
- EXPIRY;
- EVENT_SHOCK;
- MTF_CONFLICT;
- VALUE_RECLAIM;
- VALUE_REJECTION;
- FAILURE_TRANSITION;
- UNKNOWN_MARKET_QUESTION.

Multiple questions/horizons may coexist.

---

# 21. Dependency graph != argumentation graph

Maintain two graphs.

## Dependency/provenance graph

Answers whether evidence is independent.

Edges include:

- DERIVED_FROM;
- SHARES_INPUT_WITH;
- SAME_SOURCE_FAMILY;
- DUPLICATES;
- CORRELATED_WITH;
- TIMEFRAME_PARENT/CHILD.

## Reasoning/argumentation graph

Answers what argues for/against a hypothesis.

Edges include:

- SUPPORTS;
- ATTACKS;
- INVALIDATES;
- REQUIRES;
- CONDITIONAL_ON;
- FAILURE_PRECURSOR;
- EXPECTED_BEFORE/AFTER;
- TEMPORALLY_PRECEDES/FOLLOWS.

Do not merge these graphs.

Example: Call OI, PCR, max pain and GEX can all descend from the same option chain. They may be useful observations but are not four independent confirmations.

---

# 22. Dynamic evidence routing

Select evidence based on the current market question.

Routing criterion:

“Does this fact help distinguish leading competing hypotheses?”

Not:

“Is this indicator available?”

Preserve useful horizon distinctions without fake independent count.

Examples of high relevance for a breakout-at-resistance question:

- actual structural level;
- closed-bar acceptance/rejection;
- RVOL/volume;
- range re-entry;
- ATR/volatility expansion;
- VWAP/value relationship;
- liquidity sweep/SFP;
- HTF structure;
- sector/index;
- nearby derivatives positioning;
- analogous breakout/failure trajectories.

---

# 23. Hypothesis contract

`OrbHypothesisReceiptV1` must include at least:

```text
hypothesis_id
hypothesis_family
side_or_neutral
market_phase
timeframe_or_horizon
thesis
anti_thesis
required_truths[]
supporting_evidence[]
opposing_evidence[]
critical_missing_evidence[]
evidence_roles[]
dependencies[]
correlation_families[]
expected_sequence[]
failure_sequence[]
invalidation_conditions[]
expiry_condition
regime_assumptions[]
alternative_hypotheses[]
misinterpretation_consequence
availability
state
decision_as_of
d2_snapshot_hash
market_identity_hash
prior_session_hash
context_world_hash
source_snapshot_hashes[]
calculation_versions[]
output_hash
```

No raw probability field unless BUILD-12 later supplies genuine calibration provenance.

---

# 24. Hypothesis ontology and lifecycle

Do not hard-code hundreds of flat names. Compose hypotheses from direction, mechanism, location, horizon and regime.

Candidate mechanisms:

- continuation;
- reversal;
- breakout continuation;
- breakout failure;
- rejection;
- liquidity-sweep reversal;
- mean reversion;
- compression expansion;
- gap continuation/fade;
- trend pullback;
- event dislocation;
- expiry pinning;
- roll distortion;
- no-edge/unknown.

Lifecycle must be deterministic, e.g.:

```text
CANDIDATE → ACTIVE → STRENGTHENED / WEAKENED → INVALIDATED
ACTIVE → RESOLVED_SUCCESS
ACTIVE → RESOLVED_FAILURE
ACTIVE → EXPIRED
```

Store transitions with triggering fact IDs and reason codes.

---

# 25. Temporal path compiler

Every material hypothesis must state observable expectations **before** future bars are seen.

Each expectation needs:

- predicate;
- observation window;
- source facts;
- importance;
- failure consequence.

Example breakout continuation:

- hold/accept above level in next 1–2 closed bars;
- retest does not deeply re-enter range;
- participation does not immediately collapse;
- higher low forms before continuation;
- benchmark/sector do not materially reverse.

Failure hypothesis defines the competing sequence.

No future-data leakage is allowed when defining expectations.

---

# 26. Surprise and belief revision

BUILD-4 should compare pre-registered expectations to later closed-bar evidence and transition hypothesis state explicitly.

Do not represent surprise as only `score -= 0.2`.

Use reasoned transitions such as:

- EXPECTATION_CONFIRMED;
- MINOR_SURPRISE;
- MAJOR_SURPRISE;
- INVALIDATOR_OBSERVED;
- HYPOTHESIS_EXPIRED.

All updates remain deterministic and receipt-backed.

---

# 27. Anti-thesis and adversarial falsifier

Every serious directional thesis requires a serious anti-thesis.

The falsifier must actively search for:

- strongest opposing independent evidence;
- critical missingness;
- stale/degraded facts;
- correlation masquerading as confirmation;
- OOD/regime mismatch;
- event risk;
- side asymmetry;
- sample weakness;
- memory failure trajectory;
- derivatives wall/pinning distortion when source-valid.

Preferred story may not suppress its strongest alternative.

---

# 28. Value-of-information

When leading hypotheses remain unresolved, identify the next observation most useful to distinguish them.

Initial implementation must be deterministic rules, not opaque optimization.

Example output:

```text
most_discriminating_information = ORH_RETEST_ACCEPTANCE
expected_window = next_2_closed_5m_bars
uncertainty_remains_material = true
```

This explains why a state should remain unresolved/observe-more without inventing probability.

---

# 29. OOD and abstention

BUILD-4 must support OOD/novelty/insufficient-evidence states.

OOD may be caused by:

- regime outside supported context;
- source schema/data-quality anomaly;
- sparse historical support;
- missing critical evidence;
- contradictory canonical worlds;
- instrument/context combination outside registered applicability.

OOD may force abstention/NO_EDGE evidence but may not itself mint final WAIT/WATCH bands; D6 owns final output.

---

# 30. Memory and reviewer boundaries

M3.3 memory may provide:

- analogous states;
- pattern/trajectory evidence;
- failure trajectories;
- independent episode counts;
- OOD/regime mismatch.

Memory must report raw-neighbor count separately from independent-episode count.

Validated Kronos or other sequence reviewer may challenge/support a temporal hypothesis only when source/validation state is real. Mock/fallback output has zero canonical influence.

Gemini/Grok/Twin/advisor outputs remain advisory/review-only and cannot create canonical facts or authority.

---

# 31. Event context

R40 requires event context, so BUILD-4 plan must not focus only on OI/Greeks.

Event source contracts should support as applicable:

- earnings/results;
- RBI/MPC/macroeconomic calendar;
- budget/market holiday/special session;
- corporate action/ex-dividend;
- commodity-specific inventory/supply/macro/FX events where valid;
- publication/available-at timestamps;
- revisions/cancellations;
- instrument applicability.

Historical strategy thresholds such as pre/post-event buffers remain research candidates unless BUILD-7/8 proves them.

Missing event source is UNAVAILABLE, not “no event”.

---

# 32. Instrument-specific applicability

## NSE equity

Potentially applicable:

- CPR/PDH/PDL/PDC;
- NIFTY/index;
- sector/relative strength;
- corporate actions;
- stock/index derivatives where exact F&O identity exists;
- results/events.

## Non-F&O equity

Stock-specific option chain/Greeks/OI = NOT_APPLICABLE.

Benchmark index derivatives can remain market-context evidence with explicit role.

## Index/derivative instrument

Use exact BUILD-2 derivative identity/expiry/contract context.

## Commodity future

- contract/roll/settlement/OI can apply;
- equity sector/corporate-action logic = NOT_APPLICABLE;
- options/Greeks only when exact commodity-option identity/source exists;
- benchmark/FX/global/event context only through registered PIT-safe source.

No silent substitution between these categories.

---

# 33. Correlation and ancestry law

Each derived fact declares dependencies/source hashes/correlation family.

At minimum explicitly model:

- CPR width and prior-close location ancestry;
- EMA/MACD/trend shared price ancestry;
- option OI/PCR/max pain/GEX shared option-chain ancestry;
- IV/skew/Greeks shared quote/volatility ancestry;
- India VIX and NIFTY option-volatility ancestry where appropriate;
- memory outputs sharing the same historical episode pool.

Removing a raw source must invalidate descendants correctly.

No descendant count increases independent evidence count by default.

---

# 34. No generic context score / no uncertified probability

Forbidden canonical outputs:

```text
context_score = weighted_sum(...)
5 bullish votes = BUY
73% breakout probability
```

unless a separately calibrated/proven later model owns such a probability.

Prefer categorical evidence states such as:

- SUPPORTED;
- WEAKLY_SUPPORTED;
- CONTRADICTED;
- CONFLICTING;
- UNKNOWN;
- INSUFFICIENT_EVIDENCE.

Use repository vocabulary if already canonical.

---

# 35. BUILD-8 proof boundary

BUILD-4 does not prove feature value.

BUILD-8 must later compare, with chronological train/walk-forward/untouched holdout and multiple-testing controls:

- ORB baseline vs + futures OI;
- vs + option OI;
- vs + IV;
- vs + Greeks;
- vs + advanced GEX/gamma inference;
- vs + event context;
- vs full derivatives family;
- family-level ablations and correlated-source reductions.

Possible proof states:

- INFORMATIONAL_UNPROVEN;
- PROVEN_INCREMENTAL;
- NO_INCREMENTAL_VALUE;
- HARMFUL;
- SOURCE_INSUFFICIENT;
- NOT_APPLICABLE.

Map to repository vocabulary where possible.

BUILD-4 itself cannot mark `PROVEN_INCREMENTAL`.

---

# 36. Historical strategy rules are research candidates, not automatic gates

Older ORB strategy sources contain candidate thresholds for:

- VIX regimes;
- futures buildup;
- basis;
- OI walls;
- PCR;
- expected move;
- max pain;
- participant OI;
- expiry protocols;
- RVOL;
- event buffers.

BUILD-4 must preserve these as research provenance where still relevant, but it must not hard-code folklore thresholds as canonical authority.

Examples that must remain research candidates until BUILD-7/8:

- PCR extreme cutoffs;
- basis threshold directional meaning;
- IV-rank thresholds;
- GEX sign interpretations;
- max-pain pin distance;
- OI % threshold strength;
- VIX gating thresholds.

---

# 37. Determinism and hashing

Same logical input + same policy/model/source versions => same output.

Canonical identity must not depend on:

- dict/set order;
- wall-clock execution time;
- random UUID;
- cache state;
- file-load order;
- uncontrolled floating binary representation.

Define canonical numeric precision/quantization where required.

Operational telemetry such as latency/cache hits must not enter evidence identity hashes.

---

# 38. Numerical robustness

For IV/Greeks and derived analytics:

- bound solver iterations/tolerance;
- detect non-convergence;
- detect invalid domains;
- reject NaN/inf;
- handle zero/negative time-to-expiry explicitly;
- validate quote/model compatibility;
- preserve units;
- never `except: return 0.0`.

Tests should compare analytic Greeks to finite differences where appropriate.

---

# 39. Performance and cache law

Target roughly O(number of contracts) or O(n log n) per option-chain snapshot.

Avoid:

- recalculating IV/Greeks per hypothesis;
- reparsing/re-hashing same payload;
- repeated chain reconstruction per ORB parameter combination;
- cross-symbol/session/expiry cache leakage;
- unbounded hypothesis/scenario recursion.

Cache by strong identities such as:

- source snapshot hash;
- underlying;
- contract/expiry;
- model/calculation version;
- decision_as_of.

Bound:

- hypothesis count;
- scenario count;
- receipt size;
- memory/candidate retrieval.

---

# 40. Observability

Track without affecting deterministic hashes:

- source snapshot count;
- available/degraded/stale/unavailable/error counts;
- contracts/expiries/strikes processed;
- IV solver failure count;
- Greek failure count;
- source conflict/not-comparable count;
- cache hit/miss;
- processing latency;
- evidence count by family;
- hypothesis count/state transitions;
- critical missing evidence count;
- OOD/abstention count;
- expected/failure path reason codes.

No hidden thought traces.

---

# 41. Test matrix — B4-A source contracts

Must include:

- valid real-source receipt;
- versioned fixture receipt;
- future `available_at` rejected;
- naive timestamp rejected;
- wrong instrument/contract/expiry/timezone;
- source hash/schema mismatch;
- stale/partial/missing source;
- revision lineage;
- duplicate/contradictory snapshot;
- historical PIT unavailable;
- live-only source;
- EOD-only source;
- deterministic replay;
- synthetic labelled real rejected;
- source readiness not auto-promoted by code.

---

# 42. Test matrix — B4-B futures

Include:

- normal/zero/missing OI;
- OI increase/decrease;
- zero denominator;
- all four price/OI joint cases;
- wrong contract comparison;
- front/next collision;
- roll day;
- missing spot;
- basis units;
- settlement vs live price;
- expiry boundary;
- future data exclusion;
- raw vs continuous isolation;
- commodity/equity applicability.

---

# 43. Test matrix — B4-C option chain

Include:

- single/multiple expiry;
- mixed underlying rejected;
- duplicate/contradictory strike;
- call/put identity;
- partial chain;
- missing/zero OI and volume;
- stale quote/LTP;
- bid > ask invalid;
- zero bid;
- wrong multiplier/expiry;
- deterministic ordering;
- PCR definitions;
- concentration tie policy;
- current chain cannot impersonate historical PIT chain.

---

# 44. Test matrix — B4-D IV/Greeks

Include:

- source/local IV separation;
- no-arbitrage violation;
- non-convergence;
- near-expiry/expired;
- ATM/ITM/OTM/deep cases;
- low/high IV;
- missing rate/carry/dividend;
- wrong model/product;
- Delta sign;
- Gamma behavior;
- Vega/Theta units;
- analytic vs finite-difference;
- IV rank/percentile;
- insufficient history;
- skew/term structure;
- comparable vs non-comparable source conflict.

---

# 45. Test matrix — B4-E advanced inference

Include:

- absolute gamma concentration;
- missing multiplier/gamma;
- signed GEX unavailable without sign model;
- signed GEX with explicit model/version;
- sign-model version changes output hash;
- gamma concentration deterministic;
- max-pain deterministic/tie policy;
- expected-move method identity;
- pinning remains hypothesis;
- dealer positioning remains hypothesis;
- no “magnet” fact;
- roll-distortion hypothesis;
- GEX/charm remain ALERT_ONLY/unproven until BUILD-8.

---

# 46. Test matrix — B4-F context/hypothesis

Include:

- world-model composition;
- multiple competing hypotheses;
- thesis + anti-thesis;
- support/opposition/unknown/conflict;
- critical missing evidence;
- expected/failure sequence;
- invalidation;
- expiry;
- alternative hypothesis;
- hypothesis lifecycle transition;
- surprise update;
- value-of-information;
- OOD/abstention;
- same-family correlation/no double-count;
- bounded hypothesis count;
- deterministic input-order permutation;
- D2 mismatch;
- BUILD-2 identity mismatch;
- BUILD-3 prior-session mismatch;
- no generic context score;
- no uncalibrated probability;
- zero authority.

---

# 47. Pattern/location tests

Must also include non-derivatives B4 obligations:

- completed-session pattern provenance;
- mandatory legacy pattern registry accounting;
- pattern unavailable vs false;
- timeframe/session identity;
- canonical level ownership;
- stale/future pivot rejected;
- CPR ancestry/correlation;
- legacy Z1–Z5 compatibility only;
- missing CPR/PDH/PDL => unknown/unavailable;
- PDC touch distinct from close-beyond;
- gap-fill rule identifies which fact semantics it uses;
- stock-only context becomes NOT_APPLICABLE for commodities.

---

# 48. PIT / anti-leak adversarial tests

Include:

- morning cannot see EOD OI;
- current option chain cannot reconstruct historical morning;
- future revision invisible AS_KNOWN_THEN;
- future event result invisible;
- future IV surface invisible;
- later expiry/contract membership invisible;
- final-day chain cannot reconstruct 09:30;
- modern contract master cannot rewrite historical universe;
- future corporate-action mapping excluded;
- future roll outcome excluded;
- holdout rows only use causal source snapshots;
- no incomplete candle authority;
- D-1 precompute-before-split remains intact.

---

# 49. Authority attack tests

Attempt hostile construction:

```text
may_execute=true
may_set_final_band=true
trade_allowed=true
order_routing_enabled=true
live_trading_blocked=false
```

All must be impossible/rejected.

BUILD-4 package must not own broker/order APIs.

Authority registry must remain valid and `FINAL_CONFLUENCE_ARBITER` the sole finalizer.

---

# 50. Regression campaign

At each milestone, run focused tests plus surrounding regressions appropriate to touched scope.

B4-LOCK must include at minimum:

- BUILD-4 focused suite;
- BUILD-4 PIT/adversarial suite;
- BUILD-4 hypothesis/ancestry suite;
- BUILD-3 regression;
- BUILD-2 regression;
- BUILD-1 regression;
- BUILD-0 `--require-lock`;
- M3.1/M3.2/M3.3 affected canonical suites;
- Decision Spine authority/safety;
- legacy ORB regression;
- full API regression;
- deterministic replay;
- performance benchmarks.

No test may be weakened to regain green.

---

# 51. CI design

Dedicated workflow after implementation approval, e.g.:

`ORB BUILD-4 Context and Derivatives Intelligence`

Require exact SHA checkout and full history:

```yaml
ref: ${{ github.sha }}
fetch-depth: 0
```

Deterministic normal CI must use pinned/versioned fixtures, not live NSE/MCX calls.

Real-source smoke tests belong in a separately controlled integration lane and must not make deterministic CI depend on external web availability.

CI stages:

- compile/import;
- B4-A source tests;
- B4-B futures;
- B4-C option chain;
- B4-D IV/Greeks;
- B4-E advanced;
- B4-F world/hypothesis;
- PIT/correlation/authority/performance;
- BUILD-3/2/1/0 regressions;
- M3 context/price/memory affected suites;
- legacy ORB;
- full API.

---

# 52. Source fixture law

Every real-source fixture must preserve, when available:

- source owner;
- artifact/API identity;
- capture time;
- publication/available time;
- raw hash;
- schema/version;
- provenance;
- usage/licence note;
- instrument applicability.

Synthetic adversarial fixtures must be labelled `SYNTHETIC` and must never masquerade as real exchange data.

---

# 53. Package layout candidate

After final owner audit, prefer a bounded package such as:

```text
apps/api/app/orb/context_intelligence/
    __init__.py
    contracts.py
    sources.py
    futures.py
    option_chain.py
    volatility.py
    advanced.py
    world.py
    hypotheses.py
```

Provider-specific adapters should not exist until a provider/source is actually approved. Avoid circular dependencies and meaningless wrapper modules.

Dependency direction:

```text
B4 consumes B1/B2/B3/M3
B1/B2/B3/M3 never depend on B4
```

---

# 54. Milestone sequence and approval gates

## B4-D0
Discovery / source / canonical-owner freeze. No runtime code.

## B4-A
Source contracts + PIT/readiness + versioned fixtures.

## B4-B
Futures positioning: OI/ΔOI/basis/roll-safe facts.

## B4-C
Option chain: strike/expiry/OI/PCR/concentration.

## B4-D
IV / volatility surface / Greeks / skew / term structure.

## B4-E
Advanced derivatives inference: absolute gamma concentration, signed-GEX hypothesis boundary, max pain, expected move, pinning/roll hypotheses.

## B4-F
Unified ORB context world + market-question routing + competing hypotheses + temporal expectations + anti-thesis + OOD/VOI/lifecycle.

## B4-LOCK
Adversarial/replay/performance/regression/CI lock.

Each milestone must state:

- exact base SHA;
- exact scope/files;
- intent;
- contracts;
- source dependencies;
- epistemic level;
- missingness/PIT law;
- tests;
- performance;
- rollback;
- definition of done;
- what stays intentionally unavailable/unactivated.

Separate approval remains required for commit/push/PR/merge/dependencies/credentials/real-source activation according to project process.

---

# 55. Rollback / shadow migration

Initial BUILD-4 must be shadow/additive.

No current ORB decision behavior switch merely because a B4 component becomes code-green.

Rollback at component level must be possible by disabling/removing the B4 composer/adapters while leaving locked upstream facts untouched.

Legacy behavior remains available until parity/proof/migration criteria are met.

---

# 56. Two different GREEN states

Never conflate:

`CODE GREEN`

with:

`REAL SOURCE ACTIVE`

Example:

```text
Greek calculator: CODE GREEN
historical PIT option-chain feed: UNAVAILABLE
```

Then historical Greek evidence remains unavailable for BUILD-8 proof.

Real-source activation is its own reviewed milestone.

---

# 57. BUILD-4 CODE GREEN gate

BUILD-4 may be called CODE GREEN only when:

- B4 requirements traced;
- calculation/source owners resolved;
- contracts deterministic;
- source readiness honest;
- PIT/revision checks pass;
- missingness explicit;
- BUILD-2 identity reused;
- BUILD-3 prior-session facts reused;
- M3 calculations not duplicated;
- event context accounted for;
- benchmark/sector/RS accounted for;
- mandatory pattern registry accounted for;
- futures tests green;
- option-chain tests green;
- IV/Greeks tests green;
- advanced inference tests green;
- world/hypothesis tests green;
- thesis/anti-thesis/expected/failure/invalidation present;
- OOD/VOI/lifecycle present;
- correlation ancestry works;
- no uncalibrated probability;
- no generic context score;
- no authority creep;
- B3/B2/B1 regressions green;
- B0 lock green;
- affected M3 suites green;
- Decision Spine authority green;
- legacy ORB green;
- full API green;
- exact-head BUILD-4 CI green.

---

# 58. Real-source activation gate

A real derivatives/event source may become `AVAILABLE_REAL_PIT` only after:

- real source verified;
- ownership/licensing/usage acceptable;
- schema/version pinned;
- publication/available timing known;
- revisions understood;
- historical coverage understood;
- PIT semantics proven;
- deterministic fixture captured;
- exact identity mapping to BUILD-2 proven;
- replay reproducible;
- source-specific freshness policy frozen;
- source conflict/comparability rules tested.

Until then, keep the source in the appropriate NEEDS_FILE / NEEDS_EXTERNAL_FEED / UNAVAILABLE state.

---

# 59. B4-LOCK completion receipt

Final BUILD-4 lock report must state:

```text
STATUS
EXACT BASE SHA
EXACT BUILD-4 SHA
FILES CHANGED
REQUIREMENT COVERAGE
SOURCE READINESS TABLE
CODE_READY vs SOURCE_READY
B4-A RESULT
B4-B RESULT
B4-C RESULT
B4-D RESULT
B4-E RESULT
B4-F RESULT
PATTERN/LOCATION RESULT
PIT/ANTI-LEAK RESULT
DEPENDENCY/CORRELATION RESULT
HYPOTHESIS RESULT
OOD/VOI/LIFECYCLE RESULT
DETERMINISM RESULT
PERFORMANCE RESULT
B3 REGRESSION
B2 REGRESSION
B1 REGRESSION
B0 LOCK
M3 REGRESSIONS
AUTHORITY
LEGACY ORB
FULL API
CI RUN ID
SOURCE LEDGER CHANGED? MUST BE EXPLAINED
MANIFEST HASH CHANGED? MUST BE EXPLAINED
TRADING AUTHORITY CHANGED? MUST BE NO
REAL SOURCE ACTIVATED? EXPLICIT YES/NO PER SOURCE
WEAKEST LINK
UNRESOLVED QUESTIONS
NEXT GATE
```

No “GREEN” claim without observation.

---

# 60. Stop conditions

Stop and seek explicit review if:

- planning base moves materially;
- source-ledger drift occurs;
- B4 requires weakening BUILD-0/1/2/3 invariants;
- canonical owner conflict is unresolved;
- BUILD-4 would need to invent missing identity/source semantics;
- a real source lacks PIT/publication semantics but would be used as historical evidence;
- a dependency is required unexpectedly;
- authority/final-band semantics would change;
- regression changes cannot be explained;
- source terms/licensing prohibit intended use;
- scope expands into BUILD-5/6/7/8/9/10/11/12/13 execution work;
- a threshold needs proof rather than context representation.

---

# 61. Explicit out-of-scope boundaries

BUILD-4 does not implement:

- BUILD-5 OR duration/timeframe optimization;
- BUILD-6 signal state machine ownership;
- BUILD-7 final threshold/parameter research;
- BUILD-8 proof/promotion;
- BUILD-9 analog research ownership;
- BUILD-10 playbook compiler;
- BUILD-11 D6 handoff authority;
- BUILD-12 ML probability;
- BUILD-13 outcome learning/policy mutation;
- broker/live execution.

BUILD-4 may expose facts/hypotheses needed by those later stages but may not absorb their authority.

---

# 62. Re-audit additions that were missing from the earlier conversational BUILD-4 outline

The earlier B4 outline correctly emphasized OI/IV/Greeks/GEX, source contracts, competing hypotheses and BUILD-8 proof. The repository re-audit found additional material that must be in the formal plan:

1. **BUILD-4 is broader than derivatives.** It must include patterns, VWAP families, BB/ATR/volume, levels/structure/liquidity, benchmark, sector, relative strength, events, expiry/roll and quality/missingness.
2. **Mandatory legacy completed-session pattern registry** was previously under-emphasized.
3. **PDC_TOUCHED and PDC_CLOSED_BEYOND are distinct binding facts.**
4. **CPR width and prior-close location share algebraic ancestry** and must not be counted independently.
5. **Legacy Z1–Z5 is compatibility/research only**, not canonical market truth.
6. **Commodity applicability rules** must be explicit: stock-only evidence becomes NOT_APPLICABLE, not neutral.
7. **Event-source contracts** are first-class B4 requirements, not deferred behind derivatives.
8. **Hypothesis v2 is richer than thesis/anti-thesis alone:** market-question detection, dynamic evidence routing, separate dependency and argumentation graphs, temporal expectation compiler, lifecycle, surprise/belief update, OOD and deterministic value-of-information are required design elements.
9. **M3.3 memory and validated Kronos/reviewers are bounded challengers**, not independent final authorities.
10. **Historical strategy thresholds are research candidates**, not BUILD-4 canonical gates.
11. **Real-time source availability does not prove historical PIT availability**, especially for option-chain/Greeks evidence.
12. **Real-source activation must be a separate gate from code green.**
13. **Legacy `orb/context.py` calendar-day resampling cannot remain canonical** after BUILD-3.
14. **Legacy execution/OI risk proxy semantics cannot be silently promoted** into canonical facts.
15. **B4-LOCK must regress M3.1/M3.2/M3.3 as affected owners**, not only B0–B3 + API.
16. **Source conflict requires comparability checks before numeric disagreement**, not blind averaging.
17. **Revision semantics / AS_KNOWN_THEN replay** must be first-class for external feeds.
18. **Instrument-specific evidence routing** must distinguish stock-specific derivatives, benchmark derivatives and commodity derivatives.
19. **No descendant fact can multiply independent evidence count** merely because it has a different label.
20. **BUILD-4 must preserve explicit abstention/OOD semantics** without minting D6 final bands.

These additions are binding on the BUILD-4 implementation plan unless superseded by a newer approved canonical source.

---

# 63. Final design principle

Do not build a machine that merely knows more indicators.

Build a system that can say:

```text
I observed X.
Y is derived from X.
Z is only an inference.
This source was not available at decision time.
These four metrics share the same option-chain ancestry.
Two explanations remain plausible.
If H1 is correct, A then B should occur.
If B fails and C occurs, H1 is invalidated.
This state is OOD / insufficiently supported.
The most useful next observation is Q.
Therefore BUILD-4 abstains from stronger interpretation.
```

That is the BUILD-4 standard.

---

# 64. 2026-09-18 ORB_BUILD_CHANGE opening-sequence binding reconciliation

This section is a binding companion to the existing BUILD-4 plan. It reconciles `ORB_BUILD_CHANGE.txt` from commit `8ba2de96c875b02defe8f3645acbf82584f830b8`, blob `cde19d0859cc84a87f4672a58e218cea84401b61`, without changing the BUILD-4 boundary in Sections 55–63 above.

The opening-sequence capability is **not implemented by this documentation change**. It remains a future additive/shadow BUILD-4-F component and has no execution or final-band authority.

## 64.1 Binding companion/source set

BUILD-4 D0 must record, hash and reconcile at least:

- the canonical master `docs/ORB_STAGE_BY_STAGE_ADVANCED_REASONING_BUILD_PLAN.md`;
- this detailed BUILD-4 plan;
- the exact `ORB_BUILD_CHANGE.txt` source blob above;
- the protected B0–B3 baseline/source-lock receipts;
- any separately approved B00 baseline or opening-sequence addendum if one is later created.

A companion source is not automatically a BUILD-0 canonical source. BUILD-0 registration remains a deliberate source-role decision after content audit and source-lock reconciliation.

## 64.2 B4-D0 opening-sequence locks

Before B4-F implementation, B4-D0 must add an `OPENING_SEQUENCE_REQUIREMENT_MAP` covering `B4-OS-001` through `B4-OS-018` and freeze these facts:

1. **Input inventory.** Enumerate every proposed sequence input and its exact canonical owner, source receipt, availability semantics and version.
2. **Duplicate-calculation audit.** Search D2, B1, B2, B3, M3.1, M3.3, `orb/context.py`, `orb/core.py` and `orb/adaptive/**`; mark each proposed calculation `REUSE_CANONICAL`, `COMPATIBILITY_ONLY`, `RESEARCH_CANDIDATE`, or `MISSING_OWNER`.
3. **Protected baseline.** Freeze the B0/B1/B2/B3 and legacy-ORB regression set before any B4-F code.
4. **Bar identity policy.** Freeze source/formation timeframe, session anchor, availability time, resample/anchor policy and revision/sequence semantics. B4 may not infer them.
5. **OR-lock policy.** Freeze `PRE_OR_LOCK`, `CROSSES_OR_LOCK`, `POST_OR_LOCK`; a crossing bar cannot be promoted to pure post-lock evidence.
6. **Normalization semantics.** Freeze every normalized range field by calculation ID, basis and version. Historical candle-anatomy `range_atr` remains mean-candle-range normalization and is not renamed into Wilder ATR.
7. **Third-party disposition.** M3.3 remains first. STUMPY/DTW and other libraries remain optional challengers only; no install/vendor action occurs in B4-D0.
8. **Authority lock.** `authority=NONE`, `may_execute=false`, `may_set_final_band=false`.

D0 stops if a proposed sequence field requires changing a B0–B3 owner, duplicating a canonical M3 calculation, guessing session/contract identity, weakening a protected test, or inventing a probability.

## 64.3 Contract-family addition: `OrbOpeningSequenceViewV1`

`OrbOpeningSequenceViewV1` is a frozen, deterministic **composition view** over canonical receipts. It is not an independent calculator, pattern engine, timing optimizer, state machine, playbook, predictor, or authority.

Conceptual minimum contract:

```text
OrbOpeningSequenceViewV1
  schema_version
  calculation/composition_version
  candidate_identity_ref              # BUILD-1
  market_identity_ref                 # BUILD-2
  prior_session_ref                   # BUILD-3
  d2_snapshot_hash
  decision_as_of / knowledge_cutoff
  session_id / session_open
  or_lock_identity / or_lock_time
  formation_policy_ref
  bars[]                               # immutable aligned bar receipts
  events[]                             # deterministic observed/derived events
  aliases[]                            # optional interpretation, lineage-bound
  level_interactions[]
  participation_facts[]
  missing_evidence[]
  dependency_ids[]
  source_snapshot_hashes[]
  output_hash
  availability
  authority = NONE
  may_set_final_band = false
  may_execute = false
```

Supporting enums/contracts should be introduced only when they own a unique invariant. Do not manufacture a large parallel type hierarchy merely to mirror existing D2/B1/B2/B3/M3 contracts.

### Formation-bar identity

Each consumed formation bar must preserve:

```text
source_timeframe
formation_timeframe
session_id
session_open
bar_open
bar_close
available_at
bar_anchor_policy
resample_policy
source_id
source_snapshot_hash
revision_id_or_sequence_identity
or_lock_relation = PRE_OR_LOCK | CROSSES_OR_LOCK | POST_OR_LOCK
```

The receipt rejects mixed session identity, future `available_at`, inconsistent source snapshots, ambiguous resampling, duplicate/reordered sequence identities, or a claimed `POST_OR_LOCK` bar whose interval crosses the lock.

### Normalized range semantics

Do not emit a bare ambiguous “ATR-normalized range” field. Every normalized range carries:

```text
normalization_basis
normalization_version
source_calculation_id
```

When present, the preferred distinct semantics are:

```text
range_vs_mean_intraday_range
range_vs_canonical_wilder_atr
```

The first may reuse the historical M3.1 candle-anatomy mean-range basis. The second is emitted only if an independently canonical Wilder-ATR owner/receipt is available. They are never substituted for each other.

## 64.4 Sequence positions, deterministic events and aliases

`B1`, `B2`, `B3` are **ordinal sequence positions**, not permanent names for the first three 3-minute candles. BUILD-5 owns research over formation timeframe, N and OR duration/lock policy. B4-F consumes a registered formation policy and never promotes one timing choice by implementation convenience.

Sequence representation is event-first. Examples of deterministic event facts include:

```text
CLOSE_ABOVE_PDH
CLOSE_BELOW_PDL
NEW_SESSION_HIGH
NEW_SESSION_LOW
LOWER_CLOSE
HIGHER_CLOSE
LOWER_HIGH
HIGHER_LOW
CLOSE_INSIDE_B1_RANGE
WICK_THROUGH_PDH
WICK_THROUGH_PDL
```

Only after source events exist may an interpretation alias such as `PDH_OPENING_REJECTION_CANDIDATE` be derived. Aliases carry the source event IDs and cannot reverse-engineer or overwrite facts. Touch, wick-through, close-beyond, acceptance, reclaim and failure remain separate semantics.

## 64.5 Initial opening-sequence hypotheses

B4-F initially maps opening-sequence evidence into four bounded competing hypotheses:

```text
H1 BREAKOUT_ACCEPTANCE_CONTINUATION
H2 BREAKOUT_REJECTION_FAILURE
H3 PULLBACK_RECLAIM_CONTINUATION
H4 OPENING_BALANCE_NO_EDGE
```

Each is represented through the existing `OrbHypothesisReceiptV1` shape and must contain, where applicable:

- supporting evidence;
- opposing evidence;
- missing/critical evidence;
- expected sequence;
- failure sequence;
- invalidation;
- expiry;
- state;
- dependencies/correlation lineage;
- OOD/insufficient-evidence handling.

No opening-sequence contract contains an uncalibrated probability. A future calibrated event/horizon probability remains BUILD-12-only and cannot bypass B4 missingness/blockers.

## 64.6 B4-F composition seam

Candidate future package seam:

```text
apps/api/app/orb/context_intelligence/
    __init__.py
    contracts.py
    sources.py
    futures.py
    option_chain.py
    volatility.py
    advanced.py
    world.py
    hypotheses.py
    opening_sequence.py
```

`opening_sequence.py` is a **composer/validator**, not a new raw-price or indicator calculator. B4-F composes its immutable receipt into `OrbContextWorldV1`; the hypothesis layer consumes that receipt and emits bounded hypotheses. M4 may later consume the receipt/hypothesis evidence but must not rebuild the sequence.

Feature OFF is a binding migration invariant: the legacy ORB path and outputs remain semantically unchanged. No B0/B1/B2/B3 runtime module is edited merely to make B4-F easier.

## 64.7 Fixed-`as_of` replay and causal invariance

Required adversarial test:

```text
construct at as_of = 09:24
  B1/B2/B3 + events + receipt hash = H
append later source data:
  09:27
  09:30
  10:00
reconstruct at as_of = 09:24 under identical policies
required:
  receipt hash == H
otherwise:
  FUTURE_DEPENDENCY_DETECTED
```

The test must exercise both source bars and any resampled/derived formation view. Cache keys include all causal identity needed to prevent cross-session, cross-symbol, cross-policy or later-revision leakage.

## 64.8 Symmetry and metamorphic requirements

B4-F/B4-LOCK must test at minimum:

- PDH upside evidence mirrored to PDL downside evidence;
- price scale ×10 leaves normalized geometry unchanged while absolute prices scale;
- missing RVOL/participation remains `UNKNOWN`/unavailable, never numeric zero;
- missing PDH prevents PDH-derived events instead of inventing a neutral event;
- wick-through is not close-beyond;
- OR-lock exact-boundary and straddle cases;
- reversed/duplicate/revised formation-bar identity fails closed;
- long/short alias derivation is symmetric where market semantics are symmetric.

## 64.9 M3.3-first analogue/challenger order

Opening-sequence history research follows this order:

1. existing canonical M3.3 memory/analogue/pattern/nine-candle retrieval;
2. register an opening-sequence feature manifest over canonical facts;
3. measure and document a concrete limitation;
4. only if the limitation is demonstrated, evaluate STUMPY as an optional BUILD-9 challenger;
5. only if additional value is demonstrated, evaluate bounded DTW reranking.

Third-party adoption requires **all** of:

- licence compatibility;
- PIT/causality compatibility;
- dependency and maintenance assessment;
- runtime suitability;
- incremental BUILD-8 proof.

This plan does not install STUMPY, DTAIDistance/DTW, PatternPy, stock-pattern, precise-patterns or any other new dependency.

## 64.10 BUILD-8 adjacent ablation ladder

BUILD-8 must register and evaluate:

```text
A0 existing ORB
A1 + canonical candle anatomy
A2 + level-interaction sequence
A3 + B1/B2/B3 transition facts
A4 + valid RVOL/participation
A5 + benchmark/sector/context
A6 + B6 formation state
A7 + canonical M3.3 analogues
A8 + STUMPY
A9 + DTW reranking
```

Every `A[n]` is compared against `A[n-1]` under equivalent chronological splits, costs, support requirements and multiple-testing governance. A later rung does not earn adoption merely by outperforming A0. A8/A9 remain optional and stop if their prerequisites or incremental value are absent.

## 64.11 B4-LOCK opening-sequence gate

In addition to Section 57, B4-LOCK requires observed green results for:

- B4-OS-001…018 traceability;
- view-not-calculator / canonical-owner audit;
- normalization-basis/version semantics;
- exact formation-bar identity;
- OR-lock PRE/CROSSES/POST classification;
- event-before-alias derivation;
- H1–H4 receipt completeness;
- fixed-`as_of` replay invariance;
- PDH/PDL and long/short symmetry;
- price-scale and missingness metamorphic cases;
- feature-OFF legacy parity;
- protected B0/B1/B2/B3 regressions;
- affected M3.1/M3.3 regressions;
- D6/authority regression;
- no new dependency;
- exact-head CI.

No BUILD-8 trading-value claim is required for B4 CODE GREEN. Conversely, B4 CODE GREEN is not evidence that the sequence feature adds trading value.

## 64.12 Completion-receipt extension

The Section 59 receipt must additionally state:

```text
B00 BASELINE RESULT
OPENING-SEQUENCE REQUIREMENT COVERAGE
CANONICAL-OWNER / DUPLICATION AUDIT RESULT
NORMALIZATION SEMANTICS RESULT
FIXED-AS_OF REPLAY RESULT
OR-LOCK STRADDLE RESULT
SYMMETRY / METAMORPHIC RESULT
FEATURE-OFF PARITY RESULT
PROTECTED-SURFACE RESULT
THIRD-PARTY DISPOSITION RESULT
RUNTIME CODE CHANGED DURING DOC RECONCILIATION? MUST BE NO
DEPENDENCIES ADDED DURING DOC RECONCILIATION? MUST BE NO
TRADING AUTHORITY CHANGED? MUST BE NO
```

Proof levels remain distinct: plan traceability, BUILD-0 source-lock proof, B4-D0 lock, B4-F implementation proof, and BUILD-8 incremental trading-value proof are not interchangeable.

# 65. 2026-09-19 continuous intraday formation intelligence extension

Status: `PROPOSED_DOCUMENTATION_CONTRACT`; not implemented and not GREEN.

This section extends `OrbOpeningSequenceViewV1` without replacing it. Opening-sequence reasoning remains the opening-specific view; `OrbIntradayFormationViewV1` generalizes the same causal composition discipline to arbitrary intraday `decision_as_of` times.

## 65.1 Contract role

`OrbIntradayFormationViewV1` is a deterministic, read-only **VIEW / COMPOSER** over canonical receipts. It may align already-owned facts and B6 state; it may not resample a second candle truth, recalculate M3.1 structure/levels, recreate BUILD-2 market identity, rebuild BUILD-3 references, own M3.3 memory, emit uncalibrated probabilities, set a final band, or execute.

Mandatory authority:

```text
authority = NONE
may_execute = false
may_set_final_band = false
```

## 65.2 FORM-001 — arbitrary-`as_of` identity

Every view binds:

```text
decision_as_of
knowledge_cutoff
source_snapshot_hash
formation_snapshot_hash
composition_version
availability
```

All facts used must have been available no later than the knowledge cutoff. Fixed-`as_of` reconstruction after later data is appended must reproduce the same causal receipt.

## 65.3 FORM-002 — deterministic anchor registry

A formation may start only from an anchor whose underlying event is canonical, provenance-bound, and already known by `decision_as_of`.

Candidate anchor families:

```text
SESSION_OPEN
OR_LOCK
CAUSAL_PIVOT
PDH_INTERACTION
PDL_INTERACTION
ORH_INTERACTION
ORL_INTERACTION
VWAP_RECLAIM
STRUCTURE_BREAK
EXPANSION_START
```

These names are registry candidates, not proof that each producer already exists. Unsupported/unavailable candidates stay unavailable.

Anchor identity:

```text
anchor_type
anchor_event_id
anchor_owner
anchor_market_time
anchor_known_at
anchor_source_snapshot_hash
anchor_policy_version
```

Hard invariant: `anchor_known_at <= decision_as_of`. Later candles may not cause the historical replay to choose a prettier anchor.

## 65.4 FORM-003 — multi-scale formation identity

Every active formation/hypothesis records:

```text
source_timeframe
formation_timeframe
scope
horizon
anchor
```

Initial scope vocabulary:

```text
MICRO
LOCAL_SWING
OPENING_SEQUENCE
INTRADAY
SESSION
```

Different scales can coexist. A micro bearish pullback does not automatically contradict a larger bullish continuation.

## 65.5 FORM-004 — B6 lifecycle contract

B6 owns lifecycle semantics:

```text
SEED
DEVELOPING
TESTING_BOUNDARY
CONFIRMED
FAILED
EXPIRED
AMBIGUOUS
```

B4 composes the B6 state; it does not create a competing state machine. `CONFIRMED` requires registered confirmation evidence. `AMBIGUOUS` and `NO_STABLE_FORMATION` are valid outputs.

Incomplete higher-timeframe candles may yield only a `PROVISIONAL` zero-authority view until the required candle closes.

## 65.6 FORM-005 — discriminator-complete hypotheses

Every active hypothesis must include:

```text
support[]
opposition[]
unknown[]
expected_sequence[]
failure_sequence[]
next_discriminating_observation
confirmation_condition
weakening_condition
invalidation_condition
expiry_condition
```

Discriminators and conditions must resolve to deterministic events or versioned research rules. Phrases such as “looks stronger” are not machine contracts.

## 65.7 FORM-006 — prefix-safe historical analogue seam

For a current `decision_as_of=T`:

```text
current prefix through T
        ↓
historical prefixes through equivalent cutoff only
        ↓
freeze episode IDs + feature manifest + retrieval version
        ↓
reveal matured future outcomes only after retrieval is frozen
```

Historical outcomes may never influence retrieval candidates, rank, anchor, feature construction or tie-breaking. M3.3 remains the first retrieval owner. B9 may challenge it only after a concrete limitation is demonstrated.

## 65.8 FORM-007 — versioned behavioural grammar

Required derivation order:

```text
CANDLE FACTS
    ↓
RELATIONSHIPS
    ↓
SEQUENCE BEHAVIOUR
    ↓
STRUCTURAL FORMATION
    ↓
OPTIONAL HUMAN ALIAS
```

Example relationships/behaviours/aliases are descriptive vocabulary, not automatically canonical features. Every promoted grammar element requires a version and source-event lineage.

## 65.9 FORM-008 — transition diary

Formation evolution is replayable. Each state transition records:

```text
formation_id
previous_state
current_state
changed_at
evidence_added[]
evidence_removed[]
reason
source_snapshot_hash
formation_snapshot_hash
transition_version
```

Corrections use replacement/supersession lineage; prior transitions are not silently rewritten.

## 65.10 FORM-009 — dependency lineage

Every alias/hypothesis carries:

```text
source_event_ids[]
dependency_family
derived_from[]
```

If several labels derive from one underlying candle/structure sequence, B11/D6 receives one correlated family, not multiple independent votes.

## 65.11 FORM-010 — geometry/tolerance policy

B7 owns versioned policies including, where applicable:

```text
boundary_tolerance_basis
pivot_prominence_basis
minimum_touch_count
slope_policy
compression_policy
overlap_policy
retracement_policy
normalization_basis
parameter_version
```

B4/B6 consume the registered version. B8 proves it. B10 freezes only evidence-supported settings. No threshold is promoted here merely because it is visually plausible.

## 65.12 Mandatory hard-safety outcomes

1. `NO_STABLE_FORMATION` / `UNRESOLVED` must be legal.
2. Missing evidence remains unknown/unavailable; never zero/neutral by coercion.
3. Incomplete higher-timeframe interpretations are `PROVISIONAL`, zero-authority, never `CONFIRMED` before close.
4. Screenshots are scenario/example material only; canonical reasoning uses numerical timestamped source data and hashes.
5. Pattern-fishing controls freeze grammar, candidate families, anchor/search space, train/walk-forward periods and untouched holdout before evaluation.

## 65.13 Mandatory receipt shape

```text
OrbIntradayFormationViewV1
  identity:
    instrument/session/contract
    decision_as_of
    knowledge_cutoff
    source_timeframe
    formation_timeframe
    scope
    horizon
    anchor
    grammar_version
    parameter_version
    source_snapshot_hash
    formation_snapshot_hash
    composition_version
  observed_behaviour[]
  active_formations[]
  competing_hypotheses[]
  transition_history_ref
  historical_prefix_analogue_ref
  missing_or_unknown_evidence[]
  dependency_lineage[]
  authority = NONE
  may_execute = false
  may_set_final_band = false
```

## 65.14 B14 adversarial lock set

B14 must prove at least:

- future-append invariance;
- hindsight-anchor invariance;
- historical-analogue outcome non-interference;
- multi-timeframe coexistence without false contradiction;
- alias-independence/dependency-family de-duplication;
- incomplete-candle cannot confirm;
- pattern-search leakage invariance;
- legal `NO_STABLE_FORMATION` outcome;
- missingness remains explicit;
- feature-OFF legacy parity.

A documentation change does not satisfy these tests. Runtime implementation remains a later build.

# 66. 2026-09-19 source-detail preservation — PDH opening expansion / rejection research contract

Status: \`SOURCE_DERIVED_RESEARCH_DETAIL\`; additive to Sections 64–65. This section preserves the lower-level details in committed \`ORB_BUILD_CHANGE.txt\` without turning chart-specific examples into frozen runtime rules.

## 66.1 Sequence positions, not a fixed 3-minute contract

\`B1/B2/B3\` are ordinal positions under the registered formation policy. The source's 3-minute examples are explanatory fixtures only. BUILD-5 owns the eventual formation timeframe, N and OR-window/clock policy.

Required property:

\`\`\`text
same registered formation policy
+ same closed source bars
+ same decision_as_of
    -> same B1/B2/B3 identity
\`\`\`

Changing the later session or appending future candles may not re-select earlier B1/B2/B3.

## 66.2 Canonical primitive reuse

BUILD-4 must consume canonical M3.1 / pattern-taxonomy facts instead of creating duplicate candle mathematics. Verified reusable taxonomy concepts include:

\`\`\`text
body_size
body_pct_of_range
upper_wick_size
lower_wick_size
close_location_value
same_direction_body_sequence
opposite_direction_body_sequence
body_expansion_sequence
body_compression_sequence
wick_expansion_sequence
wick_compression_sequence
nearby_candle_confirmation
nearby_candle_rejection
nearby_candle_absorption
nearby_candle_exhaustion
previous_1_candle
previous_2_candles
previous_3_candles
previous_5_candles
\`\`\`

If a required primitive is unavailable, BUILD-4 exposes unavailable/unknown rather than calculating a private substitute.

## 66.3 Opening-expansion detail fields

For B1, the composed view may expose canonical references/derived relations for:

\`\`\`text
B1_range
B1_body
upper_wick
lower_wick
body_to_range

normalized_range_value
normalization_basis
normalization_version

volume
opening_RVOL
volume_availability

open_minus_previous_close
open_minus_PDH
high_minus_PDH
close_minus_PDH
close_location_value
\`\`\`

No field above gains authority by being present.

The source's \`B1 range / ATR\` example is retained only with an explicit normalization basis. It must not reuse legacy \`range_atr\` semantics when the denominator is actually Wilder ATR.

## 66.4 Giveback contract

Giveback must be a typed/versioned research metric, because the source appendix demonstrates the ratio but does not fully freeze the numerator convention.

At minimum a giveback observation must identify:

\`\`\`text
giveback_value
giveback_ratio
giveback_numerator_basis
giveback_denominator_basis
measurement_start
measurement_end
available_at
metric_version
\`\`\`

Historical example retained for regression/documentation:

\`\`\`text
B1 range = 6
measured giveback = 2.2
giveback_ratio = 2.2 / 6 = 36.7%
\`\`\`

Examples such as \`B2 giveback > 35%\` and 10% giveback remain research candidates only. They are forbidden as hidden defaults until B7 registers the policy and B8 proves it.

## 66.5 CLV contract

The source formula is:

\`\`\`text
CLV = (Close - Low) / (High - Low)
\`\`\`

The ORB view should consume the canonical \`close_location_value\` fact where available rather than recalculate it.

Historical interpretation retained only as descriptive semantics:

\`\`\`text
near 1.0 -> close near high
near 0.5 -> close near middle
near 0.0 -> close near low
\`\`\`

CLV alone cannot confirm continuation/reversal and cannot become a probability.

## 66.6 PDH opening geometry

Preserve the source's exact opening-location relationships:

\`\`\`text
previous_close
PDH
B1_open
B1_high
B1_close
extension_from_PDH
gap_above_PDH
\`\`\`

Derived research observations may include time/sequence to 25%, 50% and 75% registered giveback; PDH touch; accepted close below PDH; PDH reclaim; and new-session-high continuation. Each requires event-time, knowledge-time and level/reference lineage.

Touch, wick-through, close-below, acceptance, hold, reclaim and failure remain separate events.

## 66.7 Event-first state progression

The source-specific family \`PDH_OPENING_SPIKE_REJECTION\` is not emitted from appearance alone.

Preferred event progression:

\`\`\`text
B1:
  CLOSE_ABOVE_PDH
  NEW_SESSION_HIGH

B2:
  NO_NEW_SESSION_HIGH
  CLOSE_INSIDE_B1_RANGE
  LOWER_CLOSE_THAN_B1

B3:
  LOWER_HIGH_THAN_B2
  LOWER_CLOSE_THAN_B2
\`\`\`

Possible research states/aliases, in order:

\`\`\`text
PDH_OPENING_DRIVE
PDH_OPENING_DRIVE_REJECTION
PDH_OPENING_REJECTION_CANDIDATE
PDH_OPENING_2BAR_REJECTION
\`\`\`

\`PDH_FAILED_BREAKOUT_FADE\` is **not legal after B3 merely because the chart looks bearish**. It requires the later registered failure condition, such as the required closed-candle loss/acceptance below PDH under the versioned state policy.

The competing continuation family remains live, including the source-preserved \`PDH_BREAKOUT_PULLBACK_CONTINUATION\` path.

## 66.8 Source-preserved higher-level taxonomy

Research decomposition:

\`\`\`text
Family:       OPENING_LOCATION_STRUCTURE
Context:      ABOVE_PDH
Event:        EXPANSION
Reaction:     REJECTION
Confirmation: 2_BAR_FOLLOW_THROUGH
\`\`\`

Source-proposed IDs retained for traceability:

\`\`\`text
OPEN_ABOVE_PDH__EXPANSION__2BAR_REJECTION
OPEN_ABOVE_PDH__EXPANSION__2BAR_REJECTION__PDH_HOLD
OPEN_ABOVE_PDH__EXPANSION__2BAR_REJECTION__PDH_FAIL
\`\`\`

These are proposed research identifiers, not automatically current runtime enum members. Before promotion, B6/B7/B8 must bind lifecycle meaning, geometry, symmetry, missingness, versioning and proof.

## 66.9 Required competing-path behavior

After a strong B1 expansion and B2/B3 rejection sequence, the engine must preserve at least the competing possibilities already represented by the canonical hypothesis layer:

\`\`\`text
breakout acceptance / continuation
opening rejection / failure
pullback-reclaim continuation
balance / no-edge
\`\`\`

The source-specific state names may enrich these hypotheses but may not force one to win early.

## 66.10 Adversarial checks added by this detail bridge

BUILD-8/B14 verification must include:

1. **B1 ordinal invariance** — changing the configured formation timeframe changes policy identity, not the meaning of ordinal B1/B2/B3.
2. **No premature failed-break label** — B3 rejection alone cannot emit \`PDH_FAILED_BREAKOUT_FADE\`.
3. **Continuation coexistence** — the same B1 may still mature into \`PDH_BREAKOUT_PULLBACK_CONTINUATION\`.
4. **Giveback-policy identity** — changing numerator/denominator policy changes metric version/hash; no silent semantic reuse.
5. **No hard-coded source examples** — 3 ATR, 35%, 10%, 25/50/75 are not defaults unless separately registered/proven.
6. **CLV lineage** — ORB consumes canonical close-location fact and cannot privately redefine it.
7. **PDH event separation** — touch, wick, close, acceptance, hold, reclaim and fail remain distinct.
8. **Alias de-duplication** — \`PDH_OPENING_SPIKE_REJECTION\` and its descendant labels do not multiply one price sequence into multiple independent votes.
9. **PDH/PDL symmetry test** — mirror only where the registered market semantics are symmetric.
10. **Future-append invariance** — later session data cannot rewrite the earlier state, metric policy, taxonomy candidate or hypothesis evidence.
11. **Feature-off parity** — disabling the new detail layer preserves legacy ORB semantics.
12. **Zero authority** — every detail remains research-only and cannot execute or set D6's final band.

## 66.11 Completion boundary

This section is complete as a **documentation contract** only when all source-preserved items above are traceable to canonical owners and tests. It is not implementation proof. No threshold, pattern alias or taxonomy ID is promoted merely because it appears in this plan.

\`authority=NONE\`, \`may_execute=false\`, \`may_set_final_band=false\`. D6 remains final authority.

# 67. 2026-09-21 BUILD-4 missing-piece reconciliation

Status: `APPEND_ONLY / PLAN_RECONCILIATION / NO_RUNTIME_IMPLEMENTATION / NO_SOURCE_ACTIVATION`.

This section is additive to Sections 0-66. No earlier line is replaced, deleted, renumbered, weakened, or reinterpreted by this reconciliation.

Audited repository state:

```text
repository = onlyvictus-bit/trade-vision-app
branch = plan/orb-build4-d0-lock-full-plan
pre_append_head = cc6cde6febded9276a4a47fa2ed6b2b0ffbc3936
pre_append_blob = 61638f6cd58de2290409725dab90bda394cacac9
pre_append_line_count = 2879
append_only = true
runtime_code_changed = false
real_source_activated = false
trading_authority_changed = false
```

The second-pass audit compared this dedicated BUILD-4 plan with the current repository versions of:

- `docs/ORB_STAGE_BY_STAGE_ADVANCED_REASONING_BUILD_PLAN.md`;
- `docs/ORB_AFRE_CANONICAL_FUTURE_BUILD_PLAN_2026-09-10.md`;
- `docs/plans/ORB_CONTEXT_NATIVE_PLAN_V2.md`;
- `docs/plans/ORB_STRATEGY_MEMORANDUM.md`;
- `docs/plans/ORB_RESEARCH_ENGINE_PLAN.md`;
- `docs/ORB_SIMPLE_FLOW.md`;
- `docs/plans/FINAL_REQUIRED_FLOW.md`;
- `docs/plans/ORB_TIMING_RESEARCH_V197.md`;
- the external-review briefs;
- `apps/api/app/orb/adaptive/derivatives.py`;
- canonical M3.2 context-source code;
- BUILD-0 source-readiness and requirement-audit contracts.

The audit found two different gap classes:

1. capabilities already present in legacy/adaptive code or another canonical plan but under-specified here;
2. genuinely missing BUILD-4 typed facts/composition seams required to use those capabilities safely.

Permanent reconciliation law:

```text
legacy calculation exists != canonical BUILD-4 owner
public source exists != AVAILABLE_REAL_PIT
research threshold exists != canonical truth
derived state != observed fact
wall != support/resistance fact
gamma concentration != dealer positioning
reconstructed != observed
missing != neutral
unknown != false
correlated evidence != independent evidence
B4 describes/composes/reasons
B7 researches thresholds
B8 proves incremental value
B10 freezes proven policy
B12 calibrates probability
D6 alone sets the final guidance band
```

---

## 67.1 B4-D0 required reconciliation registry

Before B4-A runtime work, D0 must freeze one row for every capability below:

```text
capability_id
requirement_source
current_runtime_producer
canonical_owner
target_B4_stage
source_readiness
input_contracts
output_contracts
epistemic_level
dependency_family
threshold_owner
proof_owner
migration_action
```

Minimum inventory:

```text
FUTURES_OI_BUILDUP_5_STATE
FUTURES_RAW_BASIS
FUTURES_ADJUSTED_BASIS
FUTURES_ROLLOVER
PARTICIPANT_FII_POSITIONING
OPTION_OI_PCR
OPTION_CHANGE_OI_PCR
OPTION_VOLUME_PCR
PCR_CHANGE_OVER_TIME
CALL_OI_WALL
PUT_OI_WALL
CALL_DELTA_OI_WALL
PUT_DELTA_OI_WALL
OI_WALL_LIFECYCLE
INDIA_VIX_LEVEL
INDIA_VIX_CHANGE
ATM_IV
ATM_IV_CHANGE
IV_RANK
IV_PERCENTILE
IV_CRUSH_CONTEXT
SKEW_25D
SKEW_CHANGE
TERM_STRUCTURE
TERM_STRUCTURE_CHANGE
TERM_STRUCTURE_ORDERING_STATE
DELTA
GAMMA
VEGA
THETA
RHO
VANNA
CHARM
ABSOLUTE_GAMMA_CONCENTRATION
GAMMA_WALL
GAMMA_WALL_LIFECYCLE
SIGNED_DEALER_GEX_HYPOTHESIS
ZERO_GAMMA_REFERENCE
MAX_PAIN_REFERENCE
EXPECTED_MOVE
GIFT_NIFTY_CONTEXT
GIFT_OPEN_DIVERGENCE
PREOPEN_AUCTION_CONTEXT
MARKET_BREADTH_CONTEXT
INDEX_ALIGNMENT_CONTEXT
SECTOR_DIVERGENCE_CONTEXT
EVENT_VOLATILITY_INTERACTION
CORPORATE_ACTION_ADJUSTED_GAP
OPENING_QUALITY_RVOL
SOURCE_INTEGRITY_RECONCILIATION
DERIVATIVES_CHAIN_QUALITY
```

D0 must inspect current owners before new code, especially `adaptive/derivatives.py`, `orb/context.py`, BUILD-2/3, M3.1, M3.2 and retained behavior-layer OI/event proxies.

Allowed migration dispositions:

```text
REUSE_CANONICAL_OWNER
COMPOSE_UPSTREAM_FACT
WRAP_LEGACY_FOR_SHADOW
MIGRATE_FORMULA_TO_B4_CANONICAL_OWNER
NEW_B4_CALCULATION_REQUIRED
DEFER_UNTIL_SOURCE_EXISTS
REJECT_DUPLICATE
```

Legacy adaptive thresholds such as delta-VIX +8%, IV-crush -20%, term inversion >5 vol points, PCR extremes, max-pain proximity, rollover, basis, GIFT-gap and FII-crowding thresholds remain research candidates, not BUILD-4 truth.

---

# 68. B4-A additions - source, baseline, publication, replay and integrity

B4-A needs an explicit comparison-snapshot identity because dynamic facts cannot use an unspecified "previous" value.

Candidate shared reference:

```text
OrbComparisonSnapshotRefV1
comparison_role
current_fact_id
baseline_fact_id
current_snapshot_hash
baseline_snapshot_hash
current_event_time
baseline_event_time
current_available_at
baseline_available_at
decision_as_of
comparison_interval
same_instrument
same_contract
same_expiry_scope
same_strike_universe
same_units
same_adjustment_basis
comparison_policy_id
comparison_policy_version
availability
reason_codes[]
```

Comparison roles must distinguish at least previous-session close, previous available snapshot, pre-event snapshot and fixed registered intraday baseline.

Additional explicit B4-A source families:

- India VIX;
- GIFT Nifty / registered cross-market reference;
- FII/participant derivatives reports;
- option-chain current and historical PIT snapshots;
- pre-open auction;
- event/results/macro/corporate-action sources;
- M3.2 breadth/index/sector sources;
- market-status/halt/special-session facts where not already owned by BUILD-2;
- optional PIT news;
- optional depth/order-book sources.

Publication-time law for reports:

```text
report_trade_date
published_at
available_at
received_at
knowledge_cutoff
decision_as_of
```

An EOD FII/participant report cannot be used as a 09:30 same-session fact merely because its trade date is the same.

A current API/page does not prove historical PIT readiness. For every external source record separately:

```text
live_current_available
historical_snapshots_available
historical_timestamp_quality
publication_timing_reconstructable
revision_history_reconstructable
licence_usage_acceptable
fixture_captured
```

Reuse BUILD-0 readiness states only:

```text
COMPUTABLE_LOCAL
NEEDS_VERSIONED_FILE
NEEDS_EXTERNAL_FEED
AVAILABLE_REAL_PIT
UNAVAILABLE
NOT_APPLICABLE
ERROR
```

### 68.1 Source-integrity / reconciliation receipt

Add or reuse an upstream equivalent of:

```text
OrbSourceIntegrityReceiptV1
fact_family
instrument_identity
session_id
primary_source_id
secondary_source_id
primary_snapshot_hash
secondary_snapshot_hash
comparison_policy_id
same_identity
same_effective_time
same_units
same_adjustment_basis
same_revision_basis
same_session_phase
comparison_result
  MATCH
  WITHIN_REGISTERED_TOLERANCE
  CONFLICT
  NOT_COMPARABLE
  SECONDARY_UNAVAILABLE
  RECONCILIATION_PENDING
  ERROR
reconciled_at
available_at
decision_as_of
reason_codes[]
integrity_hash
```

This explicitly reconciles the old CTX-02 EOD-reconciliation and UNIV-03 dual-source mismatch requirements.

Rules:

- later EOD truth may flag an earlier data-quality issue but cannot rewrite the old `AS_KNOWN_THEN` receipt;
- `AS_REVISED_NOW` must be explicit;
- non-comparable sources are never averaged;
- comparable disagreement is `CONFLICT`;
- secondary unavailable does not prove primary correct.

---

# 69. B4-B additions - futures, five-state OI, participant positioning and basis

Formalize the existing full price/OI taxonomy:

```text
LONG_BUILDUP
SHORT_BUILDUP
SHORT_COVERING
LONG_UNWINDING
FLAT_OR_AMBIGUOUS
```

Required facts:

```text
contract_identity
comparison_contract_identity
price_current
price_baseline
price_delta
price_delta_pct
oi_current
oi_baseline
oi_delta
oi_delta_pct
comparison_interval
current_snapshot_hash
baseline_snapshot_hash
available_at
calculation_version
availability
```

Contract mismatch/roll mismatch invalidates the classification; it does not manufacture a state.

### 69.1 Participant/FII positioning

Candidate contract:

```text
OrbParticipantPositioningV1
participant_type
instrument_family
instrument_scope
long_oi
short_oi
net_oi
long_pct
short_pct
long_short_ratio
report_trade_date
published_at
available_at
decision_as_of
source_id
source_version
source_snapshot_hash
availability
quality
```

FII/index-futures positioning is market/crowding context, not stock-specific ownership and not an independent vote when multiple fields share the same report.

### 69.2 Basis and rollover

Keep raw and adjusted basis side by side:

```text
raw_basis_points
raw_basis_bps
carry_adjustment_bps
dividend_adjustment_bps
other_registered_adjustment_bps
adjusted_basis_bps
adjustment_fact_ids[]
adjustment_policy_id
adjustment_policy_version
```

Rollover must bind exact front/next contract identities, OI values, numerator/denominator, formula/version and comparison time. Historical rollover/basis thresholds stay downstream research candidates.

---

# 70. B4-C additions - PCR dynamics, typed OI walls and chain quality

PCR remains three separate facts:

```text
OI_PCR
CHANGE_OI_PCR
VOLUME_PCR
```

PCR change must additionally preserve:

```text
pcr_type
current_pcr
baseline_pcr
pcr_change_abs
pcr_change_pct
current_expiry_scope
baseline_expiry_scope
current_strike_universe_id
baseline_strike_universe_id
comparison_interval
current_snapshot_hash
baseline_snapshot_hash
availability
```

Day-over-day and intraday changes are different comparison policies.

### 70.1 Typed OI walls

Candidate contract:

```text
OrbOptionPositioningWallV1
wall_type
  CALL_OI_WALL
  PUT_OI_WALL
  CALL_DELTA_OI_WALL
  PUT_DELTA_OI_WALL
underlying_identity
expiry
strike
option_side
oi
delta_oi
concentration_share
rank_within_scope
strike_universe_id
underlying_reference
distance_points
distance_pct
distance_atr
first_observed_at
last_observed_at
observation_count
source_snapshot_hash
available_at
calculation_version
availability
quality
```

Semantic law:

```text
OI wall = positioning concentration fact
OI wall != support fact
OI wall != resistance fact
OI wall != pin fact
OI wall != reversal fact
```

### 70.2 Wall lifecycle

When comparable sequential chains exist, model:

```text
CREATED
PERSISTING
STRENGTHENING
WEAKENING
SHIFTED
REMOVED
UNKNOWN
```

A missing/partial current chain yields unknown/unavailable, not removed.

Track previous/current wall id, strike shift, OI change, concentration change, comparison interval and both snapshot hashes.

### 70.3 Chain-quality receipt

Advanced option facts must carry a chain-quality receipt including expected/observed expiries and strikes, paired call/put coverage, missing OI/volume, stale/crossed quotes, invalid/duplicate contracts, coverage percentage and freshness.

A thin/partial chain may be descriptive but cannot silently support high-precision walls, surfaces, max pain or gamma concentration.

---

# 71. B4-D additions - delta VIX, IV change/crush, dynamic surface and higher-order Greeks

### 71.1 India VIX change

Separate VIX level from change:

```text
vix_value
baseline_vix_value
vix_change_abs
vix_change_pct
baseline_role
baseline_event_time
baseline_available_at
current_event_time
current_available_at
baseline_snapshot_hash
current_snapshot_hash
comparison_policy_id
availability
```

The +8% historical rule is a research candidate only.

### 71.2 IV change / crush

Preserve:

```text
atm_iv
reference_atm_iv
iv_change_abs
iv_change_pct
reference_role
reference_event_id
reference_time
current_time
current_expiry_scope
reference_expiry_scope
current_moneyness_or_delta_policy
reference_moneyness_or_delta_policy
current_snapshot_hash
reference_snapshot_hash
availability
```

Possible inferred labels such as IV expansion/compression/crush candidate remain interpretations, not direction.

### 71.3 Term structure

Separate the raw comparable spread/order from a thresholded inversion candidate.

```text
near_expiry
far_expiry
near_dte
far_dte
comparison_delta_or_moneyness
near_iv
far_iv
spread_vol_points
ordering_state
  NEAR_ABOVE_FAR
  NEAR_EQUAL_FAR
  NEAR_BELOW_FAR
  UNKNOWN
comparison_policy_id
availability
```

A historical ">5 vol points" inversion threshold is not part of the fact definition.

### 71.4 Dynamic surface

Where causal comparable snapshots exist, allow:

```text
delta_atm_iv
delta_25d_skew
delta_term_structure
delta_expected_move
```

Each must carry baseline/current snapshot identity and comparable-expiry/moneyness policy.

### 71.5 Greeks

The existing Delta/Gamma/Vega/Theta/Rho plan is extended explicitly with Vanna and Charm because the current adaptive implementation already carries them and older plans preserve them as experimental.

Per-option Vanna/Charm must preserve model/source, units, contract identity, timestamps and quality. Aggregates remain experimental/ALERT_ONLY until B8 proof.

Vomma/Volga may be retained as `OPTIONAL_RESEARCH_CANDIDATE`. Speed, Zomma, Color, Veta, Ultima and other higher-order Greeks do not block B4 CODE GREEN.

Optional IV-vs-realized-volatility relationships also remain challengers, not required truth.

---

# 72. B4-E additions - gamma walls, zero gamma and dynamic derivatives disagreement

### 72.1 Gamma concentration wall

Candidate contract:

```text
OrbGammaConcentrationLevelV1
underlying_identity
expiry_scope
strike
option_side_scope
absolute_gamma_exposure
concentration_share
rank_within_scope
gamma_source_or_model_id
multiplier_basis
underlying_reference
distance_points
distance_pct
distance_atr
chain_quality_receipt_id
source_fact_ids[]
available_at
calculation_version
availability
quality
```

Keep separate:

```text
CALL_GAMMA_CONCENTRATION
PUT_GAMMA_CONCENTRATION
ABSOLUTE_GAMMA_WALL
```

Gamma concentration is not dealer sign.

### 72.2 Signed GEX

```text
ABSOLUTE_GAMMA_CONCENTRATION = may be locally derived
SIGNED_DEALER_GEX_HYPOTHESIS = requires explicit sign model/input
```

Open interest alone cannot infer dealer long/short gamma. Sign-model identity/version/assumptions must participate in the hash.

### 72.3 Zero gamma

A zero-gamma-style reference requires an explicit signed-exposure model, root-finding domain, interpolation method, numerical tolerance, source snapshot and quality state. If signed exposure is unavailable, zero gamma is unavailable.

Never select an arbitrary nearest strike and call it zero gamma.

### 72.4 Dynamic walls/exposures

Comparable snapshots may describe wall/gamma creation, strengthening, weakening, shift and removal. Missing current data cannot mean removal.

Aggregate Vanna/Charm exposure may be carried as experimental context with explicit aggregation formula/version and no direct direction authority.

Max pain and expected move remain deterministic references with method identity. Movement/change may be described only when baseline/current snapshots are comparable.

---

# 73. B4-F additions - GIFT, pre-open, breadth, index/sector, corporate actions and opening quality

### 73.1 GIFT Nifty

Candidate context:

```text
GiftNiftyContextV1
contract_identity
expiry
last_price
gift_reference_time
nse_previous_reference_id
nse_previous_reference
gift_implied_gap_points
gift_implied_gap_pct
gift_gap_atr
nse_preopen_iep
nse_open
gift_to_iep_divergence_points
gift_to_iep_divergence_pct
gift_to_open_divergence_points
gift_to_open_divergence_pct
available_at
freshness
source_snapshot_hash
availability
```

GIFT is pre-open/cross-market context, not a prediction.

### 73.2 NSE pre-open auction

If an approved PIT source exists, preserve:

```text
PreOpenAuctionContextV1
snapshot_time
auction_phase
previous_close
iep
ieq
indicative_imbalance_qty
best_bid
best_ask
final_preopen_price
final_preopen_volume
preopen_gap_points
preopen_gap_pct
preopen_gap_atr
preopen_imbalance_ratio
source_snapshot_hash
available_at
freshness
availability
```

Historical replay requires captured historical auction snapshots; the current pre-open page cannot reconstruct an old decision.

### 73.3 Market breadth

M3.2 remains generic breadth owner. B4-F composes an approved receipt such as:

```text
advancing_count
declining_count
unchanged_count
advance_decline_ratio
advance_decline_net
sector_advancers
sector_decliners
pct_universe_above_vwap
pct_universe_above_open
pct_universe_above_orh
pct_universe_below_orl
breadth_universe_version
breadth_available_at
availability
```

Derived breadth percentages require a causally frozen universe and same-time per-symbol facts. Missing breadth is unavailable, not neutral.

### 73.4 Index alignment / sector divergence

B4-F composes M3.2 benchmark/sector receipts with canonical OR/VWAP/structure facts. Versioned relationship states may include:

```text
INDEX_ALIGNED
INDEX_CONFLICT
INDEX_INSIDE_RANGE
SECTOR_ALIGNED
SECTOR_DIVERGENT
UNKNOWN
```

Actions such as veto/half-size remain downstream research policy.

### 73.5 Corporate-action adjusted opening gap

The raw observed gap and economically adjusted gap must remain distinct.

Candidate composition:

```text
OrbCorporateActionGapContextV1
instrument_identity
session_date
raw_previous_reference_id
raw_previous_reference_value
current_open_fact_id
current_open
raw_gap_points
raw_gap_pct
corporate_action_event_id
corporate_action_type
corporate_action_effective_date
corporate_action_amount
corporate_action_currency
corporate_action_adjustment_basis
corporate_action_source_receipt_id
corporate_action_available_at
adjusted_reference_value
adjusted_gap_points
adjusted_gap_pct
adjustment_applied
adjustment_reason_codes[]
source_fact_ids[]
calculation_version
availability
quality
snapshot_hash
```

No dividend/split/bonus adjustment may be guessed from price behavior. Missing corporate-action data is not "no action".

### 73.6 Event/calendar/expiry/market-status temporal state

Candidate composition:

```text
OrbEventTemporalContextV1
event_id
event_type
instrument_scope[]
market_scope[]
source_receipt_id
scheduled_at
announced_at
starts_at
ends_at
result_available_at
cancelled_at
revised_at
available_at
decision_as_of
session_relation
  PRE_EVENT
  EVENT_WINDOW
  POST_EVENT
  COMPLETED_RESULT_AVAILABLE
  CANCELLED
  UNKNOWN
market_status
  NORMAL_SESSION
  SPECIAL_SESSION
  TRADING_HALT
  MARKET_WIDE_CIRCUIT
  EXCHANGE_CLOSED
  UNKNOWN
expiry_relation
  NON_EXPIRY
  WEEKLY_EXPIRY
  MONTHLY_EXPIRY
  POST_EXPIRY_SESSION
  ROLL_WINDOW
  UNKNOWN
  NOT_APPLICABLE
availability
quality
reason_codes[]
context_hash
```

BUILD-2 remains calendar/contract identity owner where applicable. No weekday-memory expiry rules.

This enables causal combinations such as pre-result+IV-rank, post-result+IV-change, MPC+VIX change, budget+surface change and expiry+gamma concentration without making those combinations commands.

### 73.7 Opening-quality / RVOL context

The dedicated B4 plan must bind same-time-bucket RVOL and first-bar quality because the cross-plans preserve first-bar anomaly and RVOL research.

Candidate composition:

```text
OrbOpeningQualityContextV1
instrument_identity
session_id
formation_policy_id
bar_identity
bar_open_time
bar_close_time
decision_as_of
bar_range
bar_volume
bar_trade_count_if_available
bar_value_if_available
same_time_bucket_id
baseline_window_sessions
baseline_cutoff
baseline_universe_version
baseline_range_stat
baseline_volume_stat
baseline_value_stat_if_available
baseline_sample_count
baseline_independent_session_count
range_ratio
volume_ratio
volume_zscore_if_defined
value_ratio_if_defined
rvol
preopen_print_overlap_state
missing_volume_state
zero_volume_observed
opening_quality_state
source_fact_ids[]
calculation_version
availability
quality
context_hash
```

The baseline excludes current/future sessions. Zero observed volume != unavailable volume. Historical thresholds such as z>4, range>2x, RVOL>=1.5 or RVOL<1.0 remain research candidates.

### 73.8 News shock and microstructure

Observed volatility/price shock may exist without an attributed news cause. Without a PIT news source, `NEWS_CAUSE=UNKNOWN/UNAVAILABLE`.

Order-book/depth/microprice/queue imbalance remain `OPTIONAL_RESEARCH_CANDIDATE / NEEDS_EXTERNAL_FEED`; never simulate them from OHLCV and call them observed.

Universe/tradeability facts such as F&O ban, ASM/GSM/T2T, price band, liquidity and spread remain BUILD-1/upstream-owned and are only consumed by B4.

---

# 74. Exact connection map for the reconciled capabilities

| Capability | Canonical producer/owner | B4 seam | Purpose | Must not do |
|---|---|---|---|---|
| source readiness | BUILD-0 | B4-A consumes | honest source state | create second readiness enum |
| instrument/contract/expiry | BUILD-2 | B4-B/C/D/E/F consume | exact identity | infer from symbol/weekday |
| D-1 close/settlement | BUILD-3 | B4-B/F consume | causal baseline | daily-resample substitute |
| price/ATR/levels/VWAP | M3.1 | B4-F consumes | normalize/location | duplicate calculations |
| index/sector/breadth | M3.2 | B4-F composes | wider-market context | parallel generic owner |
| memory/analogues | M3.3 | B4-F bounded challenger | historical comparison | fabricate memory |
| five-state OI | B4-B | futures calculator | participation relationship | infer participant identity |
| FII/participant | B4-B from B4-A | futures calculator | crowding/regime | use unpublished future report |
| PCR/OI walls | B4-C | option-chain calculator | positioning/concentration | support/resistance fact |
| VIX/IV/skew/term/Greeks | B4-D | volatility calculator | volatility state | hard-code old thresholds |
| gamma/GEX/max pain/EM | B4-E | advanced calculator | advanced derivatives context | infer dealer sign from OI |
| GIFT/pre-open | B4-F from B4-A | world composer | opening context | prediction |
| corporate-action gap | B4-F | world composer | distinguish mechanical gap | overwrite raw gap |
| event/expiry/status | BUILD-2 + B4-A | B4-F composer | temporal applicability | trade/exit command |
| RVOL/opening quality | canonical bars + PIT baseline | B4-F composer | opening participation quality | threshold as fact |
| proof | BUILD-8 | outside B4 | incremental value | B4 self-promotion |
| calibrated probability | BUILD-12 | outside B4 | calibrated event/horizon probability | B4 raw confidence |
| final band | D6 | outside B4 | sole arbitration | B4 override |

Preferred bounded package remains:

```text
apps/api/app/orb/context_intelligence/
    __init__.py
    contracts.py
    sources.py
    futures.py
    option_chain.py
    volatility.py
    advanced.py
    world.py
    hypotheses.py
```

Do not add provider-specific network adapters until a source is approved.

---

# 75. Archived 50-row decision-table coverage map

This table freezes ownership only. Historical thresholds/actions remain research candidates.

| # | Historical condition | Fact owner / B4 responsibility | Policy/proof owner |
|---:|---|---|---|
| 1 | VIX coma | B4-D VIX fact | B7/B8/B10 |
| 2 | VIX normal | B4-D VIX fact | B7/B8/B10 |
| 3 | VIX elevated | B4-D VIX fact | B7/B8/B10 |
| 4 | VIX high | B4-D VIX fact | B7/B8/B10 |
| 5 | VIX kill zone | B4-D VIX fact | B7/B8/B10 |
| 6 | VIX crisis | B4-D VIX fact | B7/B8/B10 |
| 7 | delta-VIX shock | B4-D current+baseline | B7/B8/B10 |
| 8 | OR too wide | registered OR + M3.1 ATR; B4 composes | B5/B7/B8 |
| 9 | OR wide | registered OR + M3.1 ATR; B4 composes | B5/B7/B8 |
| 10 | OR normal | registered OR + M3.1 ATR; B4 composes | B5/B7/B8 |
| 11 | OR narrow | registered OR + M3.1 ATR; B4 composes | B5/B7/B8 |
| 12 | compression | M3.1/B4 world | B7/B8 |
| 13 | first-bar anomaly | B4-F opening-quality fact | B5/B7/B8 |
| 14 | OR straddles PDC | BUILD-3 PDC + registered OR | B6/B7/B8 |
| 15 | gap extreme | B4-F gap facts | B7/B8 |
| 16 | gap moderate | B4-F gap facts | B7/B8 |
| 17 | flat open | B4-F gap facts | B7/B8 |
| 18 | GIFT/open divergence | B4-F fact | B7/B8 |
| 19 | index gap extreme | B4-F GIFT/index fact | B7/B8 |
| 20 | ex-dividend | B4-A action + adjusted gap | B7/B8 |
| 21 | Nifty aligned | M3.2 + B4-F relationship | B7/B8 |
| 22 | Nifty conflict | M3.2 + B4-F relationship | B7/B8 |
| 23 | Nifty mid-range | M3.2 + canonical OR/VWAP | B7/B8 |
| 24 | sector divergence | M3.2 + B4-F relationship | B7/B8 |
| 25 | volume pass | B4-F RVOL fact | B7/B8 |
| 26 | volume fail | B4-F RVOL fact | B7/B8 |
| 27 | climax/no follow-through | causal bars/volume exposed to B4 | B6/B7/B13 |
| 28 | post-break dry-up | causal bars/volume exposed to B4 | B6/B7/B13 |
| 29 | early signal | BUILD-2 session + B6 signal time | B5/B6/B7 |
| 30 | prime window | BUILD-2 session + B6 signal time | B5/B6/B7 |
| 31 | late window | BUILD-2 session + B6 signal time | B5/B6/B7 |
| 32 | past morning cutoff | BUILD-2 session + B6 signal time | B5/B6/B7 |
| 33 | time stop | BUILD-2 session clock; no B4 exit authority | B7/B13 |
| 34 | result day | B4-F event temporal fact | B7/B8 |
| 35 | result D-1 | B4-F event temporal fact | B7/B8 |
| 36 | RBI/MPC | B4-F event temporal fact | B7/B8 |
| 37 | Budget/election | B4-F event temporal fact | B7/B8 |
| 38 | weekly expiry | BUILD-2 expiry + B4-F relation | B7/B8 |
| 39 | monthly stock expiry | BUILD-2 expiry + B4-F relation | B7/B8 |
| 40 | PCR extreme | B4-C PCR fact | B7/B8 |
| 41 | max-pain proximity | B4-E reference | B7/B8 |
| 42 | OI wall at target | B4-C wall/distance fact | B7/B8/B10 |
| 43 | basis extreme | B4-B adjusted basis | B7/B8 |
| 44 | FII crowding | B4-B participant fact | B7/B8 |
| 45 | F&O ban | BUILD-1; B4 consumes | B1/B6/D6 policy |
| 46 | ASM/GSM/T2T | BUILD-1; B4 consumes | B1/B6/D6 policy |
| 47 | narrow circuit band | BUILD-1/2; B4 consumes | B1/B6/D6 policy |
| 48 | illiquidity | BUILD-1 liquidity/spread; B4 consumes | B1/B7/D6 policy |
| 49 | chop signature | canonical failed-break/structure events; B4 composes | B6/B7/B8 |
| 50 | edge decay/sample | B8/B13; no B4 ownership | B8/B13/B10 |

Law:

```text
FACT PRESENT != RULE PROVEN
RULE PRESERVED != RULE ACTIVE
ACTION TEXT != BUILD-4 AUTHORITY
```

---

# 76. Restored Top-10 coverage

| Rank | Historical addition | Canonical BUILD-4 seam |
|---:|---|---|
| 1 | event-calendar gate | B4-A source + B4-F event facts; policy downstream |
| 2 | universe hygiene | BUILD-1 owner; B4 consumes |
| 3 | session VWAP + side veto | M3.1 VWAP + B4-F relation; veto downstream |
| 4 | ex-dividend gap adjustment | B4-A corporate action + B4-F adjusted gap |
| 5 | Nifty alignment | M3.2 + B4-F relation |
| 6 | VIX-scaled buffers | B4-D VIX fact; buffer policy downstream |
| 7 | conditional re-entry | B6/B7; B4 context only |
| 8 | OI-wall capping + expiry pinning | B4-C/E facts; cap/pin policy downstream |
| 9 | RVOL filter | canonical volume + B4-F RVOL fact |
| 10 | expectancy monitor + multiple-testing hygiene | B8/B13; no B4 self-promotion |

---

# 77. Source-readiness additions

Default planning state until separately proven:

| Capability/source | Planning readiness |
|---|---|
| India VIX intraday | NEEDS_EXTERNAL_FEED |
| GIFT Nifty | NEEDS_EXTERNAL_FEED |
| current option chain | NEEDS_EXTERNAL_FEED |
| historical intraday option chain | NEEDS_EXTERNAL_FEED |
| FII/participant EOD report | NEEDS_VERSIONED_FILE unless stronger approved feed |
| same-session participant positioning | UNAVAILABLE unless independently proven |
| pre-open auction current | NEEDS_EXTERNAL_FEED |
| historical pre-open auction | NEEDS_VERSIONED_FILE or NEEDS_EXTERNAL_FEED |
| breadth | NEEDS_EXTERNAL_FEED unless approved M3.2 source already active |
| corporate actions/dividends | NEEDS_VERSIONED_FILE unless approved PIT feed |
| event/results calendar | NEEDS_VERSIONED_FILE or approved feed |
| PIT news | NEEDS_EXTERNAL_FEED |
| order book/depth | NEEDS_EXTERNAL_FEED / optional challenger |
| OI/PCR/wall calculators | COMPUTABLE_LOCAL only after causal source admission |
| VIX/IV/skew/term changes | COMPUTABLE_LOCAL only after causal current+baseline admission |
| gamma wall/max pain/expected move | COMPUTABLE_LOCAL only with required chain/model inputs |

No row above activates a real source by this documentation commit.

---

# 78. Additional B4-LOCK tests

Add to Sections 41-50:

### Source/baseline/PIT
- current and baseline snapshots both satisfy available_at <= decision_as_of;
- contract/expiry/strike-universe mismatch rejects dynamic comparisons;
- EOD participant report cannot appear intraday before publication;
- current webpage/API cannot impersonate historical PIT data;
- comparable source disagreement yields CONFLICT, not averaging;
- later EOD reconciliation cannot rewrite AS_KNOWN_THEN.

### Futures/participant
- all four directional price/OI combinations plus flat/ambiguous;
- roll mismatch rejection;
- zero OI != unavailable;
- FII report timing and index-vs-stock applicability;
- raw and adjusted basis both preserved.

### Option chain/walls
- OI_PCR/change-OI-PCR/volume-PCR remain distinct;
- PCR change requires matching PCR type/scope;
- partial chain degrades wall/surface quality;
- wall created/persisting/strengthening/weakening/shifted/removed/unknown;
- missing current chain cannot create REMOVED;
- deterministic wall tie policy.

### Volatility/Greeks
- delta VIX baseline identity;
- IV change/crush current/reference comparability;
- raw term ordering separate from threshold inversion;
- skew/term/ATM-IV dynamic comparisons;
- Vanna/Charm source/model/unit identity;
- unstable/non-finite higher-order Greek remains error/unavailable.

### Advanced derivatives
- gamma wall distinct from OI wall;
- dealer-signed GEX unavailable without explicit sign model;
- zero gamma unavailable without signed exposure/root method;
- max pain remains reference, not magnet fact;
- expected-move method identity preserved.

### Broader context
- stale GIFT degrades/invalidates by source policy;
- GIFT remains context, not predictive output;
- pre-open IEP/IEQ field-level missingness;
- current pre-open page cannot reconstruct historical auction state;
- breadth universe/version participates in identity/hash;
- index/sector/breadth descendants sharing ancestry do not multiply votes;
- raw gap remains preserved beside corporate-action-adjusted gap;
- future corporate-action knowledge excluded;
- event scheduled vs result available distinguished;
- weekly/monthly/post-expiry uses BUILD-2 calendar identity;
- weekday-memory expiry inference rejected;
- same-time RVOL baseline excludes current/future session;
- zero observed volume distinct from unavailable volume;
- first-bar anomaly thresholds are absent from fact calculator.

### Coverage/authority
- all 50 archived rows have owner/disposition;
- all Top-10 items have owner/disposition;
- no B4 fact/action sets final band;
- no threshold promoted merely by this reconciliation;
- no real source promoted merely by this reconciliation;
- feature OFF/shadow migration preserves legacy behavior.

---

# 79. Implementation priority after reconciliation

P0 - reconcile existing/project-required semantics first:

1. five-state OI;
2. FII/participant positioning;
3. GIFT context;
4. delta VIX;
5. ATM-IV change/crush;
6. raw term ordering;
7. Vanna/Charm;
8. adjusted basis;
9. PCR change;
10. GIFT/open divergence;
11. corporate-action adjusted gap;
12. source-integrity receipt;
13. explicit readiness rows;
14. shadow mapping from adaptive derivatives.

P1 - high-value missing ORB context contracts:

1. typed call/put OI walls;
2. wall lifecycle/movement;
3. gamma walls;
4. option-chain quality;
5. breadth composition;
6. pre-open auction;
7. dynamic IV/skew/term/expected-move;
8. index/sector relationships;
9. event temporal state;
10. same-time RVOL/opening quality;
11. dependency-family wiring.

P2 - challengers only:

- Vomma/Volga;
- IV-vs-realized-volatility;
- richer options-flow features;
- order-book/depth/microprice;
- wider cross-asset macro features;
- additional higher-order Greeks.

P2 does not block B4 CODE GREEN unless a newer canonical source promotes one.

---

# 80. Completion-receipt extension

Append these fields to the existing B4-LOCK receipt:

```text
APPEND_ONLY_RECONCILIATION_RESULT
AUDITED_PRE_APPEND_HEAD
AUDITED_PRE_APPEND_BLOB
AUDITED_PRE_APPEND_LINE_COUNT
EXISTING_LINE_DELETIONS
EXISTING_LINE_MODIFICATIONS
LEGACY_ADAPTIVE_RECONCILIATION_RESULT
LEGACY_THRESHOLD_PROMOTION_COUNT
FIVE_STATE_OI_RESULT
PARTICIPANT_POSITIONING_RESULT
GIFT_CONTEXT_RESULT
PREOPEN_CONTEXT_RESULT
BREADTH_OWNER_RESULT
CORPORATE_ACTION_GAP_RESULT
EVENT_TEMPORAL_RESULT
OPENING_QUALITY_RVOL_RESULT
SOURCE_INTEGRITY_RESULT
OI_WALL_RESULT
OI_WALL_LIFECYCLE_RESULT
GAMMA_WALL_RESULT
GAMMA_SIGN_MODEL_BOUNDARY_RESULT
DELTA_VIX_RESULT
IV_CHANGE_CRUSH_RESULT
TERM_STRUCTURE_THRESHOLD_SEPARATION_RESULT
DYNAMIC_VOL_SURFACE_RESULT
VANNA_CHARM_RESULT
PCR_CHANGE_RESULT
CHAIN_QUALITY_RESULT
INDEX_SECTOR_COMPOSITION_RESULT
SOURCE_PUBLICATION_TIMING_RESULT
SOURCE_HISTORICAL_PIT_RESULT
DECISION_TABLE_50_ROW_COVERAGE
TOP10_COVERAGE
DEPENDENCY_FAMILY_NO_DOUBLE_COUNT_RESULT
OPTIONAL_P2_FEATURES_ACTIVATED
REAL_SOURCE_ACTIVATION_PER_CAPABILITY
```

For this documentation-only append:

```text
EXISTING_LINE_DELETIONS = 0
EXISTING_LINE_MODIFICATIONS = 0
LEGACY_THRESHOLD_PROMOTION_COUNT = 0
RUNTIME_CODE_CHANGED = NO
REAL_SOURCE_ACTIVATED = NO
TRADING_AUTHORITY_CHANGED = NO
```

Final reconciliation principle:

```text
MORE DATA DOES NOT CREATE MORE AUTHORITY.
MORE FEATURES DO NOT CREATE MORE INDEPENDENT EVIDENCE.
A SOURCE THAT EXISTS IS NOT AUTOMATICALLY PIT-READY.
A LEGACY CALCULATION THAT EXISTS IS NOT AUTOMATICALLY CANONICAL.
A THRESHOLD THAT WAS ONCE USED IS NOT AUTOMATICALLY PROVEN.
MISSING IS NOT NEUTRAL.
UNKNOWN IS NOT FALSE.
UNAVAILABLE IS NOT SAFE.
RECONSTRUCTED IS NOT OBSERVED.
CORRELATED EVIDENCE IS NOT INDEPENDENT EVIDENCE.
B4 DESCRIBES AND REASONS; B8 PROVES; B12 CALIBRATES; D6 DECIDES.
```
