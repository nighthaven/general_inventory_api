from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from schemas.movement_schemas import Movement
from models import movement_model
from connection.connection import get_db
from util.clock import now
from util.uuid_generator import uuid_v4



def create_movements(movement:Movement, db:Session = Depends(get_db)):
    date = now()
    new_movement = movement_model.movement_model(
        id = movement.id,
        uuid = str(uuid_v4()),
        quantity = movement.quantity,
        type = movement.type,
        created_at = date,
        updated_at = date
    )
    db.add(new_movement)
    db.commit()
    db.refresh(new_movement)
    return new_movement

def edit_movements(uuid:str,movement:Movement, db:Session = Depends(get_db)):
    query = db.query(movement_model.movement_model).filter(movement_model.movement_model.uuid == uuid)
    found_movement = query.first()
    movement.uuid = found_movement.uuid
    movement.created_at = found_movement.created_at
    movement.id = found_movement.id
    movement.updated_at=now()
    if not uuid:
        pass
    query.update(movement.dict())
    db.commit()
    db.refresh(found_movement)
    return found_movement

def delete_movements(uuid:str, db:Session = Depends(get_db)):
    deleting = db.query(movement_model.movement_model).filter(movement_model.movement_model.uuid == uuid)
    if not uuid:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="uuid not found")
    deleting.delete(synchronize_session=False)
    db.commit()
    return "article deleted successfully"

def get_movements(db:Session = Depends(get_db)):
    return db.query(movement_model.movement_model).all()




