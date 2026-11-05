# Alarmes de controladores de refrigeração comercial (manuais públicos)

Levantamento feito em 05/11/2026 para o gêmeo digital de câmara fria / supermercado (hvac-fdd-lab).
Todas as informações das tabelas da Seção 1 foram extraídas dos PDFs oficiais listados abaixo, baixados e lidos na íntegra (texto + verificação visual das tabelas quando o layout do PDF embaralhava colunas).
Nomes de parâmetros e valores de fábrica estão transcritos como aparecem nos manuais (em inglês nos manuais Danfoss/Carel, em português nos manuais Full Gauge).
A Seção 2 (causas físicas) é **interpretação de engenharia de refrigeração**, não texto dos manuais, exceto quando indicado "(manual)".

---

## 0. Fontes consultadas

| # | Controlador | Documento (código / versão) | URL | Status |
|---|---|---|---|---|
| D1 | Danfoss EKC 202A/B/C | Instructions RI8JV853, © Danfoss 06/2015, SW = 1.3x (doc. AN00008642733201-000801) | https://assets.danfoss.com/documents/28430/AN00008642733201-000801.pdf | Lido |
| D2 | Danfoss AK-CC55 Compact | User Guide BC365212986197en-000201, 2022.08, SW 2.1x | https://assets.danfoss.com/documents/206320/BC365212986197en-000201.pdf | Lido |
| D3 | Danfoss AK-CC55 Compact | Installation Guide AN300028324304en-000601, 2022.02 | https://assets.danfoss.com/documents/203084/AN300028324304en-000601.pdf | Lido (mesma lista de alarmes do D2) |
| D4 | Danfoss AK-CC55 Multi Coil | Installation Guide AN300030680307en-000501, 2022.02 | https://assets.danfoss.com/documents/203087/AN300030680307en-000501.pdf | Lido |
| D5 | Danfoss AK-CC 550A | Instructions RI8NP702, © Danfoss 2018-09 (doc. AN198586422827en-000701) | https://assets.danfoss.com/documents/34984/AN198586422827en-000701.pdf | Lido |
| D6 | Danfoss AK-CC 550A | Pocket Service Guide AX278928624187en-000101, 2018.08 | https://assets.danfoss.com/documents/51026/AX278928624187en-000101.pdf | Lido |
| D7 | Danfoss AK-PC 782A (rack CO2 transcrítico booster) | User Guide BC245386497365en-001101, 2024.06, SW 4.1x — Appendix B "Alarm texts" (p. 148–150) | https://assets.danfoss.com/documents/402020/BC245386497365en-001101.pdf | Lido |
| F1 | Full Gauge TC-900e Log | Manual Ver. 05, TC900ELOGV05-01T-20219-2510 (Rev. 03, © 2025) | https://fullgauge-strapi-prod-media-f340da7.s3.sa-east-1.amazonaws.com/TC_900_ELOGV_05_01_T_20219_PORTUGUES_57f3db1710.pdf (página do produto: https://fullgauge.com/br/produtos/tc-900e-log) | Lido |
| F2 | Full Gauge TC-900Ri power | Manual Ver. 03, TC900RIPWV03-05T-12768 | https://fullgauge-strapi-prod-media-f340da7.s3.sa-east-1.amazonaws.com/TC_900_RIPWV_03_05_T_12768_PORT_7a3f5c3b31.pdf | Lido |
| F3 | Full Gauge MT-512Ri plus | Manual Ver. 09, MT512RIPLV09-05T-11485 | https://fullgauge-strapi-prod-media-f340da7.s3.sa-east-1.amazonaws.com/MT_512_RIPLV_09_05_T_11485_PORT_368c038195.pdf | Lido |
| F4 | Full Gauge VX-950 plus (com válvula de expansão eletrônica) | Manual Ver. 02, VX950PLV02-05T-18272 | https://fullgauge-strapi-prod-media-f340da7.s3.sa-east-1.amazonaws.com/VX_950_PLV_02_05_T_18272_PORTUGUES_efa2d05d97.pdf | Lido |
| C1 | Carel MPXPRO | User manual +0300055EN rel. 1.6 – 04.04.2019 (cópia pública hospedada pelo distribuidor Reece; carel.com não retornou link direto) | https://digitalassets.reecegroup.com.au/m/224b5a89a863d40b/original/User-Manual-CAREL-Mpx-pro.pdf | Lido (Tab. 9.b "Table of alarms") |

Não acessados / não verificados: ver Seção 3 (Lacunas).

---

## 1. Tabela de alarmes por fabricante/controlador

Convenções:
- "Fábrica" = valor de fábrica (Fact./Factory setting/Def/Padrão) do manual.
- Danfoss: alarmes "A" só aparecem após o atraso; alarmes "E" aparecem imediatamente (D5: "A-alarms will not become visible until the set time delay has expired. E-alarms, on the other hand, will become visible the moment the error occurs").
- Categorias: temperatura da câmara, degelo, superaquecimento/válvula, pressão, compressor, sensor, porta, vazamento, elétrico.

### 1.1 Danfoss EKC 202A/B/C (D1 — SW 1.3x)

