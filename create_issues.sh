#!/bin/bash

REPO="nihemelandu/clickstream-propensity-model"

echo "Creating remaining issues..."

# ─── PHASE 2 — DATA UNDERSTANDING (remaining) ────────────────────────────────

gh issue create --repo $REPO \
  --title "Document session structure and behavioral signal sufficiency" \
  --body "## Description
Examine the distribution of events per session to confirm that sessions contain sufficient behavioral signal for modeling.

## Acceptance Criteria
- [ ] Distribution of events per session plotted
- [ ] Percentage of sessions with fewer than 3 events documented
- [ ] Percentage of sessions with more than 100 events documented
- [ ] Minimum viable session length justified with data

## Reference
Tokuç & Dağ (2025), Section III-D: Data Preprocessing" \
  --label "phase:data-understanding"

gh issue create --repo $REPO \
  --title "Document data quality issues — missing values and anomalies" \
  --body "## Description
Identify and document all data quality issues in the raw dataset that will need to be addressed in data preparation.

## Acceptance Criteria
- [ ] Missing values documented by column
- [ ] Anomalous sessions identified and characterized
- [ ] Data quality issues prioritized by severity
- [ ] Remediation approach proposed for each issue

## Reference
Tokuç & Dağ (2025), Table 6: Number of Empty Cells by Feature Name" \
  --label "phase:data-understanding"

# ─── PHASE 3 — EDA ───────────────────────────────────────────────────────────

gh issue create --repo $REPO \
  --title "Compute correlation matrix and document feature-purchase relationships" \
  --body "## Description
Compute pairwise correlations between all session-level features and the target variable has_purchase to identify which features carry signal and which do not.

## Acceptance Criteria
- [ ] Correlation matrix computed and visualized
- [ ] Correlation of each feature with has_purchase documented
- [ ] Multicollinearity between features identified and noted
- [ ] Key positive and negative predictors highlighted
- [ ] Implications for feature engineering documented

## Reference
Tokuç & Dağ (2025), Figure 2: Correlation Matrix" \
  --label "phase:eda"

gh issue create --repo $REPO \
  --title "Replicate Tokuç and Dağ EDA methodology transparently" \
  --body "## Description
Replicate the full EDA methodology from the reference paper, documenting every step, finding, and decision it informed.

## Acceptance Criteria
- [ ] Event type distribution replicated
- [ ] Session statistics replicated
- [ ] User statistics replicated
- [ ] Correlation matrix replicated
- [ ] All findings documented with implications for feature engineering
- [ ] Deviations from the paper noted and justified

## Reference
Tokuç & Dağ (2025), Section III-C: Exploratory Data Analysis" \
  --label "phase:eda"

gh issue create --repo $REPO \
  --title "Review and document Tokuç and Dağ feature importance analysis methodology" \
  --body "## Description
Closely examine how Tokuç and Dağ conducted their feature importance analysis — what they did, how transparently they documented it, and what we need to replicate.

## Acceptance Criteria
- [ ] Feature importance methodology documented for each model
- [ ] Top features identified per model and representation
- [ ] How importance scores were normalized documented
- [ ] Consistency of important features across models noted
- [ ] Gaps in their transparency identified and noted

## Reference
Tokuç & Dağ (2025), Section IV-D: Feature Importance Analysis
Tokuç & Dağ (2025), Figure 7: Normalized Feature Importance Scores" \
  --label "phase:eda"

# ─── PHASE 4 — DATA PREPARATION ──────────────────────────────────────────────

gh issue create --repo $REPO \
  --title "Remove duplicate records" \
  --body "## Description
Identify and remove duplicate event records from the raw dataset.

## Acceptance Criteria
- [ ] Duplicate records identified and counted
- [ ] Deduplication applied
- [ ] Row count before and after documented

## Reference
Tokuç & Dağ (2025), Section III-D-1: Data Cleaning and Validation" \
  --label "phase:data-preparation"

gh issue create --repo $REPO \
  --title "Remove sessions with missing or invalid data" \
  --body "## Description
Filter out sessions containing missing or invalid entries that would compromise model integrity.

## Acceptance Criteria
- [ ] Sessions with missing critical fields identified
- [ ] Invalid sessions removed
- [ ] Row count before and after documented

