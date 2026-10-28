# Análise de Compelexidade

**Qual é a complexidade de tempo esperada para localizar um chamado pelo ID utilizando a estrutura escolhida?**
A complexidade é O(n). Porque o programa precisa percorrer as chaves do dicionário e verificar se corresponde com o ID selecionado pelo usuário. Caso ele não encontre ele vai precisar percorrer todo o dicionário, e nesse caso quanto mais elementos mais ele vai precisar percorrer.

**Qual é a complexidade de tempo da operação utilizada para retirar o primeiro chamado da fila?**
A compelexidade é O(1) utilizando popleft. Essa operação é adequadada porque remove o primeiro elemento de uma fila e possui métodos intenrnos para deslocar os outros elementos para novas posições, nesse caso(-1 a esquerda)

**Qual princípio de estrutura de dados foi utilizado para implementar o desfazimento de atendimentos?**
Foi utilizado o pŕincipio LIFO. Esse princípio é apropriado porque garante que o ultimo atendimento realizado seja desfeito, já que ele armazena e retira elementos do topo da pilha.

**Qual é a complexidade de tempo no pior caso da ordenação nativa do Python para uma coleção com n elementos?**
A complexidade de tempo no pior caso da ordenação nativa do Python é O(n log n). O Python utiliza um algoritmo híbrido chamado Timsort, que combina características do Merge Sort e do Insertion Sort. Essa abordagem garante que o tempo de execução nunca exceda esse limite, independentemente de como os $n$ elementos da coleção estejam distribuídos inicialmente.

**Explique por que você escolheu as estruturas de dados utilizadas para armazenar chamados, controlar atendimentos e permitir operações de desfazer.**
Eu escolhi as estrutura de dados dicionário para que eu pudesse armazenar todos os chamados cadastados(Servindo quase como um banco de dados). Escolhi a fila para atendenr o príncipo de uma fila mesmo, onde o primeiro que chega é o primeiro a ser atendido. E escolhi pilha por causa do príncipio LIFO, onde o último a entrar é o primeiro a sair, facilitando para armazenar histórico de atendimento
