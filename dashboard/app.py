# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:34:52 2026

@author: ngozi
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

import streamlit as st
from tabs import overview, segments, model, impact

st.set_page_config(
    page_title="Customer Purchase Intent Dashboard",
    page_icon="🛒",
    layout="wide"
)

# Header
col_title, col_meta = st.columns([3, 1])
with col_title:
    st.title("🛒 Customer Purchase Intent Dashboard")
with col_meta:
    st.markdown("**Last Updated:** —")
    st.markdown("**Data:** Oct 2019 – Apr 2020")

st.divider()

# Navigation tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Overview",
    "🎯 Segments",
    "⚙️ Model",
    "💼 Business Impact"
])

with tab1:
    overview.render()

with tab2:
    segments.render()

with tab3:
    model.render()

with tab4:
    impact.render()
