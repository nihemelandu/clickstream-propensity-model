# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:03:19 2026

@author: ngozi
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

import streamlit as st
from tabs import overview, problem, solution, performance

st.set_page_config(
    page_title="Purchase Propensity Model | Sprint 1",
    page_icon="🛒",
    layout="wide"
)

# Header
st.title("🛒 Purchase Propensity Model")
st.markdown(
    """
    **Project:** Clickstream Purchase Propensity | 
    **Sprint:** 1 | 
    **Status:** Baseline
    """
)
st.divider()

# Navigation tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📋 Overview",
    "🔍 The Problem",
    "💡 The Solution",
    "📊 Model Performance"
])

with tab1:
    overview.render()

with tab2:
    problem.render()

with tab3:
    solution.render()

with tab4:
    performance.render()