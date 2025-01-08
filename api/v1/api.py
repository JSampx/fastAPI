from fastapi import APIRouter

from api.v1.endpoints import curso
from api.v1.endpoints import autor


api_router = APIRouter()
api_router.include_router(curso.router, prefix='/cursos', tags=["cursos"])
api_router.include_router(autor.router, prefix='/autores', tags=["autores"])


# /api/v1/cursos
