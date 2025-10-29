from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional

# ---- Author ----
class AuthorBase(BaseModel):
    name: str = Field(..., example="George Orwell")

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: UUID

    class Config:
        orm_mode = True

# ---- Book ----
class BookBase(BaseModel):
    title: str = Field(..., example="1984")
    author_id: UUID

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: UUID

    class Config:
        orm_mode = True

# ---- Review ----
class ReviewBase(BaseModel):
    book_id: UUID
    content: str = Field(..., example="A very strong read.")
    rating: int = Field(..., ge=1, le=5, example=5)

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: UUID

    class Config:
        orm_mode = True
