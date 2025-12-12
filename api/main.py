# from typing import Union

from fastapi import FastAPI
from api.routers import usuarios


app = FastAPI()


@app.get("/")  # caminho padrao/home
def home():
    '''Pagina incial /'''
    return {"mensagem": "Estou na home"}


app.include_router(usuarios.router)
