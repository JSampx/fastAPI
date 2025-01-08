from typing import Optional, List
from schemas.curso_schema import CursoSchema
from pydantic import ConfigDict, BaseModel as SCBaseModel


class AutorSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    # cursos: List[CursoSchema] = []

    class Config:
        orm_mode = True
