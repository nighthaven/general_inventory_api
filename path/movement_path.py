from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from schemas.movement_schemas import Movement
from connection.connection import get_db
from dal import movement_dal

path = APIRouter()

@path.post("/movements")
def create_movements(movement: Movement, db:Session = Depends(get_db)):
    return movement_dal.create_movements(movement,db)

