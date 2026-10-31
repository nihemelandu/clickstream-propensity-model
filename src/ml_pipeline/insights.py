"""
Insight Generation — writes the JSON artifacts the dashboard reads.
Reads scores.parquet and evaluation metrics, writes metrics.json,
segment_stats.json and business_impact.json to the artifacts folder.
"""
import os
import json
import pandas as pd
from datetime import datetime, timezone
from src.pipeline.config import GOLD_PATH, ARTIFACTS_PATH, TARGET_COLUMN
from src.ml_pipeline.evaluate import evaluate_model


def _write_json(name: str, payload: dict) -> None:
    path = os.path.join(ARTIFACTS_PATH, name)
    with open(path, 'w') as f:
        json.dump(payload, f, indent=2)
    print(f'[INSIGHTS] {name} written')


def generate_insights() -> None:
    os.makedirs(ARTIFACTS_PATH, exist_ok=True)
    generated_at = datetime.now(timezone.utc).isoformat()

    # ── 1. Metrics ────────────────────────────────────────────────────────────
    metrics = evaluate_model()
    _write_json('metrics.json', {
        'model':          'LightGBM',
        'representation': 'Aggregated session features',
        'status':         'Pipeline test values - not validated results (see issue 18)',
        'generated_at':   generated_at,
        'performance': {
            'auc_roc':   metrics['auc_roc'],
            'auc_pr':    metrics['auc_pr'],
            'log_loss':  metrics['log_loss'],
            'f1_score':  metrics['f1_score'],
            'precision': metrics['precision'],
            'recall':    metrics['recall']
        },
        'confusion_matrix':   metrics['confusion_matrix'],
        'feature_importance': metrics['feature_importance']
    })

    # ── 2. Segment statistics ─────────────────────────────────────────────────
    scored   = pd.read_parquet(os.path.join(GOLD_PATH, 'scores.parquet'))
    total    = len(scored)
    baseline = float(scored[TARGET_COLUMN].mean())

    segments = {}
    for tier in ['High', 'Medium', 'Low']:
        tier_df = scored[scored['tier'] == tier]
        n       = len(tier_df)
        segments[tier.lower()] = {
            'sessions':        int(n),
            'share':           round(n / total, 4),
            'conversion_rate': round(float(tier_df[TARGET_COLUMN].mean()), 4) if n else 0.0
        }

    _write_json('segment_stats.json', {
        'total_sessions':     int(total),
        'baseline_conv_rate': round(baseline, 4),
        'generated_at':       generated_at,
        'segments':           segments
    })

    # ── 3. Business impact ────────────────────────────────────────────────────
    high_conv = segments['high']['conversion_rate']
    _write_json('business_impact.json', {
        'baseline_conversion_rate':    round(baseline, 4),
        'high_intent_conversion_rate': high_conv,
        'conversion_rate_lift':        round(high_conv / baseline, 2) if baseline else 0.0,
        'generated_at':                generated_at
    })

    print(f'[INSIGHTS] All artifacts written to {ARTIFACTS_PATH}')


if __name__ == '__main__':
    generate_insights()
