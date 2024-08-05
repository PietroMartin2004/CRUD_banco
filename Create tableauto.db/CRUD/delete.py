import sqlite3
import conexao

def delet():
    conexao.conectar()
    cpf = input("Informe o CPF que deseja consultar: ")
    try:
        resultado = conexao.banco.execute('''SELECT * FROM cliente where cpf = ?''',(cpf,)).fetchall()
        if(resultado == []):
            print("CPF não encontrado!")
        else:
            banco=sqlite3.connect('cadastro.db')

            cursor = banco.cursor()

            cursor.execute("DELETE FROM cliente WHERE cpf = '"+cpf+"'")

            banco.commit()
            banco.close
            print("Dado excluído com sucesso!")
            
    except Exception as erro:
        print("Erro ao excluir dados: ", erro)