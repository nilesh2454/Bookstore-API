from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas, crud
from app.database import get_db

router = APIRouter(prefix="/books", tags=["books"])

@router.post("/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    # ensure author exists
    author = crud.get_author(db, str(book.author_id))
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return crud.create_book(db, book)

@router.get("/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_books(db, skip=skip, limit=limit)

@router.get("/{book_id}", response_model=schemas.Book)
def read_book(book_id: str, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
