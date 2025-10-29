from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id", ondelete="CASCADE"))

    author = relationship("Author", backref="books")
