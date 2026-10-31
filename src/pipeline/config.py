"""
Pipeline configuration — paths, parameters, and constants.
All pipeline components import from here.
Update paths to match your local environment.
"""
import os

# ── Base Path ─────────────────────────────────────────────────────────────────
# Root of the repository — works regardless of where script is run from
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ── Data Paths ────────────────────────────────────────────────────────────────
SILVER_PATH = os.path.join(BASE_PATH, 'data', 'processed', 'silver')
GOLD_PATH   = os.path.join(BASE_PATH, 'data', 'processed', 'gold')

# ── Artifact Path — dashboard reads from here ─────────────────────────────────
ARTIFACTS_PATH = os.path.join(BASE_PATH, 'artifacts')

# ── Model Path ────────────────────────────────────────────────────────────────
MODEL_PATH = os.path.join(BASE_PATH, 'models')

# ── Input File ───────────────────────────────────────────────────────────────
SILVER_FILE = os.path.join(SILVER_PATH, 'sessions_clean.parquet')

# ── Sampling ──────────────────────────────────────────────────────────────────
RANDOM_SEED = 42

# ── Model ─────────────────────────────────────────────────────────────────────
TARGET_COLUMN = 'has_purchase'
TEST_SIZE     = 0.10

# ── Segmentation Thresholds ───────────────────────────────────────────────────
HIGH_INTENT_THRESHOLD   = 0.7
MEDIUM_INTENT_THRESHOLD = 0.3

# ── Pipeline Settings ─────────────────────────────────────────────────────────
CHUNK_SIZE = 500_000
