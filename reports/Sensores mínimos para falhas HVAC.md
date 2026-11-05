# Corrente sozinha não basta: falta temperatura

Nenhum sensor isolado cobre as dez falhas. **O conjunto mínimo com a melhor evidência publicada é um medidor elétrico de baixa taxa (Irms, P, FP, V a cerca de 1 Hz) mais 2 a 3 termistores no ciclo, sendo a temperatura de descarga o primeiro.** O medidor elétrico pega bem quatro coisas: excesso de carga (+12 a +22 % de potência com 30 % a mais de carga), condensador sujo (+6 a +11 %), capacitor e os eventos que matam o compressor (short cycling, rotor bloqueado, perda de fase). Ele é quase cego a restrição na linha de líquido (≈0 % com 48 % de restrição), subcarga leve, filtro/evaporador e vazamento de válvula. Essas falhas só aparecem nas temperaturas do ciclo (superaquecimento e subresfriamento) ou no transitório de partida amostrado em kHz ([NIST TN 1648][TN1648]; [Armstrong et al. 2006][ARM]). O alicate de alta taxa agrega de verdade só em compressor alternativo de velocidade fixa: há detecção de vazamento de palheta com 1,4 % da área do orifício a 8 kHz ([Schantz & Leeb 2012][SCH]). Em split inverter, esse ganho some ([Shaw et al. 2002][SHAW]). Vibração e acústica não têm estudo publicado com falhas impostas e quantificadas em split ou câmara fria. A exceção é o ultrassom para vazamento de R290 (4 a 13 g/min) ([Colbourne & Vonsild][COL]). A análise própria do dataset UFPB acrescenta um alerta para a entrevista: **acurácias de ~100 % em dados elétricos de split não provam detecção de falha.** Um modelo que vê só a tensão da rede acerta 96–99 % porque cada condição é uma sessão única de gravação. Para validar um gêmeo digital com licença comercial, os datasets úteis são o LBNL RTU (CC BY 4.0), o ORNL CO2 (CC BY 4.0) e o NIST 14/16 SEER (obra do governo dos EUA). O UFPB é o único com forma de onda de split e capacitor, mas é **CC-BY-NC**.

**Legenda de evidência:** ●●● forte experimental (laboratório, falha quantificada) · ●● moderada (um estudo, campo sem repetição, ou detecção sem números) · ● fraca (patente, guia de serviço, direção sem magnitude, inferência física) · ✕ testado e não detecta · ? sem evidência encontrada.

## Matriz falha × sensor: temperatura domina, elétrico vence em quatro falhas

Tipos de sensor comparados nas colunas:
- **Medidor baixa taxa:** Irms, P, Q, FP a cerca de 1 Hz ou mais lento (disjuntor inteligente ou smart meter).
- **Alicate alta taxa:** 4 a 30 kHz, com transitório de partida, harmônicas e MCSA.
- **T ciclo:** termistores de superfície para descarga, sucção, linha de líquido, temperatura bifásica (saturação) e ΔT do ar nas serpentinas.

