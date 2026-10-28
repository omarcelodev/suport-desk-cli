# Explicação da Implementação do programa

A prícipio foram escolhidas as estruturas de dados básicas para compor o armazenamento e controle de chamados, sendo eles:

- Dicionários para armazenar Id, Título e Status de todos os chamados cadastrados
- Fila para armazenar com príncipio FIFO os chamados pendentes 
- Pilhas para controlar atráves do LIFO o historico de atendimentos e permitir desfazer algum atendimento. 

O programa foi dívido em funções(Que não obedecem o príncipio da responsábilidade única). Sendo elas:

- clear_screen() Para limpar a tela sempre que o usuário realizar alguma operação e deixar O UX/UI melhor.
- show_menu() Para imrpimir o menu príncipal do programa e evitar muitos prints no main

- abrir_novo_chamado()
- atender_proximo_chamado()
- consultar_chamado_por_id()
- desfazer_ultimo_atendimento()
- exibir_fila_atendimento()
- listar_chamados_ordenados()
- exibir-estatisticas
Essas funções acima fazem o que o desafio propõe e organiza em um só lugar cada operação independente. 

No main temos a orquestração dessas funções controladas por um if/else e laço de repetição para garantir que o programa só encerre quando o usuário desejar