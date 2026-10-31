"""
Model Training — LightGBM classifier on aggregated session features.
Sprint 1b baseline: default parameters, no PSO, no hyperparameter tuning.
Saves trained model to disk for use by evaluate, score, and insights stages.
"""
import os
import pickle
import pandas as pd
import lightgbm as lgb
from src.pipeline.config import (
    GOLD_PATH, MODEL_PATH, TARGET_COLUMN
)


def train_model() -> tuple:
    """
    Load Gold train dataset, train LightGBM classifier,
    save model to disk.
    Returns (model, feature_cols).
    """
    os.makedirs(MODEL_PATH, exist_ok=True)

    # ── Load Train Data ───────────────────────────────────────────────────────
    print('[TRAIN] Loading Gold train dataset...')
    train = pd.read_parquet(os.path.join(GOLD_PATH, 'train.parquet'))
    print(f'[TRAIN] Train set: {len(train):,} rows')
    print(f'[TRAIN] Purchase rate: {train[TARGET_COLUMN].mean():.4f}')

    # ── Define Features ───────────────────────────────────────────────────────
    # Drop non-feature columns
    drop_cols    = ['user_session', TARGET_COLUMN, 'purchase_count']
    feature_cols = [c for c in train.columns if c not in drop_cols]

    X_train = train[feature_cols]
    y_train = train[TARGET_COLUMN]

    print(f'[TRAIN] Features ({len(feature_cols)}): {feature_cols}')

    # ── Train Model ───────────────────────────────────────────────────────────
    print('[TRAIN] Training LightGBM — Sprint 1b baseline...')

    model = lgb.LGBMClassifier(
        n_estimators=100,
        learning_rate=0.1,
        num_leaves=31,
        class_weight='balanced',
        random_state=42,
        verbose=-1
    )

    model.fit(X_train, y_train)
    print('[TRAIN] Training complete')

    # ── Save Model and Feature Columns ────────────────────────────────────────
    model_file    = os.path.join(MODEL_PATH, 'lgbm_baseline.pkl')
    features_file = os.path.join(MODEL_PATH, 'feature_cols.pkl')

    with open(model_file, 'wb') as f:
        pickle.dump(model, f)

    with open(features_file, 'wb') as f:
        pickle.dump(feature_cols, f)

    print(f'[TRAIN] Model saved to {model_file}')
    print(f'[TRAIN] Feature columns saved to {features_file}')

    return model, feature_cols


if __name__ == '__main__':
    train_model()
