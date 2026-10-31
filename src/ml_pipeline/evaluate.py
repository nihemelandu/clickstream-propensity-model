"""
Model Evaluation — compute performance metrics on Gold test set.
Loads trained model from disk, evaluates on test set,
returns metrics dictionary.
"""
import os
import pickle
import pandas as pd
from sklearn.metrics import (
    roc_auc_score, average_precision_score,
    log_loss, f1_score, precision_score,
    recall_score, confusion_matrix
)
from src.pipeline.config import GOLD_PATH, MODEL_PATH, TARGET_COLUMN


def evaluate_model() -> dict:
    """
    Load trained model and test set from disk.
    Compute performance metrics.
    Returns metrics dictionary.
    """
    # ── Load Model and Feature Columns ────────────────────────────────────────
    print('[EVALUATE] Loading model from disk...')
    with open(os.path.join(MODEL_PATH, 'lgbm_baseline.pkl'), 'rb') as f:
        model = pickle.load(f)

    with open(os.path.join(MODEL_PATH, 'feature_cols.pkl'), 'rb') as f:
        feature_cols = pickle.load(f)

    # ── Load Test Data ────────────────────────────────────────────────────────
    print('[EVALUATE] Loading Gold test dataset...')
    test = pd.read_parquet(os.path.join(GOLD_PATH, 'test.parquet'))
    print(f'[EVALUATE] Test set: {len(test):,} rows')

    X_test = test[feature_cols]
    y_test = test[TARGET_COLUMN]

    # ── Predictions ───────────────────────────────────────────────────────────
    print('[EVALUATE] Generating predictions...')
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    y_pred       = model.predict(X_test)

    # ── Metrics ───────────────────────────────────────────────────────────────
    auc_roc   = roc_auc_score(y_test, y_pred_proba)
    auc_pr    = average_precision_score(y_test, y_pred_proba)
    logloss   = log_loss(y_test, y_pred_proba)
    f1        = f1_score(y_test, y_pred, zero_division=0)
    precision = precision_score(y_test, y_pred, zero_division=0)
    recall    = recall_score(y_test, y_pred, zero_division=0)

    # ── Confusion Matrix ──────────────────────────────────────────────────────
    cm             = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()

    # ── Feature Importance ────────────────────────────────────────────────────
    importance = dict(zip(feature_cols, model.feature_importances_.tolist()))
    total      = sum(importance.values())
    importance = {
        k: round(v / total, 4)
        for k, v in sorted(
            importance.items(), key=lambda x: x[1], reverse=True
        )
    }

    metrics = {
        'auc_roc':   round(auc_roc,   4),
        'auc_pr':    round(auc_pr,    4),
        'log_loss':  round(logloss,   4),
        'f1_score':  round(f1,        4),
        'precision': round(precision, 4),
        'recall':    round(recall,    4),
        'confusion_matrix': {
            'true_positives':  int(tp),
            'false_positives': int(fp),
            'false_negatives': int(fn),
            'true_negatives':  int(tn)
        },
        'feature_importance': importance
    }

    print(f'[EVALUATE] AUC-ROC:   {auc_roc:.4f}')
    print(f'[EVALUATE] AUC-PR:    {auc_pr:.4f}')
    print(f'[EVALUATE] Log Loss:  {logloss:.4f}')
    print(f'[EVALUATE] F1-Score:  {f1:.4f}')
    print(f'[EVALUATE] Precision: {precision:.4f}')
    print(f'[EVALUATE] Recall:    {recall:.4f}')
    print(f'[EVALUATE] Confusion Matrix:')
    print(f'           TP: {tp:,}  FP: {fp:,}')
    print(f'           FN: {fn:,}  TN: {tn:,}')

    return metrics


if __name__ == '__main__':
    evaluate_model()
