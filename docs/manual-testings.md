# Resultados dos Testes Manuais

## Teste 01 — Cadastro 

1. Inicie o programa.
2. Cadastre três chamados.
3. Consulte cada um deles pelo ID.

**Resultado esperado:** Os três chamados deverão possuir IDs diferentes, títulos correspondentes aos cadastrados e status `Pendente`.
**Resultados:** Foram cadastrados os chamados `Impressora`, `Internet`, `Computador`, todos com ID's diferentes e status `Pendente`.

## Teste 02 — Atendimento FIFO

1. Cadastre três chamados, nesta ordem: Impressora, Internet e Monitor.
2. Execute a operação de atendimento duas vezes.
3. Consulte a fila de atendimento.

**Resultado esperado:** Os chamados Impressora e Internet deverão estar atendidos, e Monitor deverá ser o primeiro da fila.
**Resultados:** Os três chamados foram cadastrados e ao atender os dois primeiros somente o `Monitor` constava na fila de atendimento

## Teste 03 — Desfazer Atendimento

1. Partindo de três chamados cadastrados, atenda os dois primeiros.
2. Utilize a funcionalidade de desfazer uma vez.
3. Consulte o chamado restaurado e a fila.

**Resultado esperado:** O segundo chamado atendido deverá voltar ao status `Pendente` e ocupar o início da fila.
**Resultados:**  Ao realizar a função de desfazer o chamado atendindo, O segundo chamado voltou ao ínicio da fila e seus status no dicionário voltou a ser `Pendente`

## Teste 04 — Ordenação

1. Cadastre chamados com os títulos Zebra, Computador e Adaptador.
2. Utilize a opção de listagem ordenada.

**Resultado esperado:** Os chamados deverão aparecer em ordem alfabética crescente pelo título, sem que a ordem da fila de atendimento seja alterada.
**Resultados:** Após o cadastado de chamados, a opção de listagem ordenada exibiu os chamados na seguinte ordem: `Adaptador`. `Computador`, `Zebra`, com seus respectivos ID's e Status

## Teste 05 — Entradas Inválidas

Verifique o comportamento do programa nas seguintes situações:

- Tentar atender quando a fila estiver vazia.
- Tentar desfazer quando não houver atendimentos disponíveis.
- Consultar um ID inexistente.
- Selecionar uma opção inexistente no menu.
- Informar um ID com caracteres não numéricos.
- Tentar cadastrar um chamado com título vazio.

**Resultado esperado:** O programa deverá apresentar mensagens apropriadas e continuar funcionando, sem encerrar inesperadamente.
**Resultados:** Todos esses cenátios passaram no teste, o programa não encerra inesperadamente(ou quebra). O programa sempre avisa o usuário de uma falha de execução e retorna pro ponto de entrada.
