from pydantic import BaseModel
from typing import Optional

class Article(BaseModel):
    id: Optional[int]
    uuid: Optional[str]
    label: str
    description: str
    reference:str
    category_id: Optional[int]
    location_id: Optional[int]
    