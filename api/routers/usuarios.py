'''Definição das rotas (Endpoints) HTTP para a gestão de Usuários.'''
# from typing import List
from fastapi import APIRouter, HTTPException, status

from CRUD.usuarios.list_usuario import listar_usuario
from CRUD.usuarios.insert_usuario import inserir_usuario
from CRUD.usuarios.edit_usuario import editar_usuario
from CRUD.usuarios.delete_usuario import deletar_usuario

from api.models.schemas import Usuario_Schema

router = APIRouter(  # router ira separar as rotas de usuarios
    # tudo sera acessado a partir do prefix usuarios
    prefix='/usuarios', tags=["Usuarios"]
)


# GET - home mostra todos os usuarios
@router.get("/")
def retornar_todos_usuarios():
    '''Mostrar todos os usuarios'''
    usuarios = listar_usuario()
    resultado = []

    for u in usuarios:
        resultado.append({
            "id": u[0],
            "nome": u[1],
            "email": u[2]
        })

    return resultado


# GET - Usuario pelo ID
@router.get("/{usuario_id}")
def retorna_usuario_especifico(usuario_id: int):
    '''Mostra usuario do id escolhido'''
    usuarios = listar_usuario()

    for u in usuarios:
        if u[0] == usuario_id:
            return {
                "id": u[0],
                "nome": u[1],
                "email": u[2]
            }
    raise HTTPException(status_code=404, detail="Usuario nao encontrado")


# POST - Criar usuario
@router.post("/", status_code=status.HTTP_201_CREATED)  # status de sucesso
# garante que esteja no molde feito em schemas.py
def criar_usuario(dados: Usuario_Schema):
    '''criar usuario'''
    inserir_usuario(dados.nome, dados.email, dados.senha)
    return {"Mensagem": "Usuário{dados.nome} criado com  sucesso"}


# PUT - Editar usuario
@router.put("/{usuario_id}")
def alterar_informacoes_usuario(usuario_id: int, dados: Usuario_Schema):
    '''Alterar dados do usuário'''
    editar_usuario(usuario_id, dados.nome, dados.email, dados.senha)
    return {"Mensagem": "Usuário alterado com sucesso"}


# DELETE - Deletar usuario
@router.delete("/{usuario_id}")
def excluir_usuario(usuario_id: int):
    '''Excluir usuario'''
    deletar_usuario(usuario_id)
    return {"Mensagem": "Usuário excluído com sucesso"}
