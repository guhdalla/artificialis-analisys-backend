from fastapi import APIRouter, Depends, status, HTTPException
from service.palavra_chave_service import PalavraChaveService

router = APIRouter()

service = PalavraChaveService()

@router.get("/nuvemPalavras")
def nuvem_palavras(size: int = 10, offset: int = 0, filtro: str = None):
    return service.nuvem_palavras(size, offset, filtro)