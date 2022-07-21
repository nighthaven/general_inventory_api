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

@path.delete("/location/{uuid}")
def delete_location(uuid:str, db:Session = Depends(get_db)):
    return location_dal.delete_location(uuid, db)

@path.get("/location")
def get_location(db:Session = Depends(get_db)):
    locations = location_dal.get_location(db)
    return [Location_response_dto(element) for element in locations]

@path.get("/location/{uuid}")
def get_location_by_uuid(uuid:str, db:Session = Depends(get_db)):
    return Location_response_dto(location_dal.get_location_by_uuid(uuid, db))