# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:15:51 2026

@author: ngozi
"""
import streamlit as st
from utils.charts import feature_importance_chart


def render():
    # Segment cards
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown("### 🟢 High Intent")
            st.markdown("**Score > 0.7**")
            st.metric("Sessions", "—")
            st.metric("Share of Total", "—")
            st.metric("Conversion Rate", "—")
            st.divider()
            st.markdown("**Ready to buy**")
            st.markdown("→ Personalize experience")
            st.markdown("→ Surface the right product")

    with col2:
        with st.container(border=True):
            st.markdown("### 🟡 Medium Intent")
            st.markdown("**Score 0.3 – 0.7**")
            st.metric("Sessions", "—")
            st.metric("Share of Total", "—")
            st.metric("Conversion Rate", "—")
            st.divider()
            st.markdown("**Needs a nudge**")
            st.markdown("→ Trigger targeted offer")
            st.markdown("→ Cart recovery prompt")

    with col3:
        with st.container(border=True):
            st.markdown("### 🔴 Low Intent")
            st.markdown("**Score < 0.3**")
            st.metric("Sessions", "—")
            st.metric("Share of Total", "—")
            st.metric("Conversion Rate", "—")
            st.divider()
            st.markdown("**Just browsing**")
            st.markdown("→ Nurture campaign")
            st.markdown("→ Re-engagement flow")

    st.divider()

    # Feature importance
    st.subheader("Top Signals Driving Purchase Intent")
    features = [
        "Avg price per event",
        "Products viewed",
        "Cart activity",
        "Session duration",
        "Time since last action"
    ]
    importance = [0.0, 0.0, 0.0, 0.0, 0.0]
    fig = feature_importance_chart(features, importance)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Placeholder — will show actual feature importance once model is trained")
