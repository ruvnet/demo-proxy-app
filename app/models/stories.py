from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, Float, Index, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from app.db.base_class import Base

class Story(Base):
    __tablename__ = "stories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    version = Column(String, nullable=False)
    headline = Column(JSON, nullable=False)
    authors = Column(JSON, nullable=False)
    chapters = Column(JSON, nullable=False)
    theme = Column(String, nullable=True)
    palette = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_public = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    is_llm_generating = Column(Boolean, nullable=True)
    views_count = Column(Integer, default=0)
    like_count = Column(Integer, default=0)
    story_plan = Column(String, nullable=True)
    topics = Column(JSON, default=list)
    processed_llm_event_ids = Column(JSON, default=dict)
    unfurl_image_url = Column(String, nullable=True)
    capitol_rank = Column(JSON, nullable=True)
    active_section_index = Column(Integer, nullable=True)
    banner = Column(JSON, nullable=True)
    parent_story_id = Column(UUID(as_uuid=True), nullable=True)
    current_depth_level = Column(Float, nullable=True)
    project_id = Column(UUID(as_uuid=True), nullable=True)
    
    # Add indexes for common queries
    __table_args__ = (
        Index('ix_stories_created_at', created_at),
        Index('ix_stories_is_public', is_public),
    )

    def __repr__(self):
        return f"<Story {self.id}>"
