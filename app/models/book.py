from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)

    author_id = Column(UUID(as_uuid=True), ForeignKey("authors.id", ondelete="CASCADE"), nullable=False)
    author = relationship("Author", back_populates="books")

    # One-to-many: book -> reviews
    reviews = relationship("Review", back_populates="book", cascade="all, delete-orphan")
