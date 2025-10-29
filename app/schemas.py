from pydantic import BaseModel

class AuthorBase(BaseModel):
    name: str
    bio: str | None = None

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    class Config:
        from_attributes = True


class BookBase(BaseModel):
    title: str
    description: str | None = None
    author_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    class Config:
        from_attributes = True


class ReviewBase(BaseModel):
    content: str
    rating: int
    book_id: int

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    class Config:
        from_attributes = True
