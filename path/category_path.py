from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from connection.connection import get_db
from schemas.category_schemas import Category
from dal import category_dal
from dto.category_response_dto import category_response_dto


path = APIRouter()

@path.post("/category")
def create_category(category:Category, db:Session = Depends(get_db)):
    return category_response_dto(category_dal.create_category(category, db))

