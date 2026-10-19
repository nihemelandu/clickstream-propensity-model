# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:59:08 2026

@author: ngozi
"""

import streamlit as st
from utils.charts import conversion_funnel


def render():
    st.header("The Problem")

    # Problem statement
    with st.container(border=True):
        st.markdown("""
        ### What Is the Problem?
        E-commerce platforms generate enormous volumes of customer interaction 
        data, but the vast majority of sessions do not result in a purchase. 
        Without a way to distinguish high-intent customers from casual browsers, 
        businesses waste resources on customers who were never going to buy, 
        while missing customers who needed only a small nudge to convert.

        The result is **inefficient resource allocation**, **missed conversion 
        opportunities**, and **poorly targeted interventions**.
        """)

    st.divider()

    # Conversion funnel
    st.subheader("The Conversion Gap")
    st.markdown("""
    Of all sessions on the platform, only a small fraction result in a purchase. 
    This gap is the opportunity the propensity model addresses.
    """)
    fig = conversion_funnel(
        total_sessions=52321178,
        cart_sessions=9991458,
        purchase_sessions=3063117
    )
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # Business metrics
    st.subheader("Business Metrics We Will Monitor")
    st.markdown("These are the business outcomes we expect the propensity model to move:")

    metrics_data = {
        "Business Metric": [
            "Conversion Rate",
            "Revenue Per Session",
            "Campaign ROI / ROAS",
            "Cost Per Acquisition",
            "Segment Conversion Rate Differential",
            "Cart Abandonment Recovery Rate"
        ],
        "Description": [
            "Percentage of sessions resulting in a purchase",
            "Average revenue generated per customer session",
            "Revenue generated per dollar of marketing spend",
            "Marketing cost to acquire one converting customer",
            "Actual conversion rate per propensity tier",
            "Percentage of abandoned carts recovered"
        ],
        "Expected Direction": [
            "⬆ Increase",
            "⬆ Increase",
            "⬆ Increase",
            "⬇ Decrease",
            "High >> Medium >> Low",
            "⬆ Increase"
        ]
    }

    import pandas as pd
    st.dataframe(
        pd.DataFrame(metrics_data),
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # Expected return
    st.subheader("Expected Return")
    st.markdown("Industry evidence for purchase propensity models in e-commerce:")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown("### 🟡 Conservative")
            st.metric(label="Conversion Lift", value="1.5x")
            st.markdown("""
            Modest targeting improvement on high-propensity segment.
            Positive return even with open-source tooling cost only.
            """)

    with col2:
        with st.container(border=True):
            st.markdown("### 🟢 Moderate")
            st.metric(label="Conversion Lift", value="2.5x")
            st.markdown("""
            Aligns with documented industry benchmarks.
            Strongly positive return on investment.
            """)

    with col3:
        with st.container(border=True):
            st.markdown("### 🚀 Optimistic")
            st.metric(label="Conversion Lift", value="3x — 10x")
            st.markdown("""
            Consistent with documented case studies for 
            well-targeted propensity-driven campaigns.
            """)

    st.divider()

    # Cost benefit
    st.subheader("Cost-Benefit Analysis")
    with st.container(border=True):
        st.markdown("""
        **The question:** Does the expected return of solving this prediction 
        problem outweigh the cost of development and deployment?

        **The answer:** Yes — across all three scenarios.

        | Cost Category | Detail |
        |---|---|
        | Development | Data scientist time across sprints |
        | Tooling | Zero — all open source |
        | Infrastructure | Zero at this stage — local machine only |
        | Ongoing | Model monitoring and retraining |

        The cost-benefit case is strongest when framed not just as revenue 
        uplift but as **waste reduction** — money currently spent targeting 
        non-buyers redirected to high-intent customers.
        """)