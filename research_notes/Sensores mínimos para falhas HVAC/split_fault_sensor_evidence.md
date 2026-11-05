# Evidência falha × sensor em ar-condicionado split / bomba de calor residencial (compressão de vapor, velocidade fixa e inverter)

> Convenções: setas = direção do resíduo da feature em relação ao modelo de referência sem falha (↑ sobe, ↓ desce, – neutro). "Lab" = medido em câmara psicrométrica; "Sim" = apenas simulação. Siglas NIST: CMF = vazamento de válvula do compressor/4-vias; CF = fluxo de ar no condensador; EF = fluxo de ar no evaporador; LL = restrição na linha de líquido; UC/OC = sub/sobrecarga; NON = gases não condensáveis.
> Aviso: no modo aquecimento os papéis se invertem (CF = serpentina interna, EF = serpentina externa).

## Pergunta 0 — Tabela-síntese falha × sensor (para o redator)

### Takeaway
Temperaturas de refrigerante (sucção/superaquecimento, descarga, saturação de evaporação/condensação, subresfriamento) + ΔT de ar em ambas as serpentinas formam o conjunto de 7 features que diagnostica as 6 falhas clássicas; potência/corrente elétrica em regime permanente só é sensível de forma útil a sobrecarga, sujeira/bloqueio do condensador e não condensáveis, e é quase cega a subcarga pequena, restrição de linha de líquido e vazamento de válvula (que só aparecem no transitório de partida com amostragem alta).

### Cited Findings

**Tabela A — Padrões de resíduos de temperatura (cooling), split R410A 8,8 kW com TXV, Lab** — fonte: [Kim, Yoon, Payne, Domanski, NIST SP 1087 (2008), Tab. 5.2](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf). Zona A: Tsh < 9 °C (TXV ainda controlando); Zona B: Tsh > 9 °C (TXV saturada).

| Falha | Zona | TE (evap) | Tsh | TD (descarga) | TC (cond) | Tsc | ΔT ar cond | ΔT ar evap |
|---|---|---|---|---|---|---|---|---|
| CMF (vazamento válvula compressor) | A | ↑ | – | ↑ | ↓ | ↓ | ↓ | ↓ |
| CF (fluxo ar condensador) | A | ↑ | – | ↑ | ↑ | ↓ | – | ↓ |
| CF | B | ↓ | ↑ | ↑ | ↑ | ↓ | ↓ | ↓ |
| EF (fluxo ar evaporador / filtro) | A | ↓ | – | – | ↓ | – | ↓ | ↑ |
| LL (restrição linha líquido) | A | – | – | – | – | – | – | – (idêntico a sem falha) |
| LL | B | ↓ | ↑ | ↑ | ↓ | ↑ | ↓ | ↓ |
| UC (subcarga) | A | – | – | – | ↓ | ↓ | ↓ | ↓ |
| UC | B | ↓ | ↑ | ↑ | ↓ | ↓ | ↓ | ↓ |
| OC (sobrecarga) | A | – | – | ↑ | ↑ | ↑ | – | – |

**Tabela B — Padrões para unidade com orifício fixo (rooftop, Breuker & Braun 1998b), reproduzida em SP 1087 Tab. 5.1(a)** — sem índices neutros: com orifício fixo toda falha mexe em todas as features. [NIST SP 1087](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf)

| Falha | TE | Tsh | TD | TC | Tsc | ΔTca | ΔTea |
|---|---|---|---|---|---|---|---|
| Vazamento válvula compressor | ↑ | ↓ | ↑ | ↓ | ↓ | ↓ | ↓ |
| Vazamento de refrigerante (subcarga) | ↓ | ↑ | ↑ | ↓ | ↓ | ↓ | ↓ |
| Restrição linha de líquido | ↓ | ↑ | ↑ | ↓ | ↑ | ↓ | ↓ |
| Falha condensador (sujeira/ar) | ↑ | ↓ | ↑ | ↑ | ↓ | ↑ | ↓ |
| Falha evaporador (ar/filtro) | ↓ | ↓ | ↓ | ↓ | ↓ | ↓ | ↑ |

