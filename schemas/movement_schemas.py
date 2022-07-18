from pydantic import BaseModel

class Movement(BaseModel):
    id: int
    uuid: str
    quantity: int
    movement_type: str
    created_at: str