## Reference
Tokuç & Dağ (2025), Section III-D-1: Data Cleaning and Validation" \
  --label "phase:data-preparation"

gh issue create --repo $REPO \
  --title "Remove bot and anomalous sessions" \
  --body "## Description
Identify and remove sessions that are likely automated interactions rather than genuine user behavior.

## Acceptance Criteria
- [ ] Sessions with more than 1 event per second removed
- [ ] Sessions with more than 100 distinct products removed
- [ ] Sessions with suspiciously high event-to-product ratio removed
- [ ] Number of anomalous sessions removed documented

## Reference
Tokuç & Dağ (2025), Section III-D-1: Data Cleaning and Validation" \
  --label "phase:data-preparation"

gh issue create --repo $REPO \
  --title "Exclude category_code field" \
  --body "## Description
Remove the category_code field from the dataset as it is both incomplete and redundant given category_id.

## Acceptance Criteria
- [ ] category_code field excluded from all representations
- [ ] Confirmed that category_id fully captures categorical information
- [ ] No information loss documented

## Reference
Tokuç & Dağ (2025), Section III-D-1: Data Cleaning and Validation" \
  --label "phase:data-preparation"

gh issue create --repo $REPO \
  --title "Encode missing brand values as empty category" \
  --body "## Description
Handle missing brand values by encoding them as a distinct category labeled empty rather than imputing or dropping.

## Acceptance Criteria
- [ ] Missing brand values identified and counted
- [ ] Encoded as empty category
- [ ] Interpretability of the model preserved

## Reference
Tokuç & Dağ (2025), Section III-D-1: Data Cleaning and Validation" \
  --label "phase:data-preparation"

gh issue create --repo $REPO \
  --title "Remove post-purchase events within a session" \
  --body "## Description
Remove events that occurred after a purchase within the same session to prevent data leakage into the model.

## Acceptance Criteria
- [ ] Post-purchase events identified per session
- [ ] Events removed from dataset
- [ ] Data leakage risk confirmed eliminated

## Reference
Tokuç & Dağ (2025), Section III-D-2: Session-Level Data Refinement" \
  --label "phase:data-preparation"

gh issue create --repo $REPO \
  --title "Exclude last 3 page views per session" \
  --body "## Description
Remove the last 3 page views of each session to reduce noise and simulate a real-time prediction constraint.

## Acceptance Criteria
- [ ] Last 3 page views excluded from all sessions
- [ ] Real-time prediction constraint documented and justified
- [ ] Noise reduction rationale documented

## Reference
Tokuç & Dağ (2025), Section III-D-2: Session-Level Data Refinement" \
  --label "phase:data-preparation"

gh issue create --repo $REPO \
  --title "Remove sessions with fewer than 3 actions" \
  --body "## Description
Exclude sessions with fewer than 3 actions as they lack sufficient behavioral information to inform the predictive model.

## Acceptance Criteria
- [ ] Sessions with fewer than 3 actions identified and counted
- [ ] Sessions removed from dataset
- [ ] Impact on dataset size documented

## Reference
Tokuç & Dağ (2025), Section III-D-2: Session-Level Data Refinement" \
  --label "phase:data-preparation"

gh issue create --repo $REPO \
  --title "Truncate sessions with more than 100 page views" \
  --body "## Description
Truncate sessions exceeding 100 page views to standardize inputs and reduce computational overhead.

## Acceptance Criteria
- [ ] Sessions with more than 100 page views identified and counted
- [ ] Sessions truncated to 100 page views
- [ ] Impact on data quality documented

## Reference
Tokuç & Dağ (2025), Section III-D-2: Session-Level Data Refinement" \
  --label "phase:data-preparation"

gh issue create --repo $REPO \
  --title "Engineer temporal features — date, day_of_week, is_weekend" \
  --body "## Description
Derive temporal features from the event_time timestamp to capture the temporal dynamics of user behavior.

## Acceptance Criteria
- [ ] date feature derived from event_time
- [ ] day_of_week feature derived from event_time
- [ ] is_weekend binary feature derived from event_time
- [ ] Features validated against raw timestamps

