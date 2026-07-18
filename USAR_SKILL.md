# Como Usar a Skill /gerar-cards-enriquecidos

## Resumo Rápido

Quando você tiver novas fotos e quiser criar flashcards enriquecidos:

```
1. Coloque as fotos no diretório (não importa o nome)
2. Digite: /gerar-cards-enriquecidos
3. Claude vai fazer o resto automaticamente
```

## Fluxo Completo

### Passo 1: Preparar Fotos
- Tire as screenshots das perguntas
- Coloque-as no diretório `/Users/fabioalvaropereira/Desktop/desafio-fotos/`
- Os nomes não importam - podem ser Screenshots padrão do macOS ou qualquer outro formato

### Passo 2: Chamar a Skill
```
/gerar-cards-enriquecidos
```


### Passo 4: Outputs Gerados
A skill cria automaticamente:

**Card simples** (`NNN-card.md`):
- Pergunta e opções em inglês
- Pronto para processar

**Card enriquecido** (`NNN-enriched-card.md`):
- Tradução para português
- Explicação técnica detalhada
- Análise de cada opção
- Dica sobre o padrão
- Resposta correta indicada

## Exemplo de Uso

```
$ /gerar-cards-enriquecidos

✅ Renomeando fotos encontradas:
   - Screenshot 2026-07-18 at 08.46.16.png → foto-001.png
   - Screenshot 2026-07-18 at 08.46.21.png → foto-002.png
   - Screenshot 2026-07-18 at 08.46.31.png → foto-003.png

✅ Processando 3 fotos...

[Claude lê foto-001.png]

📸 Foto 001:
Pergunta: "Você está construindo ferramentas de produtividade..."
Opções: A, B, C, D

Qual é a resposta correta? (A/B/C/D): D

✅ Criados:
   - 001-card.md
   - 001-enriched-card.md

[Repete para foto-002.png, foto-003.png...]

✨ Pronto! 3 cards criados com sucesso!
```

## Checklist para Próximas Vezes

- [ ] Capturei as fotos/screenshots das perguntas
- [ ] Coloquei as fotos no diretório (não precisa renomear, a skill cuida disso)
- [ ] Digitei `/gerar-cards-enriquecidos`
- [ ] A skill renomeou automaticamente para foto-001.png, foto-002.png, etc.
- [ ] Respondi as perguntas do Claude (qual é a resposta correta para cada foto)
- [ ] Verifiquei os outputs (_card.md e _enriched-card.md)
- [ ] Revisei a tradução e explicação se necessário
