from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.stories import Story
from app.schemas.stories import StoryCreate, StoryUpdate

class CRUDStory(CRUDBase[Story, StoryCreate, StoryUpdate]):
    def get_multi(
        self,
        db: Session,
        *,
        search: str,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
        page_number: Optional[int] = None,
        sort_by: Optional[str] = None,
        descending: Optional[bool] = None,
        user_id: UUID
    ) -> List[Story]:
        query = db.query(self.model)
        
        if search:
            query = query.filter(self.model.headline['text'].astext.ilike(f"%{search}%"))
            
        if sort_by:
            order_col = getattr(self.model, sort_by)
            if descending:
                order_col = order_col.desc()
            query = query.order_by(order_col)
            
        if page_size and page_number:
            query = query.offset(page_size * (page_number - 1)).limit(page_size)
        elif limit:
            query = query.limit(limit)
            
        return query.all()

story = CRUDStory(Story)
