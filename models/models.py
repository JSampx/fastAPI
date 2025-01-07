from typing import List, Optional
from core.configs import settings
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

class CursoModel(settings.DBBaseModel):
    __tablename__ = "cursos"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    aulas: int = Column(Integer)
    horas: int = Column(Integer)


class AutorModel(settings.DBBaseModel):
    __tablename__ = "autor"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(100))