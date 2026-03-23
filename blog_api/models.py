from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from .database import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, nullable=False)
    contenu = Column(Text, nullable=False)
    auteur = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    categorie = Column(String, nullable=True)
    tags = Column(String, nullable=True)
