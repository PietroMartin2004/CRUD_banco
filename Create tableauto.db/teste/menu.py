import sqlite3
import teste.Conexão as Conexão
def menu_principal():
        opcaoCriar = input("Bem-vindo ao Banco Create. Pressione 1 para conectar um banco (se o banco não existir ele irá criar um): ")
        if opcaoCriar == '1':
            Conexão()
        elif opcaoCriar == '0':
            menu_principal()
        else:
            print("Opção inválida!")

def menu_manipulacao():
    while True:
        opcao2 = input("Bem-vindo à parte da manipulação do banco. Selecione 1 - para usar o select, 2 - para inserir os valores, 3 - para deletar os dados, 4 - para sair, e 0 para voltar ao menu principal: ")
        if opcao2 == '1':
            Conexão()
        elif opcao2 == '2':
            Conexão()
        elif opcao2 == '3':
            Conexão()
        elif opcao2 == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!")

menu_principal()