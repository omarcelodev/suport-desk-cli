import os

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

def main(): 
    while(1): 
        clear_screen()
        show_menu()

        try:
            opcao = int(input("\nEscolha uma opção: "))
        
            if opcao == 0:
                print("Encerrando programa...")
                break
            elif opcao >= 1 and opcao <= 7:
                print(f"Você escolheu a opção {opcao}.")
            else:
                print("Número fora do menu! Escolha entre 0 e 7.")
                input("Pressione Enter para tentar novamente...")
        except ValueError:
             print("\nErro: Por favor, digite uma opção do menu!")
             input("Pressione Enter para tentar novamente...")
main()
