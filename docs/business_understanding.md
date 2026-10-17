# Business Understanding
**Project:** Clickstream Purchase Propensity Model  
**Sprint:** 1  
**Last Updated:** October 2026  
**Status:** In Progress  

---

## 1. What Is the Problem?

E-commerce platforms generate enormous volumes of customer interaction data,
but the vast majority of sessions do not result in a purchase. Without a way
to distinguish high-intent customers from casual browsers, businesses are
forced into one of two costly positions:

- **Treating everyone the same** — wasting marketing resources on customers
  who were never going to buy, while potentially missing customers who needed
  only a small nudge to convert
- **Acting on intuition or simple rules** — segmenting customers by crude
  criteria like recency or spend history, which are lagging indicators that
  miss real-time purchase intent signals

The result is inefficient resource allocation, missed conversion
opportunities, and marketing interventions that are poorly timed, poorly
targeted, and poorly personalized.

---

## 2. How Do We Translate the Business Problem Into a Technical Formulation?

**Business question:**
Who is most likely to buy?

**Technical formulation:**
Given the clickstream behavior of a customer during a session, predict the
probability that the session will result in a purchase.

| Element | Definition |
|---|---|
| Unit of prediction | Session |
| Input | Session-level clickstream events — views, cart additions, time between actions, session duration, user history |
| Output | Propensity score between 0 and 1 representing purchase probability |
| Model type | Binary classification — purchase (1) vs no purchase (0) |
| Key challenge | Severe class imbalance — only 5.85% of sessions result in a purchase |
| Reference methodology | Tokuç & Dağ (2025) — hybrid data representation with LightGBM |

---

## 3. What Business Metrics Will We Monitor?

| Business Metric | Description | Expected Direction |
|---|---|---|
| Conversion Rate | Percentage of sessions resulting in a purchase | Increase |
| Revenue Per Session | Average revenue generated per customer session | Increase |
| Campaign ROI / ROAS | Revenue generated per dollar of marketing spend | Increase |
| Cost Per Acquisition | Marketing cost to acquire one converting customer | Decrease |
| Segment Conversion Rate Differential | Actual conversion rate per propensity tier | High tier >> Medium tier >> Low tier |
| Cart Abandonment Recovery Rate | Percentage of abandoned carts recovered | Increase |

---

## 4. What Does Technical Success Look Like?

| Model Metric | Why It Matters |
|---|---|
| AUC-PR (Primary) | Measures model performance on the rare positive class — most important given class imbalance |
| AUC-ROC (Primary) | Measures overall ability to discriminate buyers from non-buyers |
| Log Loss (Calibration) | Measures whether probability estimates are trustworthy enough to rank and segment customers |
| F1-Score | Balances precision and recall — important when both false positives and false negatives have costs |
| Geometric Mean | Balances performance across both classes under imbalance |
| Precision | Of sessions predicted as purchases, how many actually purchased |
| Recall | Of sessions that actually purchased, how many did the model identify |

---

## 5. How Do Model Metrics Map to Business Context?

| Model Metric | Plain English | Business Implication |
|---|---|---|
| AUC-ROC | How reliably we separate buyers from browsers | Higher = smarter targeting |
| AUC-PR | How good we are at finding rare buyers | Higher = fewer missed conversions |
| Log Loss | Can we trust the probability scores | Lower = more reliable segmentation |
| Precision | When we predict a buyer, how often we are right | Drives marketing efficiency |
| Recall | Of all actual buyers, how many we correctly identified | Drives missed revenue risk |
| Propensity Score Distribution | How purchase intent is spread across the customer base | Informs segment sizing and resource allocation |

**Key business insight:**
The cost of a false negative — marking a high propensity customer as low — 
is greater than the cost of a false positive — marking a low propensity 
customer as high. This means recall is a more business-critical metric than 
precision in most e-commerce contexts, and threshold selection should reflect 
this asymmetry.

---

## 6. What Resources Are Available? Which Tools and Techniques Will We Use?

