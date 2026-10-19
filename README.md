# Customer Purchase Intent Dashboard

## [View Live Dashboard](https://your-app.streamlit.app)

> Dashboard link will be updated once Streamlit Community Cloud deployment is complete.

---

## Overview

An end-to-end machine learning system that scores e-commerce customer sessions by purchase likelihood. The model converts raw clickstream behavior into propensity scores that enable smarter targeting, customer segmentation, and data-driven marketing decisions.

**Core question the model answers:**
> Given a customer's clickstream behavior during a session, what is the probability that the session will result in a purchase?

---

## Business Value

| Capability | Description |
|---|---|
| **Ranking** | Sort customers by purchase intent to prioritize marketing resources |
| **Segmentation** | Group customers into high, medium, and low intent tiers with distinct actions |
| **Decision Support** | Feed reliable probability estimates into real-time and strategic decisions |

---

## Methodology

This project follows the **CRISP-DM** framework, implemented through **Agile sprints** with MLOps practices. The modeling approach replicates and extends:

> Tokuç, A. A. & Dağ, T. (2025). Predicting User Purchases From Clickstream Data: A Comparative Analysis of Clickstream Data Representations and Machine Learning Models. *IEEE Access*, Vol. 13, pp. 43796-43817. [DOI: 10.1109/ACCESS.2025.3548267](https://doi.org/10.1109/ACCESS.2025.3548267)

**Key modeling decisions:**
- Binary classification — purchase vs no purchase at session level
- Hybrid data representation — aggregated session attributes combined with recent user actions
- LightGBM — computationally efficient, handles class imbalance natively, interpretable via feature importance
- Evaluation prioritizes AUC-PR and AUC-ROC given severe class imbalance (~5.85% purchase rate)

---

## Project Structure

    clickstream-propensity-model/
    ├── dashboard/                  Streamlit dashboard — one folder per sprint
    │   └── sprint_1/
    │       ├── app.py              Dashboard entry point
    │       ├── tabs/               One module per dashboard tab
    │       └── utils/              Reusable chart functions
    ├── docs/                       Project documentation
    │   └── business_understanding.md
    ├── notebooks/                  Jupyter notebooks — one folder per sprint
    │   └── sprint_1/
    ├── src/                        Source code
    │   ├── data/                   Preprocessing pipeline
    │   ├── features/               Feature engineering
    │   ├── models/                 Model training and inference
    │   └── utils/                  Shared utilities
    ├── models/                     Trained model artifacts — one folder per sprint
    │   └── sprint_1/
    ├── data/                       Raw and processed data (not tracked in Git)
    │   ├── raw/
    │   └── processed/
    ├── requirements.txt            Project dependencies
    └── README.md

---

## Dataset

| Attribute | Detail |
|---|---|
| **Source** | [eCommerce Behavior Data from Multi-Category Store](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store) |
| **Publisher** | REES46 |
| **Period** | October 2019 – April 2020 |
| **Raw Events** | 233 million records |
| **Event Types** | view, add-to-cart, purchase |
| **Purchase Rate** | 5.85% of sessions |

> **Note:** Raw data is not tracked in this repository. Download from the Kaggle link above and place in `data/raw/`.

---

## Setup

### Prerequisites
- Python 3.12+
- pip

### Installation

    git clone https://github.com/nihemelandu/clickstream-propensity-model.git
    cd clickstream-propensity-model
    pip install -r requirements.txt

### Run Dashboard Locally

    cd dashboard/sprint_1
    streamlit run app.py

---

## Sprint Progress

| Sprint | Focus | Status |
|---|---|---|
| Sprint 1 | Business understanding — problem definition, solution framework, success metrics | In Progress |
| Sprint 2 | Data understanding — EDA, class imbalance, session structure | Pending |
| Sprint 3 | EDA deep dive — correlation analysis, feature importance review | Pending |
| Sprint 4 | Data preparation — preprocessing pipeline | Pending |
| Sprint 5 | Data representations — aggregated, flattened, hybrid | Pending |
| Sprint 6 | Modeling — baseline models, PSO feature selection, hyperparameter tuning | Pending |
| Sprint 7 | Evaluation — metrics, calibration, segment validation | Pending |
| Sprint 8 | Insights and deployment — feature importance, MLOps | Pending |

---

## Tools and Technologies

| Category | Tool |
|---|---|
| Language | Python 3.12 |
| Data Processing | Pandas, PySpark |
| Modeling | LightGBM, Scikit-learn |
| Feature Selection | PySwarms (PSO) |
| Hyperparameter Tuning | Hyperopt (TPE) |
| Experiment Tracking | MLflow |
| Dashboard | Streamlit, Plotly |
| Version Control | Git, GitHub |
| Project Management | GitHub Projects, GitHub Issues |
| Process Framework | CRISP-DM, Agile, MLOps |

---

## Project Management

All tasks are tracked in the [GitHub Project board](https://github.com/nihemelandu/clickstream-propensity-model/projects).
Each sprint has a corresponding [Milestone](https://github.com/nihemelandu/clickstream-propensity-model/milestones).

---

## License

This project is for research and educational purposes.
