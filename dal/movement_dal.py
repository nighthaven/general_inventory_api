from fastapi import Depends
from sqlalchemy.orm import Session

from schemas.movement_schemas import Movement
from models.movement_model import movement_model
from connection.connection import get_db


def create_movement(movement:Movement, db:Session = Depends(get_db)):
    new_movement = movement_model(
        id = movement.id,
        uuid = movement.uuid,
        quantity = movement.quantity,
        type = movement.type,
        created_at = movement.created_at
    )
    db.add(new_movement)
    db.commit()
    db.refresh()
    return movement





