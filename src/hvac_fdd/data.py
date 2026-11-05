"""Carregamento do dataset elétrico da UFPB (MDPI Data 9(9):106)."""
from __future__ import annotations

from pathlib import Path

import numpy as np

FS = 30_000  # Hz
ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw"
INTERIM = ROOT / "data" / "interim"

CONDITIONS = ["FL", "FI50", "CD30", "CI30", "CI60", "CD30FI50", "CD30CI30", "CI60FI50", "CD30CI60"]

DESCRIPTION = {
    "FL": "Sem falha",
    "FI50": "Filtro evaporador 50%",
    "CD30": "Capacitor -30%",
    "CI30": "Condensador 30%",
    "CI60": "Condensador 60%",
    "CD30FI50": "Capacitor + filtro",
    "CD30CI30": "Capacitor + condensador 30%",
    "CI60FI50": "Condensador 60% + filtro",
    "CD30CI60": "Capacitor + condensador 60%",
}


def load(cond: str) -> tuple[np.ndarray, np.ndarray]:
    """Retorna (corrente [A], tensão [V]) a 30 kHz, com cache em .npy."""
    INTERIM.mkdir(parents=True, exist_ok=True)
    cache = INTERIM / f"{cond}.npy"
    if cache.exists():
        d = np.load(cache)
    else:
        d = np.loadtxt(RAW / f"Dataset_{cond}.txt", skiprows=2, dtype=np.float32)
        np.save(cache, d)
    # O alicate foi instalado invertido (potência média negativa): corrige o sinal.
    return -d[:, 0].astype(np.float64), d[:, 1].astype(np.float64)
