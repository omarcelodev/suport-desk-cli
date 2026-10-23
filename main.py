import os
from collections import deque

chamados = {}
fila_atendimento = deque()

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
    clear_screen()
    print("=== NOVO CHAMADO ===\n")

    id = max(chamados.keys()) + 1 if chamados else 1
    titulo = input("Descreva o problema para o novo chamado: ")

    chamados[id] = {
        "titulo": titulo,
        "status": "Pendente"
    }

    print(f"\n✅ Chamado #{id} aberto com sucesso!")
    print("Status: Pendente")

    fila_atendimento.append(id)

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
            else:
                print("Número fora do menu! Tente novamente...")
                input("Pressione Enter para tentar novamente...")
        except ValueError:
             print("\nErro: Por favor, digite uma opção do menu!")
             input("Pressione Enter para tentar novamente...")
main()
