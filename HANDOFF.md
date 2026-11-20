# Handoff: Monografia tumores mediastinais

> Última sessão: 19/11/2026

## Paramos em

Versão 2 completa em `saida/monografia_tumores_mediastino.docx` (e `.pdf`, 34 páginas): pré-texto da norma (capa, rosto, aprovação, resumo e abstract estruturados, listas, sumário) + corpo no formato do paper-modelo (1 Introdução, 2 Métodos, 3 Resultados com Figura 1 PRISMA, Quadro 1 e Tabela 1, 4 Discussão com Limitações, 5 Conclusão) e 49 referências ABNT.

## Já validado, não mexer

- PRISMA: `trabalho/prisma_numeros.md` (1.467 identificados, 755 duplicatas, 712 triados, 50 texto completo, 40 incluídos).
- Cada número das seções foi conferido contra `trabalho/extracao/*.md` e `trabalho/extracao_notas.md`.
- Citações x referências conferidas; sem travessões.

## Próximo passo

Nomes do Grupo 6 em `AUTORES` (`trabalho/scripts/gera_docx_v2.py`), rodar `python -I trabalho/scripts/gera_docx_v2.py` e atualizar o sumário no Word.

## Armadilhas desta sessão

- O primeiro CSV do PubMed tinha DOIs de referências (bug do parser); corrigido em `pubmed_search.py` e busca refeita.
- Scopus: exportação exige login; resumos vieram pela API interna da página (`/api/documents/search`, `showAbstract: true`).
- WoS: exportar com "Full Record" para vir o resumo.
- Agentes de navegador travam em SAGE e às vezes em OUP; limitar tentativas.

## Perguntas abertas para o JP

1. Nomes dos integrantes e segundo avaliador da banca.

## Caminhos que importam

```
saida/monografia_tumores_mediastino.docx
trabalho/secoes/
trabalho/extracao/
trabalho/busca/
trabalho/scripts/gera_docx_v2.py
```
