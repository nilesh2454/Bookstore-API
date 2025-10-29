from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas, crud
from app.database import get_db

router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.post("/", response_model=schemas.Review)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    # ensure book exists
    book = crud.get_book(db, str(review.book_id))
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.create_review(db, review)

@router.get("/book/{book_id}", response_model=List[schemas.Review])
def get_reviews_for_book(book_id: str, db: Session = Depends(get_db)):
    return crud.list_reviews_for_book(db, book_id)
