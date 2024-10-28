from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session

from app.schemas.stories import StoryResponse, StoryListResponse, StoryCreate, StoryUpdate
from app.api import deps
from app.crud import story as crud

router = APIRouter()

@router.get("/stories", response_model=StoryListResponse)
async def get_stories(
    db: Session = Depends(get_db),
    search_value: str = Query(..., description="Search term"),
    limit: Optional[int] = None,
    page_size: Optional[int] = None,
    page_number: Optional[int] = None,
    sort_by: Optional[str] = None,
    descending: Optional[bool] = None,
    current_user = Depends(deps.get_current_user)
):
    """Fetch a list of stories with pagination and sorting"""
    stories = crud.story.get_multi(
        db,
        search=search_value,
        limit=limit,
        page_size=page_size,
        page_number=page_number,
        sort_by=sort_by,
        descending=descending,
        user_id=current_user.id
    )
    return {
        "stories": stories,
        "story_count": len(stories)
    }

@router.post("/stories", response_model=StoryResponse)
async def create_story(
    story: StoryCreate,
    db: Session = Depends(get_db),
    current_user = Depends(deps.get_current_user)
):
    """Create a new story"""
    return crud.story.create(db, obj_in=story, user_id=current_user.id)
