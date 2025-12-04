'''Testando conexao'''
from db import get_conection


def main():
    '''Funcao principal para testar conexao'''
    conectar = get_conection()

    if conectar:
        print("Conexão OK")
        conectar.close()

    else:
        print("Falha na conexão")


if __name__ == '__main__':
    main()
