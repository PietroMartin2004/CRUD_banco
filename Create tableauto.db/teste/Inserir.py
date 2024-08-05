import teste.Conexão as Conexão

def inserir():
    
    try:
        nome = input("Qual o nome a ser inserido? ")
        idade = int(input("Qual a idade a ser inserida? "))
        email = input("Qual o email a ser inserido? ")
        Conexão.cursor.execute(f"INSERT INTO {TABLE} (nome, idade, email) VALUES ('{nome}', {idade}, '{email}')")
        Conexão.banco.commit()
        print("Dados inseridos com sucesso!")
    except Exception as e:
        print("Erro ao inserir dados: ", e)