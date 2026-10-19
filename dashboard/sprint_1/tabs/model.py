# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:17:46 2026

@author: ngozi
"""

import streamlit as st
import numpy as np
import pandas as pd
from utils.charts import precision_recall_chart, confusion_matrix_chart


def render():
    # Model metrics and PR curve side by side
    col_left, col_right = st.columns([2, 3])

    with col_left:
        st.subheader("Performance Metrics")
        metrics = {
            "Metric": ["AUC-PR", "AUC-ROC", "Log Loss", "F1-Score",
                       "Precision", "Recall"],
            "Value": ["—", "—", "—", "—", "—", "—"],
            "What It Means for the Business": [
                "Finding buyers we would otherwise miss",
                "Separating buyers from browsers",
                "Trusting the scores to make decisions",
                "Balance between finding and targeting buyers",
                "When we predict a buyer, how often we are right",
                "Of all actual buyers, how many we identified"
            ]
        }
        st.dataframe(
            pd.DataFrame(metrics),
            use_container_width=True,
            hide_index=True
        )

    with col_right:
        st.subheader("Precision-Recall Curve")
        recall = np.linspace(0, 1, 100)
        precision = np.ones(100) * 0.0
        fig = precision_recall_chart(precision, recall)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Placeholder — will show actual curve once model is trained")

    st.divider()

    # Confusion matrix
    st.subheader("Confusion Matrix")
    fig = confusion_matrix_chart(tp=0, fp=0, fn=0, tn=0)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Placeholder — will show actual confusion matrix once model is trained")
