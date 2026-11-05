# Dados

## raw/ — UFPB split-system AC electrical dataset

- **Fonte:** de Oliveira, A.C. et al. *Analysis of Split-System Air Conditioner Faults through Electrical Measurement Data*. Data 2024, 9(9), 106. https://doi.org/10.3390/data9090106
- **Arquivo:** `data-09-00106-s001.zip` (material suplementar S1), baixado em 2026-11-05
- **Licença dos dados:** CC-BY-NC (uso não comercial, com atribuição)
- **Equipamento:** split Agratto 18.000 BTU, 220 V, capacitor original de 35 µF, instalado em campo (UFPB, João Pessoa)
- **Aquisição:** SCT-013 (corrente) + transformador (tensão), DAQ NI USB-6215, 30 kHz, 62 s por condição (1.860.000 amostras)
- **Formato:** `.txt`, 2 linhas de cabeçalho, colunas `Current` (A) e `Voltage` (V)

| Arquivo | Condição |
|---|---|
| FL | Sem falha |
| CI30 / CI60 | Entrada de ar do condensador obstruída em 30% / 60% |
| FI50 | Filtro do evaporador obstruído em 50% |
| CD30 | Capacitor do compressor degradado ~30% (35 → 25 µF) |
| CD30CI30, CD30CI60, CD30FI50, CI60FI50 | Falhas duplas |

**Observação:** o artigo diz que a coleta foi repetida 3 vezes, mas o arquivo publicado tem **uma única gravação por condição**. Isso limita a validação (ver notas do projeto).

Os arquivos brutos não vão para o git (ver `.gitignore`).
