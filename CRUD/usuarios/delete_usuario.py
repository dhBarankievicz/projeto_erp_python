'''Deletar usuario com base no ID'''

from Conexao_Python_SQL.db import get_conection


def deletar_usuario(id_usuario):
    '''Funcao para deletar usuario'''
    conexao = get_conection()

    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(
                """DELETE FROM usuarios
                    WHERE id = %s
                """,
                (id_usuario,)
            )

            conexao.commit()

            if cursor.rowcount > 0:
                print("Usuario deletado com sucesso")
            else:
                print("Nenhum usuario possui esse ID")

        except Exception as erro:
            print("Nao foi possivel deletar", erro)
        finally:
            cursor.close()
            conexao.close()