| Falha | Medidor baixa taxa | Alicate alta taxa | T ciclo | Pressão | Vibração | Acústico/ultrassom |
|---|---|---|---|---|---|---|
| **Condensador sujo** | ●●● P↑ (+5,8 a +10,8 % com 30 % de ar a menos [TN1648]; é a única falha que eleva a potência total de forma visível [HJO]); Irms +12,6 % (CI30) e +27,3 % (CI60) [PRÓPRIA] | ●● transitório do ventilador do condensador com 14 % de bloqueio, em ~10 partidas [ARM] | ●●● TC↑ TD↑ Tsc↓ [SP1087] | ●● aumenta a precisão de TC [SP1087] | ? | ? |
| **Fluxo de ar no evaporador / filtro** | ● neutro ou queda de poucos % no compressor [N7350]; FI50 medido +3,2 % contra −2 % previsto pela física, indistinguível [PRÓPRIA] | ●● Q do ventilador interno 437→428 VAR com 10 % de bloqueio, em ~10 partidas; a densidade do ar confunde [ARM] | ●●● TE↓ TC↓ ΔT_ar_evap↑ [SP1087] | ● | ? | ? |
| **Vazamento / baixa carga** | ● −2,9 a −6,6 % com 30 % [TN1648]; **direção conflita** (veja a seção de conflitos) | ●● transitório de partida distinto com 20 % de subcarga [ARM] | ●●● Tsc↓ é o 1º sinal com TXV; 4 temperaturas estimam a carga a ±10 % [KB13]; Tsh↑ só em nível alto [SP1087] | ●● subresfriamento com F1 = 1,00 em vazamento catastrófico de supermercado [WIJ] | ? | ●● ultrassom detecta 4–13 g/min de R290 dentro da evaporadora, mas correlaciona mal com a vazão [COL] |
| **Excesso de carga** | ●●● +11,7 a +22,1 % com 30 % [TN1648]; +18 % com +20 % em RTU [ARM] | ●●● ângulo de fase 0,794→0,711 rad; detecção em ~10 partidas [ARM] | ●●● TD é a variável mais sensível [TN1648] | ●● | ? | ? |
| **Capacitor do motor (PSC)** | ●● Irms +9,5 % com 35→25 µF, em campo, 1 gravação [PRÓPRIA]; FP↓ + I↑ (só em patente) [P9310] | ●● FFT e análise caótica no dataset UFPB [UFPB][IIR-UFPB], **mas confundidas com a sessão de gravação** [PRÓPRIA] | ✕ não aplicável | ✕ | ? | ? |
| **Válvula / desgaste do compressor** | ● −4,4 a −5,5 % com 12 % de bypass [TN1648]; quase nada em regime [ARM] | ●●● partida 2–5× mais sensível que o regime [ARM]; palheta de sucção com 1,4 % de área a 8 kHz (compressor alternativo) [SCH] | ●●● TE↑ TD↑ Tsc↓ [SP1087]; CMF de 2,5 % não detectado | ●● | ●● compressor rotativo desmontado separa palheta e válvula, sem taxa de acerto [NIV] | ● emissão acústica é citada como alternativa, com desvantagens [ASME19] |
| **Não condensáveis** | ● Wcmp↑, só a direção [N7350] | ? não testado [ARM] | ●● TC↑, confundível com condensador sujo e excesso de carga [N7350] | ● P_desc > Psat(T_cond medida) é a assinatura direta (inferência física) [N7350] | ? | ? |
| **Restrição na linha de líquido** | ✕ 0,0 a +1,1 % com 45–48 % [TN1648] | ? não testado [ARM] | TXV: ✕ até a TXV saturar (13 % foi classificado como "sem falha") [SP1087]; orifício fixo: ●● Tsh↑ Tsc↑ [SP1087] | ● ΔP na linha seria o sensor direto (inferência) | ? | ? |
| **Gelo / degelo** | ● queda de corrente dispara o degelo (patente) [P4104]; ausência do "vale" periódico de degelo (inferência) | ● potência do ventilador do evaporador (patente) [P4831] | ●●● ΔT ar–evaporador; método indireto validado em walk-in freezer [MAL]; o gelo muda features em >50 % [TN1648] | ●● superaquecimento e perda de carga do ar [CORE] | ? | ? |
| **Porta aberta (câmara fria)** | ● duty cycle↑ (inferência; o dataset ORNL tem rótulos 5/10/15 % mas sem resultado publicado de FDD só por potência) [ORNL] | ? | ●● T_caixa [ORNL] | ✕ | ? | ? |

Mesmo onde o elétrico é ●●●, ele só funciona com **modelo de referência normalizado por clima**. A potência do compressor depende fortemente da temperatura externa ([NISTIR 7350][N7350]). O efeito de uma falha subtrativa (−3 a −7 %) tem a mesma ordem de poucos °C de variação externa. Por isso a abordagem "potência total + T externa" falhou em RTUs de campo: a sensibilidade em regime "não é suficiente dada a incerteza de medição" ([Hjortland et al. 2016][HJO]).

**Falhas que o elétrico vê e o termistor não vê.** Essas falhas respondem pela maior parte dos danos ao enrolamento: 76 % dos sinistros de compressor são elétricos, e 87 % deles são de enrolamento ([Armstrong et al. 2006][ARM], citando Stouppe & Lau).

| Evento que mata compressor | Baixa taxa | Alta taxa | Fonte |
|---|---|---|---|
| Short cycling (incluindo partidas incompletas) | ●● contagem de partidas, com ≥1 Hz | ●●● intervalo e forma do inrush | [ARM] |
| Rotor bloqueado / partida lenta / falha de partida | ●● | ●●● | [ARM] Tab. 2 |
| Perda de fase / tensão desequilibrada | ●● | ●●● | [ARM] Tab. 2 |
| Contator com defeito | ✕ | ●●● ciclo de rede com corrente zero | [SHAW] |
| Partida afogada / slugging | ✕ | ●● difícil; 5–10 % do deslocamento mexe pouco em P1 | [ARM] |
| Rolamento do compressor | ✕ | ● a corrente é "significativamente mais difícil" que a vibração | [OBA] |

