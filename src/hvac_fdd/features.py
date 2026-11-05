"""Extração de features elétricas por janela.

Grupos de features (cada um responde a uma pergunta do estudo):
- smart_breaker: o que um disjuntor inteligente comum já entrega (RMS, potência, FP).
- harmonics:     assinatura espectral da corrente (FFT), relativa à fundamental.
- sacdm:         densidade de máximos locais (SAC-DM, Medeiros et al. 2018).
- voltage_ctrl:  só a TENSÃO da rede. A falha não deveria aparecer aqui;
                 se o modelo acertar com isso, ele está reconhecendo a sessão
                 de gravação, não a falha (teste de confusão).
"""
from __future__ import annotations

import numpy as np

HARMONICS = range(2, 12)


def density_of_maxima(x: np.ndarray) -> float:
    """SAC-DM: fração de amostras que são máximos locais estritos."""
    return float(np.mean((x[1:-1] > x[:-2]) & (x[1:-1] > x[2:])))


def _harmonic_amps(x: np.ndarray, fs: float) -> tuple[float, float, np.ndarray]:
    n = len(x)
    spec = np.abs(np.fft.rfft(x * np.hanning(n))) * 2 / (n * 0.5)
    freqs = np.fft.rfftfreq(n, 1 / fs)
    band = (freqs > 55) & (freqs < 65)
    f0 = freqs[band][np.argmax(spec[band])]

    def amp(fc: float) -> float:
        b = np.abs(freqs - fc) <= 2
        return float(spec[b].max()) if b.any() else 0.0

    a1 = amp(f0)
    hs = np.array([amp(k * f0) if k * f0 < fs / 2 else 0.0 for k in HARMONICS])
    return f0, a1, hs


def window_features(i: np.ndarray, v: np.ndarray, fs: float) -> dict[str, float]:
    irms = float(np.sqrt(np.mean(i**2)))
    vrms = float(np.sqrt(np.mean(v**2)))
    p = float(np.mean(i * v))
    f: dict[str, float] = {
        "sb_irms": irms,
        "sb_vrms": vrms,
        "sb_p": p,
        "sb_pf": p / (irms * vrms),
        # versões normalizadas pela tensão: removem a variação da rede
        "norm_admittance": irms / vrms,
        "norm_conductance": p / vrms**2,
    }
    _, a1, hs = _harmonic_amps(i, fs)
    f["h_i1"] = a1
    f["h_thd"] = float(np.sqrt(np.sum(hs**2)) / a1)
    for k, h in zip(HARMONICS, hs):
        f[f"h_i{k}_rel"] = h / a1
    f["sacdm_i"] = density_of_maxima(i)
    _, va1, vhs = _harmonic_amps(v, fs)
    f["vctrl_vrms"] = vrms
    f["vctrl_thd"] = float(np.sqrt(np.sum(vhs**2)) / va1)
    for k, h in zip(range(3, 8, 2), vhs[1:6:2]):
        f[f"vctrl_v{k}_rel"] = h / va1
    f["vctrl_sacdm_v"] = density_of_maxima(v)
    return f


FEATURE_SETS: dict[str, list[str]] = {
    "1_rms_corrente": ["sb_irms"],
    "2_disjuntor_inteligente": ["sb_irms", "sb_vrms", "sb_p", "sb_pf"],
    "3_normalizado_tensao": ["norm_admittance", "norm_conductance", "sb_pf"],
    "4_harmonicos_fft": ["h_thd"] + [f"h_i{k}_rel" for k in HARMONICS],
    "5_sacdm": ["sacdm_i"],
    "6_norm+fft+sacdm": ["norm_admittance", "norm_conductance", "sb_pf", "h_thd", "sacdm_i"]
    + [f"h_i{k}_rel" for k in HARMONICS],
    "X_controle_so_tensao": ["vctrl_vrms", "vctrl_thd", "vctrl_v3_rel", "vctrl_v5_rel", "vctrl_v7_rel", "vctrl_sacdm_v"],
}
