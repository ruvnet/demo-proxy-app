from typing import List, Optional, Union, Dict, Any
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field

class BlockBase(BaseModel):
    block_type: str
    id: UUID
    event_id: Optional[str] = None
    event_block_index: Optional[int] = None
    source_ids: Optional[List[Union[str, Any]]] = []

class TextBlock(BlockBase):
    block_type: str = "text"
    content: Any
    variant: Optional[str] = None
    bans: Optional[List[Dict[str, Any]]] = []
    is_new: Optional[bool] = None
    error_code: Optional[int] = None

class ImageBlock(BlockBase):
    block_type: str = "image" 
    block_subtype: Optional[str] = None
    src: str
    original_image_source: Optional[str] = None
    width: int
    height: int
    caption: str
    llm_selection: Optional[bool] = False
    show_caption: Optional[bool] = True
    image_style: Optional[str] = None
    is_new: Optional[bool] = None
    error_code: Optional[int] = None

class MetricsBlock(BlockBase):
    block_type: str = "metrics"
    metrics: List[Dict[str, Any]]
    llm_selection: Optional[bool] = False

class ChartBlock(BlockBase):
    block_type: str = "ai_generated_chart"
    url: Optional[str]
    llm_selection: Optional[bool] = False

class LinkPreviewBlock(BlockBase):
    block_type: str = "linkPreview"
    title: str
    description: str
    url: str
    image: str
    favicon: str
    llm_selection: Optional[bool] = False

class TableBlock(BlockBase):
    block_type: str = "table"
    data: List[Union[Dict[str, Any], List[Union[int, float, str]]]]

class QuoteBlock(BlockBase):
    block_type: str = "quote"
    quote: str

class Subsection(BaseModel):
    block_type: str = "subsection"
    id: UUID
    row: str
    column: str
    blocks: List[Union[TextBlock, ImageBlock, MetricsBlock, ChartBlock, LinkPreviewBlock, TableBlock, QuoteBlock]]

class Section(BaseModel):
    block_type: str = "section"
    id: UUID
    title: Any
    intro: Any
    palette: str
    show_headings: bool
    is_collpased: bool  # Note: typo in API spec
    subsections: List[Subsection]
    created_at: Optional[str]
    remix_suggestions: Optional[List[str]] = []
    topics: Optional[List[str]] = []

class Chapter(BaseModel):
    id: UUID
    block_type: str = "chapter"
    sections: List[Section]

class Story(BaseModel):
    id: UUID
    active_draft_id: Optional[UUID]
    version: str
    perms: Any
    headline: Any
    headline_id: Optional[UUID] = None
    headline_event_id: Optional[UUID] = None
    authors: Any
    chapters: List[Chapter]
    theme: Optional[str]
    palette: Optional[str]
    created_at: datetime
    updated_at: datetime
    read_only: bool = False
    is_active: bool = True
    is_public: bool = False
    is_llm_generating: Optional[bool] = None
    last_processed_llm_event_id: Optional[UUID] = None
    views_count: int = 0
    like_count: int = 0
    story_plan: Optional[str] = None
    topics: List[str] = []
    has_liked_by_me: bool = False
    processed_llm_event_ids: Any
    unfurl_image_url: Optional[str] = None
    capitol_rank: Any
    active_section_index: Optional[int] = None
    banner: Any
    parent_story_id: Optional[UUID] = None
    current_depth_level: Optional[float] = None
    project_id: Optional[UUID] = None

class StoryList(BaseModel):
    stories: List[Story]
    matching_user_stories: List[Story] 
    story_count: int
