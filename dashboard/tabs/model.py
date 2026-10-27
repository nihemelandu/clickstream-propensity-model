"""
Model tab — performance metrics, precision-recall curve, confusion matrix.
Reads from pipeline artifacts when available.
Shows placeholders when pipeline has not yet run.
"""
import streamlit as st
import numpy as np
import pandas as pd
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.charts import precision_recall_chart, confusion_matrix_chart
from utils.data_loader import load_metrics, artifacts_exist


def render():
    metrics  = load_metrics()
    has_data = artifacts_exist()

    # ── Performance Metrics and PR Curve ──────────────────────────────────────
    col_left, col_right = st.columns([2, 3])

    with col_left:
        st.subheader('Performance Metrics')

        if has_data and metrics:
            perf = metrics['performance']
            metrics_data = {
                'Metric': [
                    'AUC-PR', 'AUC-ROC', 'Log Loss',
                    'F1-Score', 'Precision', 'Recall'
                ],
                'Value': [
                    str(perf['auc_pr']),
                    str(perf['auc_roc']),
                    str(perf['log_loss']),
                    str(perf['f1_score']),
                    str(perf['precision']),
                    str(perf['recall'])
                ],
                'What It Means for the Business': [
                    'Finding buyers we would otherwise miss',
                    'Separating buyers from browsers',
                    'Trusting the scores to make decisions',
                    'Balance between finding and targeting buyers',
                    'When we predict a buyer, how often we are right',
                    'Of all actual buyers, how many we identified'
                ]
            }
        else:
            metrics_data = {
                'Metric': [
                    'AUC-PR', 'AUC-ROC', 'Log Loss',
                    'F1-Score', 'Precision', 'Recall'
                ],
                'Value': ['—', '—', '—', '—', '—', '—'],
                'What It Means for the Business': [
                    'Finding buyers we would otherwise miss',
                    'Separating buyers from browsers',
                    'Trusting the scores to make decisions',
                    'Balance between finding and targeting buyers',
                    'When we predict a buyer, how often we are right',
                    'Of all actual buyers, how many we identified'
                ]
            }

        st.dataframe(
            pd.DataFrame(metrics_data),
            use_container_width=True,
            hide_index=True
        )

    with col_right:
        st.subheader('Precision-Recall Curve')
        recall    = np.linspace(0, 1, 100)
        precision = np.ones(100) * 0.0
        fig       = precision_recall_chart(precision, recall)
        st.plotly_chart(fig, use_container_width=True)
        if not has_data:
            st.caption(
                'Placeholder — will update automatically once pipeline runs'
            )

    st.divider()

    # ── Confusion Matrix ──────────────────────────────────────────────────────
    st.subheader('Confusion Matrix')

    if has_data and metrics:
        cm  = metrics['confusion_matrix']
        fig = confusion_matrix_chart(
            tp=cm['true_positives'],
            fp=cm['false_positives'],
            fn=cm['false_negatives'],
            tn=cm['true_negatives']
        )
    else:
        fig = confusion_matrix_chart(tp=0, fp=0, fn=0, tn=0)

    st.plotly_chart(fig, use_container_width=True)
    if not has_data:
        st.caption(
            'Placeholder — will update automatically once pipeline runs'
        )
