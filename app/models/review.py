from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    rating = Column(Integer)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"))

    book = relationship("Book", backref="reviews")