## Reference
Tokuç & Dağ (2025), Section III-E: Feature Engineering, Table 9" \
  --label "phase:data-preparation"

gh issue create --repo $REPO \
  --title "Engineer session features — session_time_so_far, time_since_last_event, session_last_event_time" \
  --body "## Description
Engineer session-based temporal features that measure user engagement and interaction frequency within a session.

## Acceptance Criteria
- [ ] session_time_so_far computed per event
- [ ] time_since_last_event computed per event
- [ ] session_last_event_time computed per session
- [ ] Features validated for correctness

## Reference
Tokuç & Dağ (2025), Section III-E: Feature Engineering, Table 9" \
  --label "phase:data-preparation"

gh issue create --repo $REPO \
  --title "Engineer user features — user_type, has_purchase_so_far, session_count_so_far" \
  --body "## Description
Engineer user-specific features that track behavior and history across sessions over time.

## Acceptance Criteria
- [ ] user_type derived — new vs returning customer
- [ ] has_purchase_so_far computed per user per session
- [ ] session_count_so_far computed per user
- [ ] Features validated for correctness

## Reference
Tokuç & Dağ (2025), Section III-E: Feature Engineering, Table 9" \
  --label "phase:data-preparation"

gh issue create --repo $REPO \
  --title "Engineer aggregated session features and construct target variable" \
  --body "## Description
Engineer aggregated session-level features that summarize overall session behavior, and construct the binary target variable.

## Acceptance Criteria
- [ ] event_count computed per session
- [ ] view_count computed per session
- [ ] cart_count computed per session
- [ ] Distinct products, brands, categories computed per session
- [ ] Average price per event computed per session
- [ ] Binary purchase label constructed as target variable

## Reference
Tokuç & Dağ (2025), Section III-E: Feature Engineering, Table 9" \
  --label "phase:data-preparation"

# ─── PHASE 5 — MODELING ──────────────────────────────────────────────────────

gh issue create --repo $REPO \
  --title "Construct aggregated session representation" \
  --body "## Description
Build the aggregated data representation that condenses each session into a single row of summary statistics.

## Acceptance Criteria
- [ ] Each session represented as a single row
- [ ] All aggregated features included
- [ ] Dataset dimensions documented

## Reference
Tokuç & Dağ (2025), Section III-B-2: Aggregated Actions Per Session" \
  --label "phase:modeling"

gh issue create --repo $REPO \
  --title "Construct flattened last N actions representation — N=1, N=5, N=10" \
  --body "## Description
Build the flattened sequential representation capturing the most recent N actions per session for N=1, N=5, and N=10.

## Acceptance Criteria
- [ ] N=1 representation constructed
- [ ] N=5 representation constructed
- [ ] N=10 representation constructed
- [ ] Padding applied for sessions with fewer than N actions
- [ ] Dataset dimensions documented for each N

## Reference
Tokuç & Dağ (2025), Section III-B-1: Flattened Last N Actions Per Session" \
  --label "phase:modeling"

gh issue create --repo $REPO \
  --title "Construct hybrid representation" \
  --body "## Description
Build the hybrid representation by concatenating the aggregated session features with the flattened last N actions features.

## Acceptance Criteria
- [ ] Hybrid-1A representation constructed
- [ ] Hybrid-5A representation constructed
- [ ] Hybrid-10A representation constructed
- [ ] Dataset dimensions documented for each variant

## Reference
Tokuç & Dağ (2025), Section III-B-3: Hybrid Representation" \
  --label "phase:modeling"

gh issue create --repo $REPO \
  --title "Implement 90/10 stratified train-test split" \
  --body "## Description
Split the dataset into 90% training and 10% test sets using stratified sampling to maintain class distribution across both sets.

## Acceptance Criteria
- [ ] Stratified split implemented across all representations
- [ ] Class distribution confirmed consistent across train and test sets
- [ ] Train and test set sizes documented

## Reference
Tokuç & Dağ (2025), Section III-G: Train-Test Set Division, Table 10" \
  --label "phase:modeling"

gh issue create --repo $REPO \
  --title "Train baseline models across all three data representations" \
  --body "## Description
Train all six machine learning models across all data representations to establish baseline performance.

