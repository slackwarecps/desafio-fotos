Scenario: Structured Data Extraction You are building a structured data extraction system using Claude. The system extracts information from unstructured documents, validates output using JSON schemas, and maintains high accuracy. It must handle edge cases gracefully and integrate with downstream systems. Your extraction QA pass produces JSON records that validate successfully, but reviewers report the findings are hard to act on. Some records describe vague problems like "date issue," others omit where the problem appears, and suggested fixes vary between full sentences, fragments and empty strings. The downstream ticketing system accepts the records, but reviewers spend significant time interpreting them. What change would most effectively improve consistency?
---
[ ] A - Make every finding field non-null in the schema so validation fails whenever Claude leaves any reviewer detail empty.
[ ] B - Add a general instruction requiring concise, high-confidence findings and asking Claude to avoid vague or incomplete reviewer notes.
[ ] C - Add targeted examples showing complete actionable findings with document location, affected field, issue description, severity, and suggested correction.
[ ] D - Post-process each finding with regular expressions to infer missing locations, severities, and suggested fixes from the text.
---
### TRANSLATED QUESTION
Você está construindo um sistema de extração de dados estruturados usando Claude. O sistema extrai informações de documentos não estruturados, valida a saída usando esquemas JSON e mantém alta precisão. Deve lidar com casos extremos de forma graciosa e integrar-se com sistemas downstream. Seu QA pass de extração produz registros JSON que validam com sucesso, mas reviewers relatam que os findings são difíceis de agir. Alguns registros descrevem problemas vagos como "date issue," outros omitem onde o problema aparece, e sugestões de fix variam entre sentenças completas, fragmentos e strings vazios. O sistema de ticketing downstream aceita os registros, mas reviewers gastam tempo significativo interpretando-os. Qual mudança melhor melhoraria a consistência?

Alternativas traduzidas:

A) Fazer cada campo de finding non-null no schema para que a validação falhe sempre que Claude deixa algum detalhe de reviewer vazio.
B) Adicionar uma instrução geral requerendo findings concisos e alta confiança, pedindo a Claude para evitar reviewer notes vagas ou incompletas.
C) Adicionar exemplos direcionados mostrando findings completos e acionáveis com localização em documento, campo afetado, descrição do problema, severidade e correção sugerida.
D) Pós-processar cada finding com expressões regulares para inferir localizações, severidades e fixes sugeridos a partir do texto.

---
### EXPLANATION (TECH LEAD)
Explicação Técnica:

Esta pergunta testa um padrão crítico em prompt engineering com LLMs: **exemplos concretos (few-shot prompting) superam instruções genéricas em múltiplas ordens de magnitude**. O cenário descreve um problema clássico — o modelo produz JSON válido (schema passa), mas conteúdo semântico dentro dos campos é inconsistente e de baixa qualidade (vagueza, omissões, variação).

A raiz do problema é falta de definição clara de "padrão esperado". Instruções genéricas como "seja conciso" ou "evite vagueza" são abstratas — o modelo as reinterpreta a cada execução. Mas exemplos concretos ("aqui está um finding bem-formado com localização específica, descrição clara, severidade quantificada, sugestão testável") estabelecem um padrão que o modelo consegue imitar consistentemente.

Por que a alternativa C é a correta:

A alternativa C usa **few-shot prompting** — a forma mais robusta de moldar comportamento de LLM. Em vez de confiar em linguagem natural abstrata ("seja conciso", "evite vagueza"), você mostra exemplos reais: "Aqui está um finding bem-formado: document='contract_123.pdf', field='expiration_date', issue='Missing expiration date in contract header', severity='high', suggestion='Insert date from contract cover page'."

Com exemplos, o modelo recebe um padrão concreto e legível que consegue replicar. Isso é mais eficaz porque:
- Exemplos são semântica clara, não interpretação linguística
- Padrão é visível e reutilizável
- Modelo consegue aprender por imitação

Por que as outras estão erradas:

**A) Schema com non-null**: Força estrutura, mas não força **qualidade de conteúdo**. Validação passa com "date issue" (vago mas não-null). Você tem JSON válido mas findings ainda inúteis. Schema resolution opera em tipos; não resolve semântica.

**B) Instruções genéricas**: Tenta comunicar expectativas via linguagem natural. Problema: "conciso" e "vago" são subjetivos. Diferentes execuções do modelo interpretam diferentemente. Sem exemplos, o modelo fica adivinhando o que você quer.

**D) Post-processing com regex**: É frágil. Você não consegue inferir confiável "localização no documento" de texto livre usando regex — existem infinitas formas de descrever localização. Além disso, não resolve o problema real: modelo gerando output de baixa qualidade desde o início.

Dica importante:

Em prompt engineering com LLMs, **exemplos > instruções genéricas** sempre. Quando precisa de output estruturado e consistente, mostre 2-3 exemplos de "exatamente o que eu quero" (com estrutura, tom, nível de detalhe). Isso treina muito melhor do que dizer "seja conciso" ou "seja claro".

---
### SIMPLE EXPLANATION
Explicação para Aprendizes:

O que está acontecendo:

Você pediu ao Claude para gerar avisos sobre problemas em documentos. O JSON é válido (estrutura OK), mas o conteúdo é inconsistente. Às vezes ele diz "date issue" (vago), às vezes omite o local do problema, às vezes escreve a sugestão de forma diferente. Reviewers gastam tempo interpretando.

A pergunta: como fazer o Claude gerar avisos **consistentes e acionáveis**?

Por que a alternativa C é a melhor:

C diz: "Mostre exemplos de avisos bem-feitos ao Claude antes de pedir que gere novos."

Um exemplo bem-feito seria:
```
documento: "contract.pdf"
campo: "expiration_date"
problema: "Data de expiração está vazia no cabeçalho"
severidade: "alto"
sugestão: "Adicione a data da página de capa do contrato"
```

Ao ver esse exemplo, Claude entende o padrão e repete em avisos novos.

Por que as outras não funcionam:

**A) Validação no schema**: Força estrutura, mas não força qualidade. "Date issue" não é nula, então passa. Ainda vago.

**B) Instruções genéricas**: "Seja conciso" é subjetivo. Claude interpreta diferente cada vez. Sem exemplo concreto, ele fica adivinhando.

**D) Regex para inferir**: Você tenta adivinhar informação a partir do texto. Frágil e não resolve — o problema é Claude gerar pobremente desde o início.

Lembrar:

**Exemplos funcionam melhor que instruções:**

Em vez de "write clear fields", mostre um exemplo de "campo claro bem feito". Claude aprende pelo exemplo melhor que por instrução.

---
### CORRECT ANSWER
Alternativa Correta: C
