"""
Feature Engineering — Silver to Gold transformation.
Computes aggregated session-level features from event-level Silver data.
Produces train and test sets ready for model training.
"""
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.pipeline.config import (
    SILVER_FILE, GOLD_PATH,
    TARGET_COLUMN, TEST_SIZE, RANDOM_SEED
)


def build_features() -> tuple:
    """
    Load Silver data, engineer aggregated session features,
    split into train and test sets, write to Gold layer.
    Returns (train, test) DataFrames.
    """
    os.makedirs(GOLD_PATH, exist_ok=True)

    print('[FEATURES] Loading Silver dataset...')
    df = pd.read_parquet(SILVER_FILE)
    print(f'[FEATURES] Loaded {len(df):,} rows, {df.shape[1]} columns')

    # Parse event_time
    df['event_time'] = pd.to_datetime(df['event_time'], utc=True)

    # ── Aggregated Session Features ───────────────────────────────────────────
    print('[FEATURES] Engineering aggregated session features...')

    agg = df.groupby('user_session').agg(
        event_count    =('event_type', 'count'),
        view_count     =('event_type', lambda x: (x == 'view').sum()),
        cart_count     =('event_type', lambda x: (x == 'cart').sum()),
        purchase_count =('event_type', lambda x: (x == 'purchase').sum()),
        product_count  =('product_id', 'nunique'),
        brand_count    =('brand', 'nunique'),
        avg_price      =('price', 'mean'),
        session_start  =('event_time', 'min'),
        session_end    =('event_time', 'max'),
        has_purchase   =(TARGET_COLUMN, 'max')
    ).reset_index()

    # Session duration in seconds
    agg['session_duration_sec'] = (
        agg['session_end'] - agg['session_start']
    ).dt.total_seconds()

    # Temporal features
    agg['day_of_week']        = agg['session_start'].dt.dayofweek
    agg['session_start_hour'] = agg['session_start'].dt.hour
    agg['is_weekend']         = agg['day_of_week'].isin([5, 6]).astype(int)

    # Drop datetime columns — not needed for modeling
    agg = agg.drop(columns=['session_start', 'session_end'])

    print(f'[FEATURES] Gold dataset — {len(agg):,} sessions, {agg.shape[1]} features')
    print(f'[FEATURES] Purchase rate: {agg[TARGET_COLUMN].mean():.4f}')
    print(f'[FEATURES] Features: {[c for c in agg.columns if c not in ["user_session", TARGET_COLUMN]]}')

    # ── Train / Test Split ────────────────────────────────────────────────────
    train, test = train_test_split(
        agg,
        test_size=TEST_SIZE,
        stratify=agg[TARGET_COLUMN],
        random_state=RANDOM_SEED
    )

    # Write to Gold
    train.to_parquet(os.path.join(GOLD_PATH, 'train.parquet'), index=False)
    test.to_parquet(os.path.join(GOLD_PATH, 'test.parquet'),  index=False)

    print(f'[FEATURES] Train set: {len(train):,} rows')
    print(f'[FEATURES] Test set:  {len(test):,} rows')
    print(f'[FEATURES] Train purchase rate: {train[TARGET_COLUMN].mean():.4f}')
    print(f'[FEATURES] Test purchase rate:  {test[TARGET_COLUMN].mean():.4f}')
    print(f'[FEATURES] Gold layer written to {GOLD_PATH}')

    return train, test


if __name__ == '__main__':
    build_features()
