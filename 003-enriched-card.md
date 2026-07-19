Scenario: Structured Data Extraction You are building a structured data extraction system using Claude. The system extracts information from unstructured documents, validates output using JSON schemas, and maintains high accuracy. It must handle edge cases gracefully and integrate with downstream systems. Your extraction QA pass produces JSON records that validate successfully, but reviewers report the findings are hard to act on. Some records describe vague problems like "date issue," others omit where the problem appears, and suggested fixes vary between full sentences, fragments, and empty strings. The downstream ticketing system accepts the records, but reviewers spend significant time interpreting them. What change would most effectively improve consistency?
---
[ ] A - Make every finding field non-null in the schema so validation fails whenever Claude leaves any detail empty.
[ ] B - Add a general instruction requiring concise, high-confidence findings and asking Claude to avoid vague or incomplete reviewer notes.
[ ] C - Add targeted examples showing complete actionable findings with document location, affected field, issue description, severity, and suggested correction.
[ ] D - Post-process each finding with regular expressions to infer missing locations, severities, and suggested fixes from the text.
---
### TRANSLATED QUESTION
Você está construindo um sistema de extração de dados estruturados usando Claude. O sistema extrai informações de documentos não estruturados, valida a saída usando esquemas JSON e mantém alta precisão. Deve lidar com casos extremos de forma graciosa e integrar-se com sistemas downstream. Sua passagem de QA de extração produz registros JSON que validam com sucesso, mas os revisores reportam que os findings são difíceis de usar. Alguns registros descrevem problemas vagos como "problema de data," outros omitem onde o problema aparece, e as correções sugeridas variam entre frases completas, fragmentos e strings vazias. O sistema de ticketing downstream aceita os registros, mas os revisores gastam tempo significativo interpretando-os. Qual mudança melhoraria a consistência de forma mais eficaz?

Alternativas traduzidas:

A) Tornar todo campo de finding não-nulo no schema para que a validação falhe sempre que Claude deixar qualquer detalhe vazio.
B) Adicionar uma instrução geral exigindo findings concisos e de alta confiança, pedindo para Claude evitar notas vagas ou incompletas.
C) Adicionar exemplos direcionados mostrando findings acionáveis completos com localização no documento, campo afetado, descrição do problema, severidade e correção sugerida.
D) Pós-processar cada finding com expressões regulares para inferir localizações, severidades e correções sugeridas ausentes a partir do texto.

---
### EXPLANATION (TECH LEAD)

Esta pergunta testa o conceito de **few-shot prompting vs. instruções abstratas** em sistemas de extração com LLMs. O problema é claro: as saídas são estruturalmente válidas (passam no JSON schema) mas semanticamente inconsistentes — falta um padrão compartilhado de como um "finding acionável" deve ser.

A validação de schema garante tipo e presença de campos, mas não garante **qualidade semântica** do conteúdo. O problema não é o que está sendo gerado, mas como está sendo gerado — falta um **template mental** consistente para o modelo seguir.

Por que a alternativa C é a correta:

**Few-shot examples são a técnica mais eficaz para shapear output quality.** Em vez de dizer abstratamente "seja consistente" (B) ou forçar campos não-nulos (A), você mostra **exemplos concretos** do que considera um finding bem formado. Isso estabelece um padrão implícito de formato, tom, nível de detalhe e estrutura que o modelo pode imitar. É a abordagem mais robusta porque ataca a causa raiz: falta de um template de referência.

Por que as outras estão erradas:

**A)** Tornar campos não-nulos é uma abordagem puramente técnica que não resolve o problema semântico. O modelo pode preencher "location: somewhere" e "severity: medium" — válido, mas ainda inútil. Você força presença, não qualidade.

**B)** Instruções abstratas são fracas para controle de formato. "Seja consistente" ou "evite notas vagas" são subjetivos — o modelo não tem uma definição operacional do que isso significa em termos de saída esperada.

**D)** Pós-processamento com regex é frágil e reativo. Você está tentando adivinhar o que o modelo quis dizer em vez de fazê-lo gerar corretamente desde o início. Além disso, inferir "severidade" ou "correção sugerida" de texto livre com regex é propenso a erros.

Dica importante: **Schemas de validação garantem estrutura; exemplos (few-shot) garantem qualidade semântica.** Em sistemas de extração, invista em exemplos cuidadosamente curados antes de tentar soluções de pós-processamento. É mais efetivo ensinar o modelo a fazer certo na primeira vez do que consertar depois.

---
### SIMPLE EXPLANATION

O que está acontecendo:

O sistema gera relatórios sobre problemas em documentos. Os relatórios têm a estrutura certa (passam na validação), mas o conteúdo é bagunçado: uns dizem "problema de data" sem explicar qual data, outros dão sugestões incompletas. Os revisores perdem tempo tentando entender o que cada relatório quer dizer.

Por que a alternativa C é a melhor:

C diz: "Mostre exemplos prontos de como um bom relatório deve ser." É como dar um modelo de redação pronto — o aluno (Claude) copia o formato, o nível de detalhe e a estrutura. Muito mais efetivo que apenas dizer "seja mais claro".

Por que as outras não funcionam:

**A)** Forçar campos obrigatórios — o modelo preenche qualquer coisa para não falhar, mas continua sendo conteúdo ruim.

**B)** Pedir para "evitar notas vagas" — subjetivo. O modelo não sabe exatamente o que é "vago" para você.

**D)** Usar regex para adivinhar informações faltando — frágil e não resolve a inconsistência na origem.

Lembrar: **Quer saída consistente? Dê exemplos consistentes.** Modelos aprendem mais vendo do que ouvindo instruções.

---
### CORRECT ANSWER

Alternativa Correta: C
