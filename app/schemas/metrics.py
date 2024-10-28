from typing import List, Optional, Dict, Any
from uuid import UUID
from pydantic import BaseModel

class MetricItem(BaseModel):
    data: Any  # Can be string or number
    descriptor: Optional[str] = None
    icon: Optional[Dict[str, str]] = None

class MetricsBlock(BaseModel):
    block_type: str = "metrics"
    id: UUID
    metrics: List[MetricItem]
    source_ids: Optional[List[Any]] = []
    llm_selection: Optional[bool] = False
    event_id: Optional[str] = None
    event_block_index: Optional[int] = None
