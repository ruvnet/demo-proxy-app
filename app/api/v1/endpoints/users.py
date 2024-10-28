from fastapi import APIRouter, Depends
from app.api.deps import get_db, get_current_user

router = APIRouter()
