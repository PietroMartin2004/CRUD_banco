import sqlite3

def conectar_banco():
    try:
        global banco, cursor
        banco = sqlite3.connect(input("Qual o nome do banco? (Insira a identificação '.db') "))
        cursor = banco.cursor()
        print("Conexão sucedida!")
    except sqlite3.Error as erro:
        print("Falha na Conexão :()")