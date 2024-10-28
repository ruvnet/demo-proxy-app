from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy import cast, String
from fastapi.encoders import jsonable_encoder
from app.crud.base import CRUDBase
from app.models.stories import Story
from app.schemas.stories import StoryCreate, StoryUpdate
import uuid

class CRUDStory(CRUDBase[Story, StoryCreate, StoryUpdate]):
    def create(self, db: Session, *, obj_in: StoryCreate, user_id: str) -> Story:
        # Convert the data to dict and handle UUID conversion
        obj_in_data = jsonable_encoder(obj_in)
        
        # Convert string UUID to UUID object
        if 'id' in obj_in_data and isinstance(obj_in_data['id'], str):
            obj_in_data['id'] = uuid.UUID(obj_in_data['id'])
            
        if 'parent_story_id' in obj_in_data and obj_in_data['parent_story_id'] and isinstance(obj_in_data['parent_story_id'], str):
            obj_in_data['parent_story_id'] = uuid.UUID(obj_in_data['parent_story_id'])
            
        if 'project_id' in obj_in_data and obj_in_data['project_id'] and isinstance(obj_in_data['project_id'], str):
            obj_in_data['project_id'] = uuid.UUID(obj_in_data['project_id'])

        # Create the database object
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        
        return {"created": {"id": db_obj.id}}

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
