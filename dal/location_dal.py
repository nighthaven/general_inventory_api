from fastapi import Depends
from sqlalchemy.orm import Session

from schemas.location_schemas import Location
from models.location_model import location_model
from connection.connection import get_db
from util.uuid_generator import uuid_v4


def create_location(location:Location, db:Session = Depends(get_db)):
    new_location = location_model(
        id = location.id,
        uuid = str(uuid_v4()),
        name = location.name
    )
    db.add(new_location)
    db.commit()
    db.refresh(new_location)
    return new_location

def edit_location(uuid:str, location:Location, db:Session = Depends(get_db)):
    query = db.query(location_model).filter(location_model.uuid == uuid)
    found_query = query.first()
    location.uuid = found_query.uuid
    location.id = found_query.id
    if not uuid:
        pass
    query.update(location.dict())
    db.commit()
    db.refresh(found_query)
    return found_query
