from typing import List, Optional, Union, Dict, Any
from uuid import UUID
from pydantic import BaseModel
from .metrics import MetricItem

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

class ChartBlock(BlockBase):
    block_type: str = "ai_generated_chart"
    url: Optional[str] = None
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

class MetricsBlock(BlockBase):
    block_type: str = "metrics"
    metrics: List[MetricItem]
    llm_selection: Optional[bool] = False

class QuoteBlock(BlockBase):
    block_type: str = "quote"
    quote: str
