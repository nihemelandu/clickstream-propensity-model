# Customer Purchase Intent

**Live dashboard: https://clickstream-propensity.streamlit.app**

> Given what a customer has done so far in a shopping session, how likely is that session to end in a purchase?

## The problem

An e-commerce store sees millions of sessions, and most end without a purchase. Marketing can only spend on some of them: a discount, a reminder, a retargeting ad. Spending on every session wastes money, and spending on the wrong ones misses buyers.

To choose, marketing needs a score for each session that says how likely it is to convert, computed from the behavior seen so far.

**This project asks:** can clickstream behavior alone produce a session-level purchase probability good enough to rank sessions and decide where to spend?

## Why it matters

- **Spend is limited.** About 87% of sessions end without a purchase. Treating them all alike is expensive.
- **Errors are costly in both directions.** Targeting low-likelihood sessions wastes budget; ignoring high-likelihood ones loses revenue.
- **Ranking is what the decision needs.** Marketing has to choose which sessions come first, so the useful output is a well-ordered probability score, not a yes/no label.

## Approach

Binary classification at the session level: purchase or no purchase. The project follows Tokuç and Dağ (2025), which compares how a session is represented to the model. Three representations were compared:

- **Aggregated:** one row per session, summarizing the whole session (event counts, duration, average price, start time, day of week).
- **Last n actions:** the most recent n actions, each described by its event type, product details and time since the previous event.
- **Hybrid:** the aggregated row joined with the last n actions. **Hybrid-1A** uses the single most recent action; Hybrid-5A uses the last five.

The best model is LightGBM on Hybrid-1A. Features are selected with particle swarm optimization (PSO) and hyperparameters tuned with a Tree-structured Parzen Estimator (TPE).

## Result

**LightGBM on Hybrid-1A reaches an AUC-PR of 0.9337 and an AUC-ROC of 0.9865 on held-out sessions. LightGBM on the aggregated representation alone reaches 0.86 and 0.97, and logistic regression on it reaches 0.53 and 0.88.**

| Model | Representation | AUC-PR | AUC-ROC |
|---|---|---|---|
| **LightGBM** | **Hybrid-1A** | **0.9337** | **0.9865** |
| LightGBM | Hybrid-5A | 0.9319 | 0.9861 |
| Gradient boosting | Hybrid-1A | 0.9192 | 0.9822 |
| LightGBM | Last action only | 0.9167 | 0.9820 |
| LightGBM | Aggregated | 0.86 | 0.97 |
| Logistic regression | Aggregated | 0.53 | 0.88 |

The best model's log loss is 0.1405. At the chosen threshold [TODO: state it], recall is 0.9340 and precision is 0.8091 (F1 about 0.87).

AUC-PR is the area under the precision-recall curve. AUC-ROC is the chance that a randomly chosen buyer is scored above a randomly chosen non-buyer.

Success targets, set before the runs: 

## How we tested it

- **Data:** 233,080,156 events from the REES46 eCommerce dataset, aggregated into 23,163,026 sessions, of which 2,963,560 (12.79%) end in a purchase.
- **Preparation:** duplicates and 2,990 bot-like sessions were removed. Purchase events and everything after them were dropped from each session, as were the last three page views. Sessions with fewer than three page views were excluded, and sessions longer than 100 page views were truncated at 100. [TODO: confirm your pipeline matches these steps.] The score therefore applies to sessions with at least three page views.
- **Split:** a random stratified 90/10 split by session, giving 20,843,007 training and 2,317,258 test sessions with the same purchase rate in both.
- **Class imbalance:** LightGBM trains on the full imbalanced training set with class weighting. The other models train on a balanced, undersampled set. All models are scored on the full, unbalanced test set.
- **Tuning:** PSO feature selection (10 particles, 50 iterations, AUC as fitness) and TPE hyperparameter search (50 trials, validation AUC-ROC). [TODO: state how the validation set was created and confirm the test set was never used for selection or tuning.]
- **Evaluation:** one split, no cross-validation. The test set holds 2.3M sessions.

## Top features

