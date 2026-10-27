"""
Business Impact tab — conversion lift, marketing efficiency, segment performance.
Reads from pipeline artifacts when available.
Shows placeholders when pipeline has not yet run.
"""
import streamlit as st
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.charts import segment_conversion_chart
from utils.data_loader import (
    load_business_impact, load_segment_stats, artifacts_exist
)


def render():
    business_impact = load_business_impact()
    segment_stats   = load_segment_stats()
    has_data        = artifacts_exist()

    # ── Business Impact KPIs ──────────────────────────────────────────────────
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown('**Conversion Rate Lift**')
            st.markdown('Targeted vs Untargeted')
            col_a, col_b = st.columns(2)

            if has_data and business_impact:
                high_conv    = business_impact['high_intent_conversion_rate']
                baseline     = business_impact['baseline_conversion_rate']
                col_a.metric('Targeted', f'{high_conv:.1%}')
                col_b.metric('Baseline', f'{baseline:.1%}')
            else:
                col_a.metric('Targeted', '—')
                col_b.metric('Baseline', '—')

    with col2:
        with st.container(border=True):
            st.markdown('**Conversion Rate Lift Factor**')
            st.markdown('How much better than baseline')
            col_a, col_b = st.columns(2)

            if has_data and business_impact:
                lift = business_impact['conversion_rate_lift']
                col_a.metric('Lift', f'{lift:.1f}x')
                col_b.metric('vs Baseline', '1.0x')
            else:
                col_a.metric('Lift',       '—')
                col_b.metric('vs Baseline', '—')

    with col3:
        with st.container(border=True):
            st.markdown('**High Intent Sessions**')
            st.markdown('Sessions ready to convert')
            col_a, col_b = st.columns(2)

            if has_data and segment_stats:
                high_sessions = segment_stats['segments']['high']['sessions']
                high_share    = segment_stats['segments']['high']['share']
                col_a.metric('Sessions', f"{high_sessions:,}")
                col_b.metric('Share',    f'{high_share:.1%}')
            else:
                col_a.metric('Sessions', '—')
                col_b.metric('Share',    '—')

    st.divider()

    # ── Segment Conversion Chart ──────────────────────────────────────────────
    st.subheader('Conversion Rate by Segment vs Baseline')

    if has_data and segment_stats:
        segs          = segment_stats['segments']
        segments      = ['High Intent', 'Medium Intent', 'Low Intent']
        baseline_rate = segment_stats['baseline_conv_rate']
        segment_rates = [
            segs['high']['conversion_rate'],
            segs['medium']['conversion_rate'],
            segs['low']['conversion_rate']
        ]
    else:
        segments      = ['High Intent', 'Medium Intent', 'Low Intent']
        baseline_rate = 0.0
        segment_rates = [0.0, 0.0, 0.0]

    fig = segment_conversion_chart(segments, baseline_rate, segment_rates)
    st.plotly_chart(fig, use_container_width=True)

    if not has_data:
        st.caption(
            'Placeholder — will update automatically once pipeline runs'
        )
