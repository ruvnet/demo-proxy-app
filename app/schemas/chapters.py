from typing import List
from uuid import UUID
from pydantic import BaseModel
from .sections import Section

class Chapter(BaseModel):
    id: UUID
    block_type: str = "chapter"
    sections: List[Section]
