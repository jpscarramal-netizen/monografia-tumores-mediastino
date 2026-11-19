# -*- coding: utf-8 -*-
"""Text content of the monograph (Portuguese). Every number traces to trabalho/extracao_notas.md."""

TITULO = "TRATAMENTO CIRÚRGICO DOS TUMORES DO MEDIASTINO ANTERIOR"
SUBTITULO = "estado atual das abordagens aberta, videotoracoscópica e robótica"
AUTORES = "[NOMES DOS INTEGRANTES DO GRUPO 6]"

RESUMO = (
    "Os tumores epiteliais tímicos são as neoplasias mais frequentes do compartimento anterior do mediastino, e a "
    "ressecção cirúrgica completa constitui o principal determinante do prognóstico. Tradicionalmente realizada por "
    "esternotomia mediana, a timectomia passou a ser feita de forma crescente por toracoscopia videoassistida (VATS) e "
    "por cirurgia robótica (RATS), o que levanta a questão da equivalência oncológica dessas vias. O objetivo deste "
    "trabalho foi analisar o estado atual do tratamento cirúrgico dos tumores do mediastino anterior, comparando as "
    "abordagens aberta, VATS e RATS quanto à segurança perioperatória e aos resultados oncológicos. Realizou-se uma "
    "revisão integrativa na base PubMed/MEDLINE, complementada por busca dirigida de diretrizes e documentos de "
    "estadiamento publicados até 2026. Foram incluídos 11 estudos lidos na íntegra: três metanálises, seis análises de "
    "registros nacionais ou internacionais, um estudo de coorte pareado e um ensaio clínico randomizado. Nos estudos "
    "pareados, a via minimamente invasiva alcançou taxas de ressecção completa semelhantes às da esternotomia (96% "
    "versus 96% no registro do International Thymic Malignancy Interest Group) e sobrevida equivalente, com menor perda "
    "sanguínea, menos complicações e internação mais curta. Na comparação entre as técnicas minimamente invasivas, a "
    "cirurgia robótica associou-se a menor chance de ressecção incompleta e de conversão, sem diferença de sobrevida e "
    "com custo hospitalar maior. Em doença localmente avançada e em tumores volumosos, séries selecionadas mostraram "
    "viabilidade da via minimamente invasiva, mas as diretrizes ainda recomendam a via aberta como padrão no estádio III. "
    "Conclui-se que a ressecção minimamente invasiva, por VATS ou RATS, é hoje uma opção padrão para tumores tímicos em "
    "estádio inicial, desde que preservados os princípios oncológicos, enquanto seu papel na doença avançada e a "
    "superioridade da robótica dependem de ensaios clínicos randomizados ainda em andamento."
)
PALAVRAS_CHAVE = "Timoma; Neoplasias do Timo; Neoplasias do Mediastino; Cirurgia Torácica Vídeoassistida; Procedimentos Cirúrgicos Robóticos."

ABSTRACT = (
    "Thymic epithelial tumors are the most frequent neoplasms of the anterior mediastinal compartment, and complete "
    "surgical resection is the main determinant of prognosis. Traditionally performed through median sternotomy, "
    "thymectomy has increasingly been carried out by video-assisted thoracoscopic surgery (VATS) and robotic-assisted "
    "thoracoscopic surgery (RATS), which raises the question of the oncologic equivalence of these approaches. This study "
    "aimed to analyze the current status of the surgical treatment of anterior mediastinal tumors, comparing open, VATS "
    "and RATS approaches regarding perioperative safety and oncologic outcomes. An integrative review was conducted in "
    "PubMed/MEDLINE, complemented by a targeted search for guidelines and staging documents published up to 2026. Eleven "
    "studies read in full were included: three meta-analyses, six analyses of national or international registries, one "
    "propensity-matched cohort and one randomized controlled trial. In matched analyses, the minimally invasive approach "
    "achieved complete resection rates similar to those of sternotomy (96% versus 96% in the International Thymic "
    "Malignancy Interest Group registry) and equivalent survival, with less blood loss, fewer complications and shorter "
    "hospital stay. When the minimally invasive techniques were compared, robotic surgery was associated with lower odds "
    "of incomplete resection and conversion, with no difference in survival and higher hospital costs. In locally advanced "
    "disease and large tumors, selected series showed that the minimally invasive approach is feasible, but guidelines "
    "still recommend the open approach as the standard for stage III. In conclusion, minimally invasive resection, by VATS "
    "or RATS, is currently a standard option for early-stage thymic tumors, provided that oncologic principles are "
    "preserved, whereas its role in advanced disease and the superiority of robotic surgery depend on randomized trials "
    "that are still ongoing."
)
KEYWORDS = "Thymoma; Thymus Neoplasms; Mediastinal Neoplasms; Thoracic Surgery, Video-Assisted; Robotic Surgical Procedures."

SIGLAS = [
    ("ESMO", "European Society for Medical Oncology"),
    ("ESTS", "European Society of Thoracic Surgeons"),
    ("IASLC", "International Association for the Study of Lung Cancer"),
    ("IC95%", "Intervalo de confiança de 95%"),
    ("ITMIG", "International Thymic Malignancy Interest Group"),
    ("JART", "Japanese Association for Research on the Thymus"),
    ("KART", "Korean Association for Research on the Thymus"),
    ("MG", "Miastenia gravis"),
    ("MIT", "Timectomia minimamente invasiva (minimally invasive thymectomy)"),
    ("NCCN", "National Comprehensive Cancer Network"),
    ("NCDB", "National Cancer Database"),
    ("OR", "Odds ratio (razão de chances)"),
    ("PSM", "Pareamento por escore de propensão (propensity score matching)"),
    ("R0", "Ressecção completa, com margens livres ao exame microscópico"),
    ("RATS", "Cirurgia torácica robótica (robotic-assisted thoracoscopic surgery)"),
    ("TET", "Tumor epitelial tímico"),
    ("TNM", "Classificação tumor, linfonodo e metástase"),
    ("VATS", "Cirurgia torácica videoassistida (video-assisted thoracoscopic surgery)"),
]

