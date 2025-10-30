from pydantic import BaseModel
from typing import Optional

class AuthorBase(BaseModel):
    name: str
    bio: Optional[str] = None

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    author_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    author: Optional[Author]
    class Config:
        orm_mode = True


class ReviewBase(BaseModel):
    content: str
    rating: int
    book_id: int

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    book: Optional[Book]
    class Config:
        orm_mode = True
