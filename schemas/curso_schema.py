from typing import Optional

from pydantic import ConfigDict, BaseModel as SCBaseModel


class CursoSchema(SCBaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    model_config = ConfigDict(from_atributes=True)