INTRODUCAO = [
    "No mediastino anterior, ou pré-vascular, os "
    "tumores epiteliais tímicos (TET), que compreendem timomas, carcinomas tímicos e neoplasias neuroendócrinas do timo, "
    "são os tumores mais frequentes desse compartimento em todas as faixas etárias (RUFFINI et al., 2023). Trata-se, ainda "
    "assim, de doenças raras: nos Estados Unidos, a incidência estimada é de cerca de dois casos por milhão de habitantes "
    "por ano para o timoma e de 0,48 por milhão para o carcinoma tímico (RIELY et al., 2025). A cirurgia é o tratamento "
    "predominante, e a ressecção completa (R0), obtida por timectomia total com excisão de toda a doença contígua e não "
    "contígua, é o principal objetivo oncológico e um dos fatores prognósticos mais importantes (RIELY et al., 2025; "
    "FANG et al., 2026).",

    "Historicamente, a timectomia por esternotomia mediana consolidou-se como a abordagem padrão, por oferecer ampla "
    "exposição do mediastino anterior e dos grandes vasos (AGATSUMA et al., 2017; YANG et al., 2020). Desde a primeira "
    "timectomia toracoscópica para timoma, descrita em 1992, as técnicas minimamente invasivas ganharam espaço, inicialmente "
    "por toracoscopia videoassistida (VATS) e, mais recentemente, por cirurgia robótica (RATS) (GU et al., 2023; YANG et al., "
    "2020). A resistência inicial à via minimamente invasiva decorreu do receio de ruptura da cápsula tumoral, implante "
    "pleural, ressecção incompleta e maior recorrência local (FRIEDANT et al., 2016). A plataforma robótica acrescenta "
    "visão tridimensional ampliada, instrumentos articulados e filtragem de tremor, recursos que poderiam facilitar a "
    "dissecção no espaço restrito do mediastino anterior (SHEN et al., 2026).",

    "As diretrizes atuais refletem esse momento de transição. O National Comprehensive Cancer Network admite os "
    "procedimentos minimamente invasivos no estádio clínico I a II, desde que todos os objetivos oncológicos sejam "
    "atingidos e que a cirurgia seja feita em centros especializados, mas não os recomenda de rotina pela escassez de "
    "dados de longo prazo (RIELY et al., 2025). A diretriz publicada no Journal of Thoracic Oncology considera as vias "
    "aberta e minimamente invasiva igualmente padrão para os estádios I e II, mas mantém a via aberta como padrão no "
    "estádio III (FALKSON et al., 2022), e os padrões do International Thymic Malignancy Interest Group (ITMIG) "
    "consideram a via minimamente invasiva razoável quando se evita a ruptura tecidual (FANG et al., 2026). Paralelamente, "
    "a nona edição da classificação TNM passou a separar os tumores T1 em até 5 cm (T1a) e maiores que 5 cm (T1b), "
    "incorporando o tamanho tumoral, variável central na escolha da via de acesso (RUFFINI et al., 2023).",

    "Permanecem, contudo, lacunas relevantes: a equivalência oncológica da via minimamente invasiva fora do estádio "
    "inicial, a existência de um limite de tamanho tumoral para sua indicação e a eventual superioridade da robótica "
    "sobre a videotoracoscopia, questão para a qual o primeiro ensaio clínico randomizado ainda está em andamento "
    "(ARDESHIR-LARINANI et al., 2026; WANG et al., 2025). Diante da raridade desses tumores e da predominância de estudos "
    "observacionais, uma síntese crítica das melhores evidências disponíveis é necessária para orientar a prática "
    "cirúrgica e o ensino da cirurgia torácica.",
]

OBJ_GERAL = (
    "Analisar o estado atual do tratamento cirúrgico dos tumores do mediastino anterior, comparando as abordagens "
    "aberta (esternotomia mediana), videotoracoscópica (VATS) e robótica (RATS) quanto à segurança perioperatória e aos "
    "resultados oncológicos."
)
OBJ_ESPECIFICOS = [
    "Comparar as taxas de ressecção completa (R0) entre as vias de acesso;",
    "Comparar perda sanguínea, tempo operatório, complicações pós-operatórias e taxas de conversão para esternotomia;",
    "Comparar o tempo de internação hospitalar e a recuperação pós-operatória;",
    "Comparar recorrência e sobrevida em médio e longo prazo;",
    "Descrever as indicações atuais e os limites da via minimamente invasiva segundo as diretrizes vigentes.",
]

