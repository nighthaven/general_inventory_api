from pydantic import BaseModel
from typing import Optional

class Article(BaseModel):
    id: Optional[int]
    uuid: str
    label: str
    description: str
    reference:str
    