"""
Pipeline configuration — paths, parameters, and constants.
All pipeline components import from here.
"""
import os

# ── Data Paths ────────────────────────────────────────────────────────────────
# Update DRIVE_PATH to match your Google Drive mount point in Colab
DRIVE_PATH = '/content/drive/MyDrive/clickstream-propensity-model'

RAW_PATH    = f'{DRIVE_PATH}/data/raw'
BRONZE_PATH = f'{DRIVE_PATH}/data/processed/bronze'
SILVER_PATH = f'{DRIVE_PATH}/data/processed/silver'
GOLD_PATH   = f'{DRIVE_PATH}/data/processed/gold'

# ── Source Files ──────────────────────────────────────────────────────────────
RAW_FILES = [
    '2019-Oct.parquet',
    '2019-Nov.parquet'
]

# ── Sampling ──────────────────────────────────────────────────────────────────
SAMPLE_FRACTION = 0.05
RANDOM_SEED     = 42

# ── Model ─────────────────────────────────────────────────────────────────────
TARGET_COLUMN    = 'has_purchase'
TEST_SIZE        = 0.10
MODEL_PATH       = f'{DRIVE_PATH}/models/sprint_1b'

# ── Dashboard Artifacts ───────────────────────────────────────────────────────
ARTIFACTS_PATH = f'{DRIVE_PATH}/dashboard/artifacts'

# ── Segmentation Thresholds ───────────────────────────────────────────────────
HIGH_INTENT_THRESHOLD   = 0.7
MEDIUM_INTENT_THRESHOLD = 0.3

# ── Pipeline Settings ─────────────────────────────────────────────────────────
CHUNK_SIZE = 500_000
