from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import DeclarativeMeta

@as_declarative()
class Base:
    """
    Base class for all database models
    Automatically generates table name and provides string representation
    """
    id: Any
    __name__: str
    __table__: DeclarativeMeta
    
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"
