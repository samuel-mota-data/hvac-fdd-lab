# Datasets públicos de falhas em equipamentos HVAC&R por compressão de vapor com medições elétricas

Escopo: datasets com falhas injetadas ou rotuladas que trazem pelo menos uma variável elétrica (potência, corrente, tensão ou forma de onda), para validar um gêmeo digital e FDD baseado só em sinais elétricos. Pesquisa feita em 2026-11-05. Vários portais (MDPI, Nature, PMC, ScienceDirect, figshare) bloquearam acesso automatizado (403 ou captcha), então parte dos detalhes veio do Europe PMC (texto completo), do OEDI/LBNL e de PDFs de documentação baixados. Onde algo não foi lido na fonte primária, isso está dito.

## 1. LBNL/PNNL/NREL/ORNL "FDD Datasets" (Granderson et al., Scientific Data 2023): conteúdo, variáveis elétricas, licença

### Takeaway
É o maior conjunto público de dados HVAC com falhas, sob CC BY 4.0 no OEDI, permitindo uso comercial com atribuição. Mas a parte elétrica é só potência ativa média de 1 min (W de compressor, ventilador e total). Para compressão de vapor, o que interessa é o **dataset RTU**: falhas de refrigerante simuladas (carga, fouling, restrições) com potência do compressor, e dados de campo com subcarga de 40% e pressões/temperaturas de refrigerante. Não há corrente, tensão nem formas de onda.

