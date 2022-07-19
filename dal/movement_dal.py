from fastapi import Depends
from sqlalchemy.orm import Session

from schemas.movement_schemas import Movement
from models.movement_model import movement_model
from connection.connection import get_db
from util.clock import now



def create_movements(movement:Movement, db:Session = Depends(get_db)):
    new_movement = movement_model(
        id = movement.id,
        uuid = movement.uuid,
        quantity = movement.quantity,
        type = movement.type,
        created_at = now()
    )
    db.add(new_movement)
    db.commit()
    db.refresh(new_movement)
    return new_movement





