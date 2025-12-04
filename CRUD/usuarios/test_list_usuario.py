'''Teste listar usuarios do banco de dados'''
from CRUD.usuarios.list_usuario import listar_usuario

if __name__ == "__main__":
    lista_usuarios = listar_usuario()
    for usuario in lista_usuarios:
        print(usuario)