## Acceptance Criteria
- [ ] LightGBM trained across all representations
- [ ] Gradient Boosting trained across all representations
- [ ] Decision Tree trained across all representations
- [ ] Random Forest trained across all representations
- [ ] Logistic Regression trained across all representations
- [ ] Linear SVC trained across all representations
- [ ] All runs logged in MLflow

## Reference
Tokuç & Dağ (2025), Section III-H: Model Training" \
  --label "phase:modeling"

gh issue create --repo $REPO \
  --title "Implement PSO feature selection" \
  --body "## Description
Apply Particle Swarm Optimization to identify the most predictive subset of features for each data representation.

## Acceptance Criteria
- [ ] Binary PSO implemented using PySwarms
- [ ] AUC-ROC used as fitness function
- [ ] PSO run for each data representation
- [ ] Selected feature subsets documented per representation

## Reference
Tokuç & Dağ (2025), Section III-F: Feature Selection" \
  --label "phase:modeling"

gh issue create --repo $REPO \
  --title "Implement Bayesian hyperparameter optimization via TPE" \
  --body "## Description
Optimize hyperparameters for each model using the Tree-structured Parzen Estimator algorithm via the hyperopt package.

## Acceptance Criteria
- [ ] TPE implemented via hyperopt for all models
- [ ] Optimization run for 50 trials per model
- [ ] AUC-ROC used as objective function
- [ ] Best hyperparameters documented per model and representation

## Reference
Tokuç & Dağ (2025), Section III-H: Model Training, Table 11" \
  --label "phase:modeling"

gh issue create --repo $REPO \
  --title "Handle class imbalance across all models" \
  --body "## Description
Apply appropriate class imbalance handling strategies for each model type.

## Acceptance Criteria
- [ ] LightGBM class-weighted objective implemented
- [ ] Balanced subsampling applied for non-LightGBM models
- [ ] Impact of imbalance handling on performance documented

## Reference
Tokuç & Dağ (2025), Section III-G: Train-Test Set Division" \
  --label "phase:modeling"

gh issue create --repo $REPO \
  --title "Document hyperparameter search space and best values per model-representation combination" \
  --body "## Description
Record the hyperparameter search space and optimal values found for every model across every data representation.

## Acceptance Criteria
- [ ] Search space documented for each model
- [ ] Best hyperparameter values recorded per model-representation combination
- [ ] Results stored in MLflow model registry

## Reference
Tokuç & Dağ (2025), Appendix A: Table 11" \
  --label "phase:modeling"

# ─── PHASE 6 — EVALUATION ────────────────────────────────────────────────────

gh issue create --repo $REPO \
  --title "Compute AUC-ROC and AUC-PR across all model-representation combinations" \
  --body "## Description
Compute the primary evaluation metrics across every model and data representation combination.

## Acceptance Criteria
- [ ] AUC-ROC computed for all combinations
- [ ] AUC-PR computed for all combinations
- [ ] Results organized in a comparison table

## Reference
Tokuç & Dağ (2025), Section III-I: Model Evaluation" \
  --label "phase:evaluation"

gh issue create --repo $REPO \
  --title "Compute geometric mean, IBA, F1-score, precision, recall, and log loss" \
  --body "## Description
Compute the full suite of evaluation metrics to provide a comprehensive assessment of model performance under class imbalance.

## Acceptance Criteria
- [ ] Geometric mean computed for all combinations
- [ ] IBA computed for all combinations
- [ ] F1-score, precision, recall computed for all combinations
- [ ] Log loss computed as calibration check for all combinations

## Reference
Tokuç & Dağ (2025), Section III-I: Model Evaluation" \
  --label "phase:evaluation"

gh issue create --repo $REPO \
  --title "Generate confusion matrices and precision-recall curves" \
  --body "## Description
Generate visual diagnostic outputs for all model-representation combinations to assess classification behavior.

## Acceptance Criteria
- [ ] Confusion matrix generated for each combination
- [ ] Precision-recall curve generated for each combination
- [ ] True positive rate and false positive rate documented per combination

## Reference
Tokuç & Dağ (2025), Figure 3: Precision-Recall Curves
Tokuç & Dağ (2025), Figure 5: Confusion Matrix" \
  --label "phase:evaluation"

