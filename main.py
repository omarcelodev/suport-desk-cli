import os
from collections import deque

chamados = {}
fila_atendimento = deque()
historico = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu(): 
    print("==================================")
    print("    CENTRAL DE SUPORTE TÉCNICO")
    print("==================================\n")

    print("1 - Abrir novo chamado")
    print("2 - Atender próximo chamado")
    print("3 - Consultar chamado por ID")
    print("4 - Desfazer último atendimento")
    print("5 - Exibir fila de atendimento")
    print("6 - Listar chamados ordenados")
    print("7 - Exibir estatísticas")
    print("0 - Encerrar sistema")

def abrir_novo_chamado():        
    while(1):
        clear_screen()
        print("=== NOVO CHAMADO ===\n")

        id = max(chamados.keys()) + 1 if chamados else 1
        titulo = input("Descreva o problema para o novo chamado: ")

        if(titulo == ""):
            print("Erro: titulo vazio. Tente novamente!")
            input()
            continue
        break

    chamados[id] = {
        "titulo": titulo,
        "status": "Pendente"
    }

    print(f"\n✅ Chamado #{id} aberto com sucesso!")
    print("Status: Pendente")

    fila_atendimento.append(id)

def atender_proximo_chamado():
    clear_screen()

    if len(fila_atendimento) == 0:
            print("A fila não possui nenhum chamado...")
            return
    id = fila_atendimento[0]

    print(f"=== CHAMADO: #{id} - {chamados[id]['titulo']} ===\n")

    print(f"✅ Chamado #{id} foi atendido com sucesso!")
    historico.append(id)
    chamados[id]["status"] = "Atendido"
    fila_atendimento.popleft()

def consultar_cahamado_por_id():
    while(1):
        clear_screen()
        print("=== CONSULTAR CHAMDOS ===")

        try:
            id = int(input("Digite o ID do chamado: "))

            if id < 1:
                print("\nErro: Digite um número inteiro e maior que 0!")
                input("Pressione Enter para tentar novamente!")
            elif id in chamados:
                print(chamados[id])
                return
            else:
                print(f"\nNão foi encontrado nenhum chamdo com o ID #{id}")
                return
        except ValueError:
            print("\nErro: Por favor, digite uma opção númerica!")
            input("Pressione Enter para tentar novamente...")

def main(): 
    while(1): 
        clear_screen()
        show_menu()
        try:
            opcao = int(input("\nEscolha uma opção: "))
        
            if opcao == 0:
                print("Encerrando programa...")
                break
            elif opcao == 1:
                abrir_novo_chamado()
                input("Pressione Enter para voltar ao Menu...")
            elif opcao == 2:
                atender_proximo_chamado()
                input("Pressione Enter para voltar ao Menu...")
            elif opcao == 3:
                consultar_cahamado_por_id()
                input("Pressione Enter para voltar ao Menu...")
            else:
                print("\nNúmero fora do menu! Tente novamente...")
                input("Pressione Enter para tentar novamente...")
        except ValueError:
             print("\nErro: Por favor, digite uma opção do menu!")
             input("Pressione Enter para tentar novamente...")
main()
