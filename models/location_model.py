from sqlalchemy import Column, String, Integer

from connection.connection import Base

class location_model(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True, index=True)
    UUID = Column(String)
    name = Column(String)