| Rank | Feature | Importance |
|---|---|---|
| 1 | Time since last action | 20.1% |
| 2 | Session duration so far | 16.3% |
| 3 | Event count so far | 14.2% |
| 4 | Session start time | 11.8% |
| 5 | Product price | 9.7% |

Importance shows what the model relies on, not how customers respond if a feature changes. [TODO: link or list the full feature set.]

## Customer segments

**Purpose.** Marketing cannot act on every session, and about 87% of sessions end without a purchase whatever is done. This section answers one question: **which sessions should marketing tentatively prioritize, and what does each score band justify doing?**

| Band | Score | Sessions | Share of sessions | Conversion rate | Share of all buyers | What it justifies |
|---|---|---|---|---|---|---|
| High intent | > 0.7 | 287,432 | 12.4% | 84.7% | 54.8% | Low-cost support only, such as a frictionless checkout. Likely to buy anyway, so avoid discounts. |
| Medium intent | 0.3 to 0.7 | 489,651 | 21.1% | 31.2% | 34.4% | Light nudges, such as a cart reminder or small incentive. The most plausible place for an intervention to change the outcome. |
| Low intent | < 0.3 | 1,540,175 | 66.5% | 3.1% | 10.8% | No spend, or the cheapest touch. |

Computed from the model's scores on the held-out 10% test set (2,317,258 sessions). Thresholds of 0.7 and 0.3 were [TODO: chosen in advance / tuned on validation data].

Conversion rate shows who is likely to buy, not who is persuadable. A high-intent session may buy with or without an intervention, so the actions above are proposals to test, not measured effects of marketing.

## Limits of these results

- The score estimates the likelihood of a purchase. It does not measure the effect of any marketing action. Whether a nudge changes the outcome is an uplift question this project does not answer.
- Results come from one retailer's data, October 2019 to April 2020.
- The score applies only to sessions with at least three page views, and it is computed with the purchase and the last three page views removed. [TODO: state what that means for live use.]
- No business-impact figures (cost per acquisition, revenue per session) are reported, because no campaign was run.

## Where this departs from the paper

The approach replicates and extends Tokuç and Dağ (2025). [TODO: list each extension, such as the dashboard and the segmentation, and compare your numbers with the paper's.]

## Repository

```
dashboard/   Streamlit dashboard, one folder per sprint
docs/        Business and data understanding notes
notebooks/   Exploration, one folder per sprint
src/         Preprocessing, features, model training and inference
models/      Trained model artifacts and metrics.json
data/        Raw and processed data (not tracked in Git)
```

## Data

| Attribute | Detail |
|---|---|
| Source | [eCommerce Behavior Data from Multi-Category Store](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store) |
| Publisher | REES46 |
| Period | October 2019 to April 2020 |
| Raw events | 233,080,156 (after removing duplicates and invalid rows) |
| Sessions analyzed | 23,163,026 |
| Purchase sessions | 2,963,560 (12.79%) |
| Event types | view, add-to-cart, purchase |

Raw data is not tracked in this repository. Download it from the Kaggle link above and place it in `data/raw/`.

## Run it

Requires Python 3.12+.

```bash
git clone https://github.com/nihemelandu/clickstream-propensity-model.git
cd clickstream-propensity-model
pip install -r requirements.txt
# TODO: preprocessing command
# TODO: training command, with seed and expected runtime
cd dashboard/sprint_1
streamlit run app.py
```

## Tools

Python 3.12, Pandas, Dask, LightGBM, Scikit-learn, PySwarms, Hyperopt, MLflow, Streamlit, Plotly. [TODO: remove MLflow, or add a line showing how experiments were tracked.]

## How the work is run

CRISP-DM in Agile sprints. Tasks are tracked on the [GitHub Project board](https://github.com/nihemelandu/clickstream-propensity-model/projects), with one [milestone](https://github.com/nihemelandu/clickstream-propensity-model/milestones) per sprint.

## Reference

Tokuç, A. A., & Dağ, T. (2025). Predicting user purchases from clickstream data: A comparative analysis of clickstream data representations and machine learning models. *IEEE Access*, 13, 43796–43817. https://doi.org/10.1109/ACCESS.2025.3548267

## License
