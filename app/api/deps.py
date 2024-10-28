from typing import Generator
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.db.session import SessionLocal

class CurrentUser(BaseModel):
    id: str

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_current_user() -> CurrentUser:
    # TODO: Implement actual user authentication
    return CurrentUser(id="1")  # Return a CurrentUser instance instead of dict