| Fabricante/controlador | Código | Nome do alarme | Condição/limite típico (parâmetro e fábrica) | Atraso padrão | Categoria |
|---|---|---|---|---|---|
| Danfoss EKC 202 | A1 | High temperature alarm | Sair > `A13 High alarm limit` = 8 °C (faixa -50…50 °C) | `A03 Delay for temperature alarm` = 30 min; após degelo `A12 Delay for temperature alarm after defrost` = 90 min | temperatura da câmara |
| Danfoss EKC 202 | A2 | Low temperature alarm | Sair < `A14 Low alarm limit` = -30 °C | `A03` = 30 min | temperatura da câmara |
| Danfoss EKC 202 | A4 | Door alarm | DI1 configurada como porta (`o02` = 2 "door function with alarm when open" ou 3 "door alarm when open") | `A04 Delay for door alarm` = 60 min | porta |
| Danfoss EKC 202 | A5 | Max. Hold time | Espera após degelo coordenado excede `o16 Max hold time after coordinated defrost` = 20 min | — (o próprio o16) | degelo |
| Danfoss EKC 202 | A15 | DI 1 alarm | `o02` = 8 "alarm function when closed" ou 9 "alarm function when open" (alarme externo genérico — p.ex. pressostato, detector de gás) | `A27 Alarm delay DI1` = 30 min | elétrico (entrada externa) |
| Danfoss EKC 202 | A45 | Standby mode | Refrigeração parada por `r12` (main switch) ou DI | — | elétrico |
| Danfoss EKC 202 | A59 | Case cleaning | Limpeza do expositor (`o46`, DI `o02`=10) | — | elétrico (modo operacional) |
| Danfoss EKC 202 | A61 | Condenser alarm | S5 usado como sensor de condensador (`o70` = 2 "condenser sensor with alarm"); temp. > `A37 High alarm limit for condenser temperature (o70)` = 50 °C | não indicado no manual | pressão (condensação) |
| Danfoss EKC 202 | E1 | Fault in controller | Falha interna | imediato | elétrico |
| Danfoss EKC 202 | E6 | Change battery + check clock | Relógio | imediato | elétrico |
| Danfoss EKC 202 | E27 | S5 sensor error | Sensor de evaporador/degelo S5 | imediato | sensor |
| Danfoss EKC 202 | E29 | Sair sensor error | Sensor de ar | imediato | sensor |
| Danfoss EKC 202 | (sem código) | Degelo por tempo máximo | `d04 Max. defrost duration` = 45 min (0–180 min). O manual não define código de alarme para término por tempo. | — | degelo |

### 1.2 Danfoss AK-CC55 Compact (D2/D3) e AK-CC55 Multi Coil (D4)

| Fabricante/controlador | Código | Nome do alarme | Condição/limite típico (parâmetro e fábrica) | Atraso padrão | Categoria |
|---|---|---|---|---|---|
| Danfoss AK-CC55 | A01 | High temperature alarm A | Temp. de alarme (ponderada S4/S3 por `A36 Alarm sensor S4% A` = 100 %) > `A13 High alarm limit 1` = 8.0 °C (termostato 2: `A20` = 8.0 °C) | `A03 Alarm delay A` = 30 min; `A12 Alarm delay pulldown A` = 90 min | temperatura da câmara |
| Danfoss AK-CC55 | A02 | Low temperature alarm A | < `A14 Low alarm limit 1` = -30.0 °C (termostato 2: `A21` = -30.0 °C) | `A03` = 30 min | temperatura da câmara |
| Danfoss AK-CC55 Multi Coil | A70 / A71 | High / Low temperature alarm B | Mesma lógica, seção B | idem | temperatura da câmara |
| Danfoss AK-CC55 Multi Coil | a05 / a06 | High / Low temperature alarm C | Mesma lógica, seção C | idem | temperatura da câmara |
| Danfoss AK-CC55 Multi Coil | a02 / a03 | High / Low humidity alarm | Umidade acima/abaixo do limite | não extraído | sensor (umidade) |
| Danfoss AK-CC55 | A04 | Door open alarm | "The door has been open for a too long time" | `A04 Door open alarm delay` = 60 min | porta |
| Danfoss AK-CC55 | A05 | Max defrost hold time exceeded | Espera pós-degelo coordenado excedida | — | degelo |
| Danfoss AK-CC55 | A11 | Refrigerant not selected | `o30 Refrigerant` não configurado | — | elétrico (configuração) |
| Danfoss AK-CC55 | A15 / A16 | DI alarm 1 / DI alarm 2 | Sinal em DI1/DI2 | `A27 Alarm delay DI 1` = 30 min; `A28 Alarm delay DI 2` = 30 min | elétrico (entrada externa) |
| Danfoss AK-CC55 | A45 | Main switch set OFF | `r12` em Stop/Manual ou DI "main switch" | — | elétrico |
| Danfoss AK-CC55 | A59 | Case in cleaning mode | Limpeza iniciada | — | elétrico (modo operacional) |
| Danfoss AK-CC55 | AA2 | CO2 leak detected | Sinal de detector de vazamento em DI (função DI "Leak detection" = 20) com refrigerante CO2 | prioridade `q36 Leak Prio` | vazamento |
| Danfoss AK-CC55 | AA3 | Refrigerant leak detected | Idem, outros refrigerantes | `q36 Leak Prio` | vazamento |
| Danfoss AK-CC55 | a04 | Wrong IO configuration | Configuração de E/S inválida | — | elétrico |
| Danfoss AK-CC55 | E01 | Hardware failure | — | imediato | elétrico |
| Danfoss AK-CC55 | E06 | Clock lost time | — | imediato | elétrico |
| Danfoss AK-CC55 | E20 | Pe Evap. pressure A - Sensor error | Transmissor de pressão de evaporação fora de faixa | imediato | sensor |
| Danfoss AK-CC55 | E24 | S2 Gas outlet A - Sensor error | Sensor de saída do evaporador (cálculo de superaquecimento) | imediato | sensor |
| Danfoss AK-CC55 | E25 / E26 / E27 | S3 Air ON / S4 Air OFF / S5 Evaporator - Sensor error | — | imediato | sensor |
| Danfoss AK-CC55 Multi Coil | E37, E59–E63 | S5 B, umidade, S4 B/C, S2 B/C - Sensor error | — | imediato | sensor |
| Danfoss AK-CC55 | (sem código) | Degelo por tempo | `d04 Max defrost time` = 45 min (0–360 min). Não há código de alarme na lista; prioridade de grupo "Defrost" em `q32 Defrost Prio` | — | degelo |
| Danfoss AK-CC55 | (função, não alarme) | MOP | `n11 MOP temperature` = 15.0 °C (faixa -60…15 °C; no AK-CC 550A "Off if MOP temp. = 15.0 °C") — limita abertura da AKV, não gera código | — | superaquecimento/válvula |

Grupos de prioridade de alarme no AK-CC55 (D2, Table 35): `q28 Hi Temp Prio`, `q29 Lo Temp Prio`, `q30 Sensor Prio`, `q31 DIAlarm Prio`, `q32 Defrost Prio`, `q33 Misc Prio`, `q34 Inject Prio`, `q35 CtrlOFF Prio`, `q36 Leak Prio`; relé: `P41 Al.Rel.Prio`.

