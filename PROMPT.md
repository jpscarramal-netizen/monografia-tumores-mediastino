# Prompt para outro Claude Code assumir o projeto

Cole o bloco abaixo em uma sessão nova do Claude Code (desktop, terminal ou claude.ai/code).
O repositório é público: funciona de qualquer computador.

```
Você vai assumir a monografia do Grupo 6 de Clínica Cirúrgica II (Medicina UFOP):
"Estado atual do tratamento cirúrgico dos tumores mediastinais".

1. Clone o repositório e entre na pasta:
   gh repo clone jpscarramal-netizen/monografia-tumores-mediastino
   cd monografia-tumores-mediastino
   (sem gh: git clone https://github.com/jpscarramal-netizen/monografia-tumores-mediastino.git)

2. Leia, nesta ordem: CLAUDE.md, PROJETO.md, HANDOFF.md e PLANO.md.
   Abra também entrada/normas/normas_monografia_cirurgia.pdf e
   entrada/exemplo-semestre-anterior/LEIA.md (formato que o professor já aprovou).
   PDFs de artigos NÃO vão para o git: salve em entrada/artigos/ (já está no .gitignore).

3. Antes de executar qualquer coisa, me responda em português, em até 8 linhas:
   - o que você entendeu do objetivo e do formato exigido;
   - em que fase o projeto está;
   - qual é o próximo passo concreto;
   - quais perguntas abertas do HANDOFF.md você precisa que eu responda.
   Não comece a executar até eu confirmar.

4. Depois da minha confirmação, siga as fases da seção 7 do PLANO.md, uma de cada vez,
   parando ao fim de cada fase para eu revisar. Regras inegociáveis:
   - Artigo só entra no texto depois de lido COMPLETO (PDF + suplementar). Resumo não basta.
   - Prioridade de fontes: guidelines vigentes (NCCN, ESMO, ITMIG, TNM IASLC/ITMIG 9a ed.),
     metanálises recentes, registros grandes (ESTS, ITMIG, JART, NCDB, ChART), estudos pareados
     e ensaios, em revistas de alto impacto. Sempre a versão mais recente.
   - Nunca invente número, DOI, autor ou referência; o que não foi conferido leva [CONFERIR].
   - Todo número do texto precisa apontar para a página/tabela do artigo de onde saiu,
     registrado na planilha de extração.
   - Texto em português acentuado, sem travessões; referências em ABNT autor-data.

5. Ao fim de cada fase: atualize PROJETO.md, reescreva HANDOFF.md, faça commit e push.
```
