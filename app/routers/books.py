from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=list[schemas.Book])
def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@router.post("/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)
