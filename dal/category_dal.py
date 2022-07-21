from fastapi import Depends, HTTPException, status
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

def edit_category(uuid:str, category:Category, db:Session = Depends(get_db)):
    query = db.query(category_model.category_model).filter(category_model.category_model.uuid == uuid)
    found_category = query.first()
    category.uuid = found_category.uuid
    category.id = found_category.id
    if not uuid:
        pass
    query.update(category.dict())
    db.commit()
    db.refresh(found_category)
    return found_category

def delete_category(uuid:str, db:Session = Depends(get_db)):
    query = db.query(category_model.category_model).filter(category_model.category_model.uuid == uuid)
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="can't find uuid")
    query.delete(synchronize_session=False)
    db.commit()
    return "article deleted successfully"

def get_category(db:Session = Depends(get_db)):
    return db.query(category_model.category_model).all()


