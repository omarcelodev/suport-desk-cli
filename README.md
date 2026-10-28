# Support Desk CLI

### Technical Support Ticket Management System

A command-line application (CLI) developed in **Python** to manage technical support tickets.

This project was created as the final challenge of **Phase 0 — Programming Fundamentals and Data Structures**, with the goal of applying fundamental programming concepts to build a functional application.

The system allows users to create tickets, manage a support queue, search for records, undo completed operations, and view statistics using different data structures.

---

## Features

The application provides the following features:

- **Ticket Creation:** Register new support tickets with a unique ID, title, and status.
- **Ticket Processing:** Handle support requests following the First In, First Out (FIFO) principle.
- **Ticket Search:** Retrieve ticket information using its unique identifier.
- **Undo Operations:** Reverse the most recently completed ticket using the Last In, First Out (LIFO) principle.
- **Queue Management:** Display pending tickets in their processing order.
- **Sorted Ticket List:** Display all registered tickets in alphabetical order.
- **Statistics:** Track the total number of registered, pending, and completed tickets.

The application also includes input validation and error handling for situations such as empty queues, invalid IDs, and unavailable operations.

---

## Technologies

- **Python 3.12+**
- **Collections (`deque`)** — Queue implementation.
- **Python Standard Library** — No external dependencies required.

### Data Structures

| Data Structure | Implementation | Purpose |
|---|---|---|
| Dictionary | `dict` | Store and retrieve tickets by ID |
| Queue | `collections.deque` | Manage pending tickets using FIFO |
| Stack | `list` | Track completed tickets and support undo operations |
| Sorting | `sorted()` | Display tickets in alphabetical order |

These structures were selected to demonstrate how different data structures can be combined to solve practical programming problems.

---

## Installation and Usage

### Prerequisites

- Python 3.12 or higher.
- Git (to clone the repository).

### 1. Clone the repository

```bash
git clone https://github.com/omarcelodev/suport-desk-cli.git
```

### 2. Navigate to the project directory

```bash
cd suport-desk-cli
```

### 3. Run the application

**Linux/macOS:**

```bash
python3 main.py
```

**Windows:**

```bash
python main.py
```

No additional packages or dependencies are required.

---

## Application Interface

When the application starts, the following menu is displayed:

```text
==================================
    CENTRAL DE SUPORTE TÉCNICO
==================================

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

**Note:** The application interface is currently available in Portuguese.

Users can interact with the system by entering the number corresponding to the desired operation.

The application continues running until the user selects the exit option.

---

## How It Works

### Ticket Management

Each support ticket contains three attributes:

| Attribute | Description |
|---|---|
| ID | Automatically generated unique identifier |
| Title | Description of the reported issue |
| Status | Current ticket status: `Pendente` (Pending) or `Atendido` (Completed) |

Tickets are stored in a Python dictionary, using their IDs as keys.

### Ticket Creation

When a new ticket is created:

1. A unique ID is automatically generated.
2. The ticket information is stored in the dictionary.
3. Its initial status is set to `Pendente`.
4. The ticket ID is added to the end of the support queue.

### Ticket Processing

When processing a ticket:

1. The first ticket in the queue is selected.
2. Its status is updated to `Atendido`.
3. The ticket is removed from the queue.
4. Its ID is pushed onto the history stack.

This ensures that tickets are processed according to the **FIFO (First In, First Out)** principle.

### Undo Operations

The application allows users to reverse the most recently completed ticket.

This feature uses a stack following the **LIFO (Last In, First Out)** principle.

When an operation is undone:

1. The most recently completed ticket is retrieved from the stack.
2. Its status is changed back to `Pendente`.
3. The ticket is inserted at the beginning of the support queue.
4. The corresponding entry is removed from the history stack.

This ensures that undo operations are performed in reverse chronological order.

---

## Time Complexity Analysis

The main operations have the following time complexities:

| Operation | Time Complexity |
|---|---|
| Ticket lookup by ID | O(1) — Average case |
| ID generation using `max()` | O(n) |
| Queue insertion (`append`) | O(1) |
| Queue removal (`popleft`) | O(1) |
| Stack insertion (`append`) | O(1) — Amortized |
| Undo operation (`pop`, `appendleft`) | O(1) |
| Ticket sorting (`sorted`) | O(n log n) — Worst case |
| Statistics retrieval | O(1) |

Where `n` represents the number of registered tickets.

The use of `collections.deque` enables efficient insertion and removal operations at both ends of the queue.

Python dictionaries provide average-case constant-time lookups through hash-based indexing.

Ticket ID generation uses `max()` to find the highest existing identifier. Although this operation has linear time complexity, it was intentionally retained to keep the implementation simple and appropriate for the project's educational scope.

A more detailed explanation is available in the complexity analysis documentation.

---

## Testing

Manual tests were performed to validate the application's core functionality.

The test scenarios included:

1. **Ticket Creation:** Verify unique IDs, correct information storage, and initial status.
2. **FIFO Processing:** Ensure tickets are handled in their original arrival order.
3. **Undo Operations:** Verify that completed tickets can be restored using LIFO.
4. **Sorting:** Confirm alphabetical ordering without modifying the original support queue.
5. **Input Validation:** Verify error handling for invalid inputs, empty queues, and nonexistent tickets.

All required test scenarios were successfully completed.

Detailed test results are available in `docs/testes-manuais.md`.

---

## Project Structure

```text
suport-desk-cli/
│
├── main.py
├── README.md
├── .gitignore
│
└── docs/
    ├── complexity-analysis.md
    ├── implementacao-explicada.md
    └── testes-manuais.md
```

### Additional Documentation

- **Complexity Analysis:** Explanation of the data structures and their computational costs.
- **Implementation Details:** Overview of the application's structure and technical decisions.
- **Manual Testing:** Documentation of the test scenarios and their results.

---

## Project Limitations

This application was developed for educational purposes, focusing on programming fundamentals and data structures.

The following limitations are intentional:

- Data is stored exclusively in memory.
- All records are lost when the application terminates.
- No database integration is implemented.
- No graphical user interface is provided.
- The application is designed for local execution.

These limitations help maintain the project's focus on fundamental programming concepts rather than infrastructure or advanced software architecture.

---

## Learning Objectives

This project represents the completion of the first phase of a structured software development learning roadmap.

The main concepts explored include:

- Programming logic and control flow.
- Functions and code organization.
- Data structures and collections.
- FIFO and LIFO principles.
- Sorting algorithms.
- Big O notation and time complexity.
- Exception handling and input validation.
- Git and GitHub version control.

The project was developed individually to strengthen the foundational skills required for more advanced software engineering topics.

---

## Author

**Marcelo Gomes**

Software Engineering Student

[GitHub — @omarcelodev](https://github.com/omarcelodev)