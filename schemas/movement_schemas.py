from pydantic import BaseModel
from typing import Optional

class Movement(BaseModel):
    id: Optional[int]
    uuid: Optional[str]
    quantity: int
    type: str
    created_at: Optional[str]
    updated_at: Optional[str]

