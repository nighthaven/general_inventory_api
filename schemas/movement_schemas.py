from pydantic import BaseModel
from typing import Optional

class Movement(BaseModel):
    id: Optional[int]
    uuid: str
    quantity: int
    type: str
    created_at: Optional[str]

