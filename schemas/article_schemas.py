from pydantic import BaseModel

class Article(BaseModel):
    id: int
    uuid: str
    label: str
    description: str
    reference:str
    