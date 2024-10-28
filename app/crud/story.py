from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy import cast, String
from app.crud.base import CRUDBase
from app.models.stories import Story
from app.schemas.stories import StoryCreate, StoryUpdate

class CRUDStory(CRUDBase[Story, StoryCreate, StoryUpdate]):
    def create(self, db: Session, *, obj_in: StoryCreate, user_id: str) -> Story:
        # Override create method to handle user_id
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return {"created": {"id": db_obj.id}}  # Match the StoryResponse model

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
            # For SQLite, we'll do a simple string search
            # Note: This is not ideal for production, but works for development
            query = query.filter(self.model.headline.like(f"%{search}%"))
            
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
