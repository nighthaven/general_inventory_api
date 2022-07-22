from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from connection.connection import Base

class category_model(Base):
    __tablename__ = "categorie"
    id = Column(Integer,primary_key=True, index=True)
    uuid = Column(String)
    name = Column(String)
    child_article_category = relationship("article_model", back_populates="parent_category")