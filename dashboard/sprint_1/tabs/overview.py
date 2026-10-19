# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:57:26 2026

@author: ngozi
"""

import streamlit as st


def render():
    st.header("Project Overview")
    st.markdown("""
    This dashboard is the Sprint 1 deliverable for the 
    **Clickstream Purchase Propensity Model** project. Its purpose is to align 
    all stakeholders on the business problem, the proposed solution, and what 
    success looks like — moving understanding from heads to a shared visual artifact.
    """)

    st.subheader("Sprint 1 Goal")
    with st.container(border=True):
        st.markdown("""
        **Align all stakeholders on the business problem, the proposed solution, 
        and what success looks like — delivered through a dashboard that makes 
        this understanding visual and shareable.**
        """)

    st.subheader("Dataset at a Glance")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Raw Events",
            value="233M",
            help="Total number of raw clickstream events in the dataset"
        )
    with col2:
        st.metric(
            label="Total Sessions",
            value="52.3M",
            help="Total number of user sessions"
        )
    with col3:
        st.metric(
            label="Baseline Conversion Rate",
            value="5.85%",
            help="Percentage of sessions that resulted in a purchase"
        )
    with col4:
        st.metric(
            label="Sessions Analyzed",
            value="23.16M",
            help="Sessions remaining after preprocessing"
        )

    st.subheader("How to Navigate This Dashboard")
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("**📋 Overview**")
            st.markdown("Project summary, sprint goal, and key dataset metrics")
        with col2:
            st.markdown("**🔍 The Problem**")
            st.markdown("What problem are we solving and what does success look like in business terms")
        with col3:
            st.markdown("**💡 The Solution**")
            st.markdown("How we are solving the problem — technically and in plain language")
        with col4:
            st.markdown("**📊 Model Performance**")
            st.markdown("What technical success looks like and how it maps to business outcomes")

    st.subheader("Reference")
    with st.container(border=True):
        st.markdown("""
        **Methodology Reference:**  
        Tokuç, A. A. & Dağ, T. (2025). Predicting User Purchases From Clickstream Data: 
        A Comparative Analysis of Clickstream Data Representations and Machine Learning Models. 
        *IEEE Access*, Vol. 13, pp. 43796–43817. DOI: 10.1109/ACCESS.2025.3548267

        **Process Framework:** CRISP-DM + Agile Sprints + MLOps
        """)