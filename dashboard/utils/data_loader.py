"""
Data loader — reads pipeline artifacts for the dashboard.
If artifacts exist, returns real data.
If artifacts do not exist, returns None so tabs show placeholders.
"""
import os
import json
import pandas as pd

# Path to artifacts — relative to repository root
ARTIFACTS_PATH = os.path.join(
    os.path.dirname(__file__), '..', '..', 'artifacts'
)


def load_metrics() -> dict:
    """Load model performance metrics."""
    path = os.path.join(ARTIFACTS_PATH, 'metrics.json')
    if not os.path.exists(path):
        return None
    with open(path, 'r') as f:
        return json.load(f)


def load_segment_stats() -> dict:
    """Load segment statistics."""
    path = os.path.join(ARTIFACTS_PATH, 'segment_stats.json')
    if not os.path.exists(path):
        return None
    with open(path, 'r') as f:
        return json.load(f)


def load_business_impact() -> dict:
    """Load business impact metrics."""
    path = os.path.join(ARTIFACTS_PATH, 'business_impact.json')
    if not os.path.exists(path):
        return None
    with open(path, 'r') as f:
        return json.load(f)


def load_scores() -> pd.DataFrame:
    """Load session propensity scores."""
    # Look in local data/processed/gold/
    path = os.path.join(
        os.path.dirname(__file__), '..', '..',
        'data', 'processed', 'gold', 'scores.parquet'
    )
    if not os.path.exists(path):
        return None
    return pd.read_parquet(path)


def artifacts_exist() -> bool:
    """Check if pipeline has been run and artifacts exist."""
    path = os.path.join(ARTIFACTS_PATH, 'metrics.json')
    return os.path.exists(path)
