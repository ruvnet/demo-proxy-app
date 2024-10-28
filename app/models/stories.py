from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, Float, Index
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from app.db.base_class import Base

class Story(Base):
    __tablename__ = "stories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    version = Column(String, nullable=False)
    headline = Column(JSONB, nullable=False)  # Changed from JSON to JSONB
    authors = Column(JSONB, nullable=False)   # Changed from JSON to JSONB 
    chapters = Column(JSONB, nullable=False)  # Changed from JSON to JSONB
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_public = Column(Boolean, default=False)
    views_count = Column(Integer, default=0)
    like_count = Column(Integer, default=0)
    
    # Add indexes for common queries
    __table_args__ = (
        Index('ix_stories_created_at', created_at),
        Index('ix_stories_is_public', is_public),
    )

    def __repr__(self):
        return f"<Story {self.id}>"
