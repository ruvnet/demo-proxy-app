from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from pathlib import Path

# Create the database directory if it doesn't exist
db_dir = Path("./data")
db_dir.mkdir(exist_ok=True)

# Database URL points to a file in the data directory
SQLALCHEMY_DATABASE_URL = f"sqlite:///{db_dir}/sql_app.db"

# Create engine with appropriate settings for SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False,  # Required for SQLite
        "timeout": 30  # Increase timeout for busy database
    },
    poolclass=StaticPool,  # Use static pool for SQLite
    echo=True  # Enable SQL logging for debugging
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
