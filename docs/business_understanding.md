
# Business Understanding

## Business Problem
E-commerce platforms generate enormous volumes of customer interaction data,
but the vast majority of sessions do not result in a purchase. Without a way
to distinguish high-intent customers from casual browsers, businesses are forced
into one of two costly positions:

- Treating everyone the same — wasting marketing resources on customers who
  were never going to buy, while potentially missing customers who needed only
  a small nudge to convert
- Acting on intuition or simple rules — segmenting customers by crude criteria
  like recency or spend history, which are lagging indicators that miss
  real-time purchase intent signals

The result is inefficient resource allocation, missed conversion opportunities,
and marketing interventions that are poorly timed, poorly targeted, and poorly
personalized.

## Analytical Question
Given a customer's clickstream behavior during a session, what is the
probability that this session will result in a purchase?

## The Propensity Model as Means to an End
The propensity model is not the deliverable — it is the enabling infrastructure.
The real deliverable is the downstream value it unlocks:

- **Ranking** — sorting customers by purchase intent so the business can
  prioritize who to target, when to intervene, and where to concentrate
  finite marketing resources
- **Segmentation** — grouping customers into behaviorally meaningful tiers
  that map to distinct business actions
- **Decision-making** — feeding reliable probability estimates into both
  real-time and strategic business decisions

## Success Metrics

### Technical Success
- Primary metrics: AUC-PR and AUC-ROC — chosen because of class imbalance
  where purchase events represent a small fraction of all sessions
- Calibration check: Log loss — ensures probability estimates are trustworthy
  enough to rank and segment customers meaningfully

### Business Success
| Metric | Description |
|---|---|
| Conversion Rate | More sessions end in a purchase due to better-targeted interventions |
| Revenue Per Session | Higher value conversions through propensity-driven targeting |
| Marketing Efficiency | Same budget generates more conversions — lower cost per conversion |
| Segment Conversion Rate Differential | High, medium, and low propensity tiers convert at meaningfully different rates |
| Cart Abandonment Recovery Rate | High-propensity sessions that have not checked out are identified and acted on |

## Primary Business Unit Users
- **Marketing** — campaign targeting, offer personalization, budget allocation
- **CRM** — real-time session interventions, post-session follow-up sequences
- **E-Commerce / Product** — on-site personalization, search result ranking
- **Supply Chain / Demand Planning** — aggregate propensity scores as leading demand indicators
- **Finance** — revenue forecasting, scenario planning

## Forms of Customer Interaction Data
- Clickstream data — primary input, sequential timestamped record of every session action
- Transactional data — provides the ground truth label (purchase or no purchase)
- Session-level metadata — aggregated session summaries derived from clickstream
- User profile data — longitudinal context across sessions
- Product interaction data — product-level signals embedded in the clickstream

## Project Constraints

### Interpretability
- Both data scientists and business stakeholders require model explanations
- Feature importance scores required at the model level
- Individual prediction explanations required at the customer level (SHAP values — future sprint)

### Compute
- Training environment: Local machine
- Hardware: Intel Core 5 120U, 6 cores, 16GB RAM
- No cloud compute budget at this stage
- LightGBM selected as primary model — computationally efficient for this hardware
- Memory management will be critical given the dataset size (233M raw rows)

### Time
- Sprint 1 deliverable: Next-day turnaround
- Production scoring: Batch overnight (real-time scoring deferred to future sprint)

## Actionable Customer Segments
To be defined in issue #3 — Define actionable customer segments

## Reference
- Tokuç, A. A. & Dağ, T. (2025). Predicting User Purchases From Clickstream Data:
  A Comparative Analysis of Clickstream Data Representations and Machine Learning
  Models. IEEE Access, Vol. 13, pp. 43796–43817. DOI: 10.1109/ACCESS.2025.3548267
- CRISP-DM Framework — Phase 1: Business Understanding
