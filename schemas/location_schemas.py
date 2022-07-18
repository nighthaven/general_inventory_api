from pydantic import BaseModel

class Location(BaseModel):
    id: int
    uuid: str
    name: str