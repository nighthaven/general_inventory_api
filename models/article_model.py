from sqlalchemy import Column, String, Integer

from connection.connection import Base

class Article_model(Base):
    __tablename__ = "article"
    id = Column(Integer,primary_key=True, index=True)
    UUID = Column(String)
    label = Column(String)
    description = Column(String)
    reference = Column(String)