METODOLOGIA = [
    "Trata-se de uma revisão integrativa da literatura, relatada com base nos itens aplicáveis do Preferred Reporting "
    "Items for Systematic Reviews and Meta-Analyses (PRISMA 2020) (PAGE et al., 2021), cujo objetivo foi reunir, analisar e sintetizar as "
    "evidências disponíveis sobre o tratamento cirúrgico dos tumores do mediastino anterior, com ênfase na comparação "
    "entre as vias de acesso aberta (esternotomia mediana), videotoracoscópica (VATS) e robótica (RATS).",

    "A pergunta norteadora foi estruturada pelo acrônimo PICO: em adultos com tumor do mediastino anterior ressecável, "
    "predominantemente tumores epiteliais tímicos (P), a ressecção minimamente invasiva por VATS ou RATS (I), comparada à "
    "ressecção aberta ou entre si (C), oferece resultados perioperatórios e oncológicos equivalentes ou superiores (O)?",

    "A busca foi realizada em 19 de novembro de 2026 na base PubMed/MEDLINE, por meio da interface E-utilities da "
    "National Library of Medicine, combinando descritores controlados (MeSH) e termos livres com os operadores booleanos "
    "AND, OR e NOT. A estratégia combinou três blocos: (1) a doença, com os descritores Thymoma, Thymus Neoplasms e "
    "Mediastinal Neoplasms e os termos thymoma*, \"thymic carcinoma\", \"thymic epithelial tumor*\", \"anterior "
    "mediastinal\" e \"mediastinal tumor*\"; (2) a via de acesso, com os descritores Thoracic Surgery, Video-Assisted e "
    "Robotic Surgical Procedures e os termos VATS, RATS, robot*, thoracoscop*, \"minimally invasive\", sternotomy e "
    "\"open surgery\"; e (3) o caráter comparativo, com os termos compar*, versus e propensity e os tipos de publicação "
    "meta-analysis, systematic review e randomized controlled trial. Aplicaram-se os limites de publicação entre 2015 e "
    "2026, idioma inglês e exclusão de relatos de caso, comentários, editoriais e cartas. Uma segunda busca, dirigida, "
    "identificou diretrizes de prática clínica, consensos e documentos de estadiamento sobre tumores epiteliais tímicos "
    "publicados entre 2014 e 2026, para fundamentar a contextualização e a discussão na versão mais recente das "
    "recomendações.",

    "Foram incluídos estudos que compararam vias de acesso para a ressecção de tumores do mediastino anterior (coortes, "
    "análises pareadas por escore de propensão, registros multicêntricos ou nacionais, ensaios clínicos e revisões "
    "sistemáticas com metanálise) e que relataram ao menos um dos desfechos de interesse. Foram excluídos relatos e séries "
    "de casos, estudos exclusivamente pediátricos, estudos de timectomia para miastenia gravis sem tumor, estudos de "
    "técnica sem grupo comparador e publicações cujo texto completo não pôde ser obtido. Diante do grande número de "
    "comparações unicêntricas de pequeno porte, priorizaram-se as publicações de maior peso metodológico e alcance: "
    "metanálises recentes, registros internacionais e nacionais, estudos pareados por escore de propensão e ensaios "
    "clínicos randomizados, publicados em periódicos de referência da cirurgia e da oncologia torácica.",

    "A busca principal recuperou 416 registros. Após a leitura de títulos e resumos, 13 estudos foram selecionados para "
    "leitura do texto completo, dos quais dois foram excluídos por indisponibilidade do texto completo, resultando em 11 "
    "estudos incluídos. A busca dirigida recuperou 160 registros, dos quais quatro documentos (duas diretrizes, um "
    "documento de padronização e uma proposta de estadiamento) foram utilizados na contextualização e na discussão, "
    "juntamente com dois documentos identificados na busca principal: uma revisão de controvérsias da International "
    "Association for the Study of Lung Cancer e o protocolo do primeiro ensaio randomizado entre RATS e VATS.",

    "Nenhum dado foi extraído apenas do resumo: todos os estudos foram lidos na íntegra. Para cada estudo registraram-se "
    "autor, ano, país, delineamento, nível de evidência segundo o Oxford Centre for Evidence-Based Medicine (OCEBM LEVELS OF EVIDENCE WORKING GROUP, 2011), "
    "objetivo e principais achados, além dos desfechos quantitativos: taxa de ressecção completa, perda sanguínea, tempo "
    "operatório, conversão para esternotomia, complicações, tempo de internação, recorrência e sobrevida. Os dados foram "
    "organizados em quadro e tabela e submetidos a análise descritiva, com síntese narrativa por desfecho. Por se tratar "
    "de revisão baseada exclusivamente em dados publicados, não houve necessidade de submissão ao Comitê de Ética em "
    "Pesquisa.",
]

RESULTADOS_ABERTURA = (
    "Os 11 estudos incluídos foram publicados entre 2016 e 2026 e somam mais de 30 mil pacientes, com sobreposição "
    "parcial entre as metanálises e os registros, provenientes de "
    "Estados Unidos, Japão, Coreia do Sul, China e de registros multinacionais europeus e internacionais. Três são "
    "metanálises, seis analisam registros nacionais ou internacionais, um é uma coorte unicêntrica pareada e um é ensaio "
    "clínico randomizado. O Quadro 1 sintetiza os estudos, e a Tabela 1 reúne os principais resultados numéricos."
)

