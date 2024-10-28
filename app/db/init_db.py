from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base_class import Base
from app.db.session import engine
from app.models.stories import Story  # Import the Story model

def init_db() -> None:
    # Import all models here so they are registered with Base
    Story  # This ensures the Story model is imported
    
    # Drop all tables first to ensure clean state
    Base.metadata.drop_all(bind=engine)
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
