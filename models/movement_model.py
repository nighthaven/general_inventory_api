from sqlalchemy import Column, ForeignKey, String, Integer, DateTime
from sqlalchemy.orm import relationship


from connection.connection import Base


class movement_model(Base):
    __tablename__ = "movement"
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String)
    quantity = Column(Integer)
    type = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    article_id = Column(Integer, ForeignKey("article.id"))
    child_article_movement = relationship("article_model", back_populates="parent_movement")

