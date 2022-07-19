from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "sqlite:///./inventory_test.db" if 'TEST' in  os.environ else "sqlite:///./inventory.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
    "check_same_thread":False
})

SessionLocal = sessionmaker(bind=engine,autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()