# Quadro 1: (codigo, autor/pais, delineamento/nivel, objetivo, achados)
QUADRO1 = [
    ("1", "Friedant et al. (2016) / Estados Unidos",
     "Revisão sistemática com metanálise de 30 estudos observacionais (2.038 pacientes) / 3",
     "Comparar a via minimamente invasiva e a aberta em neoplasias tímicas.",
     "Menor perda sanguínea e internação mais curta na via minimamente invasiva, sem diferença em tempo operatório e "
     "complicações; no Masaoka I e II, taxas de R0 e recorrência semelhantes. Metanálise não ajustada."),
    ("2", "Burt et al. (2017) / Internacional (ITMIG)",
     "Coorte retrospectiva de registro internacional, com pareamento por propensão (2.514 pacientes) / 3",
     "Identificar determinantes da ressecção completa do timoma nas vias minimamente invasiva e aberta.",
     "R0 de 96% em ambos os grupos pareados; a via de acesso não se associou à completude da ressecção, ao contrário do "
     "estádio, da região e do período."),
    ("3", "Agatsuma et al. (2017) / Japão (JART)",
     "Coorte retrospectiva multicêntrica pareada (140 VATS x 140 esternotomia) / 3",
     "Avaliar a viabilidade e os resultados oncológicos da VATS em comparação com a esternotomia.",
     "Morbidade, margens positivas, recorrência e sobrevida semelhantes; sobrevida global em 5 anos de 97,9% no grupo "
     "VATS; disseminação pleural foi o local mais comum de recorrência."),
    ("4", "Yang et al. (2020) / Estados Unidos (NCDB)",
     "Coorte retrospectiva de base nacional com pareamento por propensão (1.223 pacientes) / 3",
     "Comparar desfechos de curto prazo e sobrevida da timectomia aberta e minimamente invasiva no timoma I a III.",
     "Internação mais curta na via minimamente invasiva, sem diferença em margem positiva, readmissão, mortalidade em "
     "30 dias e sobrevida em 5 anos."),
    ("5", "Hurd et al. (2022) / Estados Unidos (NCDB)",
     "Coorte retrospectiva de base nacional com pareamento por propensão (216 pacientes) / 3",
     "Comparar as vias aberta e minimamente invasiva no carcinoma tímico Masaoka I a III.",
     "Sem diferença em internação, readmissão, mortalidade, margem positiva e sobrevida em 5 anos após o pareamento."),
    ("6", "Hwang et al. (2022) / Coreia do Sul (KART)",
     "Coorte retrospectiva multicêntrica com pareamento por propensão (1.239 pacientes) / 3",
     "Comparar resultados oncológicos de longo prazo da timectomia minimamente invasiva e aberta.",
     "Menor tempo operatório, internação e complicações na via minimamente invasiva; R0, sobrevida em 10 anos e "
     "sobrevida livre de recorrência sem diferença, com seguimento médio superior a 11 anos."),
    ("7", "Gu et al. (2023) / China",
     "Coorte retrospectiva unicêntrica com pareamento por propensão (128 pacientes) / 3",
     "Avaliar a timectomia minimamente invasiva em tumores tímicos localmente avançados (T2-T3).",
     "Com ressecções de estruturas adjacentes equivalentes, menor perda sanguínea, menos complicações e internação mais "
     "curta; liberdade de recorrência em 5 anos semelhante; conversão de 13,8%."),
    ("8", "Wang et al. (2024) / China",
     "Ensaio clínico randomizado multicêntrico (101 pacientes) / 2",
     "Comparar a VATS por via subxifoide e por via intercostal lateral no timoma Masaoka-Koga I e II.",
     "Dor pós-operatória menor na via subxifoide, sem diferença em internação, consumo de opioide e complicações; "
     "ressecção completa em todos."),
    ("9", "Patel et al. (2024) / Europa e internacional (ESTS)",
     "Coorte de banco prospectivo multicêntrico com pareamento por propensão (732 pacientes) / 3",
     "Comparar RATS e VATS quanto ao estado da ressecção e à sobrevida.",
     "Menor chance de ressecção incompleta com RATS (R0 de 98,3% versus 94,7%), sem diferença em sobrevida global e "
     "livre de doença."),
    ("10", "Liang et al. (2026) / China",
     "Revisão sistemática com metanálise de 7 estudos retrospectivos (12.880 pacientes) / 3",
     "Comparar a via minimamente invasiva e a aberta em timomas grandes.",
     "Menor perda sanguínea, internação mais curta, menos complicações e menor recorrência na via minimamente "
     "invasiva, com tempo operatório semelhante."),
    ("11", "Shen et al. (2026) / China",
     "Revisão sistemática com metanálise de 30 estudos (7.347 pacientes) / 3",
     "Comparar RATS e VATS quanto a desfechos perioperatórios, curva de aprendizado e custos.",
     "RATS com menos conversão, mais R0, menor perda sanguínea e menos complicações; queda do tempo operatório após 20 "
     "casos; custo hospitalar maior; mortalidade semelhante."),
]

