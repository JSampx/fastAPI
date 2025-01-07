from typing import List, Optional
from core.configs import settings
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from pydantic import BaseModel

class CursoModel(settings.DBBaseModel):
    __tablename__ = "cursos"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    aulas: int = Column(Integer)
    horas: int = Column(Integer)
    autor = relationship('AutorModel', back_populates='cursos')


class AutorModel(settings.DBBaseModel):
    __tablename__ = "autores"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(100))
    cursos = relationship("CursoModel", back_populates="autor", cascade="all, delete-orphan")
