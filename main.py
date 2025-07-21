#Lista para armazenas os projetos
projetos = []

#Função para exibir o menu principal que retorna o número da opção escolhida
def menu():
    print("\n MENU PRINCIPAL \n")
    print("1. Adicionar um Novo Projeto")
    print("2. Listar Todos os Projetos")
    print("3. Marcar Projeto como Concluído")
    print("4. Sair\n")

    try:
        escolha = int(input("Escolha uma opção: "))
        return escolha
    except:
        pass

#Função para adicionar nossos projetos
def adicionar_projeto():
    print("\n Novo Projeto \n")
    titulo = str(input("Título: "))
    status = False #Iniciado como False por padrão

    try:
        projetos.append({
            "titulo" : titulo,
            "status" : status
        })

        print(f"{titulo} adicionado a lista com sucesso!")
    except:
        print("Tivemos um problema ao criar o projeto, tente novamente...")

#Função para listar os projetos da lista
def listar_projetos():
    print("\n Lista de Projetos \n")
    for projeto in projetos:
        print(f"{projeto["titulo"]} - Status: {"Concluído" if projeto["status"] else "Pendente"}")

def mudar_status():
    print("\n Mudar Statuss \n")
    for e, projeto in enumerate(projetos):
        print(f"{e}. {projeto["titulo"]} - Status: {"Concluído" if projeto["status"] else "Pendente"}")

    escolha_mudar_status = int(input("Digite o número do projeto que deseja alterar: "))

    for e, projeto in enumerate(projetos):
        try:
            if e == escolha_mudar_status:
                projeto["status"] = True

                print(f"{projeto["titulo"]} alterado para {projeto["status"]} com sucesso!")

        except:
            print("Tivemos um problema ao mudar o status do projeto, tente novamente...")
    


#Função principal para controle do sistema
def main():
    while True:
        escolha = menu() #Chamada das opções

        match escolha:
            case 1:
                adicionar_projeto()
            case 2:
                listar_projetos()
            case 3:
                mudar_status()
            case 4:
                print("Finalizando sistema...")
                break
            case _:
                print("Escolha uma opção válida. Tente novamente...")


if __name__ == "__main__":
    main()