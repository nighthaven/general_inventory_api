from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.location_schemas import Location
from connection.connection import get_db
from dto.location_response_dto import Location_response_dto
from dal import location_dal


path = APIRouter()

@path.post("/location")
def create_location(location:Location, db:Session = Depends(get_db)):
    return Location_response_dto(location_dal.create_location(location, db))

@path.put("/location/{uuid}")
def edit_location(uuid:str, location:Location, db:Session = Depends(get_db)):
    return Location_response_dto(location_dal.edit_location(uuid, location, db))