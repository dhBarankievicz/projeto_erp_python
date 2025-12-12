from pydantic import BaseModel


class Usuario_Schema(BaseModel):
    nome: str
    email: str
    senha: str