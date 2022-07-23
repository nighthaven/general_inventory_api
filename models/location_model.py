from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from connection.connection import Base

class location_model(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String)
    name = Column(String)
    articles = relationship("article_model", back_populates="location")
