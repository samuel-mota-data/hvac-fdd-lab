# hvac-fdd-lab

Diagnóstico e prognóstico de falhas em ar-condicionado **só com medição elétrica** (sensor mínimo).

| Fase | O quê | Onde |
|---|---|---|
| 1 | Análise do dataset elétrico real da UFPB (9 condições, 30 kHz): quais features separam as falhas, e o teste de confusão por sessão | `src/hvac_fdd/`, [NOTAS_FASE1.md](NOTAS_FASE1.md) |
| 2 | Gêmeo digital do split (R410A + motor PSC) calibrado com a UFPB: falhas injetadas, proteção do compressor, prognóstico | painel interativo em samuel.simia.digital/lab |

## Rodar a fase 1

```bash
pip install -e .
cd src && python -m hvac_fdd.experiment
pytest
```

Os dados brutos não estão no repositório (licença CC-BY-NC): ver [data/README.md](data/README.md).
