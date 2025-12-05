'''Editar o usuario'''

from Conexao_Python_SQL.db import get_conection


def editar_usuario(id_usuario, nome, email, senha):
    '''funcao para alterar nome, email e senha'''
    conexao = get_conection()

    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(
                """UPDATE usuarios
                    SET nome = %s,
                        email = %s,
                        senha = %s
                    WHERE id = %s
                """,
                (nome, email, senha, id_usuario)
            )

            conexao.commit()

            if cursor.rowcount > 0:
                print("Usuario atualizado com sucesso!")
            else:
                print("Nenhum usuario possui esse ID")

        except Exception as erro:
            print("Erro ao editar usuario", erro)

        finally:
            cursor.close()
            conexao.close()
