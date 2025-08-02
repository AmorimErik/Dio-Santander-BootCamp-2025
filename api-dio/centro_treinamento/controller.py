from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy import select

from categorias.models import CategoriaModel
from categorias.schemas import CategoriaIn, CategoriaOut
from centro_treinamento.models import CentroTreinamentoModel
from centro_treinamento.schemas import CentroTreinamentoOut
from contrib.repository.dependencies import DatabaseDependency


router = APIRouter()

@router.post(
    path="/", 
    summary="Criar um novo Centro de Treinamento",
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut,
    )

async def post(db_session: DatabaseDependency, centro_treinamento_in: CategoriaIn = Body(...)) -> CentroTreinamentoOut:
    centro_treinamento_out = CentroTreinamentoOut(id=UUID4(), **centro_treinamento_in.model_dump())
    centro_treinamento_model = CentroTreinamentoModel(**centro_treinamento_out.model_dump())
    db_session.add(centro_treinamento_model)
    await db_session.commit()
    return centro_treinamento_out

@router.get(
    path="/",
    summary="Consultar todos os Centros de Treinamento",
    status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamentoOut]
    )

async def query(db_session: DatabaseDependency) -> list[CentroTreinamentoOut]:
    centros_treinamentos_out: list[CentroTreinamentoOut] = (await db_session.execute(select(CategoriaModel))).scalars().all()
    return centros_treinamentos_out

@router.get(
    path="/{id}",
    summary="Consulta um Centro de Treinamento pelo id.",
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoOut
    )

async def get(id: UUID4, db_session: DatabaseDependency) -> CentroTreinamentoOut:
    centro_treinamento_out: CentroTreinamentoOut = (await db_session.execute(select(CentroTreinamentoOut).filter_by(id=id))).scalars().first()
    
    if not centro_treinamento_out:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Centro de Treinamento não encontrado no id: {id}"
        )
    return centro_treinamento_out