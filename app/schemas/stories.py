from typing import List, Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from .blocks import TextBlock, ImageBlock, MetricsBlock, ChartBlock, LinkPreviewBlock, TableBlock, QuoteBlock

class StoryResponse(BaseModel):
    id: UUID
    headline: dict
    version: str
    authors: dict
    created_at: datetime
    updated_at: datetime
    is_public: bool
    views_count: int
    like_count: int
    
    class Config:
        from_attributes = True

class StoryListResponse(BaseModel):
    stories: List[StoryResponse]
    story_count: int
    
    class Config:
        from_attributes = True

class StoryCreate(BaseModel):
    headline: dict
    authors: dict
    is_public: bool = False
    
    class Config:
        json_schema_extra = {
            "example": {
                "headline": {"text": "My Story Title"},
                "authors": {"primary": "John Doe"},
                "is_public": False
            }
        }

class StoryUpdate(BaseModel):
    headline: Optional[dict] = None
    authors: Optional[dict] = None
    is_public: Optional[bool] = None
