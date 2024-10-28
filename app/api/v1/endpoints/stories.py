from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session

from app.schemas.stories import StoryResponse, StoryListResponse, StoryCreate, StoryUpdate
from app.api.deps import get_db, get_current_user, CurrentUser
from app.crud.story import story

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
    current_user: CurrentUser = Depends(get_current_user)
):
    """Fetch a list of stories with pagination and sorting"""
    stories = story.get_multi(
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
        "matching_user_stories": stories,  # Add matching user stories
        "story_count": len(stories)
    }

@router.post("/stories", response_model=StoryResponse)
async def create_story(
    story_in: StoryCreate,
    db: Session = Depends(get_db),
    current_user: CurrentUser = Depends(get_current_user)
):
    """Create a new story"""
    return story.create(db, obj_in=story_in, user_id=current_user.id)
