import sqlite3
import teste.Conexão as Conexão

def deletar():
    Conexão.conectar_banco()
    try:
        opcaoDeletar = input("O que você quer deletar? 1 - para nome, 2 - para idade, 3 - para email ")
        if opcaoDeletar == '1':
            DelNome = input("Qual o nome a ser excluído? ")
            Conexão.cursor.execute("DELETE FROM {TABLE} WHERE nome = '{DelNome}'")
            print("Dado excluído com sucesso!")
        elif opcaoDeletar == '2':
            DelIdade = int(input("Qual a idade a ser excluída? "))
            Conexão.cursor.execute("DELETE FROM {TABLE} WHERE idade = {DelIdade}")
            print("Dado excluído com sucesso!")
        elif opcaoDeletar == '3':
            DelEmail = input("Qual o email a ser excluído? ")
            Conexão.cursor.execute("DELETE FROM {TABLE} WHERE email = '{DelEmail}'")
            print("Dado excluído com sucesso!")
        else:
            print("Opção inválida")
        Conexão.banco.commit()
    except Exception as e:
        print("Erro ao excluir dados: ", e)