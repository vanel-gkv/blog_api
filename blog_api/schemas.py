from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class ArticleBase(BaseModel):
    titre: str = Field(..., min_length=1)
    contenu: str = Field(..., min_length=1)
    auteur: str = Field(..., min_length=1)
    categorie: Optional[str] = None
    tags: Optional[str] = None


class ArticleCreate(ArticleBase):
    pass


class ArticleUpdate(BaseModel):
    titre: Optional[str]
    contenu: Optional[str]
    categorie: Optional[str]
    tags: Optional[str]


class ArticleOut(ArticleBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True
