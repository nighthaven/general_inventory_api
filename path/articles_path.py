from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.article_schemas import Article
from connection.connection import get_db
from dal import articles_dal
from dto.article_response_dto import article_response_dto

path = APIRouter()

@path.post("/articles")
def create_articles(article: Article,db:Session = Depends(get_db)):
    return article_response_dto(articles_dal.create_articles(article, db))

@path.put("/articles/{uuid}")
def edit_articles(uuid:str,article: Article, db:Session = Depends(get_db)):
    return article_response_dto(articles_dal.edit_articles(uuid, article, db))

@path.delete("/articles/{uuid}")
def delete_articles(uuid:str,db:Session = Depends(get_db)):
    return articles_dal.delete_articles(uuid, db)

@path.get("/articles")
def get_articles(db:Session = Depends(get_db)):
    articles = articles_dal.get_articles(db)
    return [article_response_dto(element) for element in articles]

@path.get("/articles/{uuid}")
def get_articles_by_uuid(uuid:str, db:Session = Depends(get_db)):
    return article_response_dto(articles_dal.get_articles_by_uuid(uuid, db))


