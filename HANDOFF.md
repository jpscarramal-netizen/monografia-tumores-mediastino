# Handoff: Monografia tumores mediastinais

> Última sessão: 19/11/2026

## Paramos em

Monografia completa em `saida/monografia_tumores_mediastino.docx` (e `.pdf`), 21 páginas: capa, folha de rosto, folha de aprovação, resumo, abstract, listas, sumário, Introdução, Objetivos, Metodologia, Resultados e Discussão (Quadro 1 com 11 estudos, Tabela 1, seções 4.1 a 4.8), Considerações finais e 19 referências ABNT.

## Já validado, não mexer

- Cada número do texto confere com `trabalho/extracao_notas.md`, que aponta a página/tabela do artigo (textos completos em `trabalho/textos/`, só locais).
- Toda citação no texto tem referência e vice-versa (checagem automática).
- Sem travessões; resumo com 280 palavras (norma: 150 a 500).

## Próximo passo

Colocar os nomes do Grupo 6 em `AUTORES` (`trabalho/scripts/conteudo.py`), rodar `python -I trabalho/scripts/gera_docx.py` e atualizar o sumário no Word (botão direito > Atualizar campo).

## Armadilhas desta sessão

- Edge/Chrome bloqueia o 2º download automático; servidor local (127.0.0.1) trava a aba. Solução que funcionou: subagentes lendo o HTML do texto completo e salvando com Write.
- OUP (EJCTS) e ScienceDirect às vezes ficam presos no Cloudflare; JTO, JTCVS e ATS passam após ~10 s.
- PubMed E-utilities e efetch do PMC funcionam por Python; Europe PMC PDF deu 403.

## Perguntas abertas para o JP

1. Nomes dos integrantes e segundo avaliador da banca.

## Caminhos que importam

```
saida/monografia_tumores_mediastino.docx
trabalho/scripts/conteudo.py
trabalho/scripts/gera_docx.py
trabalho/extracao_notas.md
trabalho/busca/
```
