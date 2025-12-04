'''Listar usuarios'''
from Conexao_Python_SQL.db import get_conection


def listar_usuario():
    '''Funcao de retornar usuario'''
    conexao = get_conection()

    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(
                "SELECT id, nome, email, senha FROM usuarios"
            )
            usuarios = cursor.fetchall()
            return usuarios

        except Exception as erro:
            print("Erro ao listar usuários", erro)
            return []

        finally:
            cursor.close()
            conexao.close()
