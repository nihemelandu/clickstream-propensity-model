# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:01:23 2026

@author: ngozi
"""

import streamlit as st


def render():
    st.header("The Solution")

    # Plain language solution
    with st.container(border=True):
        st.markdown("""
        ### In Plain Language
        We are building a model that scores each customer session by purchase 
        likelihood — producing a number between 0 and 1 that represents how 
        likely that customer is to make a purchase. This score is then used to 
        rank customers by intent, group them into actionable segments, and 
        inform real-time or strategic business decisions.
        """)

    st.divider()

    # Technical formulation
    st.subheader("Technical Formulation")
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Problem Type**  
            Binary Classification

            **Input**  
            Session-level clickstream events — views, cart additions, 
            time between actions, session duration, user history

            **Output**  
            Propensity score between 0 and 1
            """)
        with col2:
            st.markdown("""
            **Model**  
            LightGBM on hybrid clickstream representation

            **Key Challenge**  
            Severe class imbalance — only 5.85% of sessions result 
            in a purchase

            **Reference**  
            Tokuç & Dağ (2025) — hybrid data representation with LightGBM
            """)

    st.divider()

    # How the model works
    st.subheader("How the Model Works")
    st.markdown("From raw clickstream behavior to actionable propensity score:")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        with st.container(border=True):
            st.markdown("### 📥")
            st.markdown("**Raw Clickstream**")
            st.markdown("Views, cart additions, purchases, timestamps")
    with col2:
        with st.container(border=True):
            st.markdown("### ⚙️")
            st.markdown("**Session Features**")
            st.markdown("Time since last event, session duration, cart activity")
    with col3:
        with st.container(border=True):
            st.markdown("### 🔀")
            st.markdown("**Hybrid Representation**")
            st.markdown("Aggregated session + recent user actions combined")
    with col4:
        with st.container(border=True):
            st.markdown("### 🤖")
            st.markdown("**LightGBM Model**")
            st.markdown("Trained on hybrid representation with class weighting")
    with col5:
        with st.container(border=True):
            st.markdown("### 🎯")
            st.markdown("**Propensity Score**")
            st.markdown("0 to 1 — probability of purchase this session")

    st.divider()

    # Customer segmentation
    st.subheader("Customer Segmentation")
    st.markdown("""
    Propensity scores are used to group customers into three actionable tiers.
    Thresholds are provisional and will be revised in a future sprint once 
    actual score distributions are available.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown("### 🟢 High Intent")
            st.metric(label="Score Range", value="> 0.7")
            st.markdown("""
            **Description**  
            Ready to buy

            **Business Action**  
            Personalize experience — surface the right product 
            at the right moment
            """)

    with col2:
        with st.container(border=True):
            st.markdown("### 🟡 Medium Intent")
            st.metric(label="Score Range", value="0.3 — 0.7")
            st.markdown("""
            **Description**  
            On the fence — needs a nudge

            **Business Action**  
            Trigger a targeted offer, discount, or 
            cart recovery prompt
            """)

    with col3:
        with st.container(border=True):
            st.markdown("### 🔴 Low Intent")
            st.metric(label="Score Range", value="< 0.3")
            st.markdown("""
            **Description**  
            Just browsing — no immediate intent

            **Business Action**  
            Nurture — add to re-engagement or 
            awareness campaign
            """)

    st.divider()

    # Tools
    st.subheader("Tools and Techniques")
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            | Category | Tool |
            |---|---|
            | Language | Python |
            | Data Processing | Pandas, PySpark |
            | Modeling | LightGBM, Scikit-learn |
            | Feature Selection | PySwarms (PSO) |
            | Hyperparameter Tuning | Hyperopt (TPE) |
            """)
        with col2:
            st.markdown("""
            | Category | Tool |
            |---|---|
            | Experiment Tracking | MLflow |
            | Dashboard | Streamlit + Plotly |
            | Version Control | Git + GitHub |
            | Project Management | GitHub Projects |
            | Methodology | CRISP-DM + Agile + MLOps |
            """)
