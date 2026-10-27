# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:05:34 2026

@author: ngozi
"""

import streamlit as st
import pandas as pd
import numpy as np
from utils.charts import score_distribution


def render():
    # Headline metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Sessions Scored", value="—",
                  help="Total sessions scored by the model")
    with col2:
        st.metric(label="Predicted Buyers", value="—",
                  help="Sessions predicted as high intent")
    with col3:
        st.metric(label="Conversion Rate", value="—",
                  help="Percentage of sessions resulting in a purchase")
    with col4:
        st.metric(label="Revenue at Risk", value="—",
                  help="Estimated revenue from sessions predicted to convert")

    st.divider()

    # Score distribution and tier breakdown
    col_left, col_right = st.columns([3, 2])

    with col_left:
        st.subheader("Propensity Score Distribution")
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
        fig = score_distribution(score_df)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Placeholder — will show actual score distribution once model is trained")

    with col_right:
        st.subheader("Sessions by Intent Tier")
        with st.container(border=True):
            st.markdown("🟢 **High Intent**")
            col_a, col_b = st.columns(2)
            col_a.metric("Sessions", "—")
            col_b.metric("Share", "—")
        with st.container(border=True):
            st.markdown("🟡 **Medium Intent**")
            col_a, col_b = st.columns(2)
            col_a.metric("Sessions", "—")
            col_b.metric("Share", "—")
        with st.container(border=True):
            st.markdown("🔴 **Low Intent**")
            col_a, col_b = st.columns(2)
            col_a.metric("Sessions", "—")
            col_b.metric("Share", "—")