### Cited Findings
- Artigo: Granderson J. et al., "A labeled dataset for building HVAC systems operating in faulted and fault-free states", *Scientific Data* 10, 342 (2023), DOI 10.1038/s41597-023-02197-w. Apresentado como o maior dataset público conhecido de operação com e sem falhas. Os dados vêm de simulação, de laboratório e de campo — [DOAJ](https://doaj.org/article/d8cbee367b4d4e7389baf74179a3848b)
- Repositório oficial OEDI: "LBNL Fault Detection and Diagnostics Datasets", DOI 10.25984/1881324, **licença Creative Commons Attribution 4.0 (CC BY 4.0)**. Cobre 7 sistemas: RTU, AHU de duto simples, AHU de duto duplo, caixa VAV, fan coil, planta de chiller e planta de caldeira. Cada dataset traz um PDF, CSVs (um por severidade, mais o caso sem falha) e um TTL no esquema Brick — [OEDI submission 5763](https://data.openei.org/submissions/5763)
- Os dados também estão em faultdetection.lbl.gov/data, com links por sistema. O RTU tem "10 faults … in 5 RTUs" (simulação EnergyPlus-Modelica, laboratório e campo, de 1 a 183 dias). A planta de chiller tem 7 falhas simuladas em 1 ano. A página não informa licença; o contato é afdd@lbl.gov — [LBNL FDD data](https://faultdetection.lbl.gov/data)
- Tamanhos segundo o artigo: chiller plant com 22 arquivos e 1,14 GB; RTU com 84 arquivos e 293 MB; AHU SD com 593 MB; DD-AHU com 1,65 GB; FPU com 2,04 GB; FCU com 518 MB. O passo é de 1 minuto. O chiller é **só simulado**, e o artigo cita o RP-1043 como trabalho anterior, sem incluí-lo — [Europe PMC full text PMC10235024](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10235024/fullTextXML)
- Variáveis elétricas do RTU (documentação oficial, PDF de 26 páginas): `RTU_TOT_WATT` (potência total, W), `RTU_COMP_WATT_1`/`_2` (potência elétrica dos compressores, W), `RTU_SA_FAN_WATT` (ventilador de insuflamento, W), `HVAC_TOT_WATT` e `VAV_RM_WATT_xxx`. Todos são potência ativa em W; **não há corrente, tensão nem forma de onda** — [LBNL_FDD_Data_Sets_RTU.pdf](https://fdddata.lbl.gov/data/Simulated_LBNL_FDD_Data_Sets_RTU/LBNL_FDD_Data_Sets_RTU.pdf)
- RTU **simulado** (Modelica, R410A, TXV): 100 dias (20/jul a 28/out) com TMY3 de San Francisco. Falhas e severidades: sobrecarga 10/15/20%; subcarga 10/15/20%; fouling do condensador (redução de vazão de ar 10–50%, em 5 níveis); fouling do evaporador (10–50%); restrição na linha de líquido (1/4/8/10 bar); restrição na linha de sucção (1/3/6/9 bar); mais o baseline. São cerca de 25 CSVs (`RTU_sim_*.csv`), com pressões e temperaturas de refrigerante (descarga, sucção, saída do condensador) e potência do compressor — [LBNL_FDD_Data_Sets_RTU.pdf](https://fdddata.lbl.gov/data/Simulated_LBNL_FDD_Data_Sets_RTU/LBNL_FDD_Data_Sets_RTU.pdf)
- RTU **de campo** (UConn, Prof. Ravi Gorthala, monitorado com ClimaCheck/Enerfit). Site 1 (restaurante em Milford, CT; 7,5 TR): falha de estágio do compressor ("Stage 2 will not engage") de 9/jun a 8/ago/2021, mais baseline. Site 2 (centro de distribuição em Colchester, CT; 10 TR): **subcarga de 40% no circuito B** de 1 a 29/jun/2020, mais cerca de 5 meses de baseline. Medições a cada 1 min: potência de ventilador, compressor e total (W), pressões de descarga e sucção por estágio (bar) e temperaturas de linha de descarga — [LBNL_FDD_Data_Sets_RTU.pdf](https://fdddata.lbl.gov/data/Simulated_LBNL_FDD_Data_Sets_RTU/LBNL_FDD_Data_Sets_RTU.pdf)
- RTU **experimental** (FRP, Oak Ridge): 48 casos com falha e 4 sem falha, todas no lado do ar ou do controle (damper OA travado, setpoint de economizador errado, sensor de temperatura de insuflamento enviesado), sem falha de refrigerante. Passo de 1 min — [LBNL_FDD_Data_Sets_RTU.pdf](https://fdddata.lbl.gov/data/Simulated_LBNL_FDD_Data_Sets_RTU/LBNL_FDD_Data_Sets_RTU.pdf)
- Existe uma versão anterior (Granderson et al. 2020, "LBNL Data Synthesis Inventory") no figshare, com 24 falhas em AHU e RTU e duração de 1 a 7 dias — [figshare 11752740](https://figshare.com/articles/dataset/LBNLDataSynthesisInventory_pdf/11752740/3)

### Inferences
- Para validar um gêmeo digital de **potência do compressor sob falhas de refrigerante**, o RTU simulado é o melhor ponto de partida: severidades graduadas e licença comercial-friendly (CC BY 4.0). Como ele é gerado por modelo Modelica, serve mais para comparar modelo com modelo do que como "verdade de campo".
- O caso de campo Colchester (subcarga de 40%) é o único dado **real** de subcarga com potência e pressões disponível sob CC BY. É útil para testar FDD só elétrico, usando as pressões como verificação.
- A resolução de 1 min e a variável em W (média) não permitem análise espectral de corrente (MCSA). Só servem para FDD baseado em potência e duty-cycle.

### Gaps
- Não consegui abrir o artigo na Nature (redirecionamento de autenticação). Os detalhes vieram do Europe PMC, cujo texto lido não mostrava a licença dos **dados** no figshare. A licença CC BY 4.0 confirmada é a do OEDI.
- Não verifiquei, arquivo por arquivo, quais colunas elétricas existem no dataset da planta de chiller (potência do chiller em kW, por exemplo).

## 2. ASHRAE RP-1043 (chiller centrífugo, Comstock & Braun): disponibilidade e licença

### Takeaway
Os dados do RP-1043 (chiller centrífugo de 90 TR, 7 falhas × 4 severidades) circulam amplamente, mas a distribuição oficial é da ASHRAE (relatório final e dados vendidos ou distribuídos pelo TC 4.11/bookstore). Não achei licença aberta explícita. Há um espelho de terceiros no figshare (48,73 MB) que não consegui abrir. Para uso comercial, o RP-1043 deve ser tratado como **"licença incerta / direitos ASHRAE"**.

### Cited Findings
- Os dados são descritos como condição normal mais sete condições de falha em quatro níveis de severidade. O relatório final esteve no site do TC 4.11. Referências: Comstock, Braun & Bernhard (1999), "Experimental Data from Fault Detection and Diagnostic Studies on a Centrifugal Chiller" (Purdue); e Comstock, Braun & Groll, "A Survey of Common Faults for Chillers", ASHRAE Trans. 108(1), 2002 — [resultado de busca agregando IIR/Sandia](https://www.sandia.gov/raiice/?p=6519)
- Espelho de terceiros: "Chiller operation data set" no figshare, de Zengrui Tian, postado em 18/02/2025, 48,73 MB. O conteúdo é descrito como vários tipos de falha de chiller (aparentemente RP-1043). A página retornou 403 ao fetch, então não conferi a licença — [figshare 28435232](https://figshare.com/articles/dataset/Chiller_operation_data_set/28435232)
- A Sandia (RAIICE) lista o RP-1043 como "chiller operation data set" da ASHRAE — [Sandia RAIICE](https://www.sandia.gov/raiice/?p=6519)
- O artigo LBNL 2023 cita o RP-1043 como fonte histórica, mas não o redistribui — [Europe PMC PMC10235024](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10235024/fullTextXML)

### Inferences
- Pela literatura que usa o RP-1043 (conhecimento prévio, não verificado nesta sessão), as variáveis incluem cerca de 64 pontos, entre eles a potência do compressor (kW), em passos de ~10 s. A parte elétrica se limita à potência, sem formas de onda.
- Um espelho no figshare costuma vir com CC BY 4.0 por padrão, mas isso não transfere direitos que pertencem à ASHRAE. Para produto, convém pedir permissão à ASHRAE.

### Gaps
- Não confirmei a licença do espelho figshare (403), a URL atual do TC 4.11 nem a lista exata de variáveis e a taxa de amostragem a partir da fonte primária.

## 3. NIST: heat pump/AC residencial com falhas (Domanski, Payne, Yoon, Kim)

### Takeaway
Existe um release público do NIST (DOI 10.18434/M32132) com dados de testes em modo resfriamento de uma heat pump 14 SEER e de um AC 16 SEER, em vários tipos de falha simples, regime permanente, distribuídos como planilhas Excel. Por ser obra do governo dos EUA, deve ser de domínio público nos EUA, mas a página não traz declaração de licença explícita.

### Cited Findings
- O catálogo descreve medições de desempenho sem falha e com falha de duas máquinas (uma heat pump 14 SEER e um ar-condicionado 16 SEER), em modo resfriamento, em regime permanente, numa ampla faixa de temperaturas e umidades interna e externa. DOI: 10.18434/M32132 — [data.commerce.gov](https://data.commerce.gov/node/317714)
- O DOI redireciona à página do NIST HVAC&R Equipment Performance Group. Há três downloads diretos (sem registro): "NISTIR 7350 test data summaries (Appendix D)" em .xls; "Data description for the 14 and 16 SEER FDD cooling tests" em .xlsx; "FDD data for the 14 and 16 SEER cooling tests" em .xlsx. O grupo diz ter mais de 200 GB de dados de testes, entre resumos e séries temporais. **A página não traz declaração de licença**, e a página não menciona variáveis elétricas — [NIST FDD page](https://www.nist.gov/el/energy-and-environment-division-73200/hvacr-equipment-performance-group/fault-detection-and)
- Relatórios associados: NISTIR 7350 (Kim, Payne, Domanski 2006), com falhas simples em resfriamento ([PDF](https://nvlpubs.nist.gov/nistpubs/ir/2006/ir7350.pdf)), e NIST TN 1648 (Payne, Domanski, Yoon 2009), com 6 falhas em modo aquecimento: sub e sobrecarga, restrição na linha de líquido, problemas de vazão de ar e outras, mais testes transientes — [NIST TN](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.1774.pdf)

### Inferences
- Os testes calorimétricos do NIST normalmente registram a potência do sistema, do compressor e dos ventiladores. Pelo padrão desses relatórios, o .xlsx deve conter potência em W em médias de regime permanente, sem formas de onda. Isso **precisa ser verificado abrindo a planilha**.
- Nos EUA, obras de funcionários federais não têm copyright (17 U.S.C. §105). O uso comercial tende a ser livre, mas não há declaração no próprio dataset, e a lei não necessariamente se aplica fora dos EUA.

### Gaps
- Não abri as planilhas: as colunas elétricas, o número de pontos e a lista de falhas por máquina não foram confirmados. Os 200 GB de séries temporais não aparecem como download público.

## 4. UFPB: split AC com medição elétrica de alta frequência (de Oliveira et al., Data 2024, 9(9):106)

### Takeaway
É o candidato mais alinhado ao objetivo de FDD só elétrico: corrente e tensão brutas a 30 kHz, por 60 s, num split de 18.000 BTU/h instalado em campo, com fouling de condensador e evaporador em vários níveis, degradação do capacitor do compressor e combinações de duas falhas. A licença do dataset é **CC-BY-NC**, que **impede uso comercial** sem autorização dos autores.

### Cited Findings
- Artigo: de Oliveira A.C., Lima Filho A.C., Belo F.A., Cadena A.V.O., "Analysis of Split-System Air Conditioner Faults through Electrical Measurement Data", *Data* (MDPI) 9(9):106, set. 2024, DOI 10.3390/data9090106. O artigo é open access sob CC BY — [IDEAS/RePEc](https://ideas.repec.org/a/gam/jdataj/v9y2024i9p106-d1477561.html); [OpenAlex](https://api.openalex.org/works/doi:10.3390%2FDATA9090106)
- Equipamento: split de 5272 W (18.000 Btu/h), instalado num escritório do grupo de pesquisa (operação em campo). Sensores: corrente não invasivo e tensão (sensor de "grão orientado"). Falhas: incrustação na entrada de ar do condensador e do evaporador, em diferentes níveis, e degradação do capacitor do compressor, rotulada como % de perda de capacitância. O artigo inclui exemplos de FFT para FDD — [MDPI (snippet de busca)](https://www.mdpi.com/2306-5729/9/9/106); [IDEAS](https://ideas.repec.org/a/gam/jdataj/v9y2024i9p106-d1477561.html)
- Formato: arquivos .txt, com a corrente na 1ª coluna e a tensão na 2ª. Cada registro tem 60 s a 30.000 Hz (1.800.000 amostras). Há um arquivo por condição: sem falha, cada falha individual e combinações de duas falhas — [MDPI (snippet)](https://www.mdpi.com/2306-5729/9/9/106)
- Licença do dataset indicada na página MDPI: **"Dataset License: CC-BY-NC"**. Esta informação veio do snippet de busca; a página respondeu 403 ao fetch direto — [MDPI](https://www.mdpi.com/2306-5729/9/9/106)
- Tese associada (UFPB, A.C. de Oliveira, orientador Lima Filho, set/2024): diagnóstico por análise caótica da corrente. Cobre fouling do evaporador, do condensador e do filtro de ar, e degradação do capacitor, com comparação contra FFT — [Repositório UFPB](https://repositorio.ufpb.br/jspui/handle/123456789/33632); [PDF da tese](https://repositorio.ufpb.br/jspui/bitstream/123456789/33632/1/AndersonCarlosDeOliveira_Tese.pdf)
- Resultado reportado pelo grupo (IIR/FRIDOC): 100% de FDD em falhas simples, e 96,55% de detecção e 82,76% de diagnóstico em falhas múltiplas — [IIR FRIDOC](https://iifiir.org/en/fridoc/fault-diagnosis-in-split-system-air-conditioner-by-analyzing-the-chaos-150329)

### Inferences
- Pela tensão de rede e pelo capacitor de partida/marcha, o split é provavelmente on-off (compressor PSC monofásico). Isso o torna representativo de splits residenciais brasileiros convencionais, não de inverter.
- A NC impede usar os dados diretamente em produto. Para pesquisa e validação de algoritmo dá para usar; para produto, é preciso obter licença dos autores (UFPB) ou gerar dados próprios.
- Não há temperaturas nem pressões, ou seja, não há verdade termodinâmica. O dataset serve para validar a assinatura elétrica, não o modelo termodinâmico do gêmeo.

### Gaps
- **Não confirmei o link exato de download nem o DOI do depósito.** O MDPI deu 403, e um resultado de busca citou "Mendeley Data 2023, 2, 109208", o que não parece um DOI Mendeley válido. O DOI Mendeley 10.17632/2mmf3ts9dk é **outro** dataset (ver seção 5). É preciso abrir a seção "Data Availability" do artigo manualmente.
- Não confirmei os níveis exatos de severidade (% de obstrução, % de perda de capacitância), o número total de arquivos nem o tamanho.

## 5. Refrigeração/câmara fria/supermercado, compressores e eletrodomésticos (Mendeley, Kaggle, IEEE DataPort, Zenodo, figshare)

### Takeaway
O melhor dataset de refrigeração comercial é o do ORNL (Sun et al., Scientific Data 2021): rack de CO2 com 6 falhas em 3 níveis, potência por compressor a 1 s, sob CC BY 4.0. Para corrente bruta de compressor doméstico, o mais próximo é o dataset de eletrodomésticos (geladeiras) de Fonseca et al. (Data in Brief 2023, CC BY), com corrente a 1 Hz e 2048 Hz rotulada normal/defeito. Os demais candidatos são simulados ou mal documentados.

### Cited Findings
- **ORNL, supermercado com refrigerante de baixo GWP (CO2):** Sun J., Im P., Bae Y., Munk J., Kuruganti T., Fricke B., "Dataset of low global warming potential refrigerant refrigeration system for fault detection and diagnostics", *Scientific Data* (2021), DOI 10.1038/s41597-021-00927-6. É um sistema de laboratório com rack de 2 compressores LT e 3 MT — [ORNL](https://impact.ornl.gov/en/publications/dataset-of-low-global-warming-potential-refrigerant-refrigeration/); [DOAJ](https://doaj.org/article/0f4e6cea84194516a8164c381b9213ea)
  - Falhas e severidades: porta do expositor LT aberta (5/10/15% do tempo); gelo no evaporador LT (leve/moderado/severo); falha da válvula de expansão LT (parcialmente ou totalmente fechada); falha dos ventiladores do evaporador MT (25/50/75%); bloqueio do ar no condensador ou gas cooler (25/50/75%); bloqueio do ar no evaporador MT (25/50/75%). São 6 testes de falha, cada um com baseline, num total de 12 CSVs de ~95 MB cada (o de gelo tem 30,7 MB) — [Europe PMC PMC8159987](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8159987/fullTextXML)
  - Variáveis elétricas: transdutores de potência (W) nos 3 compressores MT (0–80 kW) e nos 2 LT (0–8 kW), com ±5% da leitura, além de potência de ventiladores do condensador, resistências de carga falsa, degelo e ventiladores dos expositores. **Não há corrente nem tensão.** Amostragem de 1 s (3 s no arquivo de gelo). Também há temperaturas e pressões do circuito — [Europe PMC PMC8159987](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8159987/fullTextXML)
  - Repositório: figshare, DOI 10.6084/m9.figshare.13232627 (dados) e 10.6084/m9.figshare.14384321 (metadados, CC0). O artigo está sob CC BY 4.0 — [Europe PMC PMC8159987](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8159987/fullTextXML)
- **Eletrodomésticos (geladeiras e lavadoras), dados reais de oficina:** Fonseca T., Chaves P., Ferreira L.L., Gouveia N., Costa D., Oliveira A., Landeck J., "Dataset for identifying maintenance needs of home appliances using artificial intelligence", *Data in Brief* 48:109068 (2023), DOI 10.1016/j.dib.2023.109068, licença CC BY. Corrente elétrica e vibração a 1 Hz e 2048 Hz, rotuladas normal/defeito, com dataset de features por ciclo — [Europe PMC search](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22maintenance%20needs%20of%20home%20appliances%22&format=json&resultType=core); [PMC10063395](https://europepmc.org/articles/PMC10063395)
- **IEEE DataPort, "Public dataset of air conditioner faults"** (GuangXi Sun, Harbin Engineering University, criado em 13/10/2025): um .xlsx de 155,46 KB com features e rótulo, CC BY 4.0, DOI 10.21227/jjd4-j051. Os arquivos exigem login. A página não informa equipamento, falhas nem variáveis — [IEEE DataPort](https://ieee-dataport.org/documents/public-dataset-air-conditioner-faults)
- **Mendeley, split simulado para clima tropical insular** (Ramananandro, Murad, Andrianarimanana, Randriatefison; v3 de 26/06/2026): simulação OpenStudio/EnergyPlus de falhas simples e múltiplas, de ciclo e de sensor, em 4 níveis (0 = sem falha, 1 = baixa, 2 = média, 3 = severa). As variáveis incluem consumo elétrico de energia e variação de COP. CC BY 4.0, DOI 10.17632/2mmf3ts9dk.3 — [Mendeley Data](https://data.mendeley.com/datasets/2mmf3ts9dk/3)
- **Kaggle, "Simulated Refrigerator Fault Diagnosis Dataset":** dados termodinâmicos simulados a partir de equações de primeiros princípios, sem corrente medida — [Kaggle](https://www.kaggle.com/datasets/samoilovmikhail/simulated-refrigerator-fault-diagnosis-dataset)
- **arXiv 2609.22229, "A Synthetic Multivariate Refrigerator Time-Series Dataset for Predictive Maintenance":** dados sintéticos com consumo elétrico, 7.066.161 linhas em 27 séries e 27 logs de falha, publicados no Zenodo (DOI 10.5281/zenodo.22076228, segundo o snippet) — [arXiv](https://arxiv.org/abs/2609.22229)
- Um survey de 2023 sobre máquinas com compressor aponta a falta de datasets públicos com dados reais como um dos principais problemas em aberto — [arXiv 2402.17802](https://arxiv.org/html/2402.17802v2)

### Inferences
- O ORNL é o melhor par "falha de refrigeração ↔ potência por compressor" com licença comercial-friendly, mas é CO2 transcrítico com rack de supermercado, muito diferente de um split residencial.
- O dataset de Fonseca et al. é o único achado com **corrente real de compressor de geladeira** rotulada e licença CC BY. Os rótulos, porém, são genéricos (normal/defeito), não falhas de ciclo graduadas.

### Gaps
- **Supermercados dinamarqueses** (dados de Aalborg/Danfoss, comuns na literatura) e **datasets de expositores refrigerados com falha**: não encontrei release público verificável nesta sessão.
- Não verifiquei o repositório nem a licença de dados do Fonseca et al. (o Europe PMC indica que há dados, mas não dá a URL), nem quais falhas de geladeira estão rotuladas.
- Não abri o Zenodo 22076228 para confirmar a licença.

## 6. Corrente de motor monofásico / falha de capacitor; relevância do Paderborn

### Takeaway
Não encontrei dataset público aberto de **corrente de motor monofásico com falha de capacitor**. O registro Zenodo que parecia candidato é apenas um artigo em PDF. Os datasets de corrente de motor existentes (Paderborn, Zenodo startup currents, Scientific Data 2025) são trifásicos ou de outro domínio. Servem para pré-treinar ou testar métodos de MCSA, não para validar falhas de HVAC.

### Cited Findings
- Zenodo 4963381, "Detection of internal and external faults of single-phase induction motor using current signature" (IJECE 11(4):2830-2841, 2021): é **artigo**, não dataset. Contém só um PDF de 1,2 MB sob CC BY 4.0. As falhas estudadas são barra de rotor quebrada e rolamento em motor monofásico capacitor-run, sem taxa de amostragem informada — [Zenodo 4963381](https://zenodo.org/records/4963381)
- Um estudo de 2025 (Springer, *Discover AI*) monitora em tempo real um motor monofásico de 320 W com falha de capacitor aberto, entre outras condições. Não confirmei se os dados foram publicados — [Springer](https://link.springer.com/article/10.1007/s44163-025-00509-0)
- Zenodo 17048028, "Induction motor fault detection dataset – startup currents for mains powered motors": correntes de partida de motores alimentados pela rede (não verifiquei fase, licença nem falhas) — [Zenodo 17048028](https://zenodo.org/records/17048028)
- Scientific Data 2025: dataset multissensor de falhas em motores de indução **trifásicos** — [Nature s41597-025-05437-3](https://www.nature.com/articles/s41597-025-05437-3)

### Inferences
- O Paderborn (KAt bearing dataset) é corrente de motor trifásico (PMSM/inversor) com falhas de rolamento. É relevante só como benchmark de MCSA e de redes neurais em sinais de corrente, não para compressores monofásicos PSC de split on-off.
- Para falha de capacitor em compressor de split, o único dado público medido encontrado é o da UFPB (seção 4), sob NC.

### Gaps
- Não verifiquei nesta sessão a licença exata do Paderborn. De memória, costuma ser citado como CC BY-NC 4.0, mas isso não foi confirmado e deve ser checado antes de uso comercial.
- Não abri o Zenodo 17048028 para confirmar o conteúdo e a licença.

## Catálogo resumo

| # | Dataset | Equipamento | Falhas / severidades | Elétrico (taxa) | Termo-hidráulico | Formato / tamanho | Licença | Uso comercial | Link | Paper |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | LBNL FDD – RTU (sim/lab/campo) | Rooftop R410A | Sim: sobre e subcarga 10–20%, fouling cond./evap. 10–50%, restrição de líquido 1–10 bar, de sucção 1–9 bar. Campo: subcarga 40%, falha de estágio. Lab: damper/economizador/sensor | Potência W de compressor, ventilador e total (1 min) | P/T de refrigerante, temperaturas de ar | CSV, 293 MB, 84 arquivos | CC BY 4.0 (OEDI) | Sim, com atribuição | [OEDI 5763](https://data.openei.org/submissions/5763) · [LBNL](https://faultdetection.lbl.gov/dataset/rtu/) | Granderson et al., Sci Data 2023 |
| 2 | LBNL FDD – Chiller plant | Planta de chiller (simulada) | 7 falhas, várias severidades, 1 ano | Não confirmado (1 min) | Água gelada / condensação | CSV, 1,14 GB | CC BY 4.0 (OEDI) | Sim | [LBNL](https://faultdetection.lbl.gov/dataset/simulated-chiller-plant/) | idem |
| 3 | ASHRAE RP-1043 | Chiller centrífugo 90 TR | 7 falhas × 4 níveis | Potência do compressor (a verificar) | ~64 pontos (a verificar) | Espelho figshare 48,73 MB | Direitos ASHRAE; espelho não verificado | Incerto | [figshare 28435232](https://figshare.com/articles/dataset/Chiller_operation_data_set/28435232) | Comstock & Braun 1999; Comstock et al. 2002 |
| 4 | NIST 14/16 SEER FDD cooling | Heat pump split 14 SEER + AC 16 SEER | Falhas simples (carga, restrição, vazão de ar etc.), regime permanente | Provável potência (a verificar) | T/P/umidade | .xls/.xlsx | Sem declaração (obra do governo dos EUA) | Provável sim (verificar) | [NIST](https://www.nist.gov/el/energy-and-environment-division-73200/hvacr-equipment-performance-group/fault-detection-and) · DOI 10.18434/M32132 | NISTIR 7350; NIST TN 1648 |
| 5 | UFPB split electrical | Split on-off 18 kBTU/h (campo) | Fouling cond./evap. (vários níveis), degradação do capacitor (%), pares de falhas | Corrente + tensão brutas, 30 kHz × 60 s | Nenhum | .txt (2 colunas) | **CC-BY-NC** | **Não** (pedir aos autores) | [Artigo MDPI](https://www.mdpi.com/2306-5729/9/9/106) (link dos dados não confirmado) | de Oliveira et al., Data 2024 |
| 6 | ORNL CO2 supermarket | Rack de refrigeração comercial (lab) | 6 falhas × 3 níveis (porta, gelo, TXV, ventiladores, bloqueio cond./evap.) | Potência W por compressor e ventiladores (1 s) | T/P do circuito | 12 CSV, ~95 MB cada | CC BY 4.0 (artigo); metadados CC0 | Sim | [figshare 13232627](https://doi.org/10.6084/m9.figshare.13232627) | Sun et al., Sci Data 2021 |
| 7 | Home appliances (Fonseca et al.) | Geladeiras/lavadoras (oficina) | Normal vs. defeito | Corrente a 1 Hz e 2048 Hz (+ vibração) | Nenhum | Não verificado | CC BY | Sim | [PMC10063395](https://europepmc.org/articles/PMC10063395) | Data in Brief 2023 |
| 8 | Split tropical simulado (Mendeley) | Split (EnergyPlus) | Múltiplas falhas, 4 níveis | Energia elétrica (passo não informado) | Temperatura externa, COP | Não informado | CC BY 4.0 | Sim | [Mendeley 2mmf3ts9dk.3](https://data.mendeley.com/datasets/2mmf3ts9dk/3) | Ramananandro et al. 2026 |
| 9 | IEEE DataPort AC faults (Harbin) | AC (não especificado) | Rotulado (não especificado) | Não especificado | — | .xlsx 155 KB | CC BY 4.0 (exige login) | Sim | [IEEE DataPort](https://ieee-dataport.org/documents/public-dataset-air-conditioner-faults) | — |
