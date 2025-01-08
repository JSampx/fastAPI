from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.models import AutorModel
from schemas.autor_schema import AutorSchema
from core.deps import get_session


router = APIRouter()


# POST Autor
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=AutorSchema)
async def post_autor(autor: AutorSchema, db: AsyncSession = Depends(get_session)):
    novo_autor = (AutorModel(nome=autor.nome))

    db.add(novo_autor)
    await db.commit()

    return novo_autor


# GET autores
@router.get('/', response_model=List[AutorSchema])
async def get_autores(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AutorModel)
        result = await session.execute(query)
        autor: List[AutorModel] = result.scalars().all()

        return autor


# GET curso
@router.get('/{autor_id}', response_model=AutorSchema, status_code=status.HTTP_200_OK)
async def get_autor(autor_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AutorModel).filter(AutorModel.id == autor_id)
        result = await session.execute(query)
        autor = result.scalar_one_or_none()

        if autor:
            return autor
        else:
            raise HTTPException(detail='Curso não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# PUT curso
@router.put('/{autor_id}', response_model=AutorSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_autor(autor_id: int, autor: AutorSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AutorModel).filter(AutorModel.id == autor_id)
        result = await session.execute(query)
        autor_up = result.scalar_one_or_none()

        if autor_up:
            autor_up.nome = autor.nome

            await session.commit()

            return autor_up
        else:
            raise HTTPException(detail='Autor não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# DELETE curso
@router.delete('/{autor_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_autor(autor_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AutorModel).filter(AutorModel.id == autor_id)
        result = await session.execute(query)
        autor_del = result.scalar_one_or_none()

        if autor_del:
            await session.delete(autor_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Autor não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)
