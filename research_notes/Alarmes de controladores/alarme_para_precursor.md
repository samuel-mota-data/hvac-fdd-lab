# Do alarme ao sinal precursor

Os alarmes dos controladores (lista em `alarmes_manuais.md`) disparam quando um valor **instantâneo** cruza um limite. Para cada alarme, a tabela abaixo diz:
- qual **tendência** costuma aparecer antes do alarme;
- qual **sensor mínimo** enxerga essa tendência.

Esse é o alvo da predição no gêmeo da câmara fria. As tendências são hipóteses de engenharia, a validar na simulação e em dados reais.

| Alarme do controlador (códigos) | Sinal precursor (tendência antes do alarme) | Sensor mínimo | Evidência |
|---|---|---|---|
| Nível baixo no reservatório / vazamento (AK-PC "Rec. Low liquid level"; AA3) | Subresfriamento ↓; pressão parada ÷ Psat(T amb) ↓; abertura da válvula eletrônica ↑ | P alta + T linha de líquido; ou P parada + T externa | Caso real anônimo: razão 0,93 → 0,41 em ~25 dias antes da parada pelo pressostato. Wijethunga 2024 (subresfriamento, F1 = 1,00 em vazamento catastrófico) |
| Superaquecimento alto / injeção (ASHH; A10; "High superheat") | SH médio ↑ dia a dia com abertura da válvula ↑ (válvula eletrônica) ou com SC ↓ (gás) | P baixa + T sucção | Caso real anônimo: SH 35–44 K × 12 K no controle |
| Superaquecimento baixo / crítico (LSH, LSA, ASHL, ASHC) | Amplitude de oscilação do SH ↑ (válvula "caçando"); SH médio ↓ após degelo | P baixa + T sucção (≥ 1 amostra/min) | Inferência física |
| Pressão de evaporação baixa (LOP, APLo, P0 min) | P0 ↓ com a mesma carga e o mesmo clima; ΔT ar–evaporador ↑ | P baixa (+ T ar) | Inferência física; NIST SP 1087 (TE↓ com subcarga/ar) |
| Temperatura alta na câmara (A1, Athi, HI) | Duty cycle do compressor ↑ para o mesmo clima; tempo de recuperação após porta/degelo ↑ | Corrente do compressor + T caixa | Corrente + T caixa = degrau 0 da câmara fria (relatório de sensores) |
| Degelo terminado por tempo (Max Def.Time, Ed1/Ed2, d04) | Duração do degelo ↑ dia a dia; tempo até a T de fim de degelo ↑ | T evaporador (sensor S2 do controlador) + corrente da resistência | Manual TC-900Ri power (causas); inferência |
| Evaporador congelado (AD Iced) | ΔT ar–evaporador cresce dentro do ciclo e não volta ao normal após o degelo | T ar + T evaporador | Maldonado et al. 2020 (método indireto validado em câmara) |
| Pressão/temperatura de condensação alta (High pressure Pc, A61, AtC) | (Tc − T externa) ↑ ou potência ↑ com a mesma T externa | Medidor elétrico + T externa (API) ou P alta | NIST TN 1648 (+6 a +11 % de potência com condensador sujo) |
| Temperatura de descarga alta (High disch. temp.) | T descarga − valor esperado ↑; acompanha SH de sucção ↑ | 1 termistor na descarga | NIST TN 1648 (T descarga = variável mais sensível a excesso de carga) |
| Desarme de segurança do compressor (motor prot., over current) | Partidas por hora ↑ (ciclo curto); corrente vs RLA ↑; desequilíbrio de tensão | Medidor elétrico ≥ 1 Hz | Armstrong et al. 2006 |

## Economia de energia (não é alarme)

| Oportunidade | Sinal | Sensor |
|---|---|---|
| Degelo por demanda (pular ou encurtar) | ΔT ar–evaporador ainda baixo na hora do degelo programado; dia frio/seco, poucas aberturas de porta | T ar + T evaporador + chave de porta (+ umidade externa via API) |
| Válvula termostática desregulada | SH alto com SC normal, estável ao longo de dias | P baixa + T sucção + T linha de líquido |
| Setpoint de condensação flutuante | Pc acima do necessário em dias frios | P alta + T externa |
