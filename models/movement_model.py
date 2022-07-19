from sqlalchemy import Column, String, Integer, DateTime


from connection.connection import Base


class movement_model(Base):
    __tablename__ = "movement"
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String)
    quantity = Column(Integer)
    type = Column(String)
    created_at = Column(DateTime)


