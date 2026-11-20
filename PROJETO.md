# Monografia: estado atual do tratamento cirúrgico dos tumores mediastinais

> Md-mestre do projeto. É um estado, não um diário.
> Criado em 16/11/2026 | Última atualização: 19/11/2026

## Objetivo

Escrever a monografia do **Grupo 6** da disciplina **CGP012 Clínica Cirúrgica II** (UFOP, 2026/2,
Prof. Iure Kalinine Ferraz de Souza), tema oficial do Moodle: "Estado atual do tratamento
cirúrgico dos tumores mediastinais". Revisão integrativa feita com rigor de publicação
(PRISMA 2020, artigos de alta referência, guidelines atuais), embora não vá ser publicada.

**Entregável final:** `saida/monografia_tumores_mediastino.docx`, formatada pelas normas da
disciplina (ABNT, TNR 12, espaçamento 1,5; detalhes no `PLANO.md`, seção 0).

**Destino:** entrega no Moodle da disciplina CGP012.

## Estado atual

**Em 19/11/2026 (v2):** monografia refeita no formato do paper-modelo do JP (Scarramal et al., Neurosurgery 2026), como revisão sistemática com síntese narrativa: `saida/monografia_tumores_mediastino.docx` e `.pdf` (34 páginas). Busca em PubMed, Scopus e Web of Science; 40 estudos incluídos. Gerada por `trabalho/scripts/gera_docx_v2.py` a partir de `trabalho/secoes/*.md` e `*.csv`. Extração por estudo em `trabalho/extracao/`.

**Percentual do caminho:** texto completo; falta revisão do grupo (nomes na capa, segundo avaliador, leitura final).

## Decisões fechadas

| Decisão | Motivo | Data |
|---|---|---|
| Desenho: revisão sistemática com síntese narrativa (PRISMA 2020), sem metanálise própria | JP pediu o formato do paper de MA dele, só a escrita; sobreposição de pacientes entre registros impede pooling | 19/11 |
| Formato e seções seguem o exemplo do semestre passado + normas da disciplina | exemplo já aprovado pelo professor | 16/11 |
| Incluir folha de aprovação e lista de quadros/tabelas | exigidas pela norma; o exemplo esqueceu | 17/11 |
| Referências ABNT, autor-data, ordem alfabética | norma da disciplina | 17/11 |
| Meta de 10 a 15 artigos no Quadro 1, mais guidelines | tamanho de trabalho de semestre com nível de publicação | 16/11 |
| Recorte: mediastino anterior (TET), aberta x VATS x RATS | JP mandou seguir com o plano ("manda bala") | 19/11 |
| Busca em PubMed, Scopus e Web of Science (19/11/2026) | pedido do JP; WoS exportado com resumo; Scopus via página (exportação exige login) | 19/11 |
| Formato idêntico ao paper-modelo (stent retriever longo x curto, Neurosurgery 2026), em português | pedido do JP; norma aceita formato de artigo | 19/11 |
| Seções escritas por agentes com as skills escrever-introducao, escrever-methods-results, discussao, escrever-abstract | pedido do JP ("autores serão os agentes" = agentes escrevem) | 19/11 |
| Triagem uniforme nas 3 bases: MA, registro multicêntrico/nacional, ECR; unicêntrico só em doença avançada | consistência entre bases | 19/11 |
| Todos os elegíveis lidos no texto completo (50), 40 incluídos | JP pediu o trabalho mais completo | 19/11 |
| ESMO 2015 e Dimmers 2026 não usados | texto completo bloqueado | 19/11 |

## Pendências

1. [ ] Grupo colocar os nomes na capa, folha de rosto e folha de aprovação (`AUTORES` em `trabalho/scripts/conteudo.py`)
2. [ ] Definir o segundo nome da banca (ou retirar a linha)
3. [ ] Leitura final do grupo; para mudar texto, editar `conteudo.py` e rodar `python -I trabalho/scripts/gera_docx.py`, depois atualizar o sumário no Word
4. [ ] (Opcional) Salvar o Guia SISBIN em `entrada/normas/` e conferir detalhes de ABNT

## Materiais

| O quê | Onde | Observação |
|---|---|---|
| Plano completo | `PLANO.md` | recorte, PICO, string de busca, estrutura, etapas, regras de formatação |
| Normas da disciplina | `entrada/normas/normas_monografia_cirurgia.pdf` | 12 p.; manual da UFMA reaproveitado pelo professor |
| Monografia-exemplo | `entrada/exemplo-semestre-anterior/monografia_exemplo_hepatectomia_doador_vivo.pdf` | 14 p., 7 artigos, aprovada |
| Artigos do exemplo | `entrada/exemplo-semestre-anterior/Artigos/1.pdf` a `7.pdf` | só como modelo; tema diferente |
| Planilha-modelo de extração | `entrada/exemplo-semestre-anterior/planilha_extracao_exemplo.xlsx` | colunas do Quadro 1 |

## Armadilhas conhecidas

- O Moodle UFOP derruba a sessão do Chrome com frequência; o Chrome libera só o primeiro
  download automático por página. O Guia SISBIN ficou de fora por isso.
- Os nomes de guidelines, registros e autores no `PLANO.md` vieram de memória: todos precisam ser
  confirmados na busca, na versão mais recente.

## Pessoas e prazos

- **Responsável:** João Paulo (Grupo 6)
- **Aguardando:** nomes dos integrantes do Grupo 6 (capa) e prazo de entrega
- **Prazo:** a confirmar
