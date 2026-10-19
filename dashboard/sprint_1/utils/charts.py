import plotly.express as px
import plotly.graph_objects as go
#import pandas as pd


def conversion_funnel(total_sessions, cart_sessions, purchase_sessions):
    fig = go.Figure(go.Funnel(
        y=["All Sessions", "Sessions with Cart Activity", "Sessions with Purchase"],
        x=[total_sessions, cart_sessions, purchase_sessions],
        textinfo="value+percent initial",
        marker=dict(color=["#4C9BE8", "#F4A261", "#2A9D8F"])
    ))
    fig.update_layout(
        title="Session Conversion Funnel",
        margin=dict(t=50, b=20)
    )
    return fig


def propensity_distribution(scores):
    fig = px.histogram(
        scores,
        x="score",
        color="tier",
        color_discrete_map={
            "High (> 0.7)": "#2A9D8F",
            "Medium (0.3 - 0.7)": "#F4A261",
            "Low (< 0.3)": "#E76F51"
        },
        title="Propensity Score Distribution by Tier",
        labels={"score": "Propensity Score", "count": "Number of Sessions"},
        barmode="overlay",
        opacity=0.7
    )
    fig.update_layout(margin=dict(t=50, b=20))
    return fig


def precision_recall_curve(precision, recall):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=recall,
        y=precision,
        mode="lines",
        name="Baseline Model",
        line=dict(color="#4C9BE8", width=2)
    ))
    fig.update_layout(
        title="Precision-Recall Curve",
        xaxis_title="Recall",
        yaxis_title="Precision",
        margin=dict(t=50, b=20)
    )
    return fig


def confusion_matrix_chart(tp, fp, fn, tn):
    z = [[tn, fp], [fn, tp]]
    x = ["Predicted No Purchase", "Predicted Purchase"]
    y = ["Actual No Purchase", "Actual Purchase"]
    fig = go.Figure(data=go.Heatmap(
        z=z,
        x=x,
        y=y,
        colorscale="Blues",
        text=[[str(tn), str(fp)], [str(fn), str(tp)]],
        texttemplate="%{text}",
        showscale=False
    ))
    fig.update_layout(
        title="Confusion Matrix",
        margin=dict(t=50, b=20)
    )
    return fig