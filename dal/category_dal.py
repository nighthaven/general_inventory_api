from fastapi import Depends
from sqlalchemy.orm import Session

from connection.connection import get_db
from schemas.category_schemas import Category
from models import category_model
from util.uuid_generator import uuid_v4


def create_category(category:Category, db:Session = Depends(get_db)):
    new_category = category_model.category_model(
        id = category.id,
        uuid = str(uuid_v4()),
        name = category.name
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category
