# model.py
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_outliers(df: pd.DataFrame, feature_cols: list, contamination: float = 0.05, random_state: int = 42):
    """
    Runs IsolationForest and returns a copy of df with 'outlier' (bool) and 'anomaly_score' columns.
    """
    df = df.copy()
    if len(feature_cols) == 0:
        raise ValueError("feature_cols must include at least one column")

    X = df[feature_cols].fillna(0).values

    iso = IsolationForest(contamination=contamination, random_state=random_state)

    preds = iso.fit_predict(X)  # -1 = outlier, 1 = inlier
    df['outlier'] = (preds == -1)
    df['anomaly_score'] = -iso.decision_function(X)  # higher = more anomalous

    return df
