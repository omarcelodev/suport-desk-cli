# Desafio Final Integrador
## Fase 0 — Fundamentos de Programação e Estruturas de Dados

**Curso:** Engenharia de Software

**Aluno:** Marcelo Gomes de Freitas Filho

**Linguagem:** Python

**Modalidade:** Projeto prático individual

---

# 1. Apresentação do Projeto

## Central de Gerenciamento de Chamados Técnicos

Uma empresa de tecnologia deseja desenvolver um sistema simples para organizar os chamados recebidos pela sua equipe de suporte técnico.

Atualmente, os atendimentos são controlados manualmente, dificultando a organização das solicitações.

A empresa precisa de um programa que permita registrar novos chamados, organizar uma fila de atendimento, consultar informações e acompanhar os atendimentos realizados.

O sistema também deverá permitir desfazer o último atendimento, caso um técnico realize a operação por engano.

O programa será desenvolvido em Python e executado diretamente pelo terminal.

**Objetivo principal:** Aplicar os fundamentos de programação, estruturas de dados e análise de algoritmos em um programa funcional.

---

# 2. Requisitos Gerais

O sistema deverá apresentar um menu interativo por meio do terminal.

O usuário poderá selecionar as operações disponíveis digitando a opção desejada.

Após executar uma operação, o programa deverá retornar ao menu principal, permitindo novas ações.

O programa deverá continuar funcionando até que o usuário escolha a opção de encerramento.

### Menu obrigatório

```text
================================
   CENTRAL DE SUPORTE TÉCNICO
================================

1 - Abrir novo chamado
2 - Atender próximo chamado
3 - Consultar chamado por ID
4 - Desfazer último atendimento
5 - Exibir fila de atendimento
6 - Listar chamados ordenados
7 - Exibir estatísticas
0 - Encerrar sistema

Escolha uma opção:
```

A aparência do menu poderá ser personalizada, desde que todas as operações obrigatórias estejam disponíveis.

---

# 3. Requisitos Funcionais

## RF01 — Abrir Novo Chamado

O programa deverá permitir o cadastro de novos chamados.

Cada chamado deverá possuir três informações:

- ID: identificador numérico único, gerado automaticamente.
- Título: descrição curta do problema.
- Status: situação atual do chamado.

Os status permitidos serão:

- `Pendente`
- `Atendido`

**Regras de funcionamento:**

1. O primeiro chamado deverá receber o ID 1.
2. Cada novo chamado deverá receber o próximo ID disponível.
3. Um ID não poderá ser reutilizado durante a execução.
4. Todo chamado deverá ser criado com status `Pendente`.
5. O título não poderá estar vazio.
6. O chamado deverá entrar no final da fila de atendimento.

Exemplo ilustrativo:

```text
Informe o título:
Computador não liga

Chamado #1 cadastrado!
Status: Pendente
```

## RF02 — Atender Próximo Chamado

O sistema deverá permitir atender o próximo chamado da fila.

**Regras de funcionamento:**

1. O atendimento deverá respeitar a ordem de chegada (FIFO).
2. O primeiro chamado pendente deverá ser selecionado.
3. O chamado atendido deverá sair da fila.
4. Seu status deverá ser atualizado para `Atendido`.
5. O programa deverá informar qual chamado foi atendido.
6. O atendimento deverá ser registrado para permitir seu posterior desfazimento.
7. Caso a fila esteja vazia, o sistema deverá informar que não existem chamados aguardando.

**Importante:** Atender um chamado não significa excluir seu registro. Ele continuará disponível para consulta.

## RF03 — Consultar Chamado por ID

O programa deverá permitir localizar um chamado utilizando seu identificador.

O usuário informará um ID, e o sistema deverá apresentar:

- ID.
- Título.
- Status atual.

Caso não exista um chamado com o identificador informado, o programa deverá apresentar uma mensagem informando que ele não foi encontrado.

## RF04 — Desfazer Último Atendimento

O sistema deverá permitir desfazer o atendimento realizado mais recentemente.

Essa funcionalidade deverá utilizar o princípio LIFO.

**Regras de funcionamento:**

