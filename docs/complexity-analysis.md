# Análise de Complexidade

Este documento apresenta a análise de complexidade dos principais algoritmos e estruturas de dados utilizados no projeto **Support Desk CLI**.

O objetivo é compreender a eficiência das operações implementadas, considerando seu custo computacional e as características das estruturas escolhidas.

---

## 1. Complexidade de Consulta por ID

**Pergunta:** Qual é a complexidade de tempo esperada para localizar um chamado pelo ID utilizando a estrutura escolhida?

**Resposta: `O(1)` — Tempo constante, em média.**

Os chamados são armazenados em um dicionário Python (`dict`), que utiliza uma **tabela hash** para organizar e localizar seus elementos.

Essa estrutura permite acessar diretamente os valores associados a uma chave, sem a necessidade de percorrer sequencialmente todos os registros.

**Exemplo:**

```python
chamados[id]
```

Dessa forma, a consulta possui complexidade média de **O(1)**, independentemente da quantidade de chamados armazenados.

> **Observação:** Em situações excepcionais de colisões de hash, a complexidade pode chegar a O(n) no pior caso.

---

## 2. Complexidade de Remoção da Fila

**Pergunta:** Qual é a complexidade de tempo da operação utilizada para retirar o primeiro chamado da fila?

**Resposta: `O(1)` — Tempo constante.**

A fila de atendimento foi implementada utilizando `deque`, disponibilizado pelo módulo `collections` do Python.

Para remover o primeiro chamado, utiliza-se o método:

```python
fila_atendimento.popleft()
```

O `deque` foi desenvolvido para permitir inserções e remoções eficientes em ambas as extremidades da estrutura.

Diferentemente da operação `pop(0)` em uma lista convencional, o método `popleft()` não exige o deslocamento de todos os elementos restantes.

Por esse motivo, a remoção do primeiro elemento possui complexidade **O(1)**.

---

## 3. Estrutura Utilizada para Desfazer Atendimentos

**Pergunta:** Qual princípio de estrutura de dados foi utilizado para implementar o desfazimento de atendimentos?

**Resposta: LIFO — Last In, First Out.**

O sistema utiliza uma **pilha (Stack)** para armazenar o histórico dos atendimentos realizados.

O princípio LIFO estabelece que o último elemento inserido será o primeiro a ser removido.

Na implementação, uma lista Python é utilizada para representar a pilha.

**Registro de um atendimento:**

```python
historico_atendimento.append(id)
```

**Remoção do último atendimento:**

```python
historico_atendimento.pop()
```

Essa abordagem permite identificar e desfazer o atendimento realizado mais recentemente.

Ao desfazer a operação, o chamado retorna ao status `Pendente` e é reinserido no início da fila de atendimento.

O princípio LIFO é adequado porque garante que os atendimentos sejam desfeitos na ordem inversa àquela em que foram realizados.

---

## 4. Complexidade do Algoritmo de Ordenação

**Pergunta:** Qual é a complexidade de tempo no pior caso da ordenação nativa do Python para uma coleção com `n` elementos?

**Resposta: `O(n log n)` — Tempo linearítmico.**

O Python utiliza um algoritmo de ordenação chamado **Timsort**, que combina características dos algoritmos Merge Sort e Insertion Sort.

O Timsort é projetado para aproveitar sequências de elementos que já estejam parcialmente ordenadas, tornando a ordenação eficiente em diferentes cenários.

No projeto, a ordenação é realizada utilizando a função `sorted()`:

```python
chamados_ordenados = sorted(
    chamados.items(),
    key=lambda item: item[1]["titulo"]
)
```

A complexidade de tempo no pior caso é **O(n log n)**, em que `n` representa a quantidade de chamados.

Essa complexidade garante um limite superior de crescimento do tempo de execução, mesmo quando os elementos estão inicialmente desordenados.

---

## 5. Justificativa da Escolha das Estruturas de Dados

**Pergunta:** Explique por que você escolheu as estruturas de dados utilizadas para armazenar chamados, controlar atendimentos e permitir operações de desfazer.

### 5.1. Dicionário (`dict`)

O dicionário foi escolhido para armazenar todos os chamados cadastrados, associando cada identificador único às informações correspondentes.

Essa estrutura funciona como um armazenamento de registros em memória, permitindo consultas eficientes por meio de suas chaves.

### 5.2. Fila (`deque`)

A fila foi escolhida para organizar os chamados pendentes de acordo com o princípio **FIFO (First In, First Out)**.

Isso garante que o primeiro chamado a entrar na fila seja o primeiro a ser atendido, respeitando a ordem de chegada das solicitações.

A implementação com `deque` também proporciona eficiência nas operações de inserção e remoção.

### 5.3. Pilha (`list`)

A pilha foi escolhida para armazenar o histórico de atendimentos e possibilitar o desfazimento de operações.

Utilizando o princípio **LIFO (Last In, First Out)**, o último atendimento registrado é o primeiro a ser desfeito.

Essa característica torna a pilha apropriada para implementar funcionalidades de reversão de operações.

---

## 6. Resumo das Complexidades

| Operação | Estrutura | Complexidade de Tempo |
|---|---|---|
| Consultar chamado por ID | Dicionário (`dict`) | O(1) — Médio |
| Gerar novo ID com `max()` | Dicionário (`dict`) | O(n) |
| Adicionar chamado à fila | Fila (`deque`) | O(1) |
| Remover primeiro chamado | Fila (`deque`) | O(1) |
| Registrar atendimento | Pilha (`list`) | O(1) — Amortizado |
| Remover último atendimento | Pilha (`list`) | O(1) |
| Ordenar chamados | `sorted()` | O(n log n) — Pior caso |

**Legenda:**

- **O(1):** Tempo constante.
- **O(n):** Tempo linear.
- **O(n log n):** Tempo linearítmico.

---

## Conclusão

A escolha das estruturas de dados teve como objetivo equilibrar **simplicidade de implementação, organização do código e eficiência das operações**.

O uso de dicionários, filas e pilhas permitiu aplicar diferentes conceitos de estruturas de dados em um mesmo sistema, respeitando os princípios FIFO e LIFO.

A análise de complexidade também possibilitou compreender como as decisões de implementação influenciam o desempenho dos algoritmos.

Esses conhecimentos representam uma parte fundamental do desenvolvimento de software e da construção de aplicações eficientes.

---

**Projeto:** Support Desk CLI  
**Etapa:** Fase 0 — Fundamentos de Programação e Estruturas de Dados