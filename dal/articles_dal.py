from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from connection.connection import get_db
from models import article_model
from schemas.article_schemas import Article
from util.uuid_generator import uuid_v4

def create_articles(article: Article,db:Session = Depends(get_db)):
    new_article = article_model.article_model(
        id = article.id,
        uuid = str(uuid_v4()),
        label = article.label,
        description = article.description,
        reference = article.reference,
        category_id = article.category_id,
        location_id = article.location_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

def edit_articles(uuid:str,article: Article, db:Session = Depends(get_db)):
    query = db.query(article_model.article_model).filter(article_model.article_model.uuid == uuid)
    found_article = query.first()
    article.uuid = uuid
    article.id = found_article.id
    if not uuid:
        pass
    query.update(article.dict())
    db.commit()
    return found_article

def delete_articles(uuid:str, db:Session = Depends(get_db)):
    deleting = db.query(article_model.article_model).filter(article_model.article_model.uuid == uuid)
    if not deleting:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="deleting need a valid uuid")
    deleting.delete(synchronize_session=False)
    db.commit()
    return "article deleted"

def get_articles(db:Session = Depends(get_db)):
    return db.query(article_model.article_model).all()

def get_articles_by_uuid(uuid:str, db:Session = Depends(get_db)):
    article = db.query(article_model.article_model).filter(article_model.article_model.uuid == uuid).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="can't find article, need a valid uuid") 
    return article