### 1.3 Danfoss AK-CC 550A (D5/D6 — modelo anterior, com mais alarmes de injeção/degelo)

| Fabricante/controlador | Código | Nome do alarme | Condição/limite típico (parâmetro e fábrica) | Atraso padrão | Categoria |
|---|---|---|---|---|---|
| Danfoss AK-CC 550A | A1 / A2 | High t.alarm / Low t. alarm | `A13 High alarm limit for thermostat 1` = 8 °C; `A14 Low alarm limit for thermostat 1` = -30 °C (termostato 2: `A20`/`A21`) | `A03 Delay for temperature alarm` = 30 min; `A12 Delay for temperature alarm after defrost` = 90 min | temperatura da câmara |
| Danfoss AK-CC 550A | A13 / A14 | High temp S6 / Low temp S6 (temperatura de produto) | `A22`/`A24` = 8 °C (alto), `A23`/`A25` = -30 °C (baixo) | `A26 S6 alarm time delay` = 240 min ("With setting = 240 the S6 alarm will be omitted"); `A52 Delay for S6 (product sensor alarm) after defrost` = 90 min | temperatura da câmara (produto) |
| Danfoss AK-CC 550A | A4 | Door alarm | DI de porta | `A04 Delay for door alarm` = 60 min | porta |
| Danfoss AK-CC 550A | A5 | Max hold time | "The 'o16' function is activated during a coordinated defrost" | — | degelo |
| Danfoss AK-CC 550A | A10 | Inject prob. | "Control problem" (problema de controle da injeção/AKV) | não indicado | superaquecimento/válvula |
| Danfoss AK-CC 550A | A11 | No Rfg. sel. | Refrigerante não selecionado | — | elétrico (configuração) |
| Danfoss AK-CC 550A | A15 / A16 | DI1 alarm / DI2 alarm | `A27` / `A28` = 30 min | 30 min | elétrico (entrada externa) |
| Danfoss AK-CC 550A | A45 | Standby mode | Parado via `r12` ou DI | — | elétrico |
| Danfoss AK-CC 550A | A59 | Case clean | Sinal de DI | — | elétrico (modo operacional) |
| Danfoss AK-CC 550A | AA2 | Refrig Leak | "A refrigerant leak detection signal is received" | — | vazamento |
| Danfoss AK-CC 550A | AA3 | CO2 alarm | Sinal de vazamento com refrigerante CO2 | — | vazamento |
| Danfoss AK-CC 550A | --- (só via rede) | Max Def.Time | "Defrost stopped based on time instead of, as wanted, on temperature"; `d04 Max. defrost duration` = 45 min (0–360) | — | degelo |
| Danfoss AK-CC 550A | --- (só via rede) | AD fault | "Error in the adaptive defrost function" | — | degelo |
| Danfoss AK-CC 550A | --- (só via rede) | AD Iced | "Evaporator is iced up. Reduction of air flow" | — | degelo |
| Danfoss AK-CC 550A | --- (só via rede) | AD not defr. | "Defrost of evaporator is not satisfactory" | — | degelo |
| Danfoss AK-CC 550A | --- (só via rede) | AD flashgas. | "Flash gas is formed at the valve" | — | superaquecimento/válvula |
| Danfoss AK-CC 550A | E1 / E6 | Ctrl. error / RTC error | — | imediato | elétrico |
| Danfoss AK-CC 550A | E20 | Pe error | Transmissor de pressão Pe | imediato | sensor |
| Danfoss AK-CC 550A | E24–E28, E34, E37 | S2 / S3 / S4 / S5 / S6 / S3B / S5B error | — | imediato | sensor |
| Danfoss AK-CC 550A | (parâmetros de injeção) | — | `n09 Max. value of superheat reference` = 12 °C; `n10 Min. value of superheat reference` = 3 °C; `n11 MOP temperature` = 15 °C (= off) | — | superaquecimento/válvula |

Observação: os controladores de evaporador Danfoss (EKC 202, AK-CC55, AK-CC 550A) **não têm código dedicado de "superaquecimento baixo" ou "MOP"** — MOP é função de limitação da válvula; o problema de injeção aparece como A10 (550A) ou nos alarmes do rack (AK-PC 782A, abaixo).

### 1.4 Danfoss AK-PC 782A — controlador de rack (D7, Appendix B)

O manual do AK-PC 782A não traz tabela de valores de fábrica para os limites de segurança; os valores abaixo marcados "exemplo" são do exemplo de configuração do próprio manual (seção de setup e aplicação exemplo), **não** defaults.

