from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, JSON, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from app.db.base_class import Base

class Story(Base):
    __tablename__ = "stories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    active_draft_id = Column(UUID(as_uuid=True), nullable=True)
    version = Column(String, nullable=False)
    perms = Column(JSON)
    headline = Column(JSON)
    headline_id = Column(UUID(as_uuid=True), nullable=True)
    headline_event_id = Column(UUID(as_uuid=True), nullable=True)
    authors = Column(JSON)
    chapters = Column(JSON, nullable=False)  # Stores the full chapters structure
    theme = Column(String, nullable=True)
    palette = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    read_only = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    is_public = Column(Boolean, default=False)
    is_llm_generating = Column(Boolean, nullable=True)
    last_processed_llm_event_id = Column(UUID(as_uuid=True), nullable=True)
    views_count = Column(Integer, default=0)
    like_count = Column(Integer, default=0)
    story_plan = Column(String, nullable=True)
    topics = Column(JSON, default=list)
    has_liked_by_me = Column(Boolean, default=False)
    processed_llm_event_ids = Column(JSON)
    unfurl_image_url = Column(String, nullable=True)
    capitol_rank = Column(JSON)
    active_section_index = Column(Integer, nullable=True)
    banner = Column(JSON)
    parent_story_id = Column(UUID(as_uuid=True), nullable=True)
    current_depth_level = Column(Float, nullable=True)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=True)

    # Relationships
    project = relationship("Project", back_populates="stories")
