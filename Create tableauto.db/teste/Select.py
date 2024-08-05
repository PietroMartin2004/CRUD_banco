import teste.Conexão as Conexão

def select():
    Conexão.conectar_banco
    try:
        Conexão.cursor.execute(f"SELECT * FROM {TABLE}")
        print(Conexão.cursor.fetchall())
    except Exception as e:
        print("Erro ao selecionar dados: ", e)