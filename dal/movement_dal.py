from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from schemas.movement_schemas import Movement
from models import movement_model
from connection.connection import get_db
from util.clock import now



def create_movements(movement:Movement, db:Session = Depends(get_db)):
    new_movement = movement_model.movement_model(
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

def edit_movements(uuid:str,movement:Movement, db:Session = Depends(get_db)):
    movement.uuid = uuid
    movement.created_at = now()
    edition = db.query(movement_model.movement_model).filter(movement_model.movement_model.uuid == uuid)
    if not uuid:
        pass
    edition.update(movement.dict())
    db.commit()
    return "movement edited successfully"





