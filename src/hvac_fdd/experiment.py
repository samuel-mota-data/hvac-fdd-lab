"""Fase 1: o quanto só a parte elétrica revela das falhas?

Uso:  python -m hvac_fdd.experiment
Saída: results/phase1_*.csv
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.signal import resample_poly
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from .data import CONDITIONS, FS, ROOT, load
from .features import FEATURE_SETS, window_features

WIN_S = 1.0
TRAIN_END_S = 40.0  # janelas que começam antes disso → treino
TEST_START_S = 42.0  # 2 s de intervalo de guarda → teste
RATES = [30_000, 5_000, 1_000]
SEED = 0


def build_table() -> pd.DataFrame:
    rows = []
    for cond in CONDITIONS:
        i30, v30 = load(cond)
        for fs in RATES:
            q = FS // fs
            i = resample_poly(i30, 1, q) if q > 1 else i30
            v = resample_poly(v30, 1, q) if q > 1 else v30
            w = int(WIN_S * fs)
            for k in range(len(i) // w):
                f = window_features(i[k * w : (k + 1) * w], v[k * w : (k + 1) * w], fs)
                f.update(cond=cond, fs=fs, t0=k * WIN_S)
                rows.append(f)
        print(f"  features ok: {cond}")
    return pd.DataFrame(rows)


def models():
    return {
        "logistica": make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000)),
        "random_forest": RandomForestClassifier(n_estimators=300, random_state=SEED),
    }


def evaluate(df: pd.DataFrame) -> pd.DataFrame:
    out = []
    for fs, d in df.groupby("fs"):
        temporal_tr = d[d.t0 < TRAIN_END_S]
        temporal_te = d[d.t0 >= TEST_START_S]
        leaky_tr, leaky_te = train_test_split(d, test_size=0.33, random_state=SEED, stratify=d.cond)
        splits = {"temporal": (temporal_tr, temporal_te), "aleatorio_vazado": (leaky_tr, leaky_te)}
        for fset, cols in FEATURE_SETS.items():
            for split, (tr, te) in splits.items():
                for mname, model in models().items():
                    model.fit(tr[cols], tr.cond)
                    pred = model.predict(te[cols])
                    diag = balanced_accuracy_score(te.cond, pred)
                    det = balanced_accuracy_score(te.cond != "FL", pred != "FL")
                    out.append(dict(fs=fs, features=fset, split=split, modelo=mname, diagnostico=diag, deteccao=det))
    return pd.DataFrame(out)


def main() -> None:
    res_dir = ROOT / "results"
    res_dir.mkdir(exist_ok=True)
    print("Extraindo features...")
    table = build_table()
    table.to_csv(res_dir / "phase1_features.csv", index=False)
    res = evaluate(table)
    res.to_csv(res_dir / "phase1_results.csv", index=False)
    pd.set_option("display.width", 200)
    best = res.groupby(["fs", "features", "split"])[["diagnostico", "deteccao"]].max().round(3)
    print(best.unstack("split").to_string())


if __name__ == "__main__":
    main()
