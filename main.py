from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Finance API")


class Transacao(BaseModel):
    descricao: str
    valor: float
    tipo: str  # "entrada" ou "saida"


@app.get("/")
def raiz():
    return {"mensagem": "API no ar"}


@app.get("/saude")
def saude():
    return {"status": "ok"}


@app.post("/transacoes")
def criar_transacao(transacao: Transacao):
    return {"recebido": transacao}