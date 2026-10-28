# Explicação da Implementação

Este documento apresenta a organização do código, as estruturas de dados utilizadas e as principais decisões técnicas tomadas durante o desenvolvimento do projeto **Support Desk CLI**.

O objetivo é explicar como os componentes do sistema foram organizados para implementar as funcionalidades de gerenciamento de chamados técnicos.

---

## 1. Estruturas de Dados Utilizadas

Inicialmente, foram selecionadas três estruturas de dados fundamentais para organizar o armazenamento e o processamento dos chamados.

| Estrutura | Implementação | Responsabilidade |
|---|---|---|
| Dicionário | `dict` | Armazenar os dados dos chamados cadastrados |
| Fila | `collections.deque` | Controlar os chamados pendentes utilizando FIFO |
| Pilha | `list` | Registrar o histórico de atendimentos utilizando LIFO |

### 1.1. Dicionário

O dicionário foi escolhido para armazenar os chamados cadastrados, utilizando o **ID como chave** e os demais atributos como valores.

Cada chamado possui um título e um status, que pode ser `Pendente` ou `Atendido`.

```python
chamados = {}
```

Essa estrutura permite consultar e atualizar os registros de maneira eficiente, funcionando como um armazenamento de dados em memória.

### 1.2. Fila

A fila de atendimento foi implementada utilizando `deque`, disponível no módulo `collections`.

```python
from collections import deque

fila_atendimento = deque()
```

Sua finalidade é organizar os chamados pendentes seguindo o princípio **FIFO (First In, First Out)**.

Dessa forma, o primeiro chamado cadastrado será o primeiro a ser atendido, respeitando a ordem de chegada.

### 1.3. Pilha

A pilha foi implementada utilizando uma lista Python.

```python
historico_atendimento = []
```

Essa estrutura armazena os IDs dos chamados atendidos e permite desfazer operações utilizando o princípio **LIFO (Last In, First Out)**.

Assim, o último atendimento realizado será o primeiro a ser desfeito.

---

## 2. Organização do Código

O programa foi organizado em funções para separar as principais operações e facilitar a leitura, manutenção e compreensão do código.

Cada função possui uma finalidade específica dentro do funcionamento do sistema.

### 2.1. Funções Auxiliares

| Função | Responsabilidade |
|---|---|
| `clear_screen()` | Limpar o terminal para melhorar a apresentação das informações |
| `show_menu()` | Exibir as opções disponíveis no menu principal |

A função `clear_screen()` utiliza o módulo `os` para executar o comando de limpeza adequado ao sistema operacional.

Já a função `show_menu()` centraliza a apresentação das opções, evitando a repetição de instruções `print()` dentro da função principal.

### 2.2. Funções de Gerenciamento

As funcionalidades do sistema foram divididas nas seguintes funções:

| Função | Responsabilidade |
|---|---|
| `abrir_novo_chamado()` | Cadastrar um chamado e adicioná-lo à fila |
| `atender_proximo_chamado()` | Processar o primeiro chamado pendente |
| `consultar_chamado_por_id()` | Localizar e exibir um chamado pelo ID |
| `desfazer_ultimo_atendimento()` | Reverter o atendimento mais recente |
| `exibir_fila_atendimento()` | Exibir os chamados pendentes |
| `listar_chamados_ordenados()` | Listar os chamados em ordem alfabética |
| `exibir_estatisticas()` | Apresentar as estatísticas dos chamados |

Essa divisão permite que as operações sejam implementadas e compreendidas separadamente, sem concentrar toda a lógica do programa em uma única função.

---

## 3. Fluxo de Funcionamento

O funcionamento da aplicação pode ser dividido em quatro etapas principais.

### 3.1. Cadastro

Ao cadastrar um chamado, o sistema:

1. Solicita o título do problema.
2. Valida a entrada informada.
3. Gera automaticamente um identificador único.
4. Armazena os dados no dicionário.
5. Adiciona o ID ao final da fila de atendimento.

O chamado recebe inicialmente o status `Pendente`.

### 3.2. Atendimento

Quando o usuário solicita o atendimento do próximo chamado:

1. O sistema verifica se existem chamados pendentes.
2. Seleciona o primeiro ID da fila.
3. Atualiza seu status para `Atendido`.
4. Registra o ID na pilha de histórico.
5. Remove o chamado da fila.

Essa implementação garante que os atendimentos respeitem o princípio FIFO.