**Tabela C — Efeito medido na potência do compressor (Lab, NIST, mesma bomba de calor R410A 8,8 kW TXV, modo aquecimento, Tint 21,1 °C)** — fonte: [Payne, Yoon, Domanski, NIST TN 1648 (2009), Tabs. 5.1.1–5.6.2](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.1648_2009.pdf) (DOI 10.6028/nistpub.0413171251). Variação % no nível máximo de falha testado; primeiro valor a −8,3 °C externo, segundo a +8,3 °C.

| Falha (aquecimento) | Nível máx. | ΔW compressor | Capacidade / COP |
|---|---|---|---|
| Ar na serpentina interna (= condensador) reduzido | ~30 % de vazão | **+5,8 % / +10,8 %** | COP −10 % com 30 % menos ar (8,3 °C) |
| Bloqueio serpentina externa (= evaporador) | 30 % da face | **−5,7 % / −6,1 %** | cap −26 %, COP −24 % (−8,3 °C); cap −18 %, COP −14 % (8,3 °C) |
| Vazamento compressor/4-vias (CMF) | ~12,4 % de vazão mássica | **−4,4 % / −5,5 %** | cap −11,6 %, COP ~−11,6 % (8,3 °C); cap −70 W/% (8,3 °C) |
| Restrição linha de líquido | 45–48 % ΔP | **0,0 % / +1,1 %** | dentro da incerteza; sem penalidade até >48 % |
| Sobrecarga | ~30 % | **+11,7 % / +22,1 %** | capacidade ~0; COP −14,4 % (8,3 °C) |
| Subcarga | ~30 % | **−2,9 % / −6,6 %** | cap −14 %, COP −9 % (8,3 °C) |

**Tabela D — Direção do efeito na potência do compressor no modo resfriamento (Lab, mesma unidade)** — [Kim, Payne, Domanski, NISTIR 7350 (2006)](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7350.pdf): Wcmp **aumenta** com não condensáveis, sobrecarga e fluxo de ar externo baixo; **não muda ou diminui** para as demais falhas (CMF, EF, LL, UC). Na Fig. 5.24 todas as variações de Wcmp ficam dentro de aproximadamente ±10 % nos níveis testados (CF até ~40 %, EF até ~40 %, UC/OC até 30 %, NON até ~20 %). Números exatos por nível não extraídos (estão só em gráficos).

**Tabela E — Matriz falha × sensor (síntese das fontes acima; ver detalhes nas perguntas seguintes)**

| Falha | Temperaturas refrigerante | Pressão | ΔT ar | Potência/corrente baixa taxa (smart meter) | Alta taxa (NILM/MCSA/harmônicas) | Vibração / acústica |
|---|---|---|---|---|---|---|
| Sujeira/ar condensador | Detecta (TC↑, TD↑, Tsc↓) — Lab SP1087 | Melhora TC | ΔTca | **Sim**: única falha que eleva bem a potência (Hjortland 2016); +5,8–10,8 % p/ 30 % (TN1648, modo aquec.) | Potência do ventilador do condensador: 353→361 W com 14 % bloqueio, detectável em ~10 partidas (Armstrong 2006) | sem evidência encontrada |
| Ar evaporador / filtro | Detecta (TE↓, TC↓, ΔTea↑) | opcional | ΔTea essencial | **Quase invisível** no compressor (cooling: neutro/ligeira queda) | Ventilador interno: P 662→654 W (−1,2 %, precisa centenas de partidas); Q 437→428 VAR detectável em ~10 partidas com 10 % bloqueio (Armstrong 2006) | sem evidência |
| Subcarga/vazamento | Detecta (Tsc↓ é o 1º sinal com TXV; Tsh↑ só em nível alto) | Melhora | ΔTca/ΔTea ↓ | **Fraco**: −2,9 a −6,6 % para 30 % (aquec.); direção ambígua (Armstrong: power ↑ em RTU) | Transitório de partida distinto com 20 % de subcarga (Armstrong 2006) | sem evidência |
| Sobrecarga | Detecta (TD↑, TC↑, Tsc↑); TD é a variável mais sensível no aquecimento | Melhora | – | **Sim**: +11,7 a +22,1 % p/ 30 % (TN1648); +18 % p/ 20 % em RTU (Armstrong) | Também ângulo de fase (Armstrong) | sem evidência |
| Restrição linha líquido | Indetectável com TXV até a TXV saturar (zona B) | ΔP na linha seria o sensor direto | – | **Invisível** (0 a +1,1 % com 45–48 %) | não testado por Armstrong | sem evidência |
| Não condensáveis | Detecta (TC↑) — NISTIR 7350 | Pressão de condensação vs. temperatura de saturação é a assinatura clássica (inferência) | – | Potência ↑ (NISTIR 7350, direção apenas) | sem evidência | sem evidência |
| Vazamento de válvula / desgaste compressor | Detecta (TE↑, TD↑, Tsc↓) | Melhora | ↓ | **Fraco**: −4,4 a −5,5 % com 12 % de bypass | Regime quase inalterado, mas transitório de partida distinto (Armstrong 2006) | sem evidência |
| Degradação do capacitor de marcha | não aplicável | não aplicável | não | Hipótese: FP/corrente (patente US 2016/0226416, sem validação publicada) | Dataset de campo em split (UFPB 2024, FFT) | sem evidência |

