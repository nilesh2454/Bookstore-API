from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/reviews", tags=["Reviews"])

@router.get("/", response_model=list[schemas.Review])
def get_reviews(db: Session = Depends(get_db)):
    return crud.get_reviews(db)

@router.post("/", response_model=schemas.Review)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return crud.create_review(db, review)
