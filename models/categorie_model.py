from sqlalchemy import Column, String, Integer

from connection.connection import Base

class categorie_model(Base):
    __tablename__ = "categorie"
    id = Column(Integer,primary_key=True, index=True)
    uuid = Column(String)
    name = Column(String)