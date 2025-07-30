from fastapi import APIRouter, Body
from atleta.schemas import AtletaIn
from contrib.repository.dependencies import DatabaseDependency
router = APIRouter()

@router.post(path='/' summary='Criar novo atleta', status_code=status.HTTP_201_CREATED)
async def post(db_session: DatabaseDependency, atleta_in: AtletaIn = Body(...)):
    pass