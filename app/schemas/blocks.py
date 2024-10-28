from typing import List, Optional, Union, Dict, Any
from uuid import UUID
from pydantic import BaseModel

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