## Escada de sensores: descarga primeiro, pressão por último

A escada abaixo ordena os sensores pelo ganho de cobertura **das falhas que danificam o compressor**: superaquecimento do compressor, retorno de líquido, sobrecarga elétrica e carga errada. A ordenação é síntese própria a partir da matriz. As fontes estão nas células.

### Split residencial on-off (compressor PSC monofásico, típico no Brasil)

| Degrau | Adiciona | Falhas que passa a cobrir | Por que nessa ordem |
|---|---|---|---|
| **0 – mínimo** | Medidor/disjuntor inteligente (Irms, P, FP, V a 1 Hz) + T externa (API de clima) | Excesso de carga, condensador sujo, capacitor (FP/Irms), short cycling, rotor bloqueado, subtensão | O mesmo hardware cobre 4 falhas ●●/●●● e todos os eventos elétricos; a T externa é obrigatória para normalizar [N7350][HJO] |
| **1** | T de descarga (1 termistor) | Superaquecimento do compressor; é a variável mais sensível a excesso de carga [TN1648] e sobe também com condensador sujo, não condensáveis e vazamento de válvula [SP1087] | Protege diretamente o compressor; um só ponto |
| **2** | T de sucção + T bifásica do evaporador (→ superaquecimento) | Vazamento/subcarga (com orifício fixo, Tsh é muito informativo), fluxo de ar no evaporador/filtro, retorno de líquido | Cobre o ponto cego do elétrico: subcarga e filtro [SP1087] |
| **3** | T da linha de líquido + T bifásica do condensador (→ subresfriamento) | Carga a ±10 % (sensor virtual de carga, VRC) [KB13]; separa subcarga de vazamento de válvula [SP1087] | O NIST mostra que 2 temperaturas bastam para monitorar a carga em sistema TXV [TN1648] |
| **4** | Alicate de alta taxa (≥1–8 kHz, captura por evento de partida) | Vazamento de válvula, subcarga pelo transitório, contator, slugging | Evidência ●●● só em compressor alternativo/RTU [ARM][SCH]. Para rotativo e scroll só há patentes [P11280]. No UFPB, **1 kHz bastou** para todas as features que funcionaram [PRÓPRIA] |
| **5** | Transdutores de pressão de sucção e descarga | Não condensáveis, restrição na linha de líquido, mais precisão no superaquecimento e no subresfriamento | O NIST recomenda pressão para precisão [SP1087], mas é invasivo (exige acesso ao circuito); existem sensores virtuais de pressão [VPS] |
| — | Vibração / acústico | Rolamento; ultrassom para vazamento de R290 | ? sem estudo publicado em split com falhas quantificadas |

**Ressalva para inverter.** Nesse caso a escada muda. O drive compensa a falha e a rotação vira a feature-chave ([SP1087][SP1087]). O transitório de partida perde utilidade porque a partida é "lenta e complexa" ([Shaw et al. 2002][SHAW]). O degrau 0 só funciona condicionado à frequência do compressor, lida da própria unidade. Não há estudo revisado por pares com split inverter e falhas impostas (lacuna).

### Câmara fria comercial (unidade condensadora + controlador digital)

| Degrau | Adiciona | Falhas que passa a cobrir | Por que nessa ordem |
|---|---|---|---|
| **0 – mínimo** | Corrente/potência do compressor (≥1 Hz) + T_caixa + T_evaporador lidas do controlador existente + chave de porta | Short cycling, porta aberta, falha de degelo (falta do padrão periódico), gelo (ΔT ar–evaporador), condensador sujo (P↑), tendência de runtime | O controlador Full Gauge (supervisão Sitrad) já entrega T_caixa, T_evaporador e às vezes pressão e tensão via RS-485 [ROB]; só falta a corrente. Conjunto de inferência; **não há validação publicada de FDD só por potência em câmara fria** |
| **1** | T da linha de líquido + P de descarga (→ subresfriamento) | Vazamento: subresfriamento com F1 = 1,00 no catastrófico; vazamento lento só pelo COP (F1 0,92 em até 5 dias) [WIJ]; >1 % de perda com receptor monitorado [ASS] | Vazamento é a falha mais cara e mais documentada: média de 39 %/ano de recarga em 214 lojas brasileiras [LIN] |
| **2** | T + P de sucção (→ superaquecimento) | Retorno de líquido (floodback), hunting da válvula de expansão, gelo | O floodback é indistinguível sem T de sucção; ele lava o óleo do compressor [MEI] |
| **3** | Alicate de alta taxa | Vazamento de válvula (≥1,4 % de área), partida afogada após degelo (flooded start) [HVS], contator | Sobe na prioridade quando o compressor é **alternativo**, onde a evidência de 8 kHz se aplica [SCH] |
| — | Vibração / ultrassom | Rolamento; vazamento localizado | ? sem estudo em câmara fria |