| Fabricante/controlador | Código (texto de alarme) | Nome do alarme | Condição/limite típico | Atraso padrão | Categoria |
|---|---|---|---|---|---|
| Danfoss AK-PC 782A | Low pressure P0 | Low suction pressure P0 (prioridade de fábrica: Low) | "Minimum safety limit for suction pressure P0 has been exceeded"; `T0 Min limit` (faixa -120…+30 °C); exemplo: MT Po min = -35 °C, LT Po min = -45 °C; corta todos os compressores | Rearme após `Safety restart time` | pressão |
| Danfoss AK-PC 782A | High pressure P0 | High suction pressure P0 (High) | `T0 Max alarm`; exemplo Po max = -5 °C | `T0 Max delay` | pressão |
| Danfoss AK-PC 782A | Low / High pressure Psuc-MT | Pressão de sucção MT baixa/alta | Idem para o circuito MT | — | pressão |
| Danfoss AK-PC 782A | High superheat suction A / Low superheat section A | High/Low superheat Ss (Medium) | `SH Min alarm` / `SH Max alarm`; exemplo SH min = 5 K, SH max = 35 K (superaquecimento na linha de sucção, calculado de P0 e Ss) | `SH alarm delay` | superaquecimento/válvula |
| Danfoss AK-PC 782A | High disch. temp. SdA | High Sd temp. (High) | `Sd max limit` (faixa 0…195 °C); a 10 K abaixo do limite reduz capacidade; exemplo MT Sd max = 120 °C, LT = 100 °C | — | compressor |
| Danfoss AK-PC 782A | High pressure Pc | High Pc pressure (High) | `Pc Max limit` (bar); a 3 K abaixo do limite liga todo o condensador e reduz compressores; exemplo MT Pc max = 110 bar, LT = 40 bar | `Pc Max alarm delay` | pressão |
| Danfoss AK-PC 782A | Common compr. Safety cutout | Common safety (High) | Entrada de segurança comum cortou todos os compressores | — | compressor |
| Danfoss AK-PC 782A | Comp. x oil pressure cut out | Comp. x safety (Medium) | Pressostato de óleo | delay comum das entradas de segurança | compressor |
| Danfoss AK-PC 782A | Comp. x over current cut out | Comp. x safety | Sobrecorrente | idem | compressor / elétrico |
| Danfoss AK-PC 782A | Comp. x motor prot. cut out | Comp. x safety | Proteção do motor | idem | compressor |
| Danfoss AK-PC 782A | Comp. x disch. Temp cut out | Comp. x safety | Termostato de descarga individual (`Max discharge temp.`, `Sd compressor alarm delay`) | `Sd compressor alarm delay` | compressor |
| Danfoss AK-PC 782A | Comp. x disch. Press. Cut out | Comp. x safety | Pressostato de alta individual | idem | pressão |
| Danfoss AK-PC 782A | Comp. x General safety cut out | Comp. x safety | Segurança genérica | idem | compressor |
| Danfoss AK-PC 782A | Comp. x FCD safety error | VSD safety (Medium) | Inversor do compressor desarmou | — | compressor / elétrico |
| Danfoss AK-PC 782A | Low oil in separator x / No oil separated sep. x / To high oil in separator x / Remaining oil separator x | Separator alarms (Medium) | Nível de óleo no separador | `Level alarm delay`, `No oil sep. alarm delay` | compressor (óleo) |
| Danfoss AK-PC 782A | Oil recv. high level / Oil recv. low level | Receiver alarm (Medium) | Nível no reservatório de óleo | `Level alarm delay` | compressor (óleo) |
| Danfoss AK-PC 782A | Recv. High / Low pressure alarm | Rec. high / low pressure (Medium) | Pressão no reservatório de líquido | `High alarm delay` / `Low alarm delay` | pressão |
| Danfoss AK-PC 782A | Rec. High / Low liquid level alarm | Rec. High / Low liquid level (High) | Nível de líquido no reservatório | `Liquid alarm delay` | vazamento (nível baixo) / pressão |
| Danfoss AK-PC 782A | Fan Alarm 1 / Fan VSD alarm | Fan/VSD safety (Medium) | Ventilador do condensador ou inversor desarmado | — | elétrico (condensador) |
| Danfoss AK-PC 782A | P0A / Psuc / Sgc / Prec / Pgc / PcA sensor error; SsA / SdA / Sc3 / S7A sensor error | Sensor errors (High / Medium) | Sinal de transmissor/sensor defeituoso | — | sensor |
| Danfoss AK-PC 782A | Load Shed active | Load shedding (Medium) | Redução de carga ativada | — | elétrico |
| Danfoss AK-PC 782A | Control stopped, MainSwitch=OFF | Standby mode (Medium) | — | — | elétrico |
| Danfoss AK-PC 782A | External power loss | (High) | "Supply is interrupted" | — | elétrico |
| Danfoss AK-PC 782A | Stepper - Vhp, Vrec, PI, Vliq. | Steppervalve (High) | "Open coil, Shorted output, Error, Power failure" | — | superaquecimento/válvula |
| Danfoss AK-PC 782A | Thermostat x / Pressostat x / Analogue input x - High/Low alarm | Funções auxiliares (Low) | Limites configuráveis | `Alarm delay high/low` | (genérico) |
| Danfoss AK-PC 782A | Ejector Emergency / Manual Ejector control | Ejetor (High) | Sem sinal de Pgc / ejetor em manual | — | pressão |

### 1.5 Full Gauge TC-900e Log (F1 — Ver. 05)

Sinalizações (item "7. SINALIZAÇÕES") e parâmetros (tabela de funções, coluna °C, valor padrão):

