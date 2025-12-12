'''Teste de inserir usuario no banco'''
from CRUD.usuarios.insert_usuario import inserir_usuario

if __name__ == '__main__':
    inserir_usuario('Pedro sanatos', 'Ps@email.com', 'qwerty')
