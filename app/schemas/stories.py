from typing import List, Optional, Dict, Any
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from .chapters import Chapter

class StoryBase(BaseModel):
    id: UUID
    version: str
    headline: Dict[str, Any]
    authors: Dict[str, Any]
    chapters: List[Chapter]
    theme: Optional[str] = None
    palette: Optional[str] = None
    is_public: bool = False
    is_active: bool = True
    is_llm_generating: Optional[bool] = None
    story_plan: Optional[str] = None
    topics: List[str] = []
    processed_llm_event_ids: Dict = {}
    unfurl_image_url: Optional[str] = None
    capitol_rank: Optional[Dict] = {}
    active_section_index: Optional[int] = None
    banner: Optional[Dict] = {}
    parent_story_id: Optional[UUID] = None
    current_depth_level: Optional[float] = None
    project_id: Optional[UUID] = None

class StoryCreate(StoryBase):
    pass

class StoryUpdate(StoryBase):
    headline: Optional[Dict[str, Any]] = None
    authors: Optional[Dict[str, Any]] = None
    chapters: Optional[List[Chapter]] = None

class StoryInDBBase(StoryBase):
    created_at: datetime
    updated_at: datetime
    views_count: int = 0
    like_count: int = 0
    has_liked_by_me: bool = False

    class Config:
        from_attributes = True

class Story(StoryInDBBase):
    pass

class StoryInDB(StoryInDBBase):
    pass

# Response model for story creation
class StoryResponse(BaseModel):
    created: Dict[str, UUID]

class StoryListResponse(BaseModel):
    stories: List[Story]
    matching_user_stories: List[Story]
    story_count: int
