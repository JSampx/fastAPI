from typing import Optional

from pydantic import ConfigDict, BaseModel as SCBaseModel


class CursoSchema(SCBaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    autor_id: int
    # model_config = ConfigDict(from_atributes=True)
    class Config:
        from_atributtes = True