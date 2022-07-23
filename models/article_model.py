from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from connection.connection import Base

class article_model(Base):
    __tablename__ = "article"
    id = Column(Integer,primary_key=True, index=True)
    uuid = Column(String)
    label = Column(String)
    description = Column(String)
    reference = Column(String)
    category_id = Column(String, ForeignKey("categorie.id"))
    location_id = Column(String, ForeignKey("location.id"))

    movements = relationship("movement_model", back_populates="article")
    category = relationship("category_model", back_populates="articles")
    location = relationship("location_model", back_populates="articles")