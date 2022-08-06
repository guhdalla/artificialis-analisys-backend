from fastapi import APIRouter, Depends, status, HTTPException
from service.pesquisa_service import PesquisaService

router = APIRouter()

service = PesquisaService()

@router.get("/pesquisa")
def listar(size: int = 10, offset: int = 0, sentimento: str = None, nps: str = None, palavraChave: str = None):
    return service.listar(size, offset, palavraChave, sentimento, nps)