1. Apenas atendimentos poderão ser desfeitos.
2. O sistema deverá identificar o último chamado atendido que ainda não teve seu atendimento desfeito.
3. O status desse chamado deverá voltar para `Pendente`.
4. O chamado deverá retornar ao início da fila de atendimento.
5. Se o usuário desfizer dois atendimentos consecutivos, deverá desfazer primeiro o mais recente e depois o anterior.
6. Caso não exista nenhum atendimento disponível para desfazer, o programa deverá informar isso.

**Observação:** Para manter o desafio simples, não será necessário desfazer cadastros ou outras operações.

## RF05 — Exibir Fila de Atendimento

O programa deverá listar todos os chamados que continuam aguardando atendimento.

A apresentação deverá respeitar a ordem FIFO.

Para cada chamado, deverão ser apresentados:

- ID.
- Título.

Chamados já atendidos não deverão aparecer nessa listagem.

Caso a fila esteja vazia, o programa deverá informar que não existem chamados pendentes.

## RF06 — Listar Chamados Ordenados

O sistema deverá permitir visualizar todos os chamados cadastrados, incluindo pendentes e atendidos.

A listagem deverá apresentar:

- ID.
- Título.
- Status.

Os chamados deverão ser exibidos em ordem alfabética crescente pelo título, utilizando os recursos de ordenação do Python.

**Regras:**

1. Não é obrigatório implementar manualmente um algoritmo de ordenação.
2. É permitido utilizar `sorted()` ou `.sort()`.
3. A ordenação não deverá modificar a ordem da fila de atendimento.
4. A listagem deverá incluir todos os chamados registrados.

## RF07 — Exibir Estatísticas

O programa deverá apresentar um resumo dos chamados cadastrados.

As informações obrigatórias serão:

- Quantidade total de chamados cadastrados.
- Quantidade de chamados pendentes.
- Quantidade de chamados atendidos.

As estatísticas deverão refletir o estado atual do sistema, inclusive após o desfazimento de atendimentos.

---

# 4. Estruturas de Dados Obrigatórias

O projeto deverá utilizar as seguintes estruturas:

| Estrutura | Conceito que deverá demonstrar |
|---|---|
| Lista | Organização ou processamento de elementos |
| Pilha | Operações LIFO |
| Fila | Operações FIFO |
| Dicionário | Associação entre chaves e valores |
| Ordenação | Organização de elementos por critério |

O estudante deverá decidir como organizar essas estruturas em seu programa.

É permitido utilizar recursos da biblioteca padrão do Python, incluindo `collections`.

Não será necessário implementar manualmente pilhas, filas ou tabelas hash.

---

# 5. Requisitos Técnicos

O programa deverá:

1. Ser desenvolvido em Python.
2. Utilizar funções para organizar as principais operações.
3. Utilizar estruturas condicionais para controlar o fluxo do sistema.
4. Utilizar laços de repetição quando necessário.
5. Permitir a execução contínua do menu até o encerramento.
6. Tratar entradas inválidas sem encerrar inesperadamente o programa.
7. Evitar o acesso a elementos inexistentes em listas ou filas vazias.
8. Utilizar nomes de variáveis e funções que facilitem a leitura do código.

**Não será necessário:**

- Criar interfaces gráficas.
- Utilizar programação orientada a objetos.
- Conectar bancos de dados.
- Desenvolver APIs.
- Implementar autenticação.
- Utilizar Docker ou serviços de nuvem.
- Criar testes automatizados com frameworks.
- Salvar dados permanentemente em arquivos.

Os dados poderão permanecer somente na memória durante a execução.

Ao encerrar o programa, os registros poderão ser perdidos.

---

# 6. Cenários Obrigatórios de Teste

Após implementar as funcionalidades, o estudante deverá executar os seguintes testes.

## Teste 01 — Cadastro

1. Inicie o programa.
2. Cadastre três chamados.
3. Consulte cada um deles pelo ID.

**Resultado esperado:** Os três chamados deverão possuir IDs diferentes, títulos correspondentes aos cadastrados e status `Pendente`.

## Teste 02 — Atendimento FIFO

1. Cadastre três chamados, nesta ordem: Impressora, Internet e Monitor.
2. Execute a operação de atendimento duas vezes.
3. Consulte a fila de atendimento.

**Resultado esperado:** Os chamados Impressora e Internet deverão estar atendidos, e Monitor deverá ser o primeiro da fila.

