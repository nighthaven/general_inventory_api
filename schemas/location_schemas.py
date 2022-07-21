import typing
from pydantic import BaseModel
from typing import Optional

class Location(BaseModel):
    id: Optional[int]
    uuid: Optional[str]
    name: str