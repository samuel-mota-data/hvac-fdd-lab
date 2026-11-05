# FDD e prognóstico em câmaras frias e refrigeração de supermercado: sensores mínimos e proteção de compressor

> Notas de pesquisa (nov/2026). Várias fontes primárias (MDPI, ASHRAE, PDFs do MMA) bloquearam a leitura completa (HTTP 403 ou PDF binário). Nesses casos, os números vêm do resumo, da ficha bibliográfica ou de trechos indexados e estão sinalizados como tal.

## 1. Falhas típicas em câmaras frias: frequência e custo

### Takeaway
Vazamento de refrigerante é a falha mais bem quantificada. Nos EUA, a taxa média anual de vazamento em supermercados é de cerca de 25% da carga. No Brasil, os números são bem maiores: média de 39% de recarga anual em 214 lojas e casos de 62% a mais de 100%. Para as demais falhas (gelo/degelo, porta, condensador, ventilador, válvula de expansão, elétricas), não encontrei estatística confiável de frequência. Há apenas descrição qualitativa e dados de carga térmica.

### Cited Findings
**Vazamento: EUA**
- O EPA GreenChill afirma repetidamente que o supermercado típico dos EUA tem taxa anual de vazamento de cerca de 25% da carga, ou aproximadamente 1.000 lb de refrigerante por loja por ano — [Supermarket News, "GreenChill Retailers Defy Refrigerant-Leak Trends"](https://www.supermarketnews.com/new-stores/greenchill-retailers-defy-refrigerant-leak-trends)
- Os parceiros GreenChill (cerca de 8.000 lojas) tiveram média de 12,95% em 2011 — [EPA GreenChill Progress Report 2011](https://19january2021snapshot.epa.gov/sites/static/files/documents/GreenChill_ProgressReport2011_09062012.pdf). Uma revisão de 10 anos cita 13,9% para parceiros contra 25% na indústria (blog Copeland/Emerson E360; a página original retornou 404, número obtido pelo snippet de busca) — [Copeland E360 blog](https://e360hub.copeland.com/emerson-e360-blog/10-takeaways-from-10-years-of-greenchill-data-2)
- O EPA define taxa de vazamento como a fração da carga total que seria perdida em 12 meses se a taxa atual continuasse — [EPA Leak Prevention and Repair Guidelines](https://19january2021snapshot.epa.gov/sites/static/files/2020-03/documents/leakpreventionrepairguidelines.pdf)
- Varejistas de melhor desempenho chegam a cerca de 6,5% ao ano (Meijer, segundo scorecard da EIA, ONG ambiental e não fonte oficial) — [EIA US Supermarket Scorecard 2024](https://bronze-guava-6mc9.squarespace.com/scorecard)

**Vazamento: Brasil**
- No estudo de Linzmayer (Instituto Mauá, 2010), 214 supermercados foram acompanhados por 40 meses. Os 10% piores tiveram recarga anual média de 137% da carga, os 10% melhores de 4% e o restante de 39%. O consumo foi de cerca de 202 t de refrigerante em 3 anos, aproximadamente R$ 1,5 milhão. 21% das lojas (45) responderam por 50% do gasto. Os principais pontos de vazamento foram porcas flange, flanges e evaporadores. Os condensadores, no lado de alta, concentram as maiores recargas, e os compressores abertos antigos vazam pelo selo mecânico. (Fonte secundária: o artigo não traz DOI.) — [WebArCondicionado, resumo do estudo Linzmayer](https://webarcondicionado.com.br/vazamentos-em-sistemas-de-refrigeracao-comerciais-principais-pontos-de-fuga-e-como-resolver); anexo original: [ABRAS, projeto demonstrativo](https://www.abras.com.br/pdf/demostrativo1.pdf)
- Ficha técnica GIZ/MMA de projeto demonstrativo de contenção de HCFC-22: a loja Yamada (Belém/PA) perdia 62% da carga instalada por ano antes da intervenção. O número veio do resumo da busca; não consegui extrair o texto do PDF. — [MMA, Ficha técnica 1](https://www.gov.br/mma/pt-br/assuntos/mudanca-do-clima/ozonio/ficha-tcnica-1-projeto-demonstrativo-de-melhor-conteno-de-hcfc-22-em-supermercados.pdf)
- Apresentação do PBH Etapa II (GIZ Proklima): o vazamento médio anual no setor de serviços de refrigeração seria de 102% da carga instalada, e supermercados responderiam por 96% do consumo de HCFC-22 em serviços de refrigeração. É uma apresentação, não um estudo revisado por pares. — [MMA, PBH Etapa II, setor de serviços](https://www.gov.br/mma/pt-br/composicao/smc/dpmi/ozonio/repositorio/publicacoes/prrograma-brasileiro-de-eliminacao-dos-hcfcs-pbh-etapa-ii-2013-proposta-para-o-setor-de-servicos.pdf)
- Documento PNUD/ABRAVA de 2018 associa o alto consumo de HCFC-22 em supermercados à falta de técnicos qualificados — [ABRAVA/PNUD IC-31881-2018](https://abrava.com.br/wp-content/uploads/2018/02/07022018201148_IC-31881-2018-Consultor-IC-PNUD-Monitoramento-Implementação-Projetos-Demonstrativos-Contenção-HCFC-22.pdf)

**Gelo no evaporador e degelo**
- Cerca de 25% da demanda total de energia de um refrigerador com resistência elétrica pode ir para o degelo (citado pelo IIR a partir de outro artigo) — [IIR, "A novel method for frost detection"](https://iifiir.org/en/news/a-novel-method-for-frost-detection)
- Em câmaras frigoríficas (coolers), o degelo costuma ser feito desligando o compressor várias vezes ao dia com os ventiladores ligados. Um timer mal instalado pode provocar partida inundada ("flooded start") ao fim de cada degelo — [HVACR School, Walk-in cooler defrost](https://hvacrschool.com/walk-in-cooler-defrost/)
- Em freezers, o degelo é elétrico e os ventiladores param durante o aquecimento (artigo patrocinado) — [FER Magazine, "Walk-in running warm"](https://www.fermag.com/articles/walk-in-running-warm-4-quick-checks-before-you-replace-the-compressor/)
- Muito gelo restringe o fluxo de ar e faz o compressor trabalhar mais. O gelo costuma ser sintoma de falha no degelo ou na porta, não do compressor — [WebstaurantStore, Walk-in cooler troubleshooting](https://www.webstaurantstore.com/guide/1205/walk-in-cooler-troubleshooting.html)

**Porta aberta / infiltração**
- A infiltração pela porta pode passar de metade da carga térmica total de uma câmara. Em caminhões refrigerados, estima-se cerca de 34% — [UBI repositório (tese/artigo sobre cortinas de ar)](https://ubibliorum.ubi.pt/bitstreams/3bed560e-51e2-4fd4-b49a-275ff35c38a5/download); [IIR, infiltração em porta de caminhão](https://iifiir.org/en/fridoc/infiltration-heat-load-through-the-doorway-of-a-refrigerated-truck-27923)
- Em estudo da Brunel com caminhão, uma cortina de ar a 3,1 m/s reduziu o consumo de energia em quase 48% — [Brunel BURA 2438/18126](https://bura.brunel.ac.uk/handle/2438/18126)

**Compressor**
- Cerca de 30% (quase um terço) dos compressores devolvidos à Copeland em garantia não têm defeito, o que indica diagnóstico errado em campo (imprensa técnica citando a Copeland) — [ACHR News, "The compressor mysteries"](https://achrnews.com/articles/92421-the-compressor-mysteries)
- Palestrante da Copeland: mais de 50% das falhas "elétricas" em garantia têm causa mecânica (frase truncada na fonte, tratar como não verificado) — [ACHR News, conferência de refrigeração](https://achrnews.com/articles/84057-refrigeration-conference-heats-up-down-south)
- O retorno de líquido (floodback) lava o óleo das superfícies lubrificadas e causa desgaste e superaquecimento — [Meier Supply / TechSpeaking 2011, Refrigerant Floodback](https://www.MeierSupply.com/customer/docs/Techtips/TechSpeaking%202011%20Issue5%20Refrigerant%20Floodback.pdf); [HVACR School, Common causes of compressor failure](https://hvacrschool.com/common-causes-of-compressor-failure/)
- Causas de superaquecimento citadas: alta relação de compressão, gás de retorno quente, carga baixa e condensador sujo — [HVACR School, Common causes of compressor failure](https://hvacrschool.com/common-causes-of-compressor-failure/)
- Quando a pressão de sucção cai (carga baixa, evaporador sujo ou com gelo), o compressor trabalha com diferencial maior e consome mais potência. Também roda por mais tempo porque a troca de calor diminui — [Contracting Business, Diagnosing walk-in coolers & freezers](https://www.contractingbusiness.com/refrigeration/article/20863468/diagnosing-walk-in-coolers-freezers)

### Inferences
- A distribuição dos vazamentos é muito assimétrica: 10–20% das lojas ou instalações concentram metade das perdas. Para quem vende monitoramento, isso favorece a triagem por anomalia de consumo, que encontra os "piores atores", em vez de buscar alta sensibilidade em todas as lojas.
- No Brasil, com perdas de 39% ao ano em média e mais de 100% nos piores casos, um algoritmo indireto com sensibilidade de alguns por cento da carga já teria alto valor econômico.
- Como cerca de 30% dos compressores trocados não tinham defeito, há espaço para um produto de "diagnóstico antes da troca" usando corrente e temperaturas.

### Gaps
- Não encontrei estatística confiável sobre a frequência relativa de falhas em câmaras frias (porcentagem de chamados por tipo: degelo, ventilador, válvula de expansão, porta, elétrica). Não há ranking oficial da Copeland (failure analysis) acessível publicamente; os números circulantes são de fontes secundárias.
- Não encontrei custo médio por evento (perda de produto, chamado técnico) em fontes brasileiras como ABRAVA, ABRAS ou revistas técnicas.

## 2. Quais sensores detectam cada falha, e o que se consegue só com potência/corrente/ciclo de trabalho

### Takeaway
A literatura acadêmica de FDD para walk-ins, iniciada em Wichman & Braun (2009), usa temperaturas e pressões do ciclo mais potência do compressor. Sinais baseados apenas em potência ou duty cycle aparecem sobretudo em patentes e guias de serviço: queda de corrente para gelo, aumento de runtime para carga baixa ou sujeira. Não encontrei validação quantitativa publicada de FDD só com potência em câmaras frias.

### Cited Findings
- **Wichman & Braun (2009)**, "Fault Detection and Diagnostics for Commercial Coolers and Freezers", *HVAC&R Research* 15(1). Os autores adaptaram a técnica de diagnóstico por desacoplamento ("decoupling-based") de ar-condicionado para walk-ins e testaram uma câmara pequena de restaurante (cooler) e um walk-in freezer em câmara psicrométrica, com e sem falhas — [IIR Fridoc 132110](https://iifiir.org/en/fridoc/fault-detection-and-diagnostics-for-commercial-coolers-and-freezers-132110). Faltas simuladas incluíram vazamento de válvula do compressor, sujeira no condensador e sujeira no evaporador. Potência do compressor e vazão mássica foram medidas para calcular capacidade e eficiência (snippet de busca da cópia em Scribd) — [Scribd, ASHRAE RJ150104](https://es.scribd.com/document/234315304/30661ASHRAE-D-RJ150104-20081223)
- **Sensores virtuais** (Kim & Braun, *Int. J. Refrigeration*, 2016): três sensores virtuais de vazão mássica de refrigerante, obtidos de medições baratas como temperaturas e potência. A diferença entre eles indica perda de desempenho do compressor e serve para FDD. O trabalho foi feito em RTU/split, não em walk-in — [PNNL, "Development and evaluation of virtual refrigerant mass flow sensors"](https://www.pnnl.gov/publications/development-and-evaluation-virtual-refrigerant-mass-flow-sensors-fault-detection-and); [Braun, Virtual Sensors (Purdue workshop)](https://engineering.purdue.edu/HVACFDD/pdfs/Workshop_on_FDD_for_RTUs_Presentations/Virtual_Sensors_Braun.pdf)
- **Gelo/degelo, detecção indireta**:
  - Patente de bomba de calor: inicia o degelo quando a corrente do compressor cai abaixo de uma referência por um diferencial predefinido. É assinatura de potência para gelo — [US4104888A](https://patents.google.com/patent/US4104888)
  - Patente antiga: mede a potência do ventilador do evaporador, porque o gelo restringe o ar — [US4831833A](https://patents.google.com/patent/US4831833)
  - Patente recente: estima a potência esperada do compressor a partir de temperaturas e sinaliza gelo quando a potência medida se desvia — [Frost detection in HVAC&R systems, ipiq](https://ipiq.io/patents/3919068)
  - Maldonado et al. (*Int. J. Refrigeration*, 2020) propõem um método indireto de nível de gelo validado contra o método ΔT num walk-in freezer e testado num sistema multicâmara com rack. O método reduz o número de degelos e a energia de recuperação — [IIR Fridoc 141998](https://iifiir.org/en/fridoc/frost-detection-method-on-evaporator-in-vapour-compression-systems-141998); [IIR news](https://iifiir.org/en/news/a-novel-method-for-frost-detection)
  - Revisão de medição de gelo para degelo por demanda: o gelo pode ser estimado por ΔT ar–evaporador, perda de carga do ar, superaquecimento ou potência do ventilador. O degelo por demanda ainda é visto como complexo ou pouco confiável na prática — [core.ac.uk 304001116](https://core.ac.uk/download/304001116.pdf)
- **Controladores comerciais** (Heatcraft, KE2) registram falhas de degelo com timestamp no histórico. A fonte é de procedência fraca — [industrial-fixes (não verificado)](https://industrial-fixes.pages.dev/posts/norlake-walkin-error-code)
- **Full Gauge / Sitrad**: alarmes quando um parâmetro sai de uma faixa predefinida — [Full Gauge news](https://www.fullgauge.com/en/news/doing-groceries-shopping-at-the-right-temperature). O Sitrad InBox concentra até 32 controladores via RS-485 e dá acesso remoto a temperatura, umidade, pressão e tensão — [Robertshaw, Sitrad InBox](https://www.robertshaw.com/parts/temperature-controls/digital-controller-series/sitrad-inbox/). Há relatórios e gráficos a partir dos dados armazenados e alertas por e-mail — [Norlake LogiTemp Sitrad Instructions](https://beta.norlake.com/wp-content/uploads/2024/03/LogiTemp-Sitrad-Instructions.pdf)

### Inferences
Matriz falha × evidência. É síntese das fontes acima com raciocínio físico. As linhas sem citação direta são inferência.

| Falha | Sensor mínimo com melhor evidência | Assinatura em potência/corrente/duty cycle (só P) |
|---|---|---|
| Vazamento lento | Subresfriamento (T_líquido + P_desc) e COP; nível do receptor | Runtime ↑ gradual e P média ↓ (sucção cai). Fraco isolado, porque se confunde com carga térmica |
| Vazamento catastrófico | Subresfriamento (F1 = 1,0 no estudo MDPI) | Ciclo contínuo e T_caixa sobe |
| Gelo / falha de degelo | ΔT ar–evaporador; T_evap; potência do ventilador | P_compressor ↓ lentamente entre degelos; ausência periódica do "vale" de degelo no perfil de P |
| Porta aberta | Chave de porta; T_caixa | Duty cycle ↑ em horário comercial; picos de runtime correlacionados com operação |
| Condensador sujo | T_desc / P_desc; ΔT condensador–ambiente | P ↑ (pressão de alta ↑) com mesmo runtime |
| Ventilador do evaporador | Corrente do ventilador; ΔT | P_comp ↓ e T_caixa ↑ (parecido com gelo) |
| Válvula de expansão | Superaquecimento (T_suc + P_suc) | Hunting: oscilação de P; floodback é indistinguível sem T_suc |
| Short cycling | Corrente/estado on-off | Diretamente observável: partidas por hora |
| Elétrica | Tensão, corrente por fase | Desequilíbrio, sobrecorrente, trip |

- Corrente ou potência do compressor mais T_caixa mais chave de porta parece o conjunto mínimo com melhor custo-benefício: cobre short cycling, porta, falha de degelo (pela ausência do padrão periódico) e degradação lenta (tendência de runtime). Não distingue com segurança vazamento lento de gelo ou ventilador. Para isso, T_evap ou T_sucção é o próximo sensor de maior valor.

### Gaps
- Não encontrei artigo revisado por pares que valide FDD em câmara fria usando apenas potência/corrente (ou duty cycle) com métricas de acurácia. As evidências são patentes e guias de serviço.
- Não consegui acessar a lista completa de falhas e as métricas de Wichman & Braun (2009); o texto completo está em ASHRAE/Taylor & Francis.

## 3. Detecção de vazamento sem detector de gás (métodos indiretos)

### Takeaway
Os métodos indiretos usam nível do receptor, subresfriamento, COP, relação de compressão e consumo. Os melhores números: detecção com perda acima de 1% da carga em protótipo num supermercado do Colorado (2006) e F1 médio de 0,92 em até 5 dias para vazamentos lentos (Energies, 2024). Para vazamentos lentos, apenas o COP respondeu nesse estudo.

### Cited Findings
- **Assawamartbunlue & Brandemuehl (2006)**, "Refrigerant leakage detection and diagnosis for a distributed refrigeration system", *HVAC&R Research* 12(3). Usa medições simples e baratas de estados termodinâmicos e trata a complexidade do sistema e a presença do receptor de líquido — [IIR Fridoc 126876](https://iifiir.org/en/fridoc/refrigerant-leakage-detection-and-diagnosis-for-a-distributed-126876). Segundo resumo indexado, o protótipo num supermercado do Colorado detectava perda acima de 1% da carga inicial. Os autores observam que, com vários pontos de vazamento e receptor de líquido, os instrumentos e técnicas termodinâmicas usados em HVAC não garantem detecção correta — [AIVC record](https://www.aivc.org/node/30406) (resumo via busca; não li o texto completo)
- **Wijethunga, Nouraei, Zych, Samarabandu, Sadhu (2024)**, "Refrigerant leak detection in supermarket refrigeration…", *Energies* 17(3), 736. O framework detecta vazamentos lentos e catastróficos e não depende do nível do receptor. Variáveis usadas: COP, subresfriamento, superaquecimento, vazão mássica, relação de compressão e consumo de energia, com modelo de gradient boosting categórico. F1 para vazamento catastrófico: subresfriamento 1,00, relação de compressão 0,88, COP 0,72, vazão 0,70, superaquecimento 0,41. Para vazamento lento, só o COP respondeu, com F1 médio de 0,92 em até 5 dias após o início. Dados do abstract e de snippets; o MDPI retornou 403 — [MDPI Energies 17(3) 736](https://www.mdpi.com/1996-1073/17/3/736); [DOAJ](https://doaj.org/article/13bb1c0752fe4568aabe1172ac28448f)
- **Patentes de detecção pelo nível do tanque**:
  - Usa os sensores já existentes nos tanques/receptores de refrigerante mais um modelo analítico, sem sensor infravermelho adicional, para reduzir custo — [US10126031B2](https://patents.google.com/patent/US10126031)
  - Outra família trata flutuações anormais do nível como sinal de vazamento — [Justia US20180017299](https://patents.justia.com/patent/20180017299)
  - Patentes mais recentes cobrem múltiplos circuitos com um ou mais compressores — [US 12298049](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12298049); [US 12359856](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12359856)
- **Imprensa técnica**: a detecção automática indireta infere vazamentos analisando continuamente nível de refrigerante, pressão, temperatura e consumo do compressor, e pode sinalizar perda antes dos sensores diretos. O texto é de fornecedor — [ACHR News, Proactive refrigerant leak detection](https://www.achrnews.com/articles/165548-proactive-refrigerant-leak-detection-helps-protect-profits)
- **Danfoss**: o sensor de nível AKS 4100/4100U (TDR/micro-onda guiada, saída 4–20 mA) mede o nível em receptores. Não encontrei documentação pública do algoritmo de vazamento da Danfoss — [Danfoss AKS 4100 data sheet](https://assets.danfoss.com/documents/latest/103366/AI000086413930en-000101.pdf)

### Inferences
- Em câmara fria com unidade condensadora (sem receptor grande ou com receptor sem sensor de nível), o melhor indicador indireto disponível é o subresfriamento, que exige T_linha_líquido e P_descarga ou T_condensação. Sem eles, resta a tendência de COP ou runtime normalizado pela carga térmica (T_externa, aberturas de porta), que no estudo de 2024 detectou vazamentos lentos em cerca de 5 dias.
- Com subresfriamento disponível, a sensibilidade publicada fica na ordem de 1% da carga em sistema com receptor monitorado. Sem receptor ou subresfriamento, a sensibilidade cai bastante e não está bem quantificada.

### Gaps
- Não encontrei white paper Danfoss ou Emerson/Copeland com sensibilidade (% de carga) e tempo de detecção dos algoritmos comerciais (por exemplo, AK-SM, E2/E3, Site Supervisor).
- Não encontrei estudo de vazamento indireto específico para câmaras frias pequenas com unidade condensadora (tipologia predominante no varejo brasileiro).

## 4. Prognóstico: prever falha do compressor / tempo até o desarme

### Takeaway
Não encontrei estudo revisado por pares de RUL (remaining useful life) para compressores de refrigeração comercial em supermercados ou câmaras frias. O que existe são patentes (vida restante a partir de T_linha_líquido e T_ar, ou de corrente e tensão), material de fornecedor e RUL em compressores industriais não frigoríficos.

### Cited Findings
- **Família de patentes "Asset management and IoT device for refrigerated appliances"**: combina T da linha de líquido e T do ar com um modelo do fabricante para prever a vida restante do compressor e disparar alarmes de manutenção. Correlaciona essas temperaturas com a degradação da eficiência do compressor — [US 12335767](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12335767)
- **Patente japonesa**: estima a vida residual do compressor ponderando o tempo de operação por constantes obtidas em ensaios de vida sob combinações de corrente e tensão do inversor — [US 8805623](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8805623)
- **FMMEA aplicada a dispositivo de refrigeração**: propõe avaliar o estado de saúde por fusão de parâmetros como base para RUL — [Scientific.net AMM 288:69](https://www.scientific.net/AMM.288.69)
- **Compressor alternativo industrial (não frigorífico)**: CVA, Cox Proportional Hazard e SVR para prever o tempo restante a partir de dados de sensores — [IOS Press, J. Intelligent & Fuzzy Systems](https://content.iospress.com/articles/journal-of-intelligent-and-fuzzy-systems/ifs169550)
- **Blog de fornecedor (OxMaint, marketing)**: cita como precursores de falha a corrente acima da placa, o aumento da variância da pressão de sucção e a temperatura de descarga elevada — [OxMaint](https://oxmaint.com/industries/hvac/refrigeration-asset-lifecycle-benchmarks-for-grocery-chains)

### Inferences
- Um prognóstico viável com sensores mínimos seria do tipo "tempo até o desarme" (time-to-trip), não RUL mecânico. As variáveis seriam a tendência de corrente média por ciclo, partidas por hora (short cycling), a temperatura de descarga, quando disponível, e tendências de duty cycle. As causas raiz que matam compressores (floodback, superaquecimento, carga baixa) são parcialmente observáveis por esses sinais.

### Gaps
- Sem dataset público de run-to-failure de compressores de refrigeração comercial. Sem métricas publicadas de horizonte de predição.

## 5. Contexto do mercado brasileiro

### Takeaway
No Brasil predominam câmaras com unidade condensadora e controladores digitais nacionais (Full Gauge, com supervisão Sitrad). A transição de fluido no varejo está saindo de HCFC-22 e R404A para R290 (plug-ins), HFO/HFC de menor GWP (R449A/XP40) e CO2 em lojas maiores. O vazamento é o problema operacional mais documentado por fontes oficiais (MMA/GIZ/ABRAS).

### Cited Findings
- **Full Gauge / Sitrad**: o Sitrad é o software de supervisão remota da Full Gauge para refrigeração e climatização — [Full Gauge](https://www.fullgauge.com/en/). O app Sitrad Mobile faz gráficos e relatórios e envia avisos quando variáveis saem dos limites — [App Store, Sitrad](https://apps.apple.com/app/id538790187). Há caso de centro logístico brasileiro de câmaras frias com 31 soluções Full Gauge, incluindo o Sitrad (notícia corporativa) — [Full Gauge news](https://www.fullgauge.com/en/news/precise-control-that-protects-crops-full-gauge-and-sitrad-in-potato-seed-storage-in-south-africa)
- **Transição de fluidos**:
  - A AHT forneceu expositores com R290 para substituir unidades R404A em 36 lojas Swift no Brasil — [Cooling Post](https://www.coolingpost.com/features/brazilian-store-switches-to-r290-refrigeration/)
  - Casos de retrofit R404A para Opteon XP40 (R449A) no Supermercado ABC (MG) e na Superfrio. Material do fabricante, que estima consumo brasileiro de cerca de 1.500 t/ano de R404A — [Chemours, Caso ABC](https://pages.chemours.com/rs/509-VCL-038/images/Caso%20de%20Sucesso%20-%20Opteon%E2%84%A2%20XP40%20-%20ABC%20Weblight.pdf); [Chemours, Caso Superfrio](https://pages.chemours.com/rs/509-VCL-038/images/Caso%20de%20Sucesso%20-%20Opteon%E2%84%A2%20XP40%20-%20SUPERFRIO%20Weblight.pdf)
  - UFU (bancada): o R449A teve COP de 1,07% a 11,45% maior que o R404A — [Repositório UFU](https://repositorio.ufu.br/bitstream/123456789/31499/1/An%c3%a1liseExperimentalSistema.pdf)
  - R290 aceito no Brasil dentro dos limites de carga da IEC 60335-2-89 (até 500 g, segundo a Embraco em 2022) — [Embraco, Refrigerant trends 2022](https://www.embraco.com/wp-content/uploads/2022/03/en-presentation-refrigerants-trends-for-sea-region-2022.pdf); [Embraco position paper (PT)](https://www.embraco.com/wp-content/uploads/2019/09/embraco-position-paper-portugues.pdf)
- **Programa Brasileiro de Eliminação dos HCFCs (PBH)**: projetos demonstrativos GIZ/ABRAS de contenção de HCFC-22 em três supermercados (Etapa 2) — [ABRAS, projeto demonstrativo](https://www.abras.com.br/pdf/projetodemostrativo.pdf); estudo de caso Angeloni — [MMA, Estudo de caso Angeloni](https://www.gov.br/mma/pt-br/composicao/smc/dpmi/ozonio/repositorio/publicacoes/estudo-de-caso-angeloni.pdf)
- **Causas de falha em câmaras frias (fonte de fabricante chinês, baixa autoridade)**:
  - Vazamentos por tubulação corroída, conexões frouxas, vibração e instalação inadequada
  - Paradas por falta de energia, disjuntor, controlador ou sobrecarga
  - Reinícios repetidos agravam o dano

  — [Beyond, Cold room faults (PT)](https://cn-beyond.com/pt/cold-room-faults-and-troubleshooting)

### Inferences
- A combinação "Full Gauge + Sitrad" é a base instalada provável em pequenas e médias câmaras brasileiras. Esses sistemas já entregam T_caixa, T_evaporador (sensor de degelo) e, em alguns modelos, pressão e tensão. Um produto de FDD mínimo poderia ler esses dados (RS-485/Modbus) e acrescentar corrente do compressor, em vez de instalar uma nova malha de sensores.
- Como o vazamento brasileiro é muito maior que o americano (39% a mais de 100% contra cerca de 25%), um detector indireto de vazamento por tendência de runtime/COP tem caso de negócio mais forte no Brasil.

### Gaps
- Não encontrei estatística da ABRAVA ou de revistas brasileiras (Revista do Frio, Climatização & Refrigeração) sobre a frequência de falhas por tipo em câmaras frias.
- Não encontrei teses da USP ou da UFSC (POLO) específicas sobre FDD de câmaras frias nesta rodada de buscas.
- Não confirmei o cronograma regulatório brasileiro atual (Kigali/HFC) em fonte oficial.
- Não encontrei documentação pública sobre a lógica de alarmes avançados (degelo, porta, vazamento) no Sitrad Pro; o manual existe, mas não foi lido.
