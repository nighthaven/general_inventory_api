from pydantic import BaseModel

class Category(BaseModel):
    id: int
    uuid: str
    name: str