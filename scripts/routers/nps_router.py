from fastapi import APIRouter, Depends, status, HTTPException
from service.nps_service import NpsService

router = APIRouter()

service = NpsService()

@router.get("/nps")
def info():
    return service.info()