gh issue create --repo $REPO \
  --title "Produce performance heatmap across all model-representation combinations" \
  --body "## Description
Produce a comprehensive heatmap summarizing all performance metrics across every model and data representation combination.

## Acceptance Criteria
- [ ] Heatmap produced covering all model-representation combinations
- [ ] All key metrics included in the heatmap
- [ ] Best performing combination clearly identified

## Reference
Tokuç & Dağ (2025), Figure 4: Performance Metrics Heatmap" \
  --label "phase:evaluation"

gh issue create --repo $REPO \
  --title "Conduct feature importance analysis across all models and representations" \
  --body "## Description
Analyze and document which features drive purchase predictions across all models and data representations.

## Acceptance Criteria
- [ ] Feature importance computed for all tree-based models
- [ ] Importance scores normalized for comparability
- [ ] Top 10 features identified per model and representation
- [ ] Consistency of important features across models documented
- [ ] Business interpretation of top features documented

## Reference
Tokuç & Dağ (2025), Section IV-D: Feature Importance Analysis
Tokuç & Dağ (2025), Figure 7: Normalized Feature Importance Scores" \
  --label "phase:evaluation"

gh issue create --repo $REPO \
  --title "Assess score calibration — reliability diagram and Brier score" \
  --body "## Description
Assess whether the propensity scores produced by the model are well-calibrated — that the predicted probabilities reflect true purchase likelihood.

## Acceptance Criteria
- [ ] Reliability diagram produced for best performing model
- [ ] Brier score computed
- [ ] Calibration quality assessed and documented
- [ ] Recalibration need identified if necessary

## Reference
Technical success definition — log loss as calibration check" \
  --label "phase:evaluation"

gh issue create --repo $REPO \
  --title "Validate segment separation — conversion rate differential across propensity tiers" \
  --body "## Description
Confirm that the propensity score tiers produce meaningfully different actual conversion rates — validating that the segments are actionable.

## Acceptance Criteria
- [ ] Customers segmented into propensity tiers using defined thresholds
- [ ] Actual conversion rate computed per tier
- [ ] Conversion rate differential across tiers assessed
- [ ] Business actionability of segments confirmed

## Reference
Business success definition — segment conversion rate differential" \
  --label "phase:evaluation"

# ─── PHASE 7 — DEPLOYMENT / MLOPS ────────────────────────────────────────────

gh issue create --repo $REPO \
  --title "Define model serving approach" \
  --body "## Description
Define how the trained propensity model will be served to downstream consumers — marketing, CRM, demand planning.

## Acceptance Criteria
- [ ] Serving infrastructure defined — REST API, batch scoring, or both
- [ ] Latency requirements documented
- [ ] Integration points with downstream systems identified

## Reference
MLOps best practices" \
  --label "phase:deployment"

gh issue create --repo $REPO \
  --title "Define feature store requirements" \
  --body "## Description
Define the requirements for a feature store that ensures session and user features are computed consistently across training and inference.

## Acceptance Criteria
- [ ] Features requiring real-time computation identified
- [ ] Features that can be precomputed identified
- [ ] Feature store tooling evaluated and selected

## Reference
MLOps best practices" \
  --label "phase:deployment"

gh issue create --repo $REPO \
  --title "Define monitoring strategy — score drift, feature drift, performance degradation" \
  --body "## Description
Define how the deployed model will be monitored over time to detect degradation in score quality or input feature distributions.

## Acceptance Criteria
- [ ] Score distribution monitoring defined
- [ ] Feature drift detection approach defined
- [ ] Performance degradation thresholds defined
- [ ] Alerting mechanism defined

## Reference
MLOps best practices" \
  --label "phase:deployment"

gh issue create --repo $REPO \
  --title "Define retraining cadence and feedback loop" \
  --body "## Description
Define how and when the model will be retrained as new data becomes available and purchase outcomes are observed.

## Acceptance Criteria
- [ ] Retraining trigger defined — time-based or performance-based
- [ ] Feedback loop for capturing actual purchase outcomes defined
- [ ] Retraining pipeline designed
- [ ] Model versioning strategy confirmed in MLflow

## Reference
MLOps best practices" \
  --label "phase:deployment"

echo "All issues created successfully."