| Fabricante/controlador | Código | Nome do alarme | Condição/limite típico (parâmetro e padrão) | Atraso padrão | Categoria |
|---|---|---|---|---|---|
| Full Gauge TC-900e Log | [Athi] | Alarme de temperatura alta no ambiente (sensor1) | `F07 Alarme de temperatura ambiente alta (S1)` = 105,0 °C (na prática desabilitado de fábrica); modo `F65 Modo de operação dos alarmes de temperatura ambiente (S1) (0-relativo / 1-absoluto)` = 1 | `F53 Tempo de inibição de alarme por temperatura ambiente` = 0(NO); `F87 Tempo de inibição do alarme na energização` = 0(OFF) | temperatura da câmara |
| Full Gauge TC-900e Log | [Atlo] | Alarme de temperatura baixa no ambiente (sensor1) | `F06 Alarme de temperatura ambiente baixa (S1)` = -50,0 °C | idem | temperatura da câmara |
| Full Gauge TC-900e Log | [OpEn] / [AOPn] | Indicação de porta aberta / alarme de porta aberta | DI configurada como porta (`F57`/`F58`); `F55 Tempo de porta aberta para emitir alarme` = 0(NO) | F55 | porta |
| Full Gauge TC-900e Log | (ponto decimal piscando) [,,,,.] | "Indica que a temperatura para fim de degelo não foi atingida" (degelo terminado por tempo) | `F14 Duração máxima do degelo` = 30 min (0–90); `F13 Temperatura no evaporador (S2/S3) para determinar o fim de degelo` = 30,0 °C; habilitado por `F88 Indicação para alarme de degelo finalizado por tempo` = 0(OFF) | — | degelo |
| Full Gauge TC-900e Log | [AtC1] | Alarme de temperatura alta no condensador (nível 1) | `F54 Alarme de temperatura alta no condensador (S3)` = 45,0 °C | não indicado | pressão (condensação) |
| Full Gauge TC-900e Log | [AtC2] | Alarme de temperatura alta no condensador (nível 2) | `F50 Temperatura máxima no condensador (S3) para desligar saídas de controle` = 55,0 °C (histerese `F51` = 5,0 °C) — desliga as cargas | — | pressão (condensação) |
| Full Gauge TC-900e Log | [ALrC] | Compressor atingiu o tempo máximo ligado sem atingir o SP | `F52 Tempo de compressor ligado sem atingir o setpoint para desligar as saídas de controle` = 0(NO) | F52 | compressor |
| Full Gauge TC-900e Log | [AMaI] | Indica manutenção do compressor | `F66 Tempo máximo de operação da saída COMP para manutenção` = 0(NO) h | — | compressor |
| Full Gauge TC-900e Log | [Hipr] / [apHi] | Evento de pressão alta / Alarme de pressão alta (requer rearme manual) | Pressostato em entrada digital | `F68 Tempo para confirmar alarme de Alta Pressão` = 5 s; retomada `F71` = 3 min | pressão |
| Full Gauge TC-900e Log | [Lopr] / [aplo] | Evento de pressão baixa / Alarme de pressão baixa (requer rearme manual) | Pressostato em entrada digital | `F69 Tempo para confirmar alarme de Baixa Pressão` = 20 s; `F70 Tempo para retardo inicial após partida do compressor para monitorar alarme de baixa pressão` = 60 (unidade não legível na extração); retomada `F72` = 3 min | pressão |
| Full Gauge TC-900e Log | [ALrE] | Alarme externo (entrada digital) | DI configurada como alarme | — | elétrico (entrada externa) |
| Full Gauge TC-900e Log | [Err1] / [Err2] / [Err3] | Sensor ambiente / evaporador / sensor 3 desconectado ou fora da faixa | Com S1 em falha, compressor cicla por `F42`/`F43` | imediato | sensor |
| Full Gauge TC-900e Log | [ClOC] | Data e/ou hora inválidas | — | — | elétrico |
| Full Gauge TC-900e Log | [emem] / [eCAL] / [pppp] | Erro de memória / calibração / parâmetros desprogramados | — | — | elétrico |
| Full Gauge TC-900e Log | [adfl] | Memória do datalogger cheia | — | — | elétrico |
| Full Gauge TC-900e Log | (proteção, não alarme) | Porta aberta desliga ventilador / saídas | `F48 Tempo para porta aberta para desligar ventilador` = -1(NO); `F49 Tempo de porta aberta para desligar as saídas de controle` = 0(NO); `F46 Tempo de porta aberta para degelo instantâneo` = 0(NO) | — | porta |

### 1.6 Full Gauge TC-900Ri power (F2) e MT-512Ri plus (F3)

| Fabricante/controlador | Código | Nome do alarme | Condição/limite típico (parâmetro e padrão) | Atraso padrão | Categoria |
|---|---|---|---|---|---|
| Full Gauge TC-900Ri power | Er1 | Sensor ambiente desconectado ou fora da faixa | Compressor assume `F11 Situação do compressor com sensor ambiente (S1) desconectado` = 1 - lig. | imediato | sensor |
| Full Gauge TC-900Ri power | Er2 | Sensor do evaporador desconectado ou fora da faixa | Degelo termina por tempo | imediato | sensor |
| Full Gauge TC-900Ri power | AHi | Alarme de temperatura ambiente alta | `F07 Ponto de atuação do alerta de temperatura ambiente alta (S1)` = 75.0 °C (só durante refrigeração) | não há | temperatura da câmara |
| Full Gauge TC-900Ri power | (ponto piscando) | Degelo terminado por tempo | `F14 Duração máxima do degelo` = 45 min (0–90); `F13 Temperatura no evaporador (S2) para determinar fim de degelo` = 40.0 °C | — | degelo |
| Full Gauge MT-512Ri plus | [Err] | Sensor desconectado ou temperatura fora da faixa especificada | Único alarme do modelo (degelo natural por tempo: `F08 Tempo de degelo` = 030 min) | imediato | sensor |

### 1.7 Full Gauge VX-950 plus — com válvula de expansão eletrônica (F4)

| Fabricante/controlador | Código | Nome do alarme | Condição/limite típico (parâmetro e padrão) | Atraso padrão | Categoria |
|---|---|---|---|---|---|
| Full Gauge VX-950 plus | [ASHC] | Alarme de superaquecimento crítico | SH < `F14 Alarme de superaquecimento crítico` = 2.0 °C (alarme sonoro) | não indicado | superaquecimento/válvula |
| Full Gauge VX-950 plus | [ASHL] | Alarme de superaquecimento baixo | SH < `F15 Alarme de superaquecimento baixo` = 4.0 °C — fecha a VEE gradualmente (setpoint `F13 Setpoint de superaquecimento` = 9.0 °C) | não indicado | superaquecimento/válvula |
| Full Gauge VX-950 plus | [ASHH] | Alarme de superaquecimento alto | SH > `F16 Alarme de superaquecimento alto` = 15.0 °C — abre a VEE gradualmente | não indicado | superaquecimento/válvula |
| Full Gauge VX-950 plus | [APLo] | Alarme de pressão baixa | `F03 Alarme de pressão baixa (LOP)` = 0 psi / 0 bar — VEE abre para elevar a pressão | não indicado | pressão |
| Full Gauge VX-950 plus | [APhi] | Alarme de pressão alta | `F04 Alarme de pressão alta (MOP)` = 65 psi / 4.5 bar — VEE fecha ("para não deixar o superaquecimento com valor extremamente baixo ocasionando retorno de líquido no compressor") | não indicado | pressão |
| Full Gauge VX-950 plus | [athi] / [atlO] | Alarme de temperatura ambiente alta / baixa | `F59` (máx.) = 60.0 °C; `F58 Alarme sonoro da temperatura mínima ambiente` = -50.0 °C | `F61 Tempo de inibição do alarme sonoro por temperatura` = 0 min; `F62 Tempo de inibição do alarme sonoro na energização` = 10 min; inativo durante degelo/drenagem/fan-delay | temperatura da câmara |
| Full Gauge VX-950 plus | [Aopn] | Alarme de porta aberta | DI como porta (`F23`) | `F60 Tempo de porta aberta para alarme sonoro` = 5 min | porta |
| Full Gauge VX-950 plus | [alrc] | Alarme de compressor ligado sem atingir setpoint | — | — | compressor |
| Full Gauge VX-950 plus | (ponto piscando) | Fim de degelo por tempo | `F63 Alarme de fim de degelo por tempo` = 1; `F37 Tempo máximo de degelo` = 20 min; `F34 Temperatura do evaporador para finalizar degelo` = 8.0 °C | — | degelo |
| Full Gauge VX-950 plus | [ESHC] | Erro no cálculo do superaquecimento | — | imediato | sensor |
| Full Gauge VX-950 plus | [PErr] | Erro de leitura da pressão | — | imediato | sensor |
| Full Gauge VX-950 plus | [Err1] / [Err2] / [Err3] | Erro sensor de temperatura 1 / 2 / 3 | — | imediato | sensor |
| Full Gauge VX-950 plus | [Ecnn] / [PPPP] / [PPPC] / [ErUC] / [ECal] | Erro de conexão / desprogramado / HMI desprogramado / FG-CAP não instalado / contatar fabricante | — | — | elétrico |