### Inferences
- Para uma abordagem só-elétrica de baixa taxa, as falhas "bem visíveis" são sobrecarga, condensador sujo/bloqueado e não condensáveis (todas elevam pressão de descarga → potência). Subcarga, vazamento de válvula e bloqueio do evaporador tendem a *reduzir* a potência poucos % — mesmo sinal de uma carga térmica menor, o que as torna confundíveis entre si e com variação de clima.

### Gaps
- Não encontrei estudo experimental com sensores de vibração ou acústicos em split residencial com falhas impostas e quantificadas (a busca foi limitada); coluna marcada "sem evidência".
- Valores numéricos de Wcmp por nível no modo resfriamento (NISTIR 7350) estão só em gráficos; não transcritos.

## Pergunta 1 — O que os trabalhos clássicos dizem sobre conjuntos mínimos de sensores?

### Takeaway
A linha Purdue/NIST converge em ~7 features de temperatura (TE, Tsh, TD, TC, Tsc, ΔTca, ΔTea) com 3 variáveis de entrada (Tod, Tid, umidade/ponto de orvalho interno), e mostra que apenas 2–4 sensores de superfície bastam para carga de refrigerante (virtual refrigerant charge, VRC; erro ~±10 %).

### Cited Findings
- Rossi & Braun (1997) formularam o método estatístico rule-based com resíduos de temperatura vs. modelo sem falha; Li (2004) reexaminou e adicionou dois esquemas que melhoraram a sensibilidade, além de sensores virtuais — [NIST SP 1087, revisão de literatura](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf). Rossi, T.M. & Braun, J.E., 1997, HVAC&R Research 3(1):19-37.
- Chen & Braun (2001), rooftop 5 TR com TXV: simplificaram Rossi & Braun usando razões de resíduos e selecionando as **duas medidas mais sensíveis** por falha, num algoritmo rule-based sequencial — [NIST SP 1087](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf). Chen, B. & Braun, J.E., 2001, ASHRAE Trans. 107(1):847-857.
- Breuker & Braun (1998b): 5 falhas, rooftop com orifício fixo, modelos polinomiais sem falha; padrão de setas da Tabela B acima — [NIST SP 1087 Tab. 5.1(a)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf). Outros investigadores relatam dificuldade em detectar subcarga de forma confiável **antes de ≥40 % de perda de carga** (Breuker & Braun 1998b; Stylianou & Nikanpour 1996) — [NIST SP 1087](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf).
- Breuker & Braun (1998a), levantamento de campo: vazamento de refrigerante é a falha mais frequente, seguida de condensador, air handler, evaporador e compressor; compressor = 24 % do custo de serviço; ~40 % das paradas são elétricas/controle — [NIST SP 1087](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf).
- Li & Braun: decoupling — o FDD de alta dimensão é desacoplado em n problemas 1-D, permitindo diagnosticar falhas múltiplas simultâneas com sensores virtuais — [Li & Braun 2004, ACEEE](https://aceee.org/files/proceedings/2004/data/papers/SS04_Panel3_Paper16.pdf); Li & Braun 2007, "Decoupling features and virtual sensors for diagnosis of faults in vapor compression air conditioners", Int. J. Refrig. 30:546-564 (citado em [NIST TN 1648](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.1648_2009.pdf)).
- VRC (Li & Braun 2008/2009): usa **4 temperaturas de superfície** para obter superaquecimento de sucção, subresfriamento na linha de líquido e título na entrada do evaporador, entradas de um modelo empírico de carga; avaliado em dados de laboratório de 7 sistemas — [Li & Braun, ACEEE 2008](https://www.aceee.org/files/proceedings/2008/data/papers/3_514.pdf); [resumo de busca/DOE](https://www.energy.gov/eere/buildings/articles/cbei-virtual-refrigerant-charge-sensing-and-load-metering-2015-peer-review).
- Kim & Braun: versão aprimorada do VRC estimou carga **dentro de ±10 %** em ampla faixa de condições; funciona bem com parâmetros default em sistemas **sem acumulador**; com acumulador precisa de ajuste — [Kim & Braun, Int. J. Refrig. 36(3), 2013 (registro IIR)](https://iifiir.org/en/fridoc/performance-evaluation-of-a-virtual-refrigerant-charge-sensor-136209); [Purdue thesis](https://docs.lib.purdue.edu/dissertations/AAI1475985). Estendido para compressores e ventiladores de velocidade variável — [Kim, dissertação Purdue](https://docs.lib.purdue.edu/dissertations/AAI3613162).
- NIST (Kim, Yoon, Payne, Domanski 2008), split R410A 8,8 kW TXV, cooling: 7 features de temperatura; referência = polinômio multivariável de 3ª ordem em Tod, Tid, Tidp; detector de regime com janela móvel e limiar 3σ; o algoritmo **diagnosticou corretamente todas as falhas que causaram degradação de EER >3,5 %**; erros ocorreram com degradação ≤3,4 % — [NIST SP 1087](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf).
- Exemplos de não detecção (SP 1087, Tab. 5.18): CMF de 2,5 % não detectado (EER −2,5 %); CF de 2,4–2,5 % → NF ou confundido com UC; LL **classificado como "sem falha" mesmo a 13 %** (EER praticamente inalterado) — [NIST SP 1087](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf).
- TN 1648: "um FDD simples poderia monitorar a carga usando **apenas dois sensores de temperatura** (subresfriamento num sistema TXV)"; mais dois para superaquecimento formariam ferramenta de comissionamento; a **temperatura de descarga foi a variável mais sensível a sobrecarga** no aquecimento — [NIST TN 1648, Cap. 6](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.1648_2009.pdf).

### Inferences
- Conjunto mínimo prático para split TXV: Tsc (liquid line + saturação de condensação) e TD para carga; TE/Tsh + ΔTea para o lado interno; Tod/Tid/Tidp como entradas do modelo de referência. Com orifício fixo/capilar (comum em splits on-off baratos), Tsh já é muito informativo, porque não há controle compensando.

### Gaps
- Não acessei o texto integral de Li & Braun 2007 nem de Rossi & Braun 1997 para extrair as taxas de acerto por falha; números acima vêm de fontes secundárias (revisão de SP 1087 e resumos).

## Pergunta 2 — Quais falhas são distinguíveis só com temperatura (sem pressão)? Quais exigem pressão?

### Takeaway
Na prática, todas as 6 falhas clássicas foram diagnosticadas no NIST com temperaturas (saturação via termopar em curva bifásica), mas os autores recomendam transdutores de pressão para melhor precisão; restrição de linha de líquido com TXV fica invisível até a TXV saturar, e não condensáveis exigem comparar pressão com temperatura de saturação (inferência).

### Cited Findings
- SP 1087 usou só temperaturas; nas conclusões: "usar apenas temperaturas não é o método preferido" para obter as saturações de sucção/descarga exigidas pelos mapas de compressor; um FDD mais preciso incluiria **transdutores de pressão de sucção e descarga** para superaquecimento/subresfriamento mais precisos e para o cálculo de EER via mapa do compressor — [NIST SP 1087, Cap. 6](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf).
- Com TXV, a liquid-line restriction gerou pouca variação até que o líquido começasse a flashear; então a TXV abriu totalmente e o sistema passou a responder como orifício fixo — [NISTIR 7350](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7350.pdf).
- Distinção UC vs. CMF só por temperatura (zona A): UC → TE neutro, TC↓, Tsc↓; CMF → TE↑, TD↑, TC↓, Tsc↓ — [NIST SP 1087 Tab. 5.2](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf).
- VRC: 4 temperaturas de superfície bastam para carga (±10 %) — [Li & Braun ACEEE 2008](https://www.aceee.org/files/proceedings/2008/data/papers/3_514.pdf); [Kim & Braun 2013](https://iifiir.org/en/fridoc/performance-evaluation-of-a-virtual-refrigerant-charge-sensor-136209).
- Li & Braun (2009, HVAC&R Research) desenvolveram **sensores virtuais de pressão** a partir de temperaturas para uso no FDD de desacoplamento — [Virtual Refrigerant Pressure Sensors (PDF)](https://ncesr.unl.edu/wordpress/wp-content/uploads/2018/08/Virtual-Refrigerant-Pressure-Sensors-for-Use-in-Monitoring-and-Fault-Diagnosis-of-Vapor-Compression-Equipment.pdf).
- Não condensáveis aumentam a pressão de condensação acima da temperatura em que o refrigerante realmente condensa, elevando a potência; Wcmp sobe continuamente com o nível de NON — [NISTIR 7350](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7350.pdf).

### Inferences
- Como NON eleva a pressão sem elevar a temperatura medida na curva bifásica, a assinatura mais direta é pressão de descarga > Psat(T de condensação medida); com só temperaturas, NON tende a se confundir com sujeira do condensador ou sobrecarga (inferência, não verificada experimentalmente nestas fontes).

### Gaps
- Não encontrei taxa de acerto quantitativa "com vs. sem pressão" numa mesma unidade.

## Pergunta 3 — Efeito medido de cada falha na potência/corrente do compressor (% por nível)

### Takeaway
Os números de laboratório (Tabela C) mostram: sobrecarga 30 % → +12 a +22 % de potência; restrição de ar no condensador 30 % → +6 a +11 %; bloqueio do evaporador 30 % → −6 %; vazamento de válvula ~12 % → −4 a −6 %; subcarga 30 % → −3 a −7 %; restrição de linha de líquido até 48 % → ~0 %. Em rooftops, a potência total do sistema é pouco sensível à maioria das falhas, exceto condensador sujo.

### Cited Findings
- Valores da Tabela C (aquecimento, Lab) — [NIST TN 1648](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.1648_2009.pdf). Exemplo textual: com sobrecarga de 30,4 %, capacidade −0,1 % e COP −14,4 %, porque a potência do compressor subiu 22 %.
- Limiares para 5 % de queda de COP (aquecimento, 8,3 °C): sobrecarga >18 %; subcarga ~25 % (também 5 % de capacidade); LL sem penalidade até >48 % — [NIST TN 1648](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.1648_2009.pdf).
- Resfriamento (Lab): Wcmp sobe com NON, OC e ar externo baixo; não muda ou cai para as demais; vazão mássica cai fortemente para todas exceto OC — [NISTIR 7350](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7350.pdf).
- RTU (Armstrong et al. 2006): potência em regime 2542 W (normal) → 3009 W com +20 % de carga (**≈+18 %**), detectável em ~10 partidas; potência ativa P1 e ângulo de fase são os parâmetros úteis para carga. Segundo o artigo, tanto sub quanto sobrecarga elevam a razão de pressões e a potência; em subcarga a potência demora a estabilizar — [Armstrong, Laughman, Leeb, Norford, HVAC&R Research 12(1):151-175, 2006, DOI 10.1080/10789669.2006.10391172](https://emsg.mit.edu/wp-content/uploads/2016/07/27_Detection-of-Rooftop-Cooling-Unit-Faults-Based-on-Electrical-Measurements.pdf). **Conflito:** o NIST (split TXV) mediu *queda* de potência com subcarga — [TN 1648](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.1648_2009.pdf), [NISTIR 7350](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7350.pdf). A direção depende de tipo de expansão, nível e condição.
- Vazamento de bypass (válvula) em RTU: pouca ou nenhuma mudança na potência em regime, mas forma do transitório de partida distinta — [Armstrong et al. 2006](https://emsg.mit.edu/wp-content/uploads/2016/07/27_Detection-of-Rooftop-Cooling-Unit-Faults-Based-on-Electrical-Measurements.pdf).
- Hjortland, Braun & Gorbounov (2016), dados de câmara de vários rooftops: potência total responde fracamente à maioria das falhas; **só a sujeira do condensador aumenta visivelmente** a potência instantânea; carga, LL e vazamento de válvula tendem a *reduzir* a potência, com efeito fraco; dada a incerteza do modelo de potência, os limiares não detectam falhas comuns; estimativas virtuais de capacidade/COP são indicadores melhores — [Purdue IRACC 2016, paper 1817](https://docs.lib.purdue.edu/iracc/1817); [registro IIR](https://iifiir.org/en/fridoc/the-effectiveness-of-using-total-system-power-for-fault-detection-in-32216). (Li só resumo/abstract; o texto integral deu 403.)

### Inferences
- Para smart meter (1 s a 15 min), o sinal útil de falhas "subtrativas" (UC, CMF, EF) é de −3 a −7 % no nível severo (30 %), comparável à variação causada por poucos °C de temperatura externa; só é separável com modelo de referência normalizado por clima e muitos ciclos.

### Gaps
- Não encontrei dado experimental de % de potência por nível de falha para split com orifício fixo/capilar (o tipo mais comum em splits on-off no Brasil).
- Corrente (A) por falha foi medida no TN 1648, mas não extraí os valores.

## Pergunta 4 — Quais falhas são quase invisíveis eletricamente?

### Takeaway
Restrição de linha de líquido (≈0 % até 48 %), subcarga pequena (<20–25 %), bloqueio de ar do evaporador/filtro no sinal do compressor, e vazamento leve de válvula. Elas só aparecem eletricamente com alta taxa de amostragem (forma do transitório de partida, potência reativa do ventilador) ou não aparecem.

### Cited Findings
- LL: compressor 0,0 % / +1,1 % com 45–48 % de restrição; efeitos dentro da incerteza — [NIST TN 1648](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.1648_2009.pdf). Mesmo com termômetros, LL foi classificado "sem falha" até 13 % — [NIST SP 1087](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf).
- Subcarga: COP só cai 5 % por volta de 25 % de subcarga; potência −2,9 % a 30 % (−8,3 °C) — [NIST TN 1648](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.1648_2009.pdf). No RTU, subcarga só foi detectável eletricamente pela forma do transitório de partida; uma nota pós-revisão diz que, normalizando pelo mínimo pós-inrush, sub e sobrecarga são separáveis pela forma do transitório — [Armstrong et al. 2006](https://emsg.mit.edu/wp-content/uploads/2016/07/27_Detection-of-Rooftop-Cooling-Unit-Faults-Based-on-Electrical-Measurements.pdf).
- Filtro/ar interno: potência ativa do ventilador interno 662→654 W com 10 % de bloqueio (exigiria várias centenas de partidas); potência reativa 437→428 VAR (detectável em ~10 partidas); autores alertam que variações de densidade do ar/dampers geram incerteza — [Armstrong et al. 2006](https://emsg.mit.edu/wp-content/uploads/2016/07/27_Detection-of-Rooftop-Cooling-Unit-Faults-Based-on-Electrical-Measurements.pdf).
- Ingestão de líquido: quantidades não danosas (5–10 % do deslocamento) têm efeito pequeno em P1; detecção "complicada", feita por norma de inovações de modelo ARX adaptativo — [Armstrong et al. 2006](https://emsg.mit.edu/wp-content/uploads/2016/07/27_Detection-of-Rooftop-Cooling-Unit-Faults-Based-on-Electrical-Measurements.pdf).
- Desbalanceamento de ventilador: pico espectral em ~18,4–19 Hz na potência, muito sensível ao nível de desbalanceamento (2,6–5,3 g no condensador; 8–16 g no insuflamento) — [Armstrong et al. 2006](https://emsg.mit.edu/wp-content/uploads/2016/07/27_Detection-of-Rooftop-Cooling-Unit-Faults-Based-on-Electrical-Measurements.pdf).
- Capacitor de marcha: um dataset de campo de split (UFPB/UFCG, Brasil) mede corrente e tensão não invasivas com degradação do capacitor do compressor (% de perda de capacitância) e bloqueio de condensador/evaporador, com exemplos de FFT; os autores dizem que a falha é muito comum e pouco estudada — [de Oliveira, Lima Filho, Belo, Cadena, *Data* 9(9):106, 2024](https://ideas.repec.org/a/gam/jdataj/v9y2024i9p106-d1477561.html) / [MDPI](https://www.mdpi.com/2306-5729/9/9/106). Patente descreve detecção por fator de potência + corrente — [US 2016/0226416](https://uspto.report/patent/app/20160226416) (sem validação publicada).

### Inferences
- Capacitor de marcha (motor PSC) deve alterar sobretudo o fator de potência/potência reativa e a corrente do enrolamento auxiliar, não a potência ativa térmica, o que o torna, em tese, mais detectável eletricamente que as falhas termofluídicas. Não encontrei números experimentais que confirmem isso.

### Gaps
- Não extraí do dataset de 2024 os níveis de capacitância, a taxa de amostragem nem os efeitos (MDPI retornou 403).

## Pergunta 5 — Como a temperatura ambiente confunde a detecção e como os estudos normalizam?

### Takeaway
Potência e vazão dependem fortemente da temperatura externa e pouco das condições internas; todos os trabalhos usam modelo de referência sem falha (polinômio multivariável, MPR, ou mapa do compressor) em função de Tod, Tid e Tidp, mais detector de regime permanente, e comparam resíduos.

### Cited Findings
- Potência do compressor e vazão mássica são fortemente afetadas pela temperatura externa; a condição interna tem pouca influência — [NISTIR 7350](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7350.pdf).
- Normalização NIST: MPR de 2ª ordem (NISTIR 7350) e 3ª ordem (SP 1087) com entradas Tod, Tid e Tidp; o MPR de 3ª ordem ajustou melhor que a rede neural (ANN); o limiar neutro combina incerteza de medição, falta de repetibilidade dia a dia e erro do modelo — [NIST SP 1087](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf).
- Detector de regime: desvio-padrão em janela móvel <3σ do regime sem falha; ≥12 min de monitoramento para evitar falsos regimes — [NISTIR 7350](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7350.pdf); [SP 1087](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf).
- Efeito das falhas varia com o clima: quase todas as falhas têm impacto maior em temperatura externa mais alta (aquecimento) — ex.: sobrecarga de 30 % → +11,7 % de potência a −8,3 °C vs. +22,1 % a 8,3 °C — [NIST TN 1648](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.1648_2009.pdf).
- No aquecimento, o gelo na serpentina externa muda algumas features em >50 %; o FDD deve detectar degelo (ex.: temperatura de curva bifásica da serpentina externa) e só rodar fora dele — [NIST TN 1648](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.1648_2009.pdf).
- Armstrong et al.: os testes de carga não consideraram a variação da potência com as condições de operação, então a mudança de potência isolada não pode ser atribuída à falha; sugerem normalizar pela diferença de pressão descarga−sucção ou pelas temperaturas de condensação/evaporação. Temperaturas externas para ΔT de ar sofrem com radiação, gelo e viés de bulbo úmido — [Armstrong et al. 2006](https://emsg.mit.edu/wp-content/uploads/2016/07/27_Detection-of-Rooftop-Cooling-Unit-Faults-Based-on-Electrical-Measurements.pdf).
- Sensor virtual de potência do compressor: mapa AHRI com entradas de temperatura de evaporação e condensação — [DOE/CBEI peer review](https://www.energy.gov/eere/buildings/articles/cbei-virtual-refrigerant-charge-sensing-and-load-metering-2015-peer-review).
- Cada instalação split é única; os autores pedem modelos de referência auto-treináveis/adaptativos; como as features variam quase linearmente com o nível de falha, correlações adaptativas são viáveis em microcontrolador — [NIST TN 1648](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.1648_2009.pdf); [SP 1087](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf).

### Inferences
- Para abordagem só-elétrica, o mínimo é um modelo P_ref = f(Tod, Tid, [UR]) obtido de dados meteorológicos/termostato, treinado no período sem falha; sem Tod, a variação climática (~3–5 %/°C é plausível, mas não verificada aqui) mascara as falhas de −3 a −7 %.

### Gaps
- Não encontrei quantificação experimental direta de "% de potência por °C de Tod" para split residencial nestas fontes (há figuras no NISTIR 7350, não extraídas).

## Pergunta 6 — Inverter (velocidade variável): como muda a assinatura elétrica?

### Takeaway
O controle de velocidade do compressor (e a EEV) compensa a falha e tira sensibilidade das features (mais índices neutros), mas a degradação de COP pode ser maior. Eletricamente, a potência passa a depender da frequência comandada; é preciso normalizar por frequência/carga, ou usar sinais internos do drive (corrente de fase, tensão do barramento), como fazem as patentes de fabricantes. A evidência experimental revisada por pares é escassa.

### Cited Findings
- Kim & Kim (2005), bomba de calor água-água com compressor de velocidade variável + EEV (Lab): parâmetros **menos sensíveis** a falhas que com velocidade fixa; o controle de velocidade reduziu a sensibilidade; propuseram regras dependentes do estado do compressor; sugerem que a **degradação de COP é muito mais severa** com velocidade variável — [NIST SP 1087, revisão](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf). Kim, M. & Kim, M.S., Int. J. Refrig. 28(4):481-488, 2005.
- Padrões de resíduos (SP 1087 Tab. 5.1c): com velocidade variável + EEV (dois controladores), vazamento de válvula aparece só em TD↑ e na rotação N↑; subcarga <15 % só em Tsc↓ e N↑; condensador → TD↑, TC↑, Tsc↓, N↑. **A rotação do compressor vira uma feature-chave** — [NIST SP 1087](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf).
- Mais controladores → menos variabilidade das features → sistema mais tolerante a falhas (mais neutros) — [NIST SP 1087](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf).
- Com EEV, capacidade e COP dependem pouco da carga de refrigerante (−20 % a +20 %); com tubo capilar a sensibilidade é muito maior — [Choi & Kim, Energy 27(4):391-404, 2002](https://econpapers.repec.org/RePEc:eee:energy:v:27:y:2002:i:4:p:391-404) (bomba de calor água-água, Lab).
- Navarro-Esbri et al. (2007): em chiller com velocidade variável, rotação do compressor, superaquecimento e pressão de sucção foram as variáveis mais sensíveis à carga — [NIST SP 1087](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1087.pdf).
- VRC estendido para velocidade variável (Kim/Braun) e sensor virtual de potência para compressor de velocidade variável em VRF — [dissertação Purdue](https://docs.lib.purdue.edu/dissertations/AAI3613162); [IIR 140008](https://iifiir.org/en/fridoc/development-of-a-virtual-variable-speed-compressor-power-sensor-for-140008).
- Patentes (não revisadas por pares): o compressor roda em velocidade máxima de teste e o vazamento é sinalizado se a potência de entrada (via corrente) fica abaixo do limiar, cruzando com a diferença Tcond−Tevap — [US 12546495](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12546495); detecção de vazamento e anomalia do compressor por corrente do motor + tensão do barramento DC — [WO2025041299A1](https://patents.google.com/patent/WO2025041299A1/en).

### Inferences
- Para inverter, medir só a potência no medidor da casa mistura falha e modulação de carga; o que tem mais chance de funcionar é (a) condicionar a análise à frequência do compressor (se acessível pelo protocolo da unidade/IR/Wi-Fi) ou (b) usar potência × tempo de ciclo/energia por grau-dia, já que a unidade compensa a falha aumentando rotação e tempo ligado. Isso é inferência; não achei validação experimental publicada em split inverter residencial.
- A estratégia do fabricante (forçar velocidade fixa num "modo teste") sugere que a assinatura elétrica de carga só é interpretável em ponto de operação fixo.

### Gaps
- Não encontrei artigo experimental revisado por pares com split inverter residencial e falhas impostas, medindo potência/corrente por nível de falha. Fontes sobre inverter aqui são: um estudo água-água (Kim & Kim 2005, via resumo secundário), um estudo de EEV sem inverter (Choi & Kim 2002) e patentes.
- Teste NIST TN 1848 (Domanski, Henderson, Payne 2014) sobre falhas de instalação é **Sim** (simulação anual de casa unifamiliar); aponta vazamento de duto, subcarga, dutos subdimensionados, baixo fluxo interno e sobrecarga como as falhas que mais aumentam o consumo anual — [NIST node 563011](https://www.nist.gov/node/563011); [TN 1848 PDF](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.1848.pdf). Não extraí os percentuais.
