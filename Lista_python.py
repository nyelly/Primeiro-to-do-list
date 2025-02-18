class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

    def concluir(self):
        self.concluida = True

    def __str__(self):
        status = "Concluída" if self.concluida else "Pendente"
        return f"{self.descricao} [{status}]"


class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def listar_tarefas(self):
        if not self.tarefas:
            print("\nNenhuma tarefa na lista.")
        else:
            print("\n Lista de Tarefas:")
            for i, tarefa in enumerate(self.tarefas):
                print(f"{i} - {tarefa}")

    def concluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluir()
            print("Tarefa concluída!")
        else:
            print("Índice inválido.")

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            del self.tarefas[indice]
            print("Tarefa removida!")
        else:
            print("Índice inválido.")


def menu():
    lista = ListaDeTarefas()

    while True:
        print("\n--- To-Do List ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Remover Tarefa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição da tarefa: ")
            lista.adicionar_tarefa(descricao)
            print("Tarefa adicionada!")
        
        elif opcao == "2":
            lista.listar_tarefas()
        
        elif opcao == "3":
            lista.listar_tarefas()
            indice = int(input("Digite o número da tarefa para concluir: "))
            lista.concluir_tarefa(indice)
        
        elif opcao == "4":
            lista.listar_tarefas()
            indice = int(input("Digite o número da tarefa para remover: "))
            lista.remover_tarefa(indice)
        
        elif opcao == "5":
            print(" Saindo...")
            break
        
        else:
            print(" Opção inválida.")

menu()