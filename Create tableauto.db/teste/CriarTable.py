import sqlite3
import teste.Conexão as Conexão

def criartabela():
    global TABLE
    Conexão.conectar_banco()
    try:
        TABLE = input("Qual o nome da tabela? ")
        Conexão.cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE} (nome text, idade integer, email text)")
        print(f"Tabela {TABLE} criada com sucesso!")
    except Exception as e:
        print("Erro: ", e)