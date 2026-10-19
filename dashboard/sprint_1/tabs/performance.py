# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:02:42 2026

@author: ngozi
"""

import streamlit as st
import pandas as pd
import numpy as np
from utils.charts import propensity_distribution, precision_recall_curve, confusion_matrix_chart


def render():
    st.header("Model Performance")
    st.markdown("""
    This tab shows what technical success looks like for the purchase propensity 
    model and translates model metrics into business language. Sprint 1 shows 
    placeholder metrics — these will be updated with actual model results in 
    subsequent sprints.
    """)

    st.divider()

    # Technical metrics
    st.subheader("Technical Metrics — Baseline Model")
    st.markdown("*Placeholder values — will be updated with actual model results*")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="AUC-ROC", value="—", help="Area Under the ROC Curve — measures ability to discriminate buyers from non-buyers")
        st.metric(label="AUC-PR", value="—", help="Area Under the Precision-Recall Curve — measures performance on the rare positive class")
    with col2:
        st.metric(label="Log Loss", value="—", help="Measures calibration — whether probability estimates are trustworthy")
        st.metric(label="F1-Score", value="—", help="Balances precision and recall")
    with col3:
        st.metric(label="Precision", value="—", help="Of sessions predicted as purchases, how many actually purchased")
        st.metric(label="Recall", value="—", help="Of sessions that actually purchased, how many did the model identify")

    st.divider()

    # Metric translation table
    st.subheader("What the Metrics Mean in Business Terms")
    st.markdown("The translation layer between technical performance and business outcomes:")

    translation_data = {
        "Model Metric": [
            "AUC-ROC",
            "AUC-PR",
            "Log Loss",
            "Precision",
            "Recall"
        ],
        "Plain English": [
            "How reliably we separate buyers from browsers",
            "How good we are at finding rare buyers",
            "Can we trust the probability scores",
            "When we predict a buyer, how often we are right",
            "Of all actual buyers, how many we correctly identified"
        ],
        "Business Implication": [
            "Higher = smarter targeting",
            "Higher = fewer missed conversions",
            "Lower = more reliable segmentation",
            "Drives marketing efficiency",
            "Drives missed revenue risk"
        ],
        "Priority": [
            "Primary",
            "Primary",
            "Calibration check",
            "Secondary",
            "Secondary"
        ]
    }

    st.dataframe(
        pd.DataFrame(translation_data),
        use_container_width=True,
        hide_index=True
    )

    st.info("""
    **Key business insight:** The cost of a false negative — marking a 
    high-propensity customer as low — is greater than the cost of a false 
    positive. This means **recall is more business-critical than precision** 
    in most e-commerce contexts.
    """)

    st.divider()

    # Propensity score distribution placeholder
    st.subheader("Propensity Score Distribution")
    st.markdown("*Placeholder — will show actual score distribution once model is trained*")

    np.random.seed(42)
    n = 1000
    scores = np.concatenate([
        np.random.beta(2, 8, int(n * 0.6)),
        np.random.beta(5, 5, int(n * 0.25)),
        np.random.beta(8, 2, int(n * 0.15))
    ])
    tiers = (
        ["Low (< 0.3)"] * int(n * 0.6) +
        ["Medium (0.3 - 0.7)"] * int(n * 0.25) +
        ["High (> 0.7)"] * int(n * 0.15)
    )
    score_df = pd.DataFrame({"score": scores, "tier": tiers})
    fig = propensity_distribution(score_df)
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # Precision recall curve placeholder
    st.subheader("Precision-Recall Curve")
    st.markdown("*Placeholder — will show actual curve once model is trained*")

    recall = np.linspace(0, 1, 100)
    precision = 1 - recall ** 0.5
    fig = precision_recall_curve(precision, recall)
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # Confusion matrix placeholder
    st.subheader("Confusion Matrix")
    st.markdown("*Placeholder — will show actual confusion matrix once model is trained*")

    fig = confusion_matrix_chart(
        tp=246001,
        fp=58057,
        fn=17381,
        tn=1686533
    )
    st.plotly_chart(fig, use_container_width=True)
