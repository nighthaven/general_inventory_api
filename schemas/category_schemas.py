from pydantic import BaseModel
from typing import Optional

class Category(BaseModel):
    id: Optional[int]
    uuid: Optional[str]
    name: str