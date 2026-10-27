import os
from collections import deque

chamados = {}
fila_atendimento = deque()
historico_atendimento = []

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
    historico_atendimento.append(id)
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
                print(f"ID: #{id}")
                print(f"Título: {chamados[id]["titulo"]}")
                print(f"Status: {chamados[id]["status"]}\n")
                return
            else:
                print(f"\nNão foi encontrado nenhum chamdo com o ID #{id}")
                return
        except ValueError:
            print("\nErro: Por favor, digite uma opção númerica!")
            input("Pressione Enter para tentar novamente...")

def desfazer_ultimo_atendimento():
    while(1):
        clear_screen()
        print("=== DESFAZER ÚLTIMO ATENDIMENTO ===")
        
        if len(historico_atendimento) == 0:
            print("Não há atendimentos realizados para desfazer!")
            return
        
        id = historico_atendimento[-1]

        print("O último atendimento realizado foi: ")
        print(f"ID: #{id}")
        print(f"Título: {chamados[id]["titulo"]}")
        print(f"Status: {chamados[id]["status"]}\n")
        opcao = input("Deseja desfazer? (s/n): ")

        if opcao == "s":
            chamados[id]["status"] = "Pendente"
            fila_atendimento.appendleft(id)
            historico_atendimento.pop()
            print(f"✅ Atendimento #{id} desfeito com sucesso!")
            return
        elif opcao == "n":
            return
        else:
            input("Por favor informe uma opção válida!")

def exibir_fila_atendimento():
    clear_screen()
    print("=== FILA DE ATENDIMENTO ===")

    if len(fila_atendimento) == 0:
        print("Não existe atendimento na fila!")
    else:
        for id in fila_atendimento:
            print(f"ID: #{id}")
            print(f"Título: {chamados[id]["titulo"]}\n")

def listar_chamados_ordenados():
    clear_screen()
    print("=== CHAMADOS ===")
    print("__obs: a exibição da lista está ordenada em ordem alfabética crescente__\n")

def exibir_estatisticas():
    clear_screen()
    print("=== ESTATÍSTICAS ===")
    print(f"Total chamados cadastrados: {len(chamados)}")
    print(f"Total chamados pendentes: {len(fila_atendimento)}")
    print(f"Total chamados atendidos: {len(historico_atendimento)}")

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
            elif opcao == 4:
                desfazer_ultimo_atendimento()
                input("Pressione Enter para voltar ao Menu...")
            elif opcao == 5:
                exibir_fila_atendimento()
                input("Pressione Enter para voltar ao Menu...")
            elif opcao == 6:
                listar_chamados_ordenados()
                input("Pressione Enter para voltar ao Menu...")
            elif opcao == 7:
                exibir_estatisticas()
                input("Pressione Enter para voltar ao Menu...")
            else:
                print("\nNúmero fora do menu! Tente novamente...")
                input("Pressione Enter para tentar novamente...")
        except ValueError:
             print("\nErro: Por favor, digite uma opção do menu!")
             input("Pressione Enter para tentar novamente...")
main()
