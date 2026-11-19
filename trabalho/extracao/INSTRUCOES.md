# Instruções para os agentes de texto completo e extração

Projeto: revisão sistemática (síntese narrativa) sobre via de acesso na ressecção de tumores do mediastino anterior / tumores epiteliais tímicos (TET): minimamente invasiva (VATS, RATS) x aberta (esternotomia), e RATS x VATS. Responda em português.

## Para cada estudo da sua lista

1. OBTER O TEXTO COMPLETO (nunca extraia dado só do resumo).
   - Acesso institucional da UFOP por IP já funciona neste computador.
   - Caminhos que funcionam, em ordem de preferência:
     a. PMC por E-utilities (sem navegador): descubra o PMCID com
        `https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids=<DOI>&format=json` e baixe o XML com
        `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=<numero_sem_PMC>&retmode=xml` (curl ou `python -I`).
     b. Springer (link.springer.com) e Wiley: `curl -sSL -A "Mozilla/5.0" -o arquivo.pdf "https://link.springer.com/content/pdf/<DOI>.pdf"` funciona por IP. Confira se o arquivo começa com `%PDF`.
     c. Navegador (Claude in Chrome, ferramentas `mcp__claude-in-chrome__*`; carregue as que precisar numa única ToolSearch): abra `https://doi.org/<DOI>`, espere (páginas "Um momento…" do Cloudflare costumam passar sozinhas em 10 a 20 s), e extraia o texto do corpo do artigo com `javascript_tool` (innerText do elemento do artigo) em pedaços de até ~40.000 caracteres. NÃO clique em CAPTCHA. Crie UMA aba própria (tabs_context_mcp com createIfEmpty, depois tabs_create_mcp) e use só ela; outros agentes usam o mesmo navegador. Downloads automáticos estão bloqueados; não dependa deles.
   - Salve o texto completo em `C:\Users\joaop\Claude contexto\monografia-tumores-mediastino\trabalho\textos\<Sobrenome>_<ano>_<curto>.txt` (primeira linha: `FONTE: <url> | <data>`). PDFs baixados vão para `...\entrada\artigos\`; converta com `python -I` + pymupdf marcando `=== [p.N] ===` por página.
   - Se não conseguir o texto completo, registre `TEXTO COMPLETO INDISPONÍVEL: <motivo>` e não extraia nada.

2. CONFIRMAR ELEGIBILIDADE no texto completo:
   - População: adultos com tumor do mediastino anterior / TET, com resultados separáveis para tumor (miastenia sem tumor misturada, sem separar = excluir).
   - Comparação: MIS (VATS/RATS) x aberta, ou RATS x VATS.
   - Desenho: metanálise; registro/banco multicêntrico ou nacional; ECR; ou unicêntrico só se doença localmente avançada (T3/T4 ou Masaoka III+).
   - Pelo menos um desfecho: R0/margem, sangramento, tempo operatório, conversão, complicações, internação, recorrência, sobrevida, mortalidade.
   Se não for elegível: `EXCLUÍDO NA LEITURA COMPLETA: <motivo exato>`.

3. EXTRAIR (só para elegíveis), registrando a LOCALIZAÇÃO de cada número (página, tabela, figura ou seção):
   - Referência completa: autores (3 primeiros + et al.), título, periódico, ano, volume(número):páginas ou número do artigo, DOI.
   - País/região e fonte de dados (nome do registro/banco, nº de centros).
   - Desenho e período do estudo; ajuste (PSM, IPTW, multivariável).
   - População (timoma, carcinoma, TET; estádio; tamanho tumoral) e n por grupo (antes e depois do pareamento).
   - Desfechos com valores por grupo e medida de efeito (OR/RR/MD/HR, IC95%, p): R0/margem positiva; perda sanguínea; tempo operatório; conversão; complicações (gerais e maiores); internação; mortalidade 30/90 d; recorrência; sobrevida (global e livre de doença) com tempo de seguimento; custo.
   - Para METANÁLISES: nº de estudos e pacientes, bases e data da busca, modelo, I², ferramenta de qualidade, e os efeitos agrupados de cada desfecho; diga se a população mistura miastenia sem tumor.
   - Limitações declaradas pelos autores (1 a 2 linhas).

## Saída

Um arquivo por estudo: `C:\Users\joaop\Claude contexto\monografia-tumores-mediastino\trabalho\extracao\<Sobrenome>_<ano>.md`, com cabeçalho `# <Sobrenome> <ano> | <periódico> | <desenho> | STATUS: INCLUÍDO / EXCLUÍDO NA LEITURA COMPLETA / TEXTO COMPLETO INDISPONÍVEL`. Copie números exatamente como estão no artigo (não arredonde, não traduza unidades). Nada de inventar: se um dado não está no artigo, escreva NR.

Resposta final ao orquestrador: tabela curta (estudo | status | motivo se excluído/indisponível). Nada de conteúdo dos artigos na resposta.
