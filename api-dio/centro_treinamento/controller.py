from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy import select
from centro_treinamento.schemas import CentroTreinamento
from centro_treinamento.models import CentroTreinamentoModel
from contrib.repository.dependencies import DatabaseDependency

router = APIRouter()

@router.post('/', summary='Criar um novo Centro de Treinamento', status_code=status.HTTP_201_CREATED, response_model=CategoriaOut)

async def post(db_session: DatabaseDependency, categoria_in: CategoriaIn = Body(...)) -> CategoriaOut:
    categoria_out = CategoriaOut(id=UUID4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())
    db_session.add(categoria_model)
    await db_session.commit()
    
    return categoria_out