# Fase 1 — Só a parte elétrica revela as falhas?

Dados: UFPB (MDPI Data 9(9):106), split 18k BTU, 9 condições × 62 s, 30 kHz.
Código: `src/hvac_fdd/` · rodar com `python -m hvac_fdd.experiment` (de `src/`) · testes com `pytest`.

## Protocolo
- Janelas de 1 s. **Split temporal:** treino em 0–40 s, teste em 42–62 s (2 s de guarda), comparado a um split aleatório (vazado).
- Taxas: 30 kHz, 5 kHz, 1 kHz (reamostragem polifásica).
- Grupos de features: RMS da corrente; "disjuntor inteligente" (Irms, Vrms, P, FP); normalizado pela tensão; harmônicos da corrente (FFT); SAC-DM (densidade de máximos); **controle só com tensão**.
- Modelos: regressão logística e random forest; métrica: acurácia balanceada.

## Resultados (melhor modelo, split temporal)

| Features | 30 kHz | 5 kHz | 1 kHz |
|---|---|---|---|
| Só RMS da corrente | 0,88 | 0,88 | 0,89 |
| Disjuntor inteligente | 1,00 | 1,00 | 1,00 |
| Normalizado pela tensão | 0,94 | 0,96 | 0,96 |
| Harmônicos (FFT) | 1,00 | 1,00 | 1,00 |
| SAC-DM (implementação simples) | 0,69 | 0,53 | 0,51 |
| **Controle: só tensão** | **0,99** | **0,96** | **0,97** |

Detecção (falha vs sem falha) = 1,00 em quase todos os grupos.

## Achados
1. **Confusão por sessão.** Um modelo que só vê a tensão da rede diagnostica as falhas com 96–99%. Cada condição foi gravada uma única vez, em um momento diferente, então as classes são separáveis pela sessão. **Acurácia de ~100% neste dataset não prova, sozinha, que o modelo detecta a falha**, e isso vale também para os resultados publicados.
2. **A física sustenta as falhas grandes.** Entre sessões, a tensão variou no máximo 2,2%, o que explicaria cerca de ±2% na corrente. As falhas de condensador e capacitor deslocam a corrente de 8% a 40%, de 4 a 18 vezes mais. Esse efeito é real e grande.
3. **A falha sutil é ambígua.** Filtro do evaporador 50% = +3,2% de corrente. Isso fica na mesma ordem de efeitos de sessão não medidos (temperatura externa e interna), então não é conclusivo com estes dados.
4. **1 kHz basta** para tudo o que funcionou. Isso aproxima o método de hardware barato (ESP32) e de medidores de energia.
5. **SAC-DM** na implementação simples (fração de máximos locais no sinal bruto) ficou bem abaixo do artigo. Pode depender de pré-processamento não descrito no resumo. Falta conferir no texto completo.

## Próximo passo que esses achados exigem
Um experimento **intercalado** (sem falha → falha → sem falha → falha…), variando clima e tensão de forma controlada, feito **em simulação**: um gêmeo digital do split calibrado com estes dados, já que não há bancada física. Validação externa em datasets públicos com potência elétrica (NIST, ASHRAE RP-1043).
