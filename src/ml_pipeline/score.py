"""
Scoring — apply trained model to all Gold sessions.
Produces propensity scores and tier assignments for the dashboard.
"""
import os
import pickle
import pandas as pd
from src.pipeline.config import (
    GOLD_PATH, MODEL_PATH, TARGET_COLUMN,
    HIGH_INTENT_THRESHOLD, MEDIUM_INTENT_THRESHOLD
)


def score_sessions() -> pd.DataFrame:
    """
    Load trained model, score all Gold sessions, assign tiers,
    write scores.parquet. Returns the scored DataFrame.
    """
    print('[SCORE] Loading model from disk...')
    with open(os.path.join(MODEL_PATH, 'lgbm_baseline.pkl'), 'rb') as f:
        model = pickle.load(f)
    with open(os.path.join(MODEL_PATH, 'feature_cols.pkl'), 'rb') as f:
        feature_cols = pickle.load(f)

    print('[SCORE] Loading Gold datasets...')
    train = pd.read_parquet(os.path.join(GOLD_PATH, 'train.parquet'))
    test  = pd.read_parquet(os.path.join(GOLD_PATH, 'test.parquet'))
    df    = pd.concat([train, test], ignore_index=True)

    print(f'[SCORE] Scoring {len(df):,} sessions...')
    df['propensity_score'] = model.predict_proba(df[feature_cols])[:, 1]

    df['tier'] = pd.cut(
        df['propensity_score'],
        bins=[-0.001, MEDIUM_INTENT_THRESHOLD, HIGH_INTENT_THRESHOLD, 1.001],
        labels=['Low', 'Medium', 'High']
    )

    scored = df[['user_session', 'propensity_score', 'tier', TARGET_COLUMN]].copy()
    scored.to_parquet(os.path.join(GOLD_PATH, 'scores.parquet'), index=False)

    print('[SCORE] Tier counts:')
    print(scored['tier'].value_counts().to_string())
    print(f'[SCORE] Scores written to {GOLD_PATH}')

    return scored


if __name__ == '__main__':
    score_sessions()