### 1.8 Carel MPXPRO (C1 — Tab. 9.b "Table of alarms")

| Fabricante/controlador | Código | Nome do alarme | Condição/limite típico (parâmetro e Def) | Atraso padrão | Categoria |
|---|---|---|---|---|---|
| Carel MPXPRO | HI / LO | High / Low temperature alarm | `AH High temperature alarm threshold` = 10; `AL Low temperature alarm threshold` = 4 — **relativos ao setpoint** (`A1` = 0 = relative) | `Ad Delay time for high and low temperature alarms` = 120 min; após degelo `d8 Bypass high temperature alarm time after defrost` = 30 min; porta `Add High temperature alarm bypass time for door open` = 30 min | temperatura da câmara |
| Carel MPXPRO | HI2 / LO2 | High / Low temperature alarm (2º conjunto) | `AH2` = 0, `AL2` = 0 (`A2` = 0 relativo a St2) | `Ad2` = 30 min | temperatura da câmara |
| Carel MPXPRO | dor | Door open for too long alarm | Porta aberta mais que `Add` = 30 min → controle retoma e alarme dispara | `Add` = 30 min | porta |
| Carel MPXPRO | IA / dA | Immediate / Delayed alarm from external contact | DI (`A4`/`A5` = 1 ou 2); compressor conforme `A6` | `A7 Delay time for delayed external alarm` = 0 min | elétrico (entrada externa) |
| Carel MPXPRO | LSH | Low superheat alarm | SH < `P7 LowSH: low superheat threshold` = 7.0 K; desliga compressor/solenoide (com `P10` = 1) | `P9 LowSH: alarm delay - 0 = alarm disabled` = 600 s | superaquecimento/válvula |
| Carel MPXPRO | LSA | Low suction temperature alarm | Temp. de sucção < `P11 LSA: low suction temperature threshold` = -45.0 °C; `P13 LSA: alarm differential` = 10.0 | `P12 LSA: alarm delay` = 600 s | superaquecimento/válvula |
| Carel MPXPRO | MOP | Maximum evaporation pressure alarm | Temp. saturada de evaporação > `PM1 MOP: maximum saturated evaporation temperature threshold` = 50.0 °C | `PM3 MOP: alarm delay` = 0 (= função desabilitada); `PM4` = 2 s após partida | pressão |
| Carel MPXPRO | LOP | Low evaporation temperature alarm | Temp. saturada < `PL1 LOP: minimum saturated evaporation temperature threshold` = -50.0 °C | `PL3 LOP: alarm delay` = 0 (= desabilitada) | pressão |
| Carel MPXPRO | bLo | Valve blocked alarm | Válvula no fim de curso; habilitado por `P14` | rearme manual | superaquecimento/válvula |
| Carel MPXPRO | EFS / Edc | Stepper motor broken/not connected / Communication error with stepper driver | — | — | superaquecimento/válvula |
| Carel MPXPRO | Ed1 / Ed2 (sinal, não alarme) | Defrost on evaporator 1/2 ended by timeout | `dP1 Maximum defrost duration` = 45 min | — | degelo |
| Carel MPXPRO | HA / HF | Type HA / HF HACCP alarm | Temperatura alta (HA) ou após falta de energia (HF) | rearme manual | temperatura da câmara |
| Carel MPXPRO | rE | Control probe fault | — | — | sensor |
| Carel MPXPRO | E1…E7; E8…E11 | Probe S1…S7 fault; Serial probe S8…S11 not updated | — | — | sensor |
| Carel MPXPRO | Etc / EE / EF / GPE | Relógio / parâmetros flash / EEPROM / gás customizado | — | — | elétrico |
| Carel MPXPRO | MA / u1…u5 / n1…n5 | Comunicação Master/Slave; alarme em unidade da rede | — | — | elétrico |

---

## 2. Tipos únicos de alarme (deduplicados) e causas físicas

Cada item lista: códigos equivalentes por fabricante → causas físicas típicas (←). As causas são conhecimento de engenharia de refrigeração, servindo de hipótese de falha para o gêmeo digital; não constam dos manuais, salvo quando marcado "(manual)".

1. **Temperatura alta na câmara/expositor**
   Códigos: Danfoss A1/A01 (A70, a05), Full Gauge Athi/AHi/athi, Carel HI/HI2, HACCP HA.
   ← porta aberta ou mal vedada (gaxeta), cortina de ar/cortina noturna ausente; evaporador com gelo (degelo insuficiente, degelo terminado por tempo); ventilador do evaporador parado; falta de refrigerante (vazamento) ou subcarga; válvula de expansão desregulada/obstruída (superaquecimento alto, evaporador "faminto"); filtro secador entupido; condensador sujo ou ventilador do condensador parado (pressão de condensação alta → capacidade menor); compressor desarmado ou rack em alarme (P0 alto, segurança); carga térmica excessiva (produto quente, reposição); setpoint/limite mal configurado; sensor de ar mal posicionado.

