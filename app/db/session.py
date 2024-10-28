from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# TODO: Move this to environment variables
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # Add connection pooling
    echo=True  # Enable SQL logging for debugging
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
