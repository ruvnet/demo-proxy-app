from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base_class import Base
from app.db.session import engine

def init_db() -> None:
    # Create all tables
    Base.metadata.create_all(bind=engine)
