tarefas = []

while True:

    print("1 - Adicionar uma tarefa a lista")
    print("2 - Exibir lista de tarefas")
    print("3 - Remover uma tarefa da lista")
    print("4 - Sair do programa")
    
    opc = input("Escolha uma opção (1/2/3/4):")

    if opc == "1":
        tarefa = input("Qual tarefa deseja adicionar ? ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")


    elif opc == "2":
        print("Lista de tarefas: ")
        for tarefa in tarefas:
            print("- " + tarefa)


    elif opc == "3":
        tarefa = input("Qual tarefa deseja remover ? ")
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            print("Tarefa removida com sucesso!")


    else:
        print("Programa finalizado!")

