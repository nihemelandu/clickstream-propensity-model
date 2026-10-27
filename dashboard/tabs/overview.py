"""
Overview tab — headline metrics and score distribution.
Reads from pipeline artifacts when available.
Shows placeholders when pipeline has not yet run.
"""
import streamlit as st
import pandas as pd
import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.charts import score_distribution
from utils.data_loader import (
    load_segment_stats, load_scores, artifacts_exist
)


def render():
    # Load artifacts if available
    segment_stats = load_segment_stats()
    scores_df     = load_scores()
    has_data      = artifacts_exist()

    # ── Headline Metrics ──────────────────────────────────────────────────────
    col1, col2, col3, col4 = st.columns(4)

    if has_data and segment_stats:
        total     = segment_stats['total_sessions']
        high      = segment_stats['segments']['high']['sessions']
        conv_rate = segment_stats['baseline_conv_rate']

        with col1:
            st.metric(
                label="Sessions Scored",
                value=f"{total:,}",
                help="Total sessions scored by the model"
            )
        with col2:
            st.metric(
                label="Predicted Buyers",
                value=f"{high:,}",
                help="Sessions predicted as high intent"
            )
        with col3:
            st.metric(
                label="Conversion Rate",
                value=f"{conv_rate:.1%}",
                help="Percentage of sessions resulting in a purchase"
            )
        with col4:
            st.metric(
                label="High Intent Share",
                value=f"{segment_stats['segments']['high']['share']:.1%}",
                help="Share of sessions in the high intent tier"
            )
    else:
        with col1:
            st.metric(label="Sessions Scored", value="—")
        with col2:
            st.metric(label="Predicted Buyers", value="—")
        with col3:
            st.metric(label="Conversion Rate", value="—")
        with col4:
            st.metric(label="High Intent Share", value="—")

    st.divider()

    # ── Score Distribution and Tier Breakdown ─────────────────────────────────
    col_left, col_right = st.columns([3, 2])

    with col_left:
        st.subheader("Propensity Score Distribution")

        if has_data and scores_df is not None:
            # Real data from pipeline
            scores_df['tier_label'] = scores_df['tier'].map({
                'High':   'High (> 0.7)',
                'Medium': 'Medium (0.3 - 0.7)',
                'Low':    'Low (< 0.3)'
            })
            plot_df = scores_df[['propensity_score', 'tier_label']].rename(
                columns={'propensity_score': 'score', 'tier_label': 'tier'}
            )
            fig = score_distribution(plot_df)
            st.plotly_chart(fig, use_container_width=True)
        else:
            # Placeholder distribution
            np.random.seed(42)
            n      = 1000
            scores = np.concatenate([
                np.random.beta(2, 8, int(n * 0.6)),
                np.random.beta(5, 5, int(n * 0.25)),
                np.random.beta(8, 2, int(n * 0.15))
            ])
            tiers  = (
                ['Low (< 0.3)']        * int(n * 0.6) +
                ['Medium (0.3 - 0.7)'] * int(n * 0.25) +
                ['High (> 0.7)']       * int(n * 0.15)
            )
            plot_df = pd.DataFrame({'score': scores, 'tier': tiers})
            fig     = score_distribution(plot_df)
            st.plotly_chart(fig, use_container_width=True)
            st.caption(
                'Placeholder — will update automatically once pipeline runs'
            )

    with col_right:
        st.subheader("Sessions by Intent Tier")

        tiers_config = [
            ('🟢', 'High Intent',   'high'),
            ('🟡', 'Medium Intent', 'medium'),
            ('🔴', 'Low Intent',    'low')
        ]

        for emoji, label, key in tiers_config:
            with st.container(border=True):
                st.markdown(f'{emoji} **{label}**')
                col_a, col_b = st.columns(2)

                if has_data and segment_stats:
                    seg = segment_stats['segments'][key]
                    col_a.metric('Sessions', f"{seg['sessions']:,}")
                    col_b.metric('Share',    f"{seg['share']:.1%}")
                else:
                    col_a.metric('Sessions', '—')
                    col_b.metric('Share',    '—')
