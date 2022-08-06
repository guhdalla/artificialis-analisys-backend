from datetime import date
from urllib import response
from fastapi import APIRouter, Depends, status, HTTPException
from service.pesquisa_service import PesquisaService
from pydantic import BaseModel

router = APIRouter()

service = PesquisaService()

class Pesquisa(BaseModel):
    id: int
    texto: str
    data: date
    classificacao_nps: str
    valor_nps: float
    foi_analisado: bool
    sentimento: str

@router.get("/pesquisa", response_model=Pesquisa)
def listar(size: int = 10, offset: int = 0, sentimento: str = None, nps: str = None, palavraChave: str = None):
    return service.listar(size, offset, palavraChave, sentimento, nps)