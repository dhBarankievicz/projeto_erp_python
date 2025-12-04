'''Criando conexao com sql'''
import psycopg2


def get_conection():
    '''funcao para conexao, se tudo estiver certo ok, senao mostra o erro'''
    try:
        conectar = psycopg2.connect(dbname='controle_estoque',
                                    user='postgres',
                                    password='senha',
                                    host='localhost',
                                    port='5432')
        return conectar

    except Exception as erro:
        print('Erro ao conectar: ', erro)
        return None