# Tabela 1: principais resultados numéricos
TABELA1_CAB = ("Estudo", "Comparação", "n", "Ressecção completa (R0)", "Perioperatório", "Oncológico")
TABELA1 = [
    ("Burt et al. (2017)", "MIT x aberta (pareado)", "266 x 266", "96% x 96% (p = 0,7)", "NR", "NR"),
    ("Agatsuma et al. (2017)", "VATS x esternotomia (pareado)", "140 x 140", "Margem positiva: 3 x 1",
     "Morbidade sem diferença (p = 0,25)", "SG 5 anos 97,9% (VATS); SLR e SG sem diferença (p = 0,91; p = 0,74)"),
    ("Yang et al. (2020)", "MIT x aberta (pareado)", "185 x 185", "Margem positiva sem diferença (p = 0,84)",
     "Internação mediana 3 x 4 dias (p < 0,01)", "SG 5 anos 89,4% x 81,6% (p = 0,20)"),
    ("Hurd et al. (2022)", "MIT x aberta, carcinoma tímico (pareado)", "30 x 30",
     "Margem positiva sem diferença (p = 0,39)", "Internação mediana 3 x 4,5 dias (p = 0,27)",
     "SG 5 anos 78,6% x 54,6% (p = 0,15)"),
    ("Hwang et al. (2022)", "MIT x aberta, Masaoka-Koga I-II (pareado)", "378 pareados", "97,35% em ambos (p = 0,59)",
     "Tempo, internação e complicações menores na MIT (p < 0,005)",
     "SG 10 anos 85,5% x 87,7%; SLR 86,4% x 94,0% (sem diferença)"),
    ("Gu et al. (2023)", "MIT x esternotomia, T2-T3 (pareado)", "40 x 40", "100% em ambos",
     "Sangramento 117,5 x 230,0 mL; complicações 5,0% x 22,5%; internação 4,5 x 9,6 dias",
     "Liberdade de recorrência 5 anos 78,2% x 78,5% (p = 0,942)"),
    ("Wang et al. (2024)", "VATS subxifoide x intercostal (ECR)", "101", "100% em ambos",
     "Complicações 7,84% x 8,00% (p = 1,000); dor menor na via subxifoide", "Sem recorrência em 6 meses"),
    ("Patel et al. (2024)", "RATS x VATS (pareado)", "366 x 366", "98,3% x 94,7%; OR de ressecção incompleta 0,203",
     "Conversão OR 0,671 (p = 0,439)", "SG e SLD sem diferença"),
    ("Friedant et al. (2016)", "MIT x aberta (metanálise)", "2.038", "Sem diferença no Masaoka I-II",
     "Menor sangramento e internação na MIT; conversão 32/1.355", "Recorrência sem diferença no Masaoka I-II"),
    ("Liang et al. (2026)", "MIT x aberta, timomas grandes (metanálise)", "12.880", "NR",
     "Sangramento +110,4 mL e internação +2,0 dias na aberta; complicações OR 0,27", "Recorrência OR 0,54 (IC95% 0,35-0,84)"),
    ("Shen et al. (2026)", "RATS x VATS (metanálise)", "7.347", "OR 1,65 (IC95% 1,12-2,42)",
     "Conversão OR 0,34; sangramento -6,5 mL; complicações OR 0,53", "Mortalidade em 30 e 90 dias sem diferença"),
]
TABELA1_NOTA = ("Valores na ordem da comparação indicada (primeiro grupo x segundo grupo). ECR: ensaio clínico "
                "randomizado; MIT: timectomia minimamente invasiva; NR: não relatado; SG: sobrevida global; SLD: "
                "sobrevida livre de doença; SLR: sobrevida livre de recorrência.")

