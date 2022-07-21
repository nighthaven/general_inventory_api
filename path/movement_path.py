from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from schemas.movement_schemas import Movement
from connection.connection import get_db
from dal import movement_dal
from dto.movement_response_dto import Movement_response_dto

path = APIRouter()

@path.post("/movements")
def create_movements(movement: Movement, db:Session = Depends(get_db)):
    return Movement_response_dto(movement_dal.create_movements(movement,db))

@path.put("/movements/{uuid}")
def edit_movements(uuid:str,movement:Movement, db:Session = Depends(get_db)):
    return Movement_response_dto(movement_dal.edit_movements(uuid, movement, db))

@path.delete("/movements/{uuid}")
def delete_movements(uuid:str, db:Session = Depends(get_db)):
    return movement_dal.delete_movements(uuid, db)

@path.get("/movements")
def get_movements(db:Session = Depends(get_db)):
    movements = movement_dal.get_movements(db)
    return [ Movement_response_dto(element) for element in movements]

@path.get("/movements/{uuid}")
def get_movements_by_uuid(uuid:str, db:Session = Depends(get_db)):
    return Movement_response_dto(movement_dal.get_movements_by_uuid(uuid, db))