### 3.3. Desfazer Atendimento

Quando o usuário deseja desfazer um atendimento:

1. O sistema verifica se existe algum atendimento registrado no histórico.
2. Identifica o último chamado atendido.
3. Solicita a confirmação do usuário.
4. Atualiza o status do chamado para `Pendente`.
5. Reinsere o chamado no início da fila.
6. Remove o registro correspondente da pilha.

O uso da pilha garante que os atendimentos sejam desfeitos seguindo o princípio LIFO.

### 3.4. Consulta e Visualização

O sistema também permite consultar os registros armazenados.

As informações podem ser visualizadas por meio de:

- **Consulta por ID:** acesso direto às informações de um chamado.
- **Fila de atendimento:** apresentação dos chamados pendentes na ordem de processamento.
- **Listagem ordenada:** exibição de todos os chamados em ordem alfabética.
- **Estatísticas:** apresentação das quantidades de chamados cadastrados, pendentes e atendidos.

---

## 4. Função Principal (`main`)

A função `main()` é responsável por controlar o fluxo principal da aplicação.

Sua implementação utiliza um **laço de repetição** para manter o programa em funcionamento até que o usuário escolha encerrá-lo.

Dentro desse laço, estruturas condicionais (`if`, `elif` e `else`) identificam a opção selecionada e executam a função correspondente.

O fluxo principal segue a seguinte sequência:

1. Limpar o terminal.
2. Exibir o menu principal.
3. Solicitar uma opção ao usuário.
4. Validar a entrada.
5. Executar a funcionalidade selecionada.
6. Retornar ao menu principal ou encerrar a aplicação.

Essa abordagem centraliza o controle de navegação na função `main()`, enquanto as demais funções executam as operações específicas do sistema.

---

## 5. Decisões de Implementação

Durante o desenvolvimento, algumas decisões foram tomadas para manter o projeto simples, organizado e adequado aos objetivos educacionais.

### 5.1. Modularização por Funções

O programa foi dividido em funções para evitar a concentração de todas as operações em um único bloco de código.

Essa organização facilita a leitura e a identificação das responsabilidades de cada parte do sistema.

Embora exista uma separação funcional, algumas funções ainda concentram tanto a **lógica de negócio** quanto a **interação com o usuário**.

Portanto, a implementação apresenta uma modularização básica, mas não aplica integralmente o **Princípio da Responsabilidade Única (SRP)**.

Para o escopo educacional do projeto, essa abordagem foi considerada suficiente.

### 5.2. Armazenamento em Memória

Os chamados são armazenados diretamente nas estruturas de dados do Python, sem utilizar arquivos ou bancos de dados.

Essa decisão permite concentrar o desenvolvimento na aplicação dos conceitos de estruturas de dados.

Como consequência, os registros são perdidos quando o programa é encerrado.

### 5.3. Geração Automática de IDs

A geração dos identificadores utiliza a função `max()` para localizar o maior ID existente e incrementar seu valor.

```python
id = max(chamados.keys()) + 1 if chamados else 1
```

Essa abordagem foi escolhida pela simplicidade de implementação.

Embora apresente complexidade de tempo O(n), seu desempenho foi considerado adequado ao escopo do projeto.

### 5.4. Utilização da Biblioteca Padrão

O projeto utiliza exclusivamente recursos da biblioteca padrão do Python.

A escolha de `collections.deque` permite implementar a fila de maneira eficiente, sem necessidade de desenvolver manualmente uma estrutura de dados.

Além disso, a utilização de `dict` e `list` simplifica o armazenamento e o gerenciamento dos registros.

---

## 6. Conclusão

A implementação do **Support Desk CLI** permitiu integrar diferentes estruturas de dados em uma aplicação funcional de gerenciamento de chamados técnicos.

A divisão do programa em funções contribuiu para a organização do código, enquanto a utilização de dicionários, filas e pilhas possibilitou aplicar os princípios de armazenamento, FIFO e LIFO.

O projeto também proporcionou a aplicação prática de conceitos como estruturas condicionais, laços de repetição, validação de entradas e análise de complexidade.

As decisões de implementação priorizaram a **simplicidade, a clareza do código e a consolidação dos fundamentos de programação**, atendendo aos objetivos estabelecidos para o desafio.

---

**Projeto:** Support Desk CLI  
**Etapa:** Fase 0 — Fundamentos de Programação e Estruturas de Dados