SECOES = [
    ("4.1 Indicações atuais e escolha da via de acesso", [
        "A ressecção completa é o eixo de todas as recomendações. O NCCN orienta timectomia total com excisão de toda a "
        "doença, desencoraja a citorredução cirúrgica e recomenda terapia sistêmica pré-operatória quando a ressecção R0 "
        "for incerta; admite ainda a ressecção de pericárdio, nervo frênico, pleura, pulmão e grandes vasos quando "
        "necessária, evitando a secção bilateral do frênico (RIELY et al., 2025). Quanto à via de acesso, as diretrizes "
        "convergem no estádio inicial: a diretriz do Journal of Thoracic Oncology considera as vias aberta e minimamente "
        "invasiva igualmente padrão nos estádios I e II, com base em menor sangramento, menos complicações e internação "
        "mais curta, embora com certeza de evidência muito baixa (FALKSON et al., 2022). O NCCN é mais restritivo, ao "
        "admitir a via minimamente invasiva apenas em centros especializados e não recomendá-la de rotina (RIELY et al., "
        "2025).",

        "O tamanho tumoral, agora incorporado à classificação TNM pela separação entre T1a e T1b no limite de 5 cm "
        "(RUFFINI et al., 2023), permanece como critério prático de seleção. A revisão de controvérsias da IASLC reconhece "
        "que há mais evidência para tumores menores que 5 cm, mas que a ressecção minimamente invasiva de tumores maiores "
        "pode ser segura, sem limite superior padronizado, e que a técnica ideal depende da experiência do cirurgião e do "
        "serviço (ARDESHIR-LARINANI et al., 2026). Os padrões do ITMIG reforçam que a via minimamente invasiva é razoável "
        "desde que se evite a ruptura tecidual e que a peça seja retirada em bolsa, para prevenir implante (FANG et al., "
        "2026).",
    ]),
    ("4.2 Ressecção completa e resultados oncológicos", [
        "O principal receio em relação à via minimamente invasiva, a ressecção incompleta, não se confirmou nas séries "
        "pareadas. No registro internacional do ITMIG, com 2.514 timomas operados entre 1997 e 2012, a taxa de R0 foi de "
        "96% nos dois grupos pareados, e a via de acesso não se associou à completude da ressecção, ao passo que estádio "
        "de Masaoka, região geográfica, período e extensão da timectomia o fizeram (BURT et al., 2017). Resultados "
        "concordantes vieram do registro coreano, com R0 de 97,35% em ambos os grupos (HWANG et al., 2022), e das análises "
        "do National Cancer Database, sem diferença em margem positiva tanto no timoma (YANG et al., 2020) quanto no "
        "carcinoma tímico (HURD et al., 2022).",

        "A sobrevida também foi equivalente. No registro japonês, a sobrevida global em 5 anos foi de 97,9% no grupo VATS, "
        "sem diferença em relação à esternotomia, e a disseminação pleural foi o local mais frequente de recorrência no "
        "conjunto dos pacientes (AGATSUMA et al., 2017). No registro coreano, que acumula o maior seguimento disponível (média superior "
        "a 11 anos), a sobrevida em 10 anos e a sobrevida livre de recorrência não diferiram entre as vias (HWANG et al., "
        "2022); o mesmo ocorreu com a sobrevida em 5 anos nas bases norte-americanas (YANG et al., 2020; HURD et al., "
        "2022). A metanálise de Friedant et al. (2016), restrita ao Masaoka I e II, não encontrou diferença em R0 nem em "
        "recorrência. Esses achados sustentam a equivalência oncológica no estádio inicial, mas o seguimento ainda é curto "
        "para um tumor de crescimento lento, em que recorrências tardias são possíveis, ponto que justifica a cautela do "
        "NCCN (RIELY et al., 2025).",
    ]),
    ("4.3 Perda sanguínea, tempo operatório e curva de aprendizado", [
        "A redução da perda sanguínea é o benefício perioperatório mais reprodutível da via minimamente invasiva. Ela foi "
        "observada na metanálise de Friedant et al. (2016), na metanálise de tumores grandes, com diferença média de 110 mL "
        "a favor da via minimamente invasiva (LIANG et al., 2026), e na doença localmente avançada, com 117,5 mL contra "
        "230,0 mL na esternotomia após o pareamento (GU et al., 2023). Entre as técnicas minimamente invasivas, a robótica "
        "associou-se a perda ainda menor, embora a diferença absoluta, de 6,5 mL, tenha pouca relevância clínica (SHEN "
        "et al., 2026).",

        "O tempo operatório, ao contrário do observado em outras cirurgias minimamente invasivas, não foi sistematicamente "
        "maior: não houve diferença nas metanálises (FRIEDANT et al., 2016; LIANG et al., 2026) nem na série de tumores "
        "avançados (GU et al., 2023), e o registro coreano registrou tempo menor com a via minimamente invasiva (HWANG et "
        "al., 2022). Na comparação com a VATS, a robótica foi em média 7 minutos mais rápida, e a análise de curva de "
        "aprendizado mostrou queda significativa do tempo operatório após 20 procedimentos (SHEN et al., 2026). A curva "
        "institucional também apareceu na série de Gu et al. (2023), em que a conversão caiu de 50% no período inicial "
        "para 11,6% nos anos mais recentes, enquanto o uso da via minimamente invasiva subiu de 7,1% para 66,2%.",
    ]),
    ("4.4 Complicações e conversão para esternotomia", [
        "As complicações foram menos frequentes ou semelhantes com a via minimamente invasiva em todos os estudos. Na doença "
        "localmente avançada, a taxa caiu de 22,5% na esternotomia para 5,0% na via minimamente invasiva, sem mortalidade "
        "em 30 dias em nenhum grupo (GU et al., 2023); na metanálise de tumores grandes, a chance de complicação foi cerca "
        "de 70% menor (OR 0,27) (LIANG et al., 2026); e o registro japonês não mostrou diferença de morbidade (AGATSUMA et "
        "al., 2017). Dentro da própria videotoracoscopia, o único ensaio randomizado incluído mostrou que a via subxifoide "
        "reduz a dor pós-operatória em relação à via intercostal lateral, com complicações semelhantes (7,84% e 8,00%) e "
        "ressecção completa em todos os pacientes (WANG et al., 2024).",

        "A conversão para esternotomia funciona como marcador de segurança e de reprodutibilidade. Na metanálise de "
        "Friedant et al. (2016), houve 32 conversões em 1.355 procedimentos minimamente invasivos (2,4%). Em tumores "
        "localmente avançados, a taxa foi de 13,8%, motivada sobretudo por invasão tumoral extensa, e os pacientes "
        "convertidos tiveram desfechos semelhantes aos operados por esternotomia desde o início, exceto pelo tempo "
        "operatório maior (GU et al., 2023). A robótica reduziu a chance de conversão em cerca de dois terços em relação à "
        "VATS na metanálise de 7.347 pacientes (OR 0,34) (SHEN et al., 2026), embora a diferença não tenha alcançado "
        "significância no banco europeu (OR 0,671; p = 0,439) (PATEL et al., 2024).",
    ]),
    ("4.5 Tempo de internação e recuperação", [
        "A internação mais curta é o benefício mais consistente entre os estudos. Nas bases norte-americanas, a mediana "
        "foi de 3 dias com a via minimamente invasiva e de 4 dias com a aberta no timoma, diferença mantida após o "
        "pareamento (YANG et al., 2020); no carcinoma tímico, a diferença inicial de 3 contra 5 dias perdeu significância "
        "no grupo pareado, de apenas 30 pacientes por braço (HURD et al., 2022). Na doença avançada, a internação caiu de "
        "9,6 para 4,5 dias (GU et al., 2023), e a metanálise de tumores grandes estimou cerca de 2 dias a menos (LIANG et "
        "al., 2026). Entre as técnicas minimamente invasivas, a diferença a favor da robótica foi pequena (SHEN et al., "
        "2026; PATEL et al., 2024), e a escolha da via de acesso na videotoracoscopia influenciou mais a dor do que o tempo "
        "de internação (WANG et al., 2024).",
    ]),
    ("4.6 Doença localmente avançada e tumores volumosos", [
        "A fronteira atual da cirurgia minimamente invasiva está nos tumores volumosos e na doença que invade estruturas "
        "adjacentes. Em pacientes T2 e T3 pareados por um índice de complexidade da ressecção, a via minimamente invasiva "
        "obteve ressecção completa em todos os casos, inclusive com ressecção de pericárdio, pulmão, nervo frênico e "
        "grandes veias, com liberdade de recorrência em 5 anos idêntica à da esternotomia (78,2% e 78,5%) (GU et al., "
        "2023). A metanálise de timomas grandes encontrou inclusive menor recorrência com a via minimamente invasiva (OR "
        "0,54) (LIANG et al., 2026), mas esse resultado deve ser interpretado com cautela, porque todos os estudos eram "
        "retrospectivos e os tumores operados por via aberta tendiam a ser maiores, o que favorece viés de seleção.",

        "Por isso, as diretrizes ainda mantêm a via aberta como padrão no estádio III, uma vez que os estudos que "
        "sustentam a via minimamente invasiva incluíram sobretudo pacientes em estádio I e II (FALKSON et al., 2022), e o "
        "NCCN recomenda terapia sistêmica pré-operatória quando a ressecção completa for incerta (RIELY et al., 2025). Na "
        "prática, a via minimamente invasiva na doença avançada parece aceitável em casos selecionados, em centros de alto "
        "volume e com conversão precoce sempre que a margem estiver em risco.",
    ]),
    ("4.7 Cirurgia robótica versus videotoracoscopia", [
        "A comparação entre as duas técnicas minimamente invasivas é o debate mais recente. No banco prospectivo da ESTS, "
        "com 366 pacientes por grupo após o pareamento, a robótica alcançou R0 em 98,3% contra 94,7% na VATS, com chance "
        "cerca de cinco vezes menor de ressecção incompleta, mas sem diferença em sobrevida global ou livre de doença "
        "(PATEL et al., 2024). A metanálise de 30 estudos confirmou maior chance de R0 (OR 1,65), menos conversão e menos "
        "complicações com a robótica, ao custo de maior despesa hospitalar e sem diferença de mortalidade em 30 e 90 dias "
        "(SHEN et al., 2026).",

        "Essas vantagens, porém, vêm de estudos não randomizados, sujeitos a viés de seleção e à curva de aprendizado de "
        "centros que adotaram a robótica mais tarde, quando a experiência com a via minimamente invasiva já era maior. "
        "O primeiro ensaio clínico randomizado multicêntrico entre robótica e videotoracoscopia em tumores epiteliais "
        "tímicos estádio I e II, com 100 pacientes e seguimento previsto até 2027, deverá oferecer a primeira comparação "
        "direta (WANG et al., 2025). Até lá, a escolha entre as duas técnicas depende sobretudo da experiência da "
        "equipe (ARDESHIR-LARINANI et al., 2026), além da disponibilidade e do custo da plataforma robótica (SHEN et al., "
        "2026).",
    ]),
    ("4.8 Limitações da evidência", [
        "A literatura analisada tem limitações importantes. Com exceção de um ensaio randomizado que comparou duas variantes "
        "de videotoracoscopia (WANG et al., 2024), toda a evidência comparativa é observacional e retrospectiva, e mesmo o "
        "pareamento por escore de propensão não elimina a escolha preferencial da via minimamente invasiva para tumores "
        "menores e menos invasivos (FRIEDANT et al., 2016; BURT et al., 2017). Os registros envolvem centros de alto "
        "volume, o que limita a extrapolação para serviços com menor experiência, e o seguimento da maioria dos estudos "
        "ainda é curto para um tumor de evolução lenta. Por fim, esta revisão restringiu a busca ao PubMed/MEDLINE e "
        "excluiu dois estudos cujo texto completo não pôde ser obtido, o que pode ter deixado de fora evidências "
        "relevantes.",
    ]),
]