### Data
| Item | Detail |
|---|---|
| Dataset | eCommerce Behavior Data from Multi-Category Store |
| Source | REES46 / Kaggle |
| Date Range | October 2019 to April 2020 |
| Raw Events | 233 million records |
| Events | view, add-to-cart, purchase |

### Compute
| Item | Detail |
|---|---|
| Environment | Local machine |
| Processor | Intel Core 5 120U |
| Cores | 6 |
| RAM | 16GB |
| Cloud Compute | Not available at this stage |

### Tools and Techniques
| Category | Tool / Technique |
|---|---|
| Language | Python |
| Data Processing | Pandas, PySpark |
| Modeling | LightGBM, Scikit-learn |
| Feature Selection | PySwarms (PSO) |
| Hyperparameter Tuning | Hyperopt (TPE) |
| Experiment Tracking | MLflow |
| Dashboard | Streamlit + Plotly |
| Version Control | Git + GitHub |
| Project Management | GitHub Projects + Issues |
| Methodology | CRISP-DM + Agile Sprints + MLOps |

---

## 7. What Is the Expected Return or ROI?

Industry evidence for purchase propensity models in e-commerce:

| Scenario | Conversion Lift | Business Impact |
|---|---|---|
| Conservative | 1.5x on high-propensity segment | Positive — modest targeting improvement justifies open-source tooling cost |
| Moderate | 2.5x on high-propensity segment | Strongly positive — aligns with documented industry benchmarks |
| Optimistic | 3x to 10x on targeted campaigns | Very strongly positive — consistent with documented case studies |

**ROI Formula:**
(Reach of users × incremental conversion lift × average order value) — development cost = expected ROI

---

## 8. What Is the Anticipated Cost?

| Cost Category | Detail |
|---|---|
| Development | Data scientist time across sprints |
| Tooling | Zero — all open source (Python, LightGBM, Streamlit, MLflow, GitHub) |
| Infrastructure | Zero at this stage — local machine only |
| Ongoing | Model monitoring and retraining — data scientist time |
| Future Cloud Deployment | To be quantified in Phase 7 — Deployment |

---

## 9. Cost-Benefit Analysis

**The question:**
Does the expected return of solving this prediction problem outweigh the 
cost of development and deployment?

**The answer:**
Yes — the cost-benefit case is positive across all three scenarios. The case
is strongest when framed not just as revenue uplift but as waste reduction —
money currently spent targeting non-buyers that could be redirected to
high-intent customers.

The tooling cost is zero — all open source. The primary cost is data 
scientist time. Even a conservative 1.5x conversion lift on the 
high-propensity segment generates measurable return that exceeds 
development cost.

---

## 10. Project Constraints

### Interpretability
| Requirement | Detail |
|---|---|
| Audience | Both data scientists and business stakeholders |
| Model level | Feature importance scores required |
| Prediction level | Individual prediction explanations required — SHAP values (future sprint) |

### Compute
| Constraint | Detail |
|---|---|
| Training environment | Local machine — Intel Core 5 120U, 6 cores, 16GB RAM |
| Cloud compute | Not available at this stage |
| Memory management | Critical — dataset is 233 million raw rows |
| Model selection | LightGBM — computationally efficient for available hardware |

### Time
| Constraint | Detail |
|---|---|
| Sprint 1 deliverable | Next-day turnaround |
| Production scoring | Batch overnight — real-time scoring deferred to future sprint |

---

## 11. Actionable Customer Segments

*To be defined and documented upon completion of issue #3.*

---

## Reference
- Tokuç, A. A. & Dağ, T. (2025). Predicting User Purchases From Clickstream
  Data: A Comparative Analysis of Clickstream Data Representations and
  Machine Learning Models. IEEE Access, Vol. 13, pp. 43796–43817.
  DOI: 10.1109/ACCESS.2025.3548267
- CRISP-DM Framework — Phase 1: Business Understanding
