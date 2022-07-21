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

@path.put("/category/{uuid}")
def edit_category(uuid:str, category:Category, db:Session = Depends(get_db)):
    return category_response_dto(category_dal.edit_category(uuid, category, db))

@path.delete("/category/{uuid}")
def delete_category(uuid:str, db:Session = Depends(get_db)):
    return category_dal.delete_category(uuid,db)

@path.get("/category")
def get_category(db:Session = Depends(get_db)):
    categories = category_dal.get_category(db)
    return [category_response_dto(element) for element in categories]