CONSIDERACOES = [
    "A ressecção minimamente invasiva, por videotoracoscopia ou cirurgia robótica, consolidou-se como opção padrão para "
    "os tumores epiteliais tímicos em estádio inicial. Nos estudos pareados e nas metanálises analisados, ela alcançou "
    "taxas de ressecção completa e sobrevida equivalentes às da esternotomia, com menor perda sanguínea, menos "
    "complicações e internação mais curta, desde que respeitados os princípios oncológicos de timectomia total, ausência "
    "de ruptura capsular e retirada protegida da peça.",

    "Na doença localmente avançada e nos tumores volumosos, séries selecionadas demonstram viabilidade e resultados "
    "oncológicos preservados, mas a evidência é retrospectiva e as diretrizes mantêm a esternotomia como padrão no "
    "estádio III. A cirurgia robótica apresenta sinais de vantagem sobre a videotoracoscopia em ressecção completa, "
    "conversão e complicações, sem impacto demonstrado na sobrevida e com custo maior. A definição de seu papel e dos "
    "limites da via minimamente invasiva depende de ensaios clínicos randomizados, o primeiro dos quais já está em "
    "andamento, e de registros com seguimento longo, compatível com a história natural desses tumores.",
]

# ABNT references, alphabetical
REFERENCIAS = [
    "AGATSUMA, H. et al. Video-assisted thoracic surgery thymectomy versus sternotomy thymectomy in patients with thymoma. "
    "The Annals of Thoracic Surgery, v. 104, n. 3, p. 1047-1053, 2017. DOI: https://doi.org/10.1016/j.athoracsur.2017.03.054.",
    "ARDESHIR-LARINANI, F. et al. Challenges and controversies in the diagnosis and management of thymic epithelial tumors "
    "from the Thymic Tumor Subcommittee of the International Association for the Study of Lung Cancer Rare Tumors Committee. "
    "Journal of Thoracic Oncology, v. 21, n. 5, 103611, 2026. DOI: https://doi.org/10.1016/j.jtho.2026.103611.",
    "BURT, B. M. et al. Determinants of complete resection of thymoma by minimally invasive and open thymectomy: analysis "
    "of an international registry. Journal of Thoracic Oncology, v. 12, n. 1, p. 129-136, 2017. DOI: "
    "https://doi.org/10.1016/j.jtho.2016.08.131.",
    "FALKSON, C. B. et al. Surgical, radiation, and systemic treatments of patients with thymic epithelial tumors: a "
    "clinical practice guideline. Journal of Thoracic Oncology, v. 17, n. 11, p. 1258-1275, 2022. DOI: "
    "https://doi.org/10.1016/j.jtho.2022.08.007.",
    "FANG, W. et al. International Thymic Malignancy Interest Group standard definitions, policies, and reporting measures "
    "for thymic epithelial tumors. Journal of Thoracic Oncology, v. 21, n. 1, p. 102-111, 2026. DOI: "
    "https://doi.org/10.1016/j.jtho.2025.09.1757.",
    "FRIEDANT, A. J. et al. Minimally invasive versus open thymectomy for thymic malignancies: systematic review and "
    "meta-analysis. Journal of Thoracic Oncology, v. 11, n. 1, p. 30-38, 2016. DOI: https://doi.org/10.1016/j.jtho.2015.08.004.",
    "GU, Z. et al. Minimally invasive thymectomy could be attempted for locally advanced thymic malignancies: a real-world "
    "study with propensity score-matched analysis. Journal of Thoracic Oncology, v. 18, n. 5, p. 640-649, 2023. DOI: "
    "https://doi.org/10.1016/j.jtho.2022.12.013.",
    "HURD, J. et al. A national analysis of open versus minimally invasive thymectomy for stage I-III thymic carcinoma. "
    "European Journal of Cardio-Thoracic Surgery, v. 62, n. 3, ezac159, 2022. DOI: https://doi.org/10.1093/ejcts/ezac159.",
    "HWANG, S. K. et al. Long-term outcome of minimally invasive thymectomy versus open thymectomy for locally advanced "
    "cases. European Journal of Cardio-Thoracic Surgery, v. 62, n. 3, ezac238, 2022. DOI: https://doi.org/10.1093/ejcts/ezac238.",
    "LIANG, L. J. et al. Perioperative safety and efficacy of minimally invasive vs. open thymectomy for large thymomas: a "
    "systematic review and meta-analysis. Journal of Robotic Surgery, v. 20, n. 1, 126, 2026. DOI: "
    "https://doi.org/10.1007/s11701-025-03012-x.",
    "OCEBM LEVELS OF EVIDENCE WORKING GROUP. The Oxford 2011 levels of evidence. Oxford: Oxford Centre for "
    "Evidence-Based Medicine, 2011. Disponível em: https://www.cebm.ox.ac.uk/resources/levels-of-evidence/ocebm-levels-of-evidence. "
    "Acesso em: 19 nov. 2026.",
    "PAGE, M. J. et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ, v. 372, "
    "n71, 2021. DOI: https://doi.org/10.1136/bmj.n71.",
    "PATEL, A. J. et al. Robotic-assisted versus video-assisted thoracoscopic surgery for thymic epithelial tumours, from "
    "the European Society of Thoracic Surgeons Database. European Journal of Cardio-Thoracic Surgery, v. 66, n. 4, ezae346, "
    "2024. DOI: https://doi.org/10.1093/ejcts/ezae346.",
    "RIELY, G. J. et al. Thymomas and thymic carcinomas, version 2.2025, NCCN Clinical Practice Guidelines in Oncology. "
    "Journal of the National Comprehensive Cancer Network, v. 23, n. 6, p. 255-269, 2025. DOI: "
    "https://doi.org/10.6004/jnccn.2025.0027.",
    "RUFFINI, E. et al. The International Association for the Study of Lung Cancer Thymic Epithelial Tumors Staging "
    "Project: proposal for a stage classification for the forthcoming (ninth) edition of the TNM classification of "
    "malignant tumors. Journal of Thoracic Oncology, v. 18, n. 12, p. 1655-1671, 2023. DOI: "
    "https://doi.org/10.1016/j.jtho.2023.09.002.",
    "SHEN, G. et al. Comparative meta-analysis of robot- and video-assisted surgery for thymoma: efficacy, learning curve, "
    "and economic burden in 7347 patients. World Journal of Surgical Oncology, v. 24, n. 1, 14, 2026. DOI: "
    "https://doi.org/10.1186/s12957-025-04132-2.",
    "WANG, S. et al. Subxiphoid versus lateral intercostal thoracoscopic thymectomy for suspected thymoma: results of a "
    "randomized controlled trial. The Journal of Thoracic and Cardiovascular Surgery, v. 168, n. 1, p. 290-298, 2024. DOI: "
    "https://doi.org/10.1016/j.jtcvs.2023.10.040.",
    "WANG, S. et al. Robot-assisted versus video-assisted thoracoscopic thymectomy for stage I-II thymic epithelial tumour: "
    "a protocol for the first multicentre, randomised controlled clinical trial. BMJ Open, v. 15, n. 5, e095802, 2025. DOI: "
    "https://doi.org/10.1136/bmjopen-2024-095802.",
    "YANG, C. J. et al. A national analysis of open versus minimally invasive thymectomy for stage I to III thymoma. The "
    "Journal of Thoracic and Cardiovascular Surgery, v. 160, n. 2, p. 555-567.e15, 2020. DOI: "
    "https://doi.org/10.1016/j.jtcvs.2019.11.114.",
]
