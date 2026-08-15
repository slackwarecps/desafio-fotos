

Your agent needs to insert a new helper function into the middle of a 150-line utility module, between two existing functions. The Edit tool fails because its `old_string` parameter cannot find unique text to match — the file has repetitive docstrings, variable names, and structural patterns. What's the most reliable way to complete this insertion?

---

[ ] A - Use Edit with an extremely long `old_string` capturing 30+ lines of context to guarantee uniqueness
[ ] B - Use Edit's `replace_all` parameter to target a common pattern and embed the new function in the replacement text
[ ] C - Use Bash to append the function definition to the end of the file using heredoc syntax
[ ] D - Use Read to load the file, add the function at the appropriate location, then Write the updated file

---

### TRANSLATED QUESTION
{pergunta traduzida}

{alternativas traduzidas}
---

### EXPLANATION (TECH LEAD)

Explicação:
A pergunta está testando o entendimento de quando usar plan mode versus execução direta em fluxos de trabalho agentic com o Claude Agent SDK — um dos temas centrais da certificação.
O sinal-chave no enunciado é: "o ponto inicial de implementação é incerto" + "comportamento espalhado entre múltiplos lugares" + "em tarefas anteriores, edições imediatas erraram a abstração e tiveram que ser revertidas". Isso é literalmente a definição de um problema com alta incerteza estrutural: você não sabe onde a lógica de cancelamento realmente vive nem como os componentes se relacionam antes de tocar no código.
Por que a alternativa D é a correta:
O plan mode existe exatamente para esse cenário: antes de qualquer edição, o agente investiga (lê, busca, mapeia relações) e produz um plano que pode ser revisado por um humano — sem risco de side effects, porque nenhuma escrita acontece ainda. Isso permite comparar os candidatos a "ponto de implementação" (script CLI, handler web, job agendado) e decidir com base em evidência, não em suposição. Dado o histórico de retrabalho por abstrações erradas, investir em mapeamento antes de editar é a escolha que reduz risco e retrabalho.
Por que as outras estão erradas:

A) Ler todo o repositório é ineficiente e não resolve o problema real, que não é falta de leitura, mas falta de um plano estruturado de comparação entre pontos de implementação. Além disso, fazer a leitura e a implementação "na mesma sessão estendida" reintroduz o risco de editar antes de entender a relação entre os módulos — é uma falsa sensação de "pesquisa" sem a disciplina do plan mode.
B) É exatamente o padrão que já falhou antes ("early similar tasks" tiveram que ser revertidas). Confiar em falhas de teste para revelar dependências ocultas é reativo, caro e já provou não funcionar nesse contexto específico.
C) Paralelizar sessões de execução direta por módulo suspeito ainda assume que você já sabe quais são os módulos certos — e ainda gera o problema extra de reconciliar manualmente edições feitas às cegas em paralelo. É uma variação do erro de B, só que distribuída.

Dica importante: Um padrão recorrente nas perguntas da certificação é: incerteza sobre escopo/impacto + histórico de retrabalho por escrita prematura → plan mode. Sempre que o enunciado mencionar "não está claro onde", "comportamento espalhado" ou "já tivemos que reverter", isso é o sinal para investigação/planejamento antes de execução.

---