2. **Temperatura baixa na câmara**
   Códigos: Danfoss A2/A02 (A71, a06), Full Gauge Atlo/atlO, Carel LO/LO2.
   ← contator do compressor/solenoide colado; termostato/sensor descalibrado ou fora do lugar; solenoide de líquido não fecha (passagem); setpoint errado; em rack, sucção muito baixa forçando evaporador; risco de congelamento de produto resfriado.

3. **Temperatura de produto fora da faixa** (sensor de produto S6)
   Códigos: AK-CC 550A A13/A14 (S6).
   ← mesmas causas de 1/2, com inércia térmica maior; produto exposto a carga radiante/iluminação; reposição de produto quente.

4. **Porta aberta por tempo excessivo**
   Códigos: Danfoss A4/A04, Full Gauge AOPn/Aopn (OpEn = indicação), Carel dor.
   ← operação logística (porta escorada), fechadura/mola defeituosa, gaxeta danificada, chave de porta desalinhada ou com defeito (falso positivo).

5. **Degelo terminado por tempo (temperatura de fim de degelo não atingida)**
   Códigos: AK-CC 550A "Max Def.Time", Full Gauge ponto decimal (F88/F63), Carel Ed1/Ed2; EKC 202/AK-CC55 só via parâmetro d04 (sem código).
   ← (manual, TC-900Ri power) "O intervalo entre degelos está muito longo", "Existem resistências queimadas", "O gás quente não está circulando", forçador inoperante ou tempo máximo de degelo insuficiente, temperatura de fim de degelo muito alta, sensor S2 desconectado ou sem contato com o evaporador. Acrescentar: contator/fusível da resistência, umidade alta (porta) gerando gelo excessivo.

6. **Evaporador congelado / degelo insatisfatório**
   Códigos: AK-CC 550A "AD Iced" (redução de vazão de ar), "AD not defr.", "AD fault".
   ← infiltração de ar úmido (porta), degelos insuficientes ou curtos, resistência queimada, dreno entupido (água recongela), ventilador parado, superaquecimento baixo localizado.

7. **Espera excessiva após degelo coordenado**
   Códigos: Danfoss A5/A05 (o16).
   ← outro evaporador do grupo não terminou o degelo (resistência/sensor), falha de comunicação com o system manager, tempo o16 mal ajustado.

8. **Superaquecimento baixo / crítico (risco de retorno de líquido)**
   Códigos: Carel LSH, LSA; Full Gauge ASHL, ASHC; AK-PC 782A "Low superheat section A" (linha de sucção do rack).
   ← válvula de expansão superdimensionada ou travada aberta, ajuste de SH muito baixo, sensor de sucção (S2/Ss) descolado/mal isolado ou com offset, transmissor de pressão com erro, evaporador com baixa carga térmica (ventilador parado, gelo — menos troca, líquido não evapora), sobrecarga de refrigerante, sucção do rack muito baixa.

9. **Superaquecimento alto / problema de injeção (evaporador "faminto")**
   Códigos: Full Gauge ASHH; AK-CC 550A A10 "Inject prob.", "AD flashgas."; AK-PC 782A "High superheat suction A".
   ← falta de refrigerante (vazamento, subcarga), flash gas na linha de líquido (subresfriamento insuficiente, filtro secador entupido, visor com bolhas), válvula subdimensionada/obstruída/bobina queimada, pressão de condensação baixa demais (ΔP insuficiente na válvula), solenoide de líquido não abre.

10. **Pressão de evaporação alta (MOP)**
    Códigos: Carel MOP; Full Gauge APhi (F04 MOP); Danfoss n11 (função, sem código).
    ← pull-down após degelo/partida com câmara quente, carga térmica alta, compressor/rack sem capacidade (compressor desarmado), válvula de sucção/EPR desregulada.

11. **Pressão de evaporação baixa (LOP)**
    Códigos: Carel LOP; Full Gauge APLo (F03 LOP), Lopr/aplo (pressostato).
    ← falta de refrigerante, válvula de expansão fechando demais/obstruída, filtro entupido, evaporador com gelo ou ventilador parado (baixa troca), solenoide fechada, setpoint de sucção do rack muito baixo.

12. **Pressão de sucção do rack baixa (P0 min)**
    Códigos: AK-PC 782A "Low pressure P0", "Low pressure Psuc-MT".
    ← excesso de capacidade de compressores para a carga (controle mal sintonizado), muitos evaporadores em degelo/desligados, falta de refrigerante (nível baixo no reservatório), transmissor P0 com defeito.

13. **Pressão de sucção do rack alta**
    Códigos: AK-PC 782A "High pressure P0", "High pressure Psuc-MT".
    ← compressores desarmados/insuficientes, carga térmica alta (portas, reposição, pull-down após degelo coordenado), válvula de capacidade/unloader com defeito, gás de flash/bypass excessivo.

14. **Pressão/temperatura de condensação alta**
    Códigos: AK-PC 782A "High pressure Pc"; EKC 202 A61 (A37); Full Gauge AtC1/AtC2, Hipr/apHi (pressostato); Danfoss "Comp. x disch. Press. Cut out".
    ← condensador sujo/obstruído, ventilador do condensador parado (ver 22), ar recirculando/temperatura ambiente alta, incondensáveis no sistema, sobrecarga de refrigerante, válvula de alta pressão/gas cooler (CO2) mal controlada, reservatório cheio.

15. **Temperatura de descarga alta**
    Códigos: AK-PC 782A "High disch. temp. SdA", "Comp. x disch. Temp cut out".
    ← superaquecimento de sucção alto (falta de refrigerante, ver 9), taxa de compressão alta (P0 baixa + Pc alta), injeção de líquido/economizador com defeito, válvulas do compressor danificadas, refrigeração do motor insuficiente.

16. **Desarme de segurança do compressor**
    Códigos: AK-PC 782A "Common compr. Safety cutout", "Comp. x motor prot. / over current / General safety cut out", "Comp. x FCD safety error"; Full Gauge (indireto via pressostatos e ALrC).
    ← sobrecarga elétrica, desequilíbrio/falta de fase, tensão baixa, rotor travado, ciclos curtos (partidas excessivas), superaquecimento do motor por SH alto, falha do inversor.

