from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.article_schemas import Article
from connection.connection import get_db
from dal import articles_dal

path = APIRouter()

@path.post("/article")
def create_article(article: Article,db:Session = Depends(get_db)):
    return articles_dal.create_article(article, db)

