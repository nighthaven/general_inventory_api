from fastapi import Depends
from sqlalchemy.orm import Session

from connection.connection import get_db
from models import article_model
from schemas.article_schemas import Article

def create_article(article: Article,db:Session = Depends(get_db)):
    new_article = article_model.Article_model(
        id = article.id,
        UUID = article.uuid,
        label = article.label,
        description = article.description,
        reference = article.reference
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return article