17. **Óleo (pressão/nível)**
    Códigos: AK-PC 782A "Comp. X oil pressure cut out", "Low oil in separator x", "No oil separated sep. x", "Oil recv. high/low level".
    ← retorno de óleo deficiente (velocidade baixa em linhas de sucção, evaporador "aprisionando" óleo), diluição de óleo por retorno de líquido (ver 8), separador de óleo/boia defeituosos, filtro de óleo entupido, vazamento de óleo.

18. **Nível de líquido / pressão do reservatório**
    Códigos: AK-PC 782A "Rec. Low liquid level alarm", "Rec. High liquid level alarm", "Recv. High/Low pressure alarm".
    ← nível baixo: vazamento de refrigerante (principal indicador de rack), refrigerante "estocado" no condensador/evaporadores; nível alto: sobrecarga ou acúmulo durante degelo/inverno; pressão: válvula de bypass de flash gas/receiver mal controlada.

19. **Compressor funcionando sem atingir setpoint / horas de manutenção**
    Códigos: Full Gauge ALrC/alrc (F52), AMaI (F66).
    ← capacidade insuficiente (vazamento, válvulas do compressor gastas), carga térmica excessiva, gelo no evaporador, condensação alta; AMaI é apenas contador de horas.

20. **Vazamento de refrigerante (detector de gás)**
    Códigos: Danfoss AA2 (CO2) / AA3 (outros) no AK-CC55; AA2/AA3 no AK-CC 550A; nos demais via entrada digital genérica (A15/A16, ALrE, IA/dA).
    ← brasagens trincadas, vibração em tubulação, juntas/flanges, válvulas Schrader, corrosão no evaporador (principalmente expositores). Sintomas indiretos no gêmeo: SH alto, P0 baixa, nível baixo no reservatório, temperatura alta na câmara com compressor 100 %.

21. **Falha de sensor / transmissor**
    Códigos: Danfoss E20–E29, E34, E37, E59–E63; AK-PC 782A "xx sensor error"; Full Gauge Err/Err1–3/Er1/Er2, PErr, ESHC; Carel rE, E1–E11.
    ← cabo rompido/em curto, umidade no conector, sensor fora da faixa, sensor errado (NTC × Pt1000 — `o06`), transmissor de pressão 4–20 mA sem alimentação. No gêmeo, gerar como valor travado, NaN, fora de faixa ou drift.

22. **Válvula de expansão eletrônica / atuador**
    Códigos: Carel bLo, EFS, Edc; AK-PC 782A "Stepper - Vhp, Vrec, PI, Vliq." (Open coil, Shorted output, Error, Power failure); AK-CC 550A A10.
    ← bobina aberta/em curto, motor de passo travado, sujeira, cabo, driver sem alimentação.

23. **Ventilador do condensador / inversor**
    Códigos: AK-PC 782A "Fan Alarm 1", "Fan VSD alarm".
    ← motor queimado, rolamento, inversor desarmado — consequência típica: item 14.

24. **Entrada de alarme externo genérica**
    Códigos: Danfoss A15/A16 (DI1/DI2), Full Gauge ALrE, Carel IA/dA, AK-PC "Custom alarm x".
    ← tudo o que for ligado à DI: pressostato de alta/baixa, detector de gás, termostato de segurança, alarme de pessoa presa na câmara, boia de dreno.

25. **Controle parado / elétrico / sistema**
    Códigos: Danfoss A45 (standby), A59 (limpeza), A11 (refrigerante não selecionado), a04 (E/S), E01/E1 (hardware), E06/E6 (relógio); AK-PC "External power loss", "Load Shed active", "Common IO Alarm"; Full Gauge ClOC, pppp, eCAL, adfl; Carel Etc, EE, EF, MA/u1–u5.
    ← falta de energia, intervenção manual esquecida (r12 em OFF), erro de configuração, falha de comunicação, bateria/relógio.

---

## 3. Lacunas e observações

- **EKC 204A, ERC 2xx**: não verificados (não baixados). A família EKC está coberta apenas pelo EKC 202A/B/C SW 1.3x.
- **AK-PC 781/781A (rack HFC/HFO, mais comum no Brasil) e AK-PC 772**: não foram encontrados PDFs oficiais da Danfoss na busca (apenas cópias em sites de terceiros; manualslib lista "Anhang B – Alarm Texts" no 781A). Usado o **AK-PC 782A (CO2 transcrítico)** — os textos de alarme de sucção, Pc, Sd, segurança de compressor, óleo e reservatório devem ser equivalentes, mas não foi confirmado.
- **Limites de fábrica do AK-PC 782A**: o manual não traz tabela de defaults para `T0 Min limit`, `Pc Max limit`, `Sd max limit`, `SH Min/Max alarm` e atrasos; os números citados são da aplicação de exemplo do manual.
- **Atrasos de alarmes de rack e de superaquecimento do VX-950 plus**: não especificados como default no texto extraído.
- **F70 do TC-900e Log**: valor padrão 60 lido, mas a unidade não ficou legível na extração de texto.
- **Valores de fábrica do TC-900e Log** tornam os alarmes de temperatura praticamente inativos (F06 = -50 °C, F07 = 105 °C, F55 = 0(NO)); em campo eles são configurados pelo instalador — no gêmeo, usar limites realistas, não os defaults.
- **Sitrad**: não levantado separadamente; o Sitrad exibe os alarmes de cada controlador (mesmos códigos acima).
- **Eliwell (EWPlus / ID974)**: não pesquisado (opcional).
- **Carel MPXPRO**: o PDF usado é a rel. 1.6 (2019) hospedada por distribuidor (Reece, Austrália); a página da Carel não retornou link direto. Revisões posteriores podem existir.
- **Danfoss não tem código de alarme "superaquecimento baixo" ou "MOP" nos controladores de evaporador** (EKC 202, AK-CC55): MOP é limitação da válvula, e o problema de injeção só aparece como A10 no AK-CC 550A. Superaquecimento com alarme explícito na Danfoss só aparece no rack (AK-PC 782A, SH na sucção).
- **Degelo por tempo como alarme**: só o AK-CC 550A ("Max Def.Time", via rede) e Full Gauge/Carel (ponto/Ed1) sinalizam; EKC 202 e AK-CC55 não têm código.
