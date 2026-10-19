
import plotly.express as px
import plotly.graph_objects as go
#import pandas as pd
#import numpy as np


def score_distribution(score_df):
    fig = px.histogram(
        score_df,
        x="score",
        color="tier",
        color_discrete_map={
            "High (> 0.7)": "#2A9D8F",
            "Medium (0.3 - 0.7)": "#F4A261",
            "Low (< 0.3)": "#E76F51"
        },
        barmode="overlay",
        opacity=0.75,
        labels={"score": "Propensity Score", "count": "Sessions"}
    )
    fig.update_layout(
        margin=dict(t=10, b=10, l=10, r=10),
        legend_title="Intent Tier",
        height=250
    )
    return fig


def feature_importance_chart(features, importance):
    fig = go.Figure(go.Bar(
        x=importance,
        y=features,
        orientation="h",
        marker_color="#4C9BE8"
    ))
    fig.update_layout(
        margin=dict(t=10, b=10, l=10, r=10),
        xaxis_title="Importance",
        yaxis=dict(autorange="reversed"),
        height=200
    )
    return fig


def precision_recall_chart(precision, recall):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=recall,
        y=precision,
        mode="lines",
        line=dict(color="#4C9BE8", width=2),
        name="Model"
    ))
    fig.update_layout(
        xaxis_title="Recall",
        yaxis_title="Precision",
        margin=dict(t=10, b=10, l=10, r=10),
        height=250
    )
    return fig


def confusion_matrix_chart(tp, fp, fn, tn):
    z = [[tn, fp], [fn, tp]]
    text = [[f"TN: {tn:,}", f"FP: {fp:,}"],
            [f"FN: {fn:,}", f"TP: {tp:,}"]]
    fig = go.Figure(data=go.Heatmap(
        z=z,
        x=["Predicted No Purchase", "Predicted Purchase"],
        y=["Actual No Purchase", "Actual Purchase"],
        colorscale="Blues",
        text=text,
        texttemplate="%{text}",
        showscale=False
    ))
    fig.update_layout(
        margin=dict(t=10, b=10, l=10, r=10),
        height=200
    )
    return fig


def segment_conversion_chart(segments, baseline_rate, segment_rates):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name="Segment Rate",
        x=segments,
        y=segment_rates,
        marker_color=["#2A9D8F", "#F4A261", "#E76F51"]
    ))
    fig.add_hline(
        y=baseline_rate,
        line_dash="dash",
        line_color="gray",
        annotation_text="Baseline"
    )
    fig.update_layout(
        yaxis_title="Conversion Rate",
        margin=dict(t=10, b=10, l=10, r=10),
        height=220
    )
    return fig