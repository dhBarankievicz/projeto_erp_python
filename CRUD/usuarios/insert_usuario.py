'''Inserir usuario na tabela'''

from Conexao_Python_SQL.db import get_conection


def inserir_usuario(nome, email, senha):
    '''funcao para inserir usuario'''
    conexao = get_conection()

    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)",
                (nome, email, senha)
            )
            conexao.commit()
            print("Usuário foi inserido")
        except Exception as erro:
            print("Erro ao inserir o usuário", erro)
        finally:
            cursor.close()
            conexao.close()