## Conflitos e armadilhas que mudam a conclusão

| Conflito | Lado A | Lado B | Leitura |
|---|---|---|---|
| Direção da potência com subcarga | RTU: a potência sobe (3891 W contra 2542 W normal, com −20 %) [ARM] | Split TXV: a potência cai 2,9–6,6 % com 30 % [TN1648][N7350] | Depende da expansão (orifício fixo ou TXV), do nível e do clima. **Não use o sinal de P como regra de subcarga** |
| O elétrico serve para FDD? | MIT: positivo, com transitório em kHz e bancada controlada [ARM][SHAW] | Purdue: negativo, com potência em regime em campo [HJO] | Os dois estão certos: o resultado depende da taxa de amostragem e do controle de clima. Um disjuntor inteligente cai no cenário Purdue |
| Acurácia no dataset UFPB | O grupo reporta 100 % de FDD em falhas simples e 82,76 % de diagnóstico em falhas múltiplas [IIR-UFPB] | Só a tensão da rede classifica as condições com 96–99 %. Há **1 gravação de 62 s por condição**, embora o artigo cite 3 repetições [PRÓPRIA] | O classificador aprende a sessão, não a falha. A validação exige separar treino e teste por gravação, o que é impossível com n=1 por classe |
| Filtro (FI50) na corrente | Medido: +3,2 % [PRÓPRIA] | Gêmeo físico: −2 % [PRÓPRIA] | O efeito fica dentro da variação entre sessões (a tensão variou ≤2,2 %). **O filtro não é observável só pela corrente**, o que é coerente com a coluna "neutro" do NIST [N7350] |
| Restrição na linha de líquido | Detectável com orifício fixo [SP1087] | Invisível com TXV até 13 % (temperatura) e até 48 % (potência) [SP1087][TN1648] | Até o termistor falha nos casos com TXV. É candidata a "não monitorar" no mínimo |

**Evidência própria do gêmeo.** O gêmeo digital físico ([samuel.simia.digital/lab/split](https://samuel.simia.digital/lab/split)) foi calibrado com 3 falhas simples (capacitor, condensador e filtro). Ele reproduz as 4 falhas duplas do UFPB com erro de **0,6 a 6,3 pontos percentuais** na variação de Irms (medido: CD30FI50 +8,0 %, CD30CI30 +15,7 %, CI60FI50 +28,7 %, CD30CI60 +39,5 %) [PRÓPRIA]. Os efeitos combinam de forma aproximadamente aditiva e física. Isso sustenta usar o gêmeo para gerar falhas combinadas em vez de depender de rótulos de ML.

## Datasets públicos com medição elétrica

| Dataset | Equipamento | Falhas | Elétrico | Termo | Licença | Comercial | Valida gêmeo? | Link |
|---|---|---|---|---|---|---|---|---|
| **LBNL FDD – RTU** (Granderson et al. 2023) | Rooftop R410A TXV (simulação Modelica + campo + lab) | Simulação: sobre e subcarga 10–20 %, fouling do condensador/evaporador 10–50 %, restrição de líquido 1–10 bar e de sucção 1–9 bar. Campo: subcarga de 40 % | P do compressor/ventilador/total, 1 min | P/T de refrigerante | CC BY 4.0 | **Sim** | **Sim**: severidade graduada + P/T. O caso de campo com subcarga de 40 % é o único real | [OEDI 5763](https://data.openei.org/submissions/5763) · [doc](https://fdddata.lbl.gov/data/Simulated_LBNL_FDD_Data_Sets_RTU/LBNL_FDD_Data_Sets_RTU.pdf) |
| **ORNL CO2 supermercado** (Sun et al. 2021) | Rack de CO2 com 2 compressores LT e 3 MT (lab) | Porta 5/10/15 %, gelo em 3 níveis, TXV, ventilador, bloqueio do condensador e do evaporador 25/50/75 % | P por compressor, 1 s | T/P do circuito | CC BY 4.0 (metadados CC0) | **Sim** | **Sim, para câmara fria/comercial** (CO2 transcrítico ≠ unidade condensadora) | [figshare 13232627](https://doi.org/10.6084/m9.figshare.13232627) · [artigo][ORNL] |
| **NIST 14/16 SEER cooling** | Heat pump split 14 SEER + AC 16 SEER (lab) | Falhas simples em regime permanente | Provável potência (**colunas não verificadas**) | T/P/umidade | Sem declaração; obra do governo dos EUA (17 U.S.C. §105) | Provável (verificar) | **Sim, para split** em regime; é o par natural de SP1087/TN1648 | [NIST FDD](https://www.nist.gov/el/energy-and-environment-division-73200/hvacr-equipment-performance-group/fault-detection-and) · DOI 10.18434/M32132 |
| **UFPB split** (de Oliveira et al. 2024) | Split on-off 18 kBTU/h, em campo | 9 condições: FL, FI50, CD30, CI30, CI60 + 4 duplas | I + V brutas, 30 kHz × 62 s | Nenhum | **CC-BY-NC** | **Não** | Só a assinatura elétrica; 1 gravação por condição [PRÓPRIA] | [MDPI, suplemento S1](https://www.mdpi.com/2306-5729/9/9/106) |
| **Fonseca et al.** (Data in Brief 2023) | Geladeiras/lavadoras (oficina) | Normal / defeito (rótulo genérico) | Corrente 1 Hz e 2048 Hz + vibração | Nenhum | CC BY | Sim | Não (não há falhas de ciclo graduadas) | [PMC10063395](https://europepmc.org/articles/PMC10063395) |
| **ASHRAE RP-1043** | Chiller centrífugo 90 TR | 7 falhas × 4 níveis | P do compressor (a verificar) | ~64 pontos (a verificar) | Direitos ASHRAE; espelho sem licença verificada | Incerto | Referência de chiller, fora do escopo | [figshare 28435232](https://figshare.com/articles/dataset/Chiller_operation_data_set/28435232) |
| **Split tropical** (Ramananandro et al. 2026) | Split (EnergyPlus) | Múltiplas falhas, 4 níveis | Energia | COP, T externa | CC BY 4.0 | Sim | Só modelo contra modelo | [Mendeley](https://data.mendeley.com/datasets/2mmf3ts9dk/3) |
| **IEEE DataPort AC faults** | Não especificado | Não especificado | Não especificado | — | CC BY 4.0 (exige login) | Sim | Desconhecido | [IEEE DataPort](https://ieee-dataport.org/documents/public-dataset-air-conditioner-faults) |

Não existe dataset público com **corrente em forma de onda + temperaturas + falhas graduadas** no mesmo split. Nenhum dataset aberto de run-to-failure de compressor de refrigeração foi encontrado ([survey arXiv 2402.17802](https://arxiv.org/html/2402.17802v2)). Para produto comercial, a rota viável é: gêmeo calibrado nos dados NIST e LBNL (licença livre), com o UFPB usado só para pesquisa da assinatura elétrica.

**Lacunas abertas:**
- Vibração e acústica com falhas impostas em split ou câmara fria: nenhum estudo.
- MCSA em compressor rotativo ou scroll de AC: só patentes ([US 11280530][P11280]).
- Split inverter com falhas impostas e medição elétrica: nenhum estudo revisado por pares.
- Câmara fria com FDD só por potência e métricas de acurácia: nenhum estudo.
- Capacitor: nenhum artigo revisado por pares informa a perda de capacitância detectável e a taxa de falso alarme.
- As colunas das planilhas NIST e os números de sensibilidade do artigo Hjortland 2016 não foram verificados.

## Conclusão

Para a Tractian, a pergunta certa não é "qual sensor detecta mais falhas". É **qual sensor torna o modelo elétrico identificável**. O medidor elétrico mede o efeito agregado de várias causas; um ou dois termistores (descarga, superaquecimento) quebram as ambiguidades do sinal elétrico. Isso vale para subcarga contra carga térmica menor, e para filtro contra variação de rede. A análise própria do UFPB mostra o risco do caminho inverso. Com uma sessão por classe, qualquer feature elétrica rica (inclusive a tensão da rede) "classifica" perfeitamente. Por isso, o diferencial defensável é validação por física (gêmeo calibrado em falhas simples prevendo as duplas com erro de até 6,3 p.p.), não acurácia de classificador.

A segunda implicação é sobre prognóstico. Com o conjunto mínimo, o horizonte realista é **"tempo até o desarme"**, não RUL mecânico. Os sinais seriam tendência de corrente por ciclo, partidas por hora, temperatura de descarga e duty cycle normalizado por clima. As únicas fontes de RUL de compressor de refrigeração encontradas são patentes ([US 12335767][P12335]). E o mercado brasileiro, com 39 % ao ano de vazamento médio e cerca de 30 % de compressores trocados sem defeito ([LIN]; [ACHR][ACHR]), paga mais por **"diagnóstico antes da troca"** do que por sensibilidade fina.

[SP1087]: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf
[TN1648]: https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.1648_2009.pdf
[N7350]: https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7350.pdf
[ARM]: https://emsg.mit.edu/wp-content/uploads/2016/07/27_Detection-of-Rooftop-Cooling-Unit-Faults-Based-on-Electrical-Measurements.pdf
[SHAW]: https://emsg.mit.edu/wp-content/uploads/2016/07/21_Detection-and-Diagnosis-of-HVAC-Faults-via-Electrical-Load-Monitoring.pdf
[SCH]: https://docs.lib.purdue.edu/iracc/1329
[HJO]: https://iifiir.org/en/fridoc/the-effectiveness-of-using-total-system-power-for-fault-detection-in-32216
[KB13]: https://iifiir.org/en/fridoc/performance-evaluation-of-a-virtual-refrigerant-charge-sensor-136209
[VPS]: https://ncesr.unl.edu/wordpress/wp-content/uploads/2018/08/Virtual-Refrigerant-Pressure-Sensors-for-Use-in-Monitoring-and-Fault-Diagnosis-of-Vapor-Compression-Equipment.pdf
[WIJ]: https://www.mdpi.com/1996-1073/17/3/736
[ASS]: https://www.aivc.org/node/30406
[COL]: https://iifiir.org/en/fridoc/detection-of-r290-leaks-in-rachp-equipment-using-ultrasonic-sensors-147989
[UFPB]: https://www.mdpi.com/2306-5729/9/9/106
[IIR-UFPB]: https://iifiir.org/en/fridoc/fault-diagnosis-in-split-system-air-conditioner-by-analyzing-the-chaos-150329
[P9310]: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9310439
[P4104]: https://patents.google.com/patent/US4104888
[P4831]: https://patents.google.com/patent/US4831833
[P11280]: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11280530
[P12335]: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12335767
[MAL]: https://iifiir.org/en/fridoc/frost-detection-method-on-evaporator-in-vapour-compression-systems-141998
[CORE]: https://core.ac.uk/download/304001116.pdf
[ORNL]: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8159987/fullTextXML
[NIV]: https://ph01.tci-thaijo.org/index.php/TNIJournal/article/download/145160/107271/387458
[ASME19]: https://bohrium.dp.tech/paper/arxiv/814616999224147969
[OBA]: https://khazna.ku.ac.ae/en/publications/stator-current-analysis-for-bearing-damage-detection-in-induction/
[ROB]: https://www.robertshaw.com/parts/temperature-controls/digital-controller-series/sitrad-inbox/
[LIN]: https://webarcondicionado.com.br/vazamentos-em-sistemas-de-refrigeracao-comerciais-principais-pontos-de-fuga-e-como-resolver
[MEI]: https://www.MeierSupply.com/customer/docs/Techtips/TechSpeaking%202011%20Issue5%20Refrigerant%20Floodback.pdf
[HVS]: https://hvacrschool.com/walk-in-cooler-defrost/
[ACHR]: https://achrnews.com/articles/92421-the-compressor-mysteries
[PRÓPRIA]: https://samuel.simia.digital/lab/split "Análise própria, repositório hvac-fdd-lab"

*[PRÓPRIA] = análise própria, repositório hvac-fdd-lab (dataset UFPB, suplemento S1 do artigo MDPI, CC-BY-NC; gêmeo digital em samuel.simia.digital/lab/split).*
