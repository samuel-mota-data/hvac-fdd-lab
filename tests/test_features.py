import numpy as np
import pytest

from hvac_fdd.features import density_of_maxima, window_features


def test_density_of_maxima_pure_sine():
    fs, f = 30_000, 60
    t = np.arange(fs) / fs
    # 60 ciclos em 1 s → 60 máximos em 30k amostras
    assert density_of_maxima(np.sin(2 * np.pi * f * t)) == pytest.approx(60 / (fs - 2), rel=0.02)


def test_harmonics_and_power_on_synthetic_load():
    fs = 5_000
    t = np.arange(fs) / fs
    v = 220 * np.sqrt(2) * np.sin(2 * np.pi * 60 * t)
    # corrente com 10% de 3ª harmônica, em fase com a tensão
    i = 7 * np.sqrt(2) * (np.sin(2 * np.pi * 60 * t) + 0.10 * np.sin(2 * np.pi * 180 * t))
    f = window_features(i, v, fs)
    assert f["sb_vrms"] == pytest.approx(220, rel=1e-3)
    assert f["h_i3_rel"] == pytest.approx(0.10, rel=0.03)
    assert f["h_i5_rel"] < 0.01
    assert f["sb_p"] == pytest.approx(220 * 7, rel=1e-3)
    assert f["norm_admittance"] == pytest.approx(f["sb_irms"] / 220, rel=1e-3)
