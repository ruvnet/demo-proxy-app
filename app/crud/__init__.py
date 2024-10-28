"""
CRUD operations for Capitol AI Services
Contains database operations organized by model
"""

from .story import story
from .base import CRUDBase

__all__ = ["story", "CRUDBase"]
