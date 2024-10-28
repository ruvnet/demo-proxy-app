from typing import List, Optional, Union
from uuid import UUID
from pydantic import BaseModel
from .blocks import TextBlock, ImageBlock, MetricsBlock, ChartBlock, LinkPreviewBlock, TableBlock, QuoteBlock

class SubSection(BaseModel):
    block_type: str = "subsection"
    id: UUID
    row: str  # "1" or "2"
    column: str  # "1" or "2"
    blocks: List[Union[TextBlock, ImageBlock, MetricsBlock, ChartBlock, LinkPreviewBlock, TableBlock, QuoteBlock]]

class Section(BaseModel):
    block_type: str = "section"
    id: UUID
    title: dict
    intro: dict
    palette: str
    show_headings: bool = True
    is_collapsed: bool = False
    subsections: List[SubSection]
    created_at: Optional[str]
    remix_suggestions: Optional[List[str]] = []
    topics: Optional[List[str]] = []
