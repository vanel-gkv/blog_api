from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database, schemas

app = FastAPI(title="Blog API", description="API simple avec FastAPI + SQLite")

# Créer les tables
models.Base.metadata.create_all(bind=database.engine)


# Dépendance DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Créer un article
@app.post("/api/articles", response_model=schemas.ArticleOut, status_code=201)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    new_article = models.Article(**article.dict())
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


# Lire tous les articles
@app.get("/api/articles", response_model=list[schemas.ArticleOut])
def read_articles(db: Session = Depends(get_db)):
    return db.query(models.Article).all()


# Lire un article par ID
@app.get("/api/articles/{id}", response_model=schemas.ArticleOut)
def read_article(id: int, db: Session = Depends(get_db)):
    article = db.query(models.Article).filter(models.Article.id == id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    return article


# Modifier un article
@app.put("/api/articles/{id}", response_model=schemas.ArticleOut)
def update_article(
    id: int, updates: schemas.ArticleUpdate, db: Session = Depends(get_db)
):
    article = db.query(models.Article).filter(models.Article.id == id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(article, key, value)
    db.commit()
    db.refresh(article)
    return article


# Supprimer un article
@app.delete("/api/articles/{id}", status_code=200)
def delete_article(id: int, db: Session = Depends(get_db)):
    article = db.query(models.Article).filter(models.Article.id == id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    db.delete(article)
    db.commit()
    return {"message": "Article supprimé"}