## Teste 03 — Desfazer Atendimento

1. Partindo de três chamados cadastrados, atenda os dois primeiros.
2. Utilize a funcionalidade de desfazer uma vez.
3. Consulte o chamado restaurado e a fila.

**Resultado esperado:** O segundo chamado atendido deverá voltar ao status `Pendente` e ocupar o início da fila.

## Teste 04 — Ordenação

1. Cadastre chamados com os títulos Zebra, Computador e Adaptador.
2. Utilize a opção de listagem ordenada.

**Resultado esperado:** Os chamados deverão aparecer em ordem alfabética crescente pelo título, sem que a ordem da fila de atendimento seja alterada.

## Teste 05 — Entradas Inválidas

Verifique o comportamento do programa nas seguintes situações:

- Tentar atender quando a fila estiver vazia.
- Tentar desfazer quando não houver atendimentos disponíveis.
- Consultar um ID inexistente.
- Selecionar uma opção inexistente no menu.
- Informar um ID com caracteres não numéricos.
- Tentar cadastrar um chamado com título vazio.

**Resultado esperado:** O programa deverá apresentar mensagens apropriadas e continuar funcionando, sem encerrar inesperadamente.

---

# 7. Análise de Complexidade

Após concluir o código, o estudante deverá responder às seguintes questões.

### Questão A — Consulta

Qual é a complexidade de tempo esperada para localizar um chamado pelo ID utilizando a estrutura escolhida?

Explique sua resposta.

### Questão B — Atendimento

Qual é a complexidade de tempo da operação utilizada para retirar o primeiro chamado da fila?

Explique por que essa operação é adequada.

### Questão C — Desfazer

Qual princípio de estrutura de dados foi utilizado para implementar o desfazimento de atendimentos?

Por que esse princípio é apropriado?

### Questão D — Ordenação

Qual é a complexidade de tempo no pior caso da ordenação nativa do Python para uma coleção com `n` elementos?

Explique brevemente sua resposta.

### Questão E — Escolha das Estruturas

Explique por que você escolheu as estruturas de dados utilizadas para armazenar chamados, controlar atendimentos e permitir operações de desfazer.

---

# 8. Entregáveis

Para concluir o desafio, deverão ser apresentados:

**1. Código-fonte**

O programa Python completo e funcional.

O código poderá estar organizado em um arquivo `main.py` ou em mais de um arquivo, caso o estudante considere necessário.

**2. Testes manuais**

Uma breve descrição dos resultados obtidos nos cinco cenários obrigatórios.

**3. Análise de complexidade**

As respostas às cinco questões da seção anterior.

**4. Explicação da implementação**

Uma explicação breve sobre a organização geral do programa e as principais decisões tomadas.

---

# 9. Critérios de Avaliação

| Critério | Pontuação |
|---|---:|
| Funcionamento das operações obrigatórias | 4,0 |
| Utilização correta das estruturas de dados | 2,0 |
| Tratamento de entradas e situações inválidas | 1,0 |
| Clareza e organização do código | 1,0 |
| Análise de complexidade e justificativas | 2,0 |
| **Total** | **10,0** |

A avaliação considerará principalmente o funcionamento do sistema e a compreensão dos fundamentos.

Não será exigido código profissional ou arquitetura avançada.

Eventuais erros serão analisados individualmente, permitindo correções.

---

# 10. Conclusão da Fase 0

A conclusão deste projeto demonstrará que o estudante consegue reunir conhecimentos fundamentais de programação em uma aplicação funcional.

As habilidades avaliadas incluem:

- Variáveis, condicionais, funções e laços.
- Manipulação de coleções.
- Utilização de listas.
- Aplicação do princípio LIFO.
- Aplicação do princípio FIFO.
- Utilização de dicionários e pares chave-valor.
- Ordenação de dados.
- Análise básica de complexidade.
- Tratamento de situações excepcionais simples.
- Organização de um programa em funções.

**Após a avaliação e aprovação do desafio, a Fase 0 do roadmap será considerada concluída.**

A próxima etapa será:

**Fase 1 — Programação Orientada a Objetos e Banco de Dados**, com foco inicial em SQL, modelagem relacional, PostgreSQL e integração com Java.

---

**Fim do Desafio Final Integrador — Fase 0**