"""
Segments tab — customer intent tiers and top purchase signals.
Reads from pipeline artifacts when available.
Shows placeholders when pipeline has not yet run.
"""
import streamlit as st
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.charts import feature_importance_chart
from utils.data_loader import (
    load_segment_stats, load_metrics, artifacts_exist
)


def render():
    # Load artifacts if available
    segment_stats = load_segment_stats()
    metrics       = load_metrics()
    has_data      = artifacts_exist()

    # ── Segment Cards ─────────────────────────────────────────────────────────
    col1, col2, col3 = st.columns(3)

    segments_config = [
        (col1, '🟢', 'High Intent',   'Score > 0.7',   'high',
         'Ready to buy',
         ['→ Personalize experience', '→ Surface the right product']),
        (col2, '🟡', 'Medium Intent', 'Score 0.3 – 0.7', 'medium',
         'Needs a nudge',
         ['→ Trigger targeted offer', '→ Cart recovery prompt']),
        (col3, '🔴', 'Low Intent',    'Score < 0.3',   'low',
         'Just browsing',
         ['→ Nurture campaign', '→ Re-engagement flow'])
    ]

    for col, emoji, label, score_range, key, description, actions in segments_config:
        with col:
            with st.container(border=True):
                st.markdown(f'### {emoji} {label}')
                st.markdown(f'**{score_range}**')

                if has_data and segment_stats:
                    seg = segment_stats['segments'][key]
                    st.metric('Sessions',        f"{seg['sessions']:,}")
                    st.metric('Share of Total',  f"{seg['share']:.1%}")
                    st.metric('Conversion Rate', f"{seg['conversion_rate']:.1%}")
                else:
                    st.metric('Sessions',        '—')
                    st.metric('Share of Total',  '—')
                    st.metric('Conversion Rate', '—')

                st.divider()
                st.markdown(f'**{description}**')
                for action in actions:
                    st.markdown(action)

    st.divider()

    # ── Feature Importance ────────────────────────────────────────────────────
    st.subheader('Top Signals Driving Purchase Intent')

    if has_data and metrics and metrics.get('feature_importance'):
        importance_dict = metrics['feature_importance']
        # Take top 5 features
        top5       = list(importance_dict.items())[:5]
        features   = [item[0] for item in top5]
        importance = [item[1] for item in top5]

        # Make feature names business friendly
        name_map = {
            'event_count':          'Total session events',
            'view_count':           'Products viewed',
            'cart_count':           'Cart activity',
            'session_duration_sec': 'Session duration',
            'avg_price':            'Avg price per event',
            'product_count':        'Distinct products viewed',
            'brand_count':          'Distinct brands viewed',
            'day_of_week':          'Day of week',
            'session_start_hour':   'Session start hour',
            'is_weekend':           'Weekend session',
            'purchase_count':       'Prior purchases'
        }
        features = [name_map.get(f, f) for f in features]

        fig = feature_importance_chart(features, importance)
        st.plotly_chart(fig, use_container_width=True)
    else:
        features   = [
            'Avg price per event',
            'Products viewed',
            'Cart activity',
            'Session duration',
            'Time since last action'
        ]
        importance = [0.0, 0.0, 0.0, 0.0, 0.0]
        fig        = feature_importance_chart(features, importance)
        st.plotly_chart(fig, use_container_width=True)
        st.caption(
            'Placeholder — will update automatically once pipeline runs'
        )
