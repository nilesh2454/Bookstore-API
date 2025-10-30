from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/authors", tags=["Authors"])

@router.get("/", response_model=list[schemas.Author])
def get_authors(db: Session = Depends(get_db)):
    return crud.get_authors(db)

@router.post("/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db, author)
