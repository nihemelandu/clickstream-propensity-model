# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:18:07 2026

@author: ngozi
"""

import streamlit as st
from utils.charts import segment_conversion_chart


def render():
    # Business impact KPIs
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown("**Conversion Rate Lift**")
            st.markdown("Targeted vs Untargeted")
            col_a, col_b = st.columns(2)
            col_a.metric("Targeted", "—")
            col_b.metric("Baseline", "—")

    with col2:
        with st.container(border=True):
            st.markdown("**Marketing Efficiency**")
            st.markdown("Cost Per Acquisition")
            col_a, col_b = st.columns(2)
            col_a.metric("With Model", "—")
            col_b.metric("Without Model", "—")

    with col3:
        with st.container(border=True):
            st.markdown("**Revenue Per Session**")
            st.markdown("Propensity-driven vs Baseline")
            col_a, col_b = st.columns(2)
            col_a.metric("With Model", "—")
            col_b.metric("Baseline", "—")

    st.divider()

    # Segment conversion chart
    st.subheader("Conversion Rate by Segment vs Baseline")
    segments = ["High Intent", "Medium Intent", "Low Intent"]
    baseline_rate = 0.0
    segment_rates = [0.0, 0.0, 0.0]
    fig = segment_conversion_chart(segments, baseline_rate, segment_rates)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Placeholder — will show actual conversion rates once model is trained")