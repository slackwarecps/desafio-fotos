---
name: limpar-ultima-execucao
description: Remove os PDFs e cards gerados na pasta outputs deste projeto, somente após confirmação explícita do solicitante respondendo exatamente Y.
---

# Limpar última execução

Remove os artefatos gerados pela última execução do projeto.

## Confirmação obrigatória

Antes de executar qualquer comando de remoção, peça confirmação explícita ao solicitante com esta mensagem, adaptando apenas o número de arquivos se necessário:

> Esta ação removerá todos os arquivos PDF e cards Markdown encontrados em `outputs/`. A remoção não será desfeita. Responda `Y` para confirmar ou qualquer outra coisa para cancelar.

Só prossiga se a resposta, depois de remover espaços externos, for exatamente `Y` (maiúsculo). Qualquer outra resposta cancela a operação sem alterar arquivos.

## Escopo da limpeza

1. Trabalhe exclusivamente a partir da raiz deste repositório.
2. Verifique se `outputs/` existe. Se não existir, informe que nada foi removido e encerre.
3. Liste antes os alvos que serão removidos:
   - arquivos com extensão `.pdf` em qualquer nível dentro de `outputs/`;
   - cards Markdown em qualquer nível dentro de `outputs/`, identificados por nomes terminados em `-card.md` ou `-enriched-card.md`.
4. Não remova diretórios, arquivos `.DS_Store`, logs, imagens, arquivos Markdown que não sejam cards ou qualquer item fora de `outputs/`.
5. Após a confirmação `Y`, remova somente os caminhos previamente listados, usando caminhos explícitos e validados.
6. Confira o resultado e informe quantos PDFs e cards foram removidos. Se não houver alvos, informe que a pasta já estava limpa.
7. Apague todas as linhas do arquivo desafio.log na raiz do projeto;

## Regras de segurança

- Nunca peça confirmação depois de iniciar a remoção; ela deve ocorrer antes de qualquer alteração.
- Nunca interprete `y`, `yes`, `sim` ou uma frase contendo `Y` como confirmação; aceite somente `Y` isolado.
- Se a confirmação não for recebida, estiver ambígua ou a listagem mudar antes da remoção, cancele e não remova nada.
- Não use comandos destrutivos amplos como `rm -rf outputs`.

## Resumo esperado

Ao concluir, apresente:

- confirmação de cancelamento, se a resposta não foi exatamente `Y`; ou
- quantidade de PDFs removidos;
- quantidade de cards removidos;
- indicação de que os demais arquivos de `outputs